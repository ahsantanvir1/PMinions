# Vercel Deployment Setup Guide

This guide will help you deploy the PMinions web application to Vercel with continuous deployment from GitHub.

## Prerequisites

- GitHub account
- Vercel account (sign up at https://vercel.com)
- Supabase project (for database and authentication)

## Step 1: Create Vercel Project

### Option A: Via Vercel Dashboard (Recommended)

1. Go to https://vercel.com/dashboard
2. Click "Add New..." → "Project"
3. Import your GitHub repository:
   - If not connected, click "Connect GitHub Account"
   - Select the `PMinions` repository
   - Click "Import"

4. Configure project:
   - **Framework Preset:** Next.js
   - **Root Directory:** `web-app`
   - **Build Command:** `npm run build` (auto-detected)
   - **Output Directory:** `.next` (auto-detected)
   - **Install Command:** `npm install` (auto-detected)

5. Add Environment Variables:
   ```
   NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
   SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here
   NEXT_PUBLIC_ENV=production
   ```

6. Click "Deploy"

### Option B: Via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy from web-app directory
cd web-app
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Select your account
# - Link to existing project? No
# - Project name? pminions (or your preferred name)
# - Directory? ./ (current directory)
# - Override settings? No

# Deploy to production
vercel --prod
```

## Step 2: Get Vercel Credentials for GitHub Actions

### Get Vercel Token

1. Go to https://vercel.com/account/tokens
2. Click "Create Token"
3. Name: `GitHub Actions - PMinions`
4. Scope: Full Account
5. Expiration: No Expiration (or set as needed)
6. Click "Create"
7. **Copy the token** (you won't see it again!)

### Get Organization ID and Project ID

```bash
# Install Vercel CLI if not already installed
npm install -g vercel

# Login
vercel login

# Navigate to web-app directory
cd web-app

# Link to your Vercel project
vercel link

# Get project info
cat .vercel/project.json
```

You'll see output like:
```json
{
  "orgId": "team_xxxxxxxxxxxx",
  "projectId": "prj_xxxxxxxxxxxx"
}
```

## Step 3: Configure GitHub Secrets

1. Go to your GitHub repository
2. Click "Settings" → "Secrets and variables" → "Actions"
3. Click "New repository secret" for each:

| Secret Name | Value | Where to Get It |
|------------|-------|-----------------|
| `VERCEL_TOKEN` | Your Vercel token | Step 2 above |
| `VERCEL_ORG_ID` | Your org ID | `cat .vercel/project.json` |
| `VERCEL_PROJECT_ID` | Your project ID | `cat .vercel/project.json` |
| `NEXT_PUBLIC_SUPABASE_URL` | Your Supabase URL | Supabase Dashboard → Settings → API |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Your Supabase anon key | Supabase Dashboard → Settings → API |

## Step 4: Set Up Supabase (if not already done)

1. Go to https://supabase.com/dashboard
2. Create a new project:
   - **Name:** PMinions Production
   - **Database Password:** (generate strong password)
   - **Region:** Choose closest to your users
   - **Pricing Plan:** Free (for now)

3. Get your credentials:
   - Go to Settings → API
   - Copy **Project URL** → Use as `NEXT_PUBLIC_SUPABASE_URL`
   - Copy **anon/public key** → Use as `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - Copy **service_role key** → Use as `SUPABASE_SERVICE_ROLE_KEY` (keep secret!)

4. Set up authentication:
   - Go to Authentication → Providers
   - Enable Email provider
   - Configure email templates (optional)

## Step 5: Test Deployment

### Automatic Deployment (via GitHub Actions)

1. Make a change to any file in `web-app/`
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "test: Trigger deployment"
   git push origin main
   ```

3. Watch the deployment:
   - Go to GitHub → Actions tab
   - You should see "Deploy Web App to Vercel" workflow running
   - Click on it to see progress

4. Once complete, visit your site:
   - Production: https://pminions.vercel.app (or your custom domain)
   - Check the Actions summary for the exact URL

### Manual Deployment (via Vercel CLI)

```bash
cd web-app

# Deploy to preview
vercel

# Deploy to production
vercel --prod
```

## Step 6: Configure Custom Domain (Optional)

1. Go to Vercel Dashboard → Your Project → Settings → Domains
2. Click "Add Domain"
3. Enter your domain (e.g., `pminions.com`)
4. Follow DNS configuration instructions
5. Wait for DNS propagation (can take up to 48 hours)

### DNS Configuration Example

For `pminions.com`:
```
Type: A
Name: @
Value: 76.76.21.21

Type: CNAME
Name: www
Value: cname.vercel-dns.com
```

## Step 7: Verify Deployment

### Check Production Site

1. Visit your Vercel URL (e.g., https://pminions.vercel.app)
2. Verify the landing page loads correctly
3. Check browser console for errors (F12 → Console)
4. Test navigation and links

### Verify Environment Variables

Create a test API route to verify env vars are loaded:

```typescript
// web-app/src/app/api/health/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    status: 'ok',
    environment: process.env.NEXT_PUBLIC_ENV,
    supabase_configured: !!process.env.NEXT_PUBLIC_SUPABASE_URL,
    timestamp: new Date().toISOString()
  });
}
```

Visit: `https://your-site.vercel.app/api/health`

