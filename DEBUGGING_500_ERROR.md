# Debugging 500 Error - Ontology Generation

## Issue
Backend returns HTTP 500 when calling `/api/graph/ontology/generate` with OpenRouter API

## Changes Made

### 1. Enhanced Error Handling in `backend/app/utils/llm_client.py`
- ✅ Added specific exception handlers for OpenRouter API errors
- ✅ Added logging for debugging (request and response)
- ✅ Improved error messages to distinguish between:
  - `AuthenticationError` - Invalid/expired API key
  - `RateLimitError` - Rate limit exceeded
  - `APIConnectionError` - Network/connection issues
  - `APIError` - Generic API errors

### 2. Improved Logging in `backend/app/services/ontology_generator.py`
- ✅ Added logging for LLM call parameters
- ✅ Added logging for JSON parsing
- ✅ Logs model name, prompt lengths, response details

### 3. Better Error Responses in `backend/app/api/graph.py`
- ✅ Separate handling for `ValueError` (API errors) - returns 400 with error message
- ✅ Separate handling for unexpected exceptions - returns 500 with generic message
- ✅ Different log levels: warning for expected errors, error for unexpected
- ✅ Debug mode shows full error details, production hides them

## Next Steps to Debug

### Check Backend Logs
```bash
# The backend will now log:
# 1. What model is being used
# 2. Message lengths (system prompt vs user message)
# 3. API call parameters
# 4. Specific API error type
```

**Log file:** `backend/logs/YYYY-MM-DD.log`

### Verify .env Configuration

```bash
# Check your .env file has:
LLM_API_KEY=sk-or-v1-xxxxxxxxxxxxx      # Must start with sk-or-v1-
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free
ZEP_API_KEY=zep_xxxxxxxxxxxxx
```

### Test OpenRouter API Directly

```bash
# Test if your OpenRouter key works
curl -X POST https://openrouter.io/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-or-v1-YOUR_KEY_HERE" \
  -H "HTTP-Referer: https://mirofish.ai" \
  -H "X-Title: MiroFish" \
  -d '{
    "model": "nvidia/nemotron-3-super-120b-a12b:free",
    "messages": [
      {"role": "user", "content": "Say hello"}
    ]
  }'
```

### Most Likely Causes & Solutions

1. **Invalid or Expired API Key**
   - ❌ Error: `AuthenticationError` / 401 Unauthorized
   - ✅ Solution: Get new key from https://openrouter.ai/keys

2. **Model Name Incorrect**
   - ❌ Error: `APIError` / 404 Not Found
   - ✅ Solution: Check model is available at https://openrouter.ai/models
   - ✅ Current: `nvidia/nemotron-3-super-120b-a12b:free`

3. **Rate Limit Exceeded (Free Tier)**
   - ❌ Error: `RateLimitError` / 429 Too Many Requests
   - ✅ Solution: Wait a bit or upgrade account

4. **JSON Response Format Not Supported**
   - ❌ Error: `JSONDecodeError` when parsing response
   - ✅ Solution: Model might not support `response_format={"type": "json_object"}`
   - ✅ Fallback: Some models need workaround

5. **Network/Connectivity Issue**
   - ❌ Error: `APIConnectionError`
   - ✅ Solution: Check internet connection, firewall settings

## How to Read Logs

After making a request to ontology generate, check logs for:

```
[HH:MM:SS] DEBUG: LLM Request: model=nvidia/nemotron-3-super-120b-a12b:free, base_url=https://openrouter.io/api/v1, temp=0.3, max_tokens=4096
[HH:MM:SS] INFO: Calling LLM to generate ontology: model=nvidia/nemotron-3-super-120b-a12b:free, system_prompt_len=2000, user_msg_len=3000
[HH:MM:SS] ERROR: LLM call failed during ontology generation: <specific error message>
```

## Testing the Fix

1. **Restart backend:**
   ```bash
   npm run dev
   ```

2. **Try again in frontend:**
   - Upload a document
   - Fill in simulation requirement
   - Click generate

3. **Check the error response:**
   - It should now have a meaningful error message
   - Check browser console for error details

4. **Check backend logs:**
   - See specific error type
   - Understand what went wrong

## If It Still Fails

Please share:
1. The error message from the browser console
2. The relevant lines from `backend/logs/YYYY-MM-DD.log`
3. Your `.env` file (redact API keys except first 10 chars)

Then we can diagnose the exact issue.

---

## Code Changes Summary

### Before
```python
# No error handling
result = self.llm_client.chat_json(messages, temp, tokens)
```

### After
```python
# With error handling
try:
    result = self.llm_client.chat_json(messages, temp, tokens)
except ValueError as e:
    logger.error(f"LLM call failed: {str(e)}")
    raise
```

---

**Status:** ✅ Error handling improved
**Next:** Restart server and check logs for actual error
