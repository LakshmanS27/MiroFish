# 📋 MiroFish Environment Variables - Complete Reference

## Overview

All MiroFish configuration is managed through `.env` file in the project root. Use `.env.example` as a template.

---

## 🔑 Required Variables

### LLM Configuration (Primary Model)

| Variable | Value | Source | Example |
|----------|-------|--------|---------|
| **LLM_API_KEY** | OpenRouter API Key | https://openrouter.ai/keys | `sk-or-v1-abcdef...` |
| **LLM_BASE_URL** | API Endpoint | Fixed value | `https://openrouter.io/api/v1` |
| **LLM_MODEL_NAME** | Model Identifier | Model registry | `nvidia/nemotron-3-super-120b-a12b:free` |

### Memory Service Configuration

| Variable | Value | Source | Example |
|----------|-------|--------|---------|
| **ZEP_API_KEY** | Zep Memory Service Key | https://app.getzep.com/ | `zep_abc123...` |

---

## 📝 Complete .env File Example

```env
# ===== LLM API Configuration =====
# Primary LLM provider configuration (OpenAI SDK compatible)

# Option: OpenRouter with Nvidia Nemotron-3-Super (RECOMMENDED - FREE)
LLM_API_KEY=sk-or-v1-your_openrouter_key_here
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free

# Alternative Option: Alibaba Qwen via Bailian
# (Uncomment to use instead of OpenRouter)
# LLM_API_KEY=your_alibaba_key_here
# LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
# LLM_MODEL_NAME=qwen-plus

# ===== Zep Memory Service Configuration =====
# Required for agent memory and knowledge graphs
ZEP_API_KEY=your_zep_api_key_here

# ===== Optional: Acceleration Configuration =====
# For parallel simulation execution (experimental)
# Only uncomment if you plan to use parallel simulations

# LLM_BOOST_API_KEY=sk-or-v1-your_boost_key_here
# LLM_BOOST_BASE_URL=https://openrouter.io/api/v1
# LLM_BOOST_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free

# ===== Flask Configuration (Optional) =====
# FLASK_DEBUG=True
```

---

## 🔑 How to Get Each API Key

### Step 1: OpenRouter API Key

```
1. Visit: https://openrouter.ai/
2. Click "Sign Up" or "Sign In"
3. Go to: https://openrouter.ai/keys
4. Click "Create Key" button
5. Copy the key (format: sk-or-v1-xxxx...)
6. Paste into LLM_API_KEY in .env
```

**Cost:** Free tier available with Nemotron-3-Super model

**Status Check:**
```bash
curl -H "Authorization: Bearer sk-or-v1-xxx" \
  https://openrouter.io/api/v1/models
```

### Step 2: Zep Memory Service Key

```
1. Visit: https://app.getzep.com/
2. Click "Sign Up" (create free account)
3. Go to: API Keys section (usually in settings)
4. Create a new API key
5. Copy and paste into ZEP_API_KEY in .env
```

**Cost:** Free monthly quota sufficient for testing

**Status Check:**
```bash
curl -H "Authorization: Bearer zep_xxx" \
  https://api.getzep.com/api/v1/health
```

---

## 📊 Configuration Scenarios

### Scenario 1: Free OpenRouter Setup (Recommended)

Use this for testing and free tier:

```env
# Free model from OpenRouter
LLM_API_KEY=sk-or-v1-your_openrouter_key
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free

# Free Zep tier
ZEP_API_KEY=your_zep_key
```

**Cost:** ✅ Free (reasonable rate limits)

### Scenario 2: Production with Alibaba Qwen

For production with higher quality:

```env
LLM_API_KEY=your_alibaba_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

ZEP_API_KEY=your_zep_key
```

**Cost:** ⚠️ Paid (higher quality, faster)

### Scenario 3: Premium OpenAI

For highest quality (most expensive):

```env
LLM_API_KEY=sk-xxx_openai_key
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL_NAME=gpt-4o

ZEP_API_KEY=your_zep_key
```

**Cost:** 💰 Premium (best quality, highest cost)

### Scenario 4: Parallel Acceleration

For faster large-scale simulations:

```env
# Primary LLM
LLM_API_KEY=sk-or-v1-your_key_1
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free

# Acceleration LLM (for parallel runs)
LLM_BOOST_API_KEY=sk-or-v1-your_key_2
LLM_BOOST_BASE_URL=https://openrouter.io/api/v1
LLM_BOOST_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free

# Memory service
ZEP_API_KEY=your_zep_key
```

---

## ✅ Validation Checklist

Before running, ensure:

- [ ] `.env` file exists in project root (not `.env.example`)
- [ ] `LLM_API_KEY` is filled (not placeholder text)
- [ ] `LLM_BASE_URL` is correct endpoint
- [ ] `LLM_MODEL_NAME` is valid model ID
- [ ] `ZEP_API_KEY` is filled
- [ ] Keys start with correct prefix:
  - OpenRouter: `sk-or-v1-`
  - Zep: `zep_`
- [ ] No extra whitespace in keys
- [ ] File is saved after editing

### Quick Validation Script

```bash
# Check .env file
if [ -f .env ]; then
  echo "✅ .env file exists"
  grep "LLM_API_KEY" .env | grep -v "^#"
  grep "ZEP_API_KEY" .env | grep -v "^#"
else
  echo "❌ .env file missing"
fi
```

---

## 🚨 Common Issues & Solutions

### Issue: "LLM_API_KEY 未配置"

**Cause:** Missing or empty LLM_API_KEY in .env

**Solution:**
```bash
# Check if .env exists
ls -la .env

# Check if key is present
grep "LLM_API_KEY" .env

# Verify it's not a placeholder
cat .env | grep LLM_API_KEY | grep -v "your_"
```

### Issue: "401 Unauthorized" from OpenRouter

**Cause:** Invalid or expired API key

**Solution:**
```bash
# Test key directly
curl -H "Authorization: Bearer YOUR_KEY" \
  https://openrouter.io/api/v1/models

# Get new key from: https://openrouter.ai/keys
# Update .env with new key
```

### Issue: ZEP Connection Failed

**Cause:** Missing or invalid ZEP_API_KEY

**Solution:**
```bash
# Verify ZEP key exists in .env
grep "ZEP_API_KEY" .env

# Test key
curl -H "Authorization: Bearer YOUR_ZEP_KEY" \
  https://api.getzep.com/api/v1/health
```

---

## 🔄 Environment Variable Loading

MiroFish loads environment variables in this order:

1. **Project Root `.env`** (highest priority)
   - Location: `MiroFish/.env`
   - Used in development

2. **System Environment Variables** (fallback)
   - Used in Docker/production
   - Requires manual setup

3. **Hardcoded Defaults** (lowest priority)
   - `LLM_BASE_URL`: `https://api.openai.com/v1`
   - `LLM_MODEL_NAME`: `gpt-4o-mini`

---

## 🔐 Security Best Practices

1. **Never Commit .env**
   ```bash
   # Already in .gitignore, but verify
   cat .gitignore | grep ".env"
   ```

2. **Keep Keys Private**
   - Don't share `.env` file
   - Don't paste keys in chat/emails
   - Rotate keys regularly

3. **Use Service-Specific Keys**
   - Create separate OpenRouter key for MiroFish
   - Don't reuse keys across projects
   - Can revoke without affecting other services

4. **Monitor Usage**
   - Check OpenRouter dashboard: https://openrouter.ai/account
   - Check Zep usage: https://app.getzep.com/

---

## 📞 Support

If you have issues with configuration:

1. **Check SETUP_GUIDE.md** - Detailed setup instructions
2. **Check QUICK_START.md** - 5-minute quick start
3. **GitHub Issues** - https://github.com/666ghj/MiroFish/issues
4. **Discord** - http://discord.gg/ePf5aPaHnA
5. **Email** - mirofish@shanda.com

---

## 🔗 Quick Links

| Service | Link | Purpose |
|---------|------|---------|
| **OpenRouter** | https://openrouter.ai | Get LLM API key |
| **Zep** | https://app.getzep.com | Get memory service key |
| **OpenRouter Models** | https://openrouter.io/models | Browse available models |
| **Zep Docs** | https://docs.getzep.com | Memory service documentation |

---

## 📋 Variable Reference Table

| Variable | Required | Type | Default | Examples |
|----------|----------|------|---------|----------|
| `LLM_API_KEY` | ✅ Yes | String | None | `sk-or-v1-xxx` |
| `LLM_BASE_URL` | ✅ Yes | URL | `https://api.openai.com/v1` | `https://openrouter.io/api/v1` |
| `LLM_MODEL_NAME` | ✅ Yes | String | `gpt-4o-mini` | `nvidia/nemotron-3-super-120b-a12b:free` |
| `ZEP_API_KEY` | ✅ Yes | String | None | `zep_xxx` |
| `LLM_BOOST_API_KEY` | ❌ No | String | None | `sk-or-v1-xxx` |
| `LLM_BOOST_BASE_URL` | ❌ No | URL | None | `https://openrouter.io/api/v1` |
| `LLM_BOOST_MODEL_NAME` | ❌ No | String | None | `nvidia/nemotron-3-super-120b-a12b:free` |
| `FLASK_DEBUG` | ❌ No | Boolean | `True` | `True`, `False` |

---

**Last Updated:** 2026-04-23
**Status:** ✅ OpenRouter Integration Complete
