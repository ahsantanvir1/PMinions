# PMinions - Setup Guide

## 🚀 Quick Start Guide

This guide will help you set up the PMinions development environment from scratch.

## Prerequisites

- ✅ macOS (your current OS)
- ✅ Node.js 18+ installed
- ✅ Python 3.11+ installed
- ✅ Git installed
- ✅ GitHub account
- ✅ Vercel account
- ✅ Supabase account
- ✅ OpenAI account

## Step 1: Set Up Credentials

1. Navigate to `.credentials/` directory
2. Follow instructions in `.credentials/README.md`
3. Fill in all four credential files:
   - `github-token.txt`
   - `vercel-token.txt`
   - `supabase-credentials.txt`
   - `openai-key.txt`

## Step 2: Initialize Git Repository

```bash
cd ~/Documents/Cursor\ -\ Projects/PMinions
git init
git add .
git commit -m "Initial commit: Project structure and credentials setup"
```

## Step 3: Create GitHub Repository

The AI assistant will help you create the GitHub repository using your token.

## Step 4: Set Up Next.js Web Application

```bash
cd web-app
npm install
npm run dev
```

Visit: http://localhost:3000

## Step 5: Deploy to Vercel

The AI assistant will help you connect to Vercel and deploy.

## Step 6: Set Up Supabase

The AI assistant will help you set up the database schema.

## Project Structure

```
PMinions/
├── .credentials/           # Your private credentials (gitignored)
├── .gitignore             # Git ignore rules
├── .env.local.template    # Environment variables template
├── pm-minions-prd.md      # Product Requirements Document
├── docs/                  # Documentation
│   └── setup-guide.md     # This file
└── web-app/               # Next.js application (to be created)
```

## Development Workflow

1. **Local Development**: `npm run dev` in web-app/
2. **Testing**: `npm test`
3. **Build**: `npm run build`
4. **Deploy**: Push to main branch (auto-deploys to Vercel)

## Troubleshooting

### Issue: npm install fails
- Solution: Make sure Node.js 18+ is installed: `node --version`

### Issue: Can't connect to Supabase
- Solution: Check your credentials in `.env.local`

### Issue: Vercel deployment fails
- Solution: Check Vercel token in `.credentials/vercel-token.txt`

## Next Steps

After setup is complete:
1. ✅ Build landing page
2. ✅ Add authentication
3. ✅ Create agent download flow
4. ✅ Develop Agent #1

## Support

- Documentation: (to be created)
- Issues: GitHub Issues
- Contact: (your email)