Expected response:
```json
{
  "status": "ok",
  "environment": "production",
  "supabase_configured": true,
  "timestamp": "2025-11-22T..."
}
```

## Deployment Workflow

### Automatic Deployments

- **Push to `main` branch** → Production deployment
- **Open Pull Request** → Preview deployment (comment added to PR)
- **Push to PR branch** → Updated preview deployment

### Manual Deployments

```bash
# Preview deployment
cd web-app && vercel

# Production deployment
cd web-app && vercel --prod

# Rollback to previous deployment
vercel rollback
```

## Troubleshooting

### Build Fails

**Error:** `Module not found: Can't resolve 'X'`

**Solution:**
```bash
cd web-app
rm -rf node_modules package-lock.json
npm install
npm run build  # Test locally first
```

### Environment Variables Not Working

**Error:** `undefined` when accessing env vars

**Solution:**
1. Verify secrets are set in GitHub (Settings → Secrets)
2. Verify env vars are set in Vercel (Dashboard → Project → Settings → Environment Variables)
3. Redeploy after adding env vars
4. Ensure env vars start with `NEXT_PUBLIC_` for client-side access

### Deployment Succeeds but Site Shows 404

**Problem:** Vercel can't find the Next.js app

**Solution:**
1. Verify Root Directory is set to `web-app` in Vercel project settings
2. Check `vercel.json` is in the `web-app/` directory
3. Redeploy

### GitHub Actions Workflow Not Running

**Problem:** Workflow doesn't trigger on push

**Solution:**
1. Verify `.github/workflows/deploy-web-app.yml` exists in repository root
2. Check the `paths` filter in workflow file
3. Ensure you're pushing to `main` branch
4. Check GitHub Actions is enabled (Settings → Actions → General)

## Monitoring & Logs

### View Deployment Logs

1. Vercel Dashboard → Your Project → Deployments
2. Click on a deployment
3. View "Build Logs" and "Function Logs"

### View Runtime Logs

```bash
# Install Vercel CLI
npm install -g vercel

# View logs
vercel logs pminions --follow
```

### Set Up Monitoring (Optional)

1. **Vercel Analytics** (built-in):
   - Go to Project → Analytics
   - View Web Vitals, page views, etc.

2. **Sentry** (error tracking):
   - Sign up at https://sentry.io
   - Install: `npm install @sentry/nextjs`
   - Configure in `web-app/sentry.client.config.js`

## Next Steps

1. ✅ Web app deployed to Vercel
2. ⏭️ Set up Supabase database schema
3. ⏭️ Implement authentication
4. ⏭️ Build agent download functionality
5. ⏭️ Configure custom domain

## Useful Commands

```bash
# Check deployment status
vercel ls

# View project info
vercel inspect

# View environment variables
vercel env ls

# Add environment variable
vercel env add VARIABLE_NAME

# Remove deployment
vercel rm deployment-url

# View help
vercel --help
```

## Support

- **Vercel Docs:** https://vercel.com/docs
- **Next.js Docs:** https://nextjs.org/docs
- **Supabase Docs:** https://supabase.com/docs
- **GitHub Actions Docs:** https://docs.github.com/en/actions

---

**Last Updated:** November 22, 2025  
**Maintained by:** PMinions Team

