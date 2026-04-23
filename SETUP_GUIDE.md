# MiroFish Setup Guide - OpenRouter Integration

## 📋 Overview

This guide walks you through setting up **MiroFish** with **OpenRouter** using the free **Nvidia Nemotron-3-Super** model.

---

## 🔧 Prerequisites

Before starting, ensure you have:

| Tool | Version | Check |
|------|---------|-------|
| **Node.js** | 18+ | `node -v` |
| **Python** | 3.11 - 3.12 | `python --version` |
| **uv** (Python Package Manager) | Latest | `uv --version` |
| **Git** | Latest | `git --version` |

### Install Missing Tools

**Node.js & npm:**
```bash
# Download from https://nodejs.org/ (LTS version recommended)
```

**Python 3.11+ :**
```bash
# Download from https://www.python.org/
# Make sure Python is added to PATH
```

**uv (Python Package Manager):**
```bash
pip install uv
```

---

## 🚀 Step 1: Clone the Repository

```bash
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish
```

---

## 🔑 Step 2: Setup Environment Variables

### 2.1 Create `.env` File

```bash
cp .env.example .env
```

### 2.2 Get OpenRouter API Key

1. Go to **[OpenRouter](https://openrouter.ai/)**
2. Click **"Sign Up"** or **"Sign In"**
3. Navigate to **[Keys](https://openrouter.ai/keys)**
4. Create a new API key (click the **"Create Key"** button)
5. Copy the API key (starts with `sk-or-v1-`)

### 2.3 Get Zep Memory Service API Key

1. Go to **[Zep Cloud](https://app.getzep.com/)**
2. Sign up for a free account
3. Navigate to **API Keys** section
4. Create a new API key and copy it

### 2.4 Fill in `.env` File

Edit `.env` in your favorite editor and fill in:

```env
# ===== LLM Configuration with OpenRouter =====
LLM_API_KEY=sk-or-v1-YOUR_OPENROUTER_API_KEY_HERE
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free

# ===== Zep Memory Service Configuration =====
ZEP_API_KEY=YOUR_ZEP_API_KEY_HERE

# ===== Optional: Acceleration Configuration =====
# Uncomment if you want to use parallel acceleration
# LLM_BOOST_API_KEY=sk-or-v1-YOUR_BOOST_API_KEY_HERE
# LLM_BOOST_BASE_URL=https://openrouter.io/api/v1
# LLM_BOOST_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free
```

**Example filled `.env`:**
```env
LLM_API_KEY=sk-or-v1-abcdef123456789
LLM_BASE_URL=https://openrouter.io/api/v1
LLM_MODEL_NAME=nvidia/nemotron-3-super-120b-a12b:free

ZEP_API_KEY=zep_xyz123abc
```

---

## 📦 Step 3: Install Dependencies

### Option A: One-Click Installation (Recommended)

```bash
npm run setup:all
```

This installs:
- Node dependencies for frontend & root
- Python dependencies for backend (auto-creates virtual environment)

### Option B: Step-by-Step Installation

```bash
# Install Node dependencies
npm run setup

# Install Python backend dependencies
npm run setup:backend
```

---

## ▶️ Step 4: Start the Project

### Start Both Frontend & Backend

```bash
npm run dev
```

**Service URLs:**
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5001

### Start Services Individually

```bash
# Start backend only
npm run backend

# Start frontend only (in another terminal)
npm run frontend
```

---

## 📝 .env Configuration Reference

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `LLM_API_KEY` | OpenRouter API Key | `sk-or-v1-xxx...` |
| `LLM_BASE_URL` | OpenRouter API Endpoint | `https://openrouter.io/api/v1` |
| `LLM_MODEL_NAME` | Model Name | `nvidia/nemotron-3-super-120b-a12b:free` |
| `ZEP_API_KEY` | Zep Memory Service Key | `zep_xxx...` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LLM_BOOST_API_KEY` | Parallel acceleration API key | (disabled) |
| `LLM_BOOST_BASE_URL` | Parallel acceleration endpoint | (disabled) |
| `LLM_BOOST_MODEL_NAME` | Parallel acceleration model | (disabled) |
| `FLASK_DEBUG` | Flask debug mode | `True` |

---

## 🧪 Step 5: Test the Setup

### Test Backend API

```bash
# In a new terminal, check if backend is running
curl http://localhost:5001/health

# Expected response: Success status
```

### Test Frontend

Open your browser and navigate to:
```
http://localhost:3000
```

You should see the MiroFish interface.

---

## 🐳 Alternative: Docker Deployment

If you prefer using Docker:

```bash
# 1. Create .env file (same as Step 2)
cp .env.example .env
# Edit .env with your keys

# 2. Start with Docker Compose
docker compose up -d

# 3. Access the application
# Frontend: http://localhost:3000
# Backend: http://localhost:5001

# 4. View logs
docker compose logs -f

# 5. Stop services
docker compose down
```

---

## 📊 OpenRouter Model Information

### Nvidia Nemotron-3-Super-120B (Free Tier)

**Model ID:** `nvidia/nemotron-3-super-120b-a12b:free`

**Characteristics:**
- ✅ **Free** to use
- 🚀 **120B parameters** - High-quality reasoning
- 📚 **128K context window** - Can handle large documents
- 🎯 **Excellent instruction following** - Great for agentic workflows
- ⚡ **Reliable for multi-agent simulations**

**Pricing:** Free tier with reasonable rate limits

For more models, visit: https://openrouter.ai/models

---

## 🔍 Troubleshooting

### Issue: "LLM_API_KEY 未配置" (LLM_API_KEY not configured)

**Solution:**
- Check if `.env` file exists in project root
- Verify `LLM_API_KEY` is filled in (not placeholder text)
- Restart backend after editing `.env`

### Issue: "401 Unauthorized" from OpenRouter

**Solution:**
- Verify API key is correct (copy from OpenRouter dashboard again)
- Check key starts with `sk-or-v1-`
- Ensure you have free credits on OpenRouter account

### Issue: "ZEP_API_KEY not found"

**Solution:**
- Get API key from https://app.getzep.com/
- Add to `.env` file
- Restart backend

### Issue: Port 3000 or 5001 already in use

**Solution:**
```bash
# Find process using port
# On Windows: netstat -ano | findstr :3000
# On Mac/Linux: lsof -i :3000

# Kill the process or use different port
# Modify package.json scripts if needed
```

### Issue: Python version conflict

**Solution:**
```bash
# Check Python version
python --version

# If not 3.11 or 3.12, install correct version
# Then create virtual environment manually
uv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

## 🎯 Quick Commands Reference

```bash
# Setup
npm run setup:all          # Install all dependencies
npm run setup              # Install Node dependencies only
npm run setup:backend      # Install Python dependencies only

# Development
npm run dev                # Start frontend + backend
npm run backend            # Start backend only
npm run frontend           # Start frontend only

# Building
npm run build              # Build frontend
npm run build:backend      # Build backend

# Cleanup
npm run clean              # Clean all build artifacts
```

---

## 📚 Project Structure

```
MiroFish/
├── frontend/              # React frontend
├── backend/
│   ├── app/
│   │   ├── utils/
│   │   │   └── llm_client.py    # LLM client (OpenRouter compatible)
│   │   ├── config.py             # Configuration loader
│   │   └── api/                  # REST API endpoints
│   └── scripts/                  # Simulation scripts
├── .env                  # Environment variables (create this)
├── .env.example          # Environment template
└── package.json          # Node.js configuration
```

---

## 🚨 Important Notes

1. **API Costs:** While Nemotron-3-Super is free, extensive simulations may consume credits. Monitor your OpenRouter account.

2. **Simulation Rounds:** Start with <40 rounds for testing to minimize API costs.

3. **Memory Service:** Zep is used for agent memory. Free tier has monthly limits.

4. **Git Ignore:** Never commit `.env` file to git. Keep API keys private!

---

## 🆘 Getting Help

- **GitHub Issues:** https://github.com/666ghj/MiroFish/issues
- **Discord Community:** http://discord.gg/ePf5aPaHnA
- **Email Support:** mirofish@shanda.com

---

## ✅ You're Ready!

Your MiroFish instance is now set up with OpenRouter. Start by uploading a document and creating your first prediction simulation!

**Next Steps:**
1. Open http://localhost:3000 in your browser
2. Upload a sample document or text
3. Create a simulation scenario
4. Watch the magic happen! ✨

---

**Last Updated:** 2026-04-23
**MiroFish Version:** Latest
**OpenRouter Integration:** ✅ Complete
