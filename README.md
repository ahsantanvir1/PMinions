# 🤖 PMinions

**AI-Powered Desktop Agents for Project Management Automation**

> Empower project managers to focus on strategic decisions by automating repetitive administrative tasks through intelligent, locally-running AI agents.

## 🎯 Project Overview

PMinions is a SaaS platform that provides downloadable AI-powered desktop agents to automate project management tasks. The platform consists of:

1. **Web Application** (Vercel + Supabase): A modern marketplace for discovering, purchasing, and downloading PM automation agents
2. **Desktop Agents** (Python-based executables): Locally-running automation tools that integrate with organizational systems

## 🚀 Current Status

**Phase:** Foundation Setup  
**Version:** 0.1.0 (Pre-Alpha)  
**Target:** Minimal Proof of Concept

### ✅ Completed
- [x] Project structure created
- [x] Credentials management setup
- [x] Git repository initialized
- [x] Documentation framework

### 🔄 In Progress
- [ ] Next.js web application setup
- [ ] GitHub repository creation
- [ ] Vercel deployment pipeline
- [ ] Supabase database setup

### 📋 Next Steps
- [ ] Landing page development
- [ ] Authentication system
- [ ] Agent download flow
- [ ] Agent #1 development

## 📁 Project Structure

```
PMinions/
├── .credentials/           # Private credentials (gitignored)
├── .gitignore             # Git ignore rules
├── .env.local.template    # Environment variables template
├── pm-minions-prd.md      # Product Requirements Document
├── docs/                  # Documentation
│   └── setup-guide.md     # Setup instructions
├── web-app/               # Next.js application (coming soon)
└── README.md              # This file
```

## 🛠️ Tech Stack

### Web Application
- **Framework:** Next.js 14+ (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS + shadcn/ui
- **Backend:** Supabase (PostgreSQL + Auth + Storage)
- **Hosting:** Vercel
- **AI:** OpenAI API

### Desktop Agents (Future)
- **Language:** Python 3.11+
- **Packaging:** PyInstaller
- **GUI:** Tkinter

## 🔧 Development Setup

See [docs/setup-guide.md](docs/setup-guide.md) for detailed setup instructions.

### Quick Start

1. **Set up credentials** (see `.credentials/README.md`)
2. **Install dependencies:**
   ```bash
   cd web-app
   npm install
   ```
3. **Run development server:**
   ```bash
   npm run dev
   ```
4. **Open:** http://localhost:3000

## 📖 Documentation

- [Product Requirements Document](pm-minions-prd.md) - Complete PRD with architecture, features, and roadmap
- [Setup Guide](docs/setup-guide.md) - Development environment setup
- [Credentials Guide](.credentials/README.md) - How to manage API keys and tokens

## 🎨 Design Philosophy

1. **Minion-Themed Naming** - Fun, memorable agent names
2. **Hybrid AI Approach** - GPT-3.5-Turbo for speed, GPT-4 for complex tasks
3. **Privacy-First** - Local execution, data stays on user's machine
4. **Minimal Setup** - <10 minutes from signup to first use

## 🗺️ Roadmap

### Phase 1: MVP (Months 1-3)
- ✅ Foundation setup
- 🔄 Web app with landing page
- ⏳ Authentication system
- ⏳ Agent #1: Project Booking & Initiation

### Phase 2: Licensing (Months 4-6)
- ⏳ Organization accounts
- ⏳ Payment integration (Stripe)
- ⏳ License management

### Phase 3: Expansion (Months 7-12)
- ⏳ Agent #2-5 development
- ⏳ Inter-agent communication
- ⏳ Workflow orchestration

## 🤝 Contributing

This is currently a private project in early development.

## 📄 License

Proprietary - All rights reserved

## 📞 Contact

- **Project Lead:** (your name)
- **Email:** (your email)
- **Documentation:** [Setup Guide](docs/setup-guide.md)

---

**Status:** 🟡 In Development | **Last Updated:** November 21, 2025

