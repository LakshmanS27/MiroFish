# 🚀 START HERE - MiroFish OpenRouter Setup

> **Status:** ✅ Everything is ready!  
> **Cost:** FREE ($0)  
> **Setup Time:** 5-15 minutes

---

## ⚡ 30-Second Overview

MiroFish is a multi-agent AI simulation engine. It's now fully integrated with **OpenRouter** using the free **Nvidia Nemotron-3-Super** model.

**What you get:**
- ✅ Free LLM (no API costs)
- ✅ Multi-agent simulations
- ✅ Memory system for agents
- ✅ Report generation
- ✅ Interactive web UI

---

## 🎯 Quick Start (5 minutes)

### Step 1: Clone (30 seconds)
```bash
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish
```

### Step 2: Get API Keys (3 minutes)

**OpenRouter Key:**
1. Go to: https://openrouter.ai/keys
2. Click "Create Key"
3. Copy the key (starts with `sk-or-v1-`)

**Zep Key:**
1. Go to: https://app.getzep.com/
2. Create account, get API key

### Step 3: Configure (1 minute)
```bash
cp .env.example .env
```

Edit `.env` and add your keys:
```env
LLM_API_KEY=sk-or-v1-YOUR_KEY_HERE
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free
ZEP_API_KEY=YOUR_ZEP_KEY_HERE
```

### Step 4: Install & Run (2-3 minutes)
```bash
npm run setup:all   # Install everything
npm run dev         # Start servers
```

### Step 5: Open Browser
```
http://localhost:3000
```

**Done! 🎉**

---

## 📚 Documentation Files

### For Different Styles:

**⚡ "Just run it NOW"** (3 min)
→ Read: `QUICK_START.md`

**📖 "Give me full instructions"** (15 min)
→ Read: `SETUP_GUIDE.md`

**🔑 "Help with configuration"** (10 min)
→ Read: `ENV_VARIABLES.md`

**🔧 "What technically changed?"** (8 min)
→ Read: `OPENROUTER_INTEGRATION_SUMMARY.md`

**✅ "Verify everything is ready"** (5 min)
→ Read: `PROJECT_STATUS.md`

**📋 "Plain text summary"**
→ Read: `COMPLETION_SUMMARY.txt`

**📁 "File changes summary"**
→ Read: `FILES_SUMMARY.md`

---

## ✅ Checklist Before Running

- [ ] Git installed
- [ ] Node.js 18+ installed (`node -v`)
- [ ] Python 3.11-3.12 installed (`python --version`)
- [ ] `.env` file created and filled
- [ ] OpenRouter key copied (starts with `sk-or-v1-`)
- [ ] Zep key copied

---

## 🔑 API Keys Needed

| Service | Get From | Cost | Purpose |
|---------|----------|------|---------|
| **OpenRouter** | https://openrouter.ai/keys | ✅ FREE | LLM model |
| **Zep** | https://app.getzep.com/ | ✅ FREE | Memory system |

**Total Cost:** $0 USD

---

## 📋 Example .env

```env
LLM_API_KEY=sk-or-v1-abcdef123456789
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free
ZEP_API_KEY=zep_xyz123abc
```

---

## 🚨 Common Errors & Quick Fixes

**Error:** `LLM_API_KEY 未配置`
- **Fix:** Edit `.env` and add your OpenRouter key

**Error:** `401 Unauthorized`
- **Fix:** Verify OpenRouter key is correct and active

**Error:** Port 3000 already in use
- **Fix:** Kill process on port 3000 or use different port

**Error:** Python version not supported
- **Fix:** Install Python 3.11 or 3.12

**Need help?** See `SETUP_GUIDE.md` → Troubleshooting section

---

## 📝 What Was Changed

**2 Files Modified:**
1. `backend/app/utils/llm_client.py` - Added OpenRouter support
2. `.env.example` - Updated with OpenRouter config

**6 Files Created:**
- `QUICK_START.md`
- `SETUP_GUIDE.md`
- `ENV_VARIABLES.md`
- `OPENROUTER_INTEGRATION_SUMMARY.md`
- `PROJECT_STATUS.md`
- Plus this file!

**Backward Compatible:** ✅ Yes (other LLM providers still work)

---

## 🎯 Next Steps

**Immediate:**
1. Choose a documentation file above
2. Get API keys
3. Run `npm run dev`

**After Setup:**
1. Open http://localhost:3000
2. Upload a document
3. Create a simulation
4. Watch the AI agents work!

---

## 📞 Need Help?

- **Quick questions?** See `QUICK_START.md`
- **Setup issues?** See `SETUP_GUIDE.md` → Troubleshooting
- **Config questions?** See `ENV_VARIABLES.md`
- **Discord:** http://discord.gg/ePf5aPaHnA
- **GitHub:** https://github.com/666ghj/MiroFish
- **Email:** mirofish@shanda.com

---

## 💡 Pro Tips

1. **Start small** - Use <40 simulation rounds for testing
2. **Monitor credits** - Check OpenRouter dashboard occasionally
3. **Read the docs** - Each one serves a different purpose
4. **Join Discord** - Get help and updates from community
5. **Upgrade later** - Start free, upgrade models if needed

---

## ✨ Features

- ✅ Multi-agent AI simulations
- ✅ Knowledge graph building
- ✅ Long-term agent memory (Zep)
- ✅ Report generation
- ✅ REST API
- ✅ Docker support
- ✅ Easy provider switching

---

## 📊 Current Setup

| Component | Status | Details |
|-----------|--------|---------|
| OpenRouter Integration | ✅ Ready | Nvidia Nemotron-3-Super |
| Documentation | ✅ Complete | 7+ files with full guides |
| Code Changes | ✅ Done | Backward compatible |
| Configuration | ✅ Ready | Just need API keys |
| Deployment | ✅ Ready | Source or Docker |

---

## 🎬 What Happens After You Run `npm run dev`

1. **Backend starts** on http://localhost:5001
2. **Frontend builds** and starts on http://localhost:3000
3. **Open browser** to http://localhost:3000
4. **You see** the MiroFish UI
5. **Upload** a document or text
6. **Create** a simulation scenario
7. **Watch** AI agents interact
8. **Generate** detailed reports

---

## 🚀 I'm Ready!

### Choose your path:

**Impatient?**
```bash
cat QUICK_START.md        # 3 min read
# Then run the commands
```

**Thorough?**
```bash
cat SETUP_GUIDE.md        # 15 min read
# Then run step by step
```

**Visual person?**
```bash
cat PROJECT_STATUS.md     # 5 min read
# Then follow checklist
```

---

## 📌 Bookmarks for Later

- **Setup issues?** → `SETUP_GUIDE.md`
- **Config help?** → `ENV_VARIABLES.md`
- **What changed?** → `OPENROUTER_INTEGRATION_SUMMARY.md`
- **All files?** → `FILES_SUMMARY.md`

---

## 🎉 Let's Go!

1. Get your API keys (5 min)
2. Edit `.env` (1 min)
3. Run `npm run setup:all` (3 min)
4. Run `npm run dev` (1 min)
5. Open http://localhost:3000 (0 min)

**Total: ~10 minutes to a working system!**

---

**Status:** ✅ Everything is ready to go!  
**Last Updated:** 2026-04-23  
**Cost:** FREE  

Happy predicting! 🚀

---

## 🔗 Quick Links

- OpenRouter: https://openrouter.ai/
- Zep: https://app.getzep.com/
- GitHub: https://github.com/666ghj/MiroFish
- Discord: http://discord.gg/ePf5aPaHnA

---

**Choose your documentation file above and get started!**
