"""
LLM客户端封装
统一使用OpenAI格式调用
"""

import json
import re
import logging
from typing import Optional, Dict, Any, List
from openai import OpenAI, APIError, RateLimitError, AuthenticationError, APIConnectionError

from ..config import Config

logger = logging.getLogger(__name__)


class LLMClient:
    """LLM客户端"""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        self.api_key = api_key or Config.LLM_API_KEY
        self.base_url = base_url or Config.LLM_BASE_URL
        self.model = model or Config.LLM_MODEL_NAME
        
        if not self.api_key:
            raise ValueError("LLM_API_KEY 未配置")
        
        # OpenRouter requires custom headers
        headers = {}
        if "openrouter.io" in (self.base_url or ""):
            headers = {
                "HTTP-Referer": "https://mirofish.ai",
                "X-Title": "MiroFish",
            }
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
            default_headers=headers if headers else None
        )
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """
        发送聊天请求
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            response_format: 响应格式（如JSON模式）
            
        Returns:
            模型响应文本
            
        Raises:
            ValueError: API调用失败时
        """
        try:
            kwargs = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
            
            if response_format:
                kwargs["response_format"] = response_format
            
            logger.debug(f"LLM Request: model={self.model}, base_url={self.base_url}, temp={temperature}, max_tokens={max_tokens}")
            response = self.client.chat.completions.create(**kwargs)
            content = response.choices[0].message.content
            # 部分模型（如MiniMax M2.5）会在content中包含<think>思考内容，需要移除
            content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
            logger.debug(f"LLM Response received: {len(content)} characters")
            return content
            
        except AuthenticationError as e:
            error_msg = f"LLM认证失败 (检查API密钥): {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        except RateLimitError as e:
            error_msg = f"LLM速率限制: 请稍后重试。{str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        except APIConnectionError as e:
            error_msg = f"LLM连接错误: {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        except APIError as e:
            error_msg = f"LLM API错误: {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
    
    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        发送聊天请求并返回JSON
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            
        Returns:
            解析后的JSON对象
            
        Raises:
            ValueError: JSON解析失败或API调用失败
        """
        try:
            response = self.chat(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                response_format={"type": "json_object"}
            )
            # 清理markdown代码块标记
            cleaned_response = response.strip()
            cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
            cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
            cleaned_response = cleaned_response.strip()

            logger.debug(f"Attempting to parse JSON: {cleaned_response[:100]}...")
            result = json.loads(cleaned_response)
            logger.debug(f"JSON parsed successfully: {list(result.keys()) if isinstance(result, dict) else 'array'}")
            return result
        except json.JSONDecodeError as e:
            error_msg = f"LLM返回的JSON格式无效: {str(e)}\n响应内容: {cleaned_response[:500]}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        except ValueError as e:
            # LLM API错误已由chat()方法处理，直接抛出
            raise

