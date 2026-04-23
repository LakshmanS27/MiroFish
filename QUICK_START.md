# 🚀 MiroFish + OpenRouter - Quick Start (5 Minutes)

## Step 1: Get API Keys (2 min)

### OpenRouter Key
1. Go to https://openrouter.ai/
2. Sign up → Navigate to https://openrouter.ai/keys
3. Create a key → Copy it (starts with `sk-or-v1-`)

### Zep Key
1. Go to https://app.getzep.com/
2. Sign up → Go to API Keys section
3. Create a key → Copy it

## Step 2: Clone & Configure (1 min)

```bash
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish
cp .env.example .env
```

Edit `.env` and fill in:
```env
LLM_API_KEY=sk-or-v1-YOUR_KEY_HERE
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free
ZEP_API_KEY=YOUR_ZEP_KEY_HERE
```

## Step 3: Install & Run (2 min)

```bash
npm run setup:all    # Install dependencies (~2-3 min)
npm run dev          # Start project
```

## Step 4: Access

- **Frontend:** http://localhost:3000
- **Backend:** http://localhost:5001

## ✅ Done!

Start creating simulations! 🎉

---

## 📋 .env Template

```env
# ========== REQUIRED ==========
LLM_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxx
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free
ZEP_API_KEY=zep_xxxxxxxxxxxxxxxxxxxxxxxxx

# ========== OPTIONAL (parallel acceleration) ==========
# LLM_BOOST_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxx
# LLM_BOOST_BASE_URL=https://openrouter.io/api/v1
# LLM_BOOST_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free
```

---

## 🐳 Docker Alternative

```bash
cp .env.example .env
# Edit .env with keys
docker compose up -d
```

Access: http://localhost:3000

---

## 🆘 Having Issues?

See `SETUP_GUIDE.md` for detailed troubleshooting.

**Common issues:**
- ❌ "LLM_API_KEY 未配置" → Check `.env` exists & has key
- ❌ "401 Unauthorized" → Verify OpenRouter key is correct
- ❌ Port in use → Check process using port

---

## 📚 Full Documentation

- **Setup Guide:** `SETUP_GUIDE.md`
- **Integration Summary:** `OPENROUTER_INTEGRATION_SUMMARY.md`
- **Original README:** `README.md`

---

**Status:** ✅ OpenRouter Integration Complete
**Model:** Nvidia Nemotron-3-Super-120B (Free)
**Last Updated:** 2026-04-23
