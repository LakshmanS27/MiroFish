# 🔧 Error Handling Improvements - Summary

## Problem
Backend returned HTTP 500 on `/api/graph/ontology/generate` without specific error details.

## Root Cause
Missing error handling and logging for OpenRouter API failures.

## Solution Implemented

### 1. Enhanced LLM Client Error Handling
**File:** `backend/app/utils/llm_client.py`

Added specific exception handling for all OpenRouter API error types:
```python
✅ AuthenticationError - "LLM认证失败 (检查API密钥)"
✅ RateLimitError - "LLM速率限制: 请稍后重试"
✅ APIConnectionError - "LLM连接错误"
✅ APIError - "LLM API错误"
```

Also added:
- Debug logging for requests and responses
- Better error messages for troubleshooting

### 2. Improved Ontology Generator Logging
**File:** `backend/app/services/ontology_generator.py`

Added logging for:
- Model name and prompt lengths
- LLM call start/success/failure
- JSON parsing validation

### 3. Better API Error Responses
**File:** `backend/app/api/graph.py`

Changed exception handling:
- `ValueError` (LLM errors) → 400 Bad Request with error message
- Other exceptions → 500 Internal Server Error
- Better logging at different levels (warning vs error)
- Debug mode shows full error details, production hides them

## Testing

### Before (No Error Details)
```
Request: POST /api/graph/ontology/generate
Response: {
  "success": false,
  "error": "...",
  "traceback": "..."  # ← Exposes code structure
}
Status: 500
```

### After (Clear Error Messages)
```
If API Key Invalid:
Response: {
  "success": false,
  "error": "LLM认证失败 (检查API密钥): Invalid API Key"
}
Status: 400 (with logging)

If Rate Limited:
Response: {
  "success": false,
  "error": "LLM速率限制: 请稍后重试。429 Too Many Requests"
}
Status: 400 (with logging)

If Other Error:
Response: {
  "success": false,
  "error": "Ontology generation failed. Check logs."
}
Status: 500 (full error in logs)
```

## How to Debug Now

### Step 1: Restart Backend
```bash
# Press Ctrl+C to stop current process
# Then:
npm run dev
```

### Step 2: Try Ontology Generation Again
- Open http://localhost:3000
- Upload a document
- Fill in simulation requirement
- Click "Generate"

### Step 3: Check Error Response
- Look at browser console (F12)
- Error should now be more specific

### Step 4: Check Backend Logs
```bash
# File: backend/logs/YYYY-MM-DD.log
# Look for lines like:
# [HH:MM:SS] ERROR: LLM call failed: [specific error]
# [HH:MM:SS] DEBUG: LLM Request: model=...
```

## Common Errors You Might See

| Error | Cause | Solution |
|-------|-------|----------|
| `LLM认证失败` | Invalid/expired API key | Get new key from https://openrouter.ai/keys |
| `LLM速率限制` | Rate limit exceeded (free tier) | Wait a bit or upgrade |
| `LLM连接错误` | Network issue | Check internet/firewall |
| `LLM API错误` | Generic API problem | Check OpenRouter status/model name |
| `JSON格式无效` | Model returned non-JSON | Try with default model (fallback) |

## Files Modified

```
✏️  backend/app/utils/llm_client.py
    • Added API error handling (5 exception types)
    • Added debug logging
    • Better error messages

✏️  backend/app/services/ontology_generator.py
    • Added LLM call logging
    • Added validation logging
    • Better error propagation

✏️  backend/app/api/graph.py
    • Added specific error handling
    • Differentiated 400 vs 500 errors
    • Better logging levels
    • Added current_app import
```

## Verification

After restarting, check that:
- ✅ Backend starts without errors
- ✅ Frontend loads at http://localhost:3000
- ✅ Trying ontology generation shows specific error (not generic 500)
- ✅ Backend logs show debug information

---

**Status:** ✅ Ready to test
**Next:** Restart and check logs for specific error

