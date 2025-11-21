# PMinions - Product Requirements Document (PRD)

**Version:** 1.0  
**Date:** November 20, 2025  
**Status:** Draft  
**Owner:** Product Team  
**Target Platform:** Web App (Vercel) + Desktop Agents (Windows)

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Product Vision & Goals](#product-vision--goals)
3. [User Personas](#user-personas)
4. [Product Architecture](#product-architecture)
5. [Feature Requirements](#feature-requirements)
6. [Technical Specifications](#technical-specifications)
7. [Database Schema](#database-schema)
8. [API Specifications](#api-specifications)
9. [UI/UX Design System](#uiux-design-system)
10. [Security & Compliance](#security--compliance)
11. [Testing Strategy](#testing-strategy)
12. [Deployment & CI/CD](#deployment--cicd)
13. [Success Metrics](#success-metrics)
14. [Risks & Mitigations](#risks--mitigations)
15. [Roadmap](#roadmap)

---

## 1. Executive Summary

**PMinions** is a SaaS platform that provides downloadable AI-powered desktop agents to automate project management tasks. The platform consists of:

1. **Web Application** (Vercel + Supabase): A modern marketplace for discovering, purchasing, and downloading PM automation agents
2. **Desktop Agents** (Python-based executables): Locally-running automation tools that integrate with organizational systems (Outlook, network drives) and AI (ChatGPT) to perform PM tasks

**Initial Release:** Agent #1 - Project Booking and Initiation
- Automates email-based project assignment workflows
- Parses project codes (AEMA-xxxxx format)
- Manages network folder creation and file organization
- AI-powered email recognition and decision-making

**Business Model:** Organization-based licensing (to be defined in Phase 2)

---

## 2. Product Vision & Goals

### Vision Statement
*"Empower project managers to focus on strategic decisions by automating repetitive administrative tasks through intelligent, locally-running AI agents."*

### Primary Goals
1. **Reduce PM Administrative Burden** by 60% through task automation
2. **Enable Scalability** - Support 50+ agents working collaboratively
3. **Ensure Enterprise Readiness** - Security, compliance, minimal IT friction
4. **Provide Seamless UX** - From discovery to deployment in under 10 minutes

### Success Criteria
- **Adoption:** 1,000+ organizations within 12 months
- **Engagement:** Average user runs agents 20+ times per week
- **Satisfaction:** NPS score >50
- **Reliability:** 99.5% agent uptime, <0.1% error rate

---

## 3. User Personas

### Primary Persona: Sarah - Senior Project Manager
- **Age:** 35-45
- **Organization:** Mid-size consulting firm (50-200 employees)
- **Pain Points:**
  - Spends 8+ hours/week on project setup admin
  - Manual file organization leads to errors
  - Missed project assignments due to email overload
- **Goals:**
  - Automate repetitive setup tasks
  - Ensure consistency across project initiation
  - Free up time for client-facing work
- **Tech Savviness:** Moderate (comfortable with MS Office, cloud tools)

### Secondary Persona: Mike - IT Administrator
- **Age:** 30-50
- **Role:** Manages software deployments for organization
- **Pain Points:**
  - Software requiring admin permissions creates helpdesk burden
  - Security concerns with third-party executables
  - Need visibility into software usage
- **Goals:**
  - Zero-friction deployment
  - Audit trails and compliance
  - Minimal support tickets

### Tertiary Persona: Jennifer - C-Suite Decision Maker
- **Role:** COO/CFO evaluating ROI
- **Goals:**
  - Quantifiable productivity gains
  - Scalable solution as org grows
  - Vendor reliability and data security

---

## 4. Product Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        WEB APP (Vercel)                      │
│  ┌────────────────┐  ┌──────────────┐  ┌─────────────────┐ │
│  │  Landing Page  │  │  User Portal │  │  Admin Dashboard│ │
│  │  (Marketing)   │  │  (Download)  │  │  (Org Mgmt)     │ │
│  └────────────────┘  └──────────────┘  └─────────────────┘ │
│                             │                                │
│                             ▼                                │
│                    ┌─────────────────┐                      │
│                    │   REST API      │                      │
│                    │   (Next.js)     │                      │
│                    └─────────────────┘                      │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   SUPABASE            │
              │  ┌─────────────────┐  │
              │  │  PostgreSQL DB  │  │
              │  │  (Users, Orgs,  │  │
              │  │   Licenses)     │  │
              │  └─────────────────┘  │
              │  ┌─────────────────┐  │
              │  │  Storage        │  │
              │  │  (Agent .exe)   │  │
              │  └─────────────────┘  │
              │  ┌─────────────────┐  │
              │  │  Auth           │  │
              │  └─────────────────┘  │
              └───────────────────────┘
                          │
                          │ (License Verification,
                          │  Version Check,
                          │  Analytics Upload)
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              DESKTOP AGENTS (Windows PC)                     │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Agent #1: Project Booking & Initiation              │  │
│  │  ┌────────────┐  ┌──────────────┐  ┌──────────────┐ │  │
│  │  │  Email     │  │  File System │  │  OpenAI API  │ │  │
│  │  │  Parser    │  │  Manager     │  │  Integration │ │  │
│  │  └────────────┘  └──────────────┘  └──────────────┘ │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │  Local Config (JSON)                            │ │  │
│  │  │  - Network paths, Email senders, API keys       │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  [Future: Agent #2, #3... #50 - Inter-agent Communication] │
└─────────────────────────────────────────────────────────────┘
│  │  ┌────────────┐  ┌──────────────┐  ┌──────────────┐ │  │
│  │  │  Email     │  │  File System │  │  OpenAI API  │ │  │
│  │  │  Parser    │  │  Manager     │  │  Integration │ │  │
│  │  └────────────┘  └──────────────┘  └──────────────┘ │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │  Local Config (JSON)                            │ │  │
│  │  │  - Network paths, Email senders, API keys       │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  [Future: Agent #2, #3... #50 - Inter-agent Communication] │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  External Systems     │
              │  - Outlook            │
              │  - Network Drives     │
              │  - OpenAI API         │
              └───────────────────────┘
```

### Technology Stack

#### Web App
- **Frontend:** Next.js 14+ (App Router), React 18+, TypeScript
- **Styling:** Tailwind CSS, shadcn/ui components
- **Hosting:** Vercel (Edge Functions)
- **Backend:** Next.js API Routes, Serverless Functions
- **Database:** Supabase (PostgreSQL)
- **Authentication:** Supabase Auth
- **Storage:** Supabase Storage (agent executables)
- **Analytics:** Vercel Analytics, PostHog (user behavior)

#### Desktop Agents
- **Language:** Python 3.11+
- **Executable Packaging:** PyInstaller
- **GUI Framework:** Tkinter (lightweight, built-in)
- **Email Parsing:** `email` (built-in), `beautifulsoup4`
- **File Operations:** `pathlib`, `shutil`
- **AI Integration:** OpenAI Python SDK
- **Configuration:** JSON files (local storage)
- **Auto-Update:** Custom update checker + requests library
- **License Verification:** HTTPS requests to web app API

#### DevOps & Tooling
- **Version Control:** GitHub (separate repos for web app and each agent)
- **CI/CD:** GitHub Actions
- **Testing:** 
  - Web: Jest, React Testing Library, Playwright
  - Agents: pytest, unittest
- **Monitoring:** Sentry (error tracking), Datadog (infrastructure)
- **Documentation:** Notion/Confluence

---

## 5. Feature Requirements

### Phase 1: MVP (Months 1-3)

#### 5.1 Web Application - Must Have (P0)

**5.1.1 Landing Page**
- Modern, responsive hero section with value proposition
- Agent showcase with feature highlights
- Pricing placeholder (Phase 2)
- Call-to-action: "Get Started" / "Request Demo"
- Testimonials section (with placeholders)
- FAQ section
- Footer with links (About, Contact, Terms, Privacy)

**5.1.2 User Authentication**
- Email/password sign-up and login
- OAuth integration (Google, Microsoft) for faster onboarding
- Email verification
- Password reset flow
- Session management (JWT tokens)

**5.1.3 User Dashboard**
- Profile management
- View available agents (initially Agent #1)
- Download agent executable
- View download history
- Access to configuration guides
- Support/feedback form

**5.1.4 Agent Management**
- Display agent versions (current, changelog)
- One-click download with progress indicator
- Installation instructions post-download
- Configuration guide (network paths, email senders)

**5.1.5 Analytics Dashboard (Basic)**
- Total downloads
- Active users (agents "phoning home")
- Agent usage frequency

#### 5.2 Desktop Agent #1 - Must Have (P0)

**5.2.1 Installation & Setup**
- Executable installer (no admin rights required)
- First-run configuration wizard (GUI)
  - OpenAI API key input
  - Network folder path configuration
  - Email sender whitelist configuration
  - Test connection to network paths
- Save configuration to local JSON file

**5.2.2 Core Functionality**
- **Email Drag-and-Drop Interface:**
  - Window with drop zone for .msg or .eml files
  - Visual feedback on file drop
  - Display email preview (subject, sender, attachments)

- **AEMA Code Recognition:**
  - Configurable regex patterns for project codes
  - Default: `AEMA-\d{5}` (e.g., AEMA-12345)
  - Search entire email (subject + body)
  - Highlight found codes in UI
  - Prompt user for confirmation if multiple codes found

- **Proposal Folder Management:**
  - Connect to configured network drive path
  - Search for existing folder matching AEMA code
  - If found: Notify user, ask to overwrite or rename
  - If not found: Create new folder with AEMA code
  - Copy email attachments to folder
  - Generate metadata file (timestamp, email sender, PM assigned)

- **AI-Powered Decision Making:**
  - Use OpenAI API to analyze email content
  - Confirm project manager assignment ("Is this a project assignment?")
  - Extract key project details (client name, deadline, scope keywords)
  - Suggest folder naming conventions based on content

**5.2.3 Error Handling & Logging**
- Local log file (rotating, max 10MB)
- Error notifications in UI (user-friendly messages)
- Retry logic for network operations
- Graceful handling of:
  - Invalid email formats
  - Network drive unavailable
  - OpenAI API errors (rate limits, invalid key)
  - Duplicate AEMA codes

**5.2.4 Auto-Update Mechanism**
- Check for updates on startup (call web app API)
- Notify user of available updates
- One-click update download and install
- Changelog display

**5.2.5 License Verification**
- On startup, verify license with web app API
- Send anonymous usage analytics (agent ID, usage count, timestamp)
- Gracefully handle offline mode (allow X uses before re-verification)

#### 5.3 Backend API - Must Have (P0)

**5.3.1 Authentication Endpoints**
- `POST /api/auth/signup`
- `POST /api/auth/login`
- `POST /api/auth/logout`
- `POST /api/auth/verify-email`
- `POST /api/auth/reset-password`

**5.3.2 Agent Endpoints**
- `GET /api/agents` - List all available agents
- `GET /api/agents/:id` - Agent details
- `GET /api/agents/:id/download` - Download agent executable (authenticated)
- `GET /api/agents/:id/version` - Check for updates

**5.3.3 License Verification (Placeholder for Phase 2)**
- `POST /api/license/verify` - Verify agent license (return boolean)
- `POST /api/analytics/usage` - Log agent usage

**5.3.4 User Endpoints**
- `GET /api/user/profile` - Get user profile
- `PUT /api/user/profile` - Update profile
- `GET /api/user/downloads` - Download history

---

### Phase 2: Licensing & Monetization (Months 4-6)

#### 5.4 Licensing System - Should Have (P1)

**5.4.1 Organization Management**
- Organization sign-up (separate from individual users)
- Admin role assignment
- Invite team members
- Manage user seats

**5.4.2 License Key System**
- Generate unique organization license keys
- Seat-based activation (track active installations)
- License revocation capability
- Grace period for expired licenses (30 days)

**5.4.3 Payment Integration**
- Stripe integration (primary)
- PayPal integration (secondary)
- Subscription plans: Monthly, Yearly
- Pricing tiers: Per agent or bundle discounts
- Invoice generation
- Automatic renewal and cancellation

**5.4.4 Admin Dashboard**
- Organization overview (total seats, active users)
- User management (add, remove, reassign)
- Usage analytics per user
- Billing history
- Download agent configuration presets (pre-configure for team)

---

### Phase 3: Advanced Features (Months 7-12)

#### 5.5 Agent Collaboration - Could Have (P2)

**5.5.1 Inter-Agent Communication**
- Shared data store (local SQLite DB)
- Agent-to-agent messaging protocol
- Dependency management (Agent B waits for Agent A)
- Workflow orchestration UI

**5.5.2 Advanced Agent #1 Features**
- Direct Outlook integration (no drag-and-drop)
- Automatic email monitoring (background service)
- Custom AI prompts (user-configurable)
- Integration with project management tools (Jira, Asana API)

**5.5.3 Analytics & Insights**
- Time saved per user (calculated metrics)
- Error rate trends
- Most common failure points
- Predictive maintenance alerts

---

## 6. Technical Specifications

### 6.1 Web App Technical Details

#### 6.1.1 Frontend Architecture
```
src/
├── app/                    # Next.js App Router
│   ├── (auth)/            # Auth routes (login, signup)
│   ├── (marketing)/       # Public pages (landing, pricing)
│   ├── dashboard/         # Protected user dashboard
│   ├── admin/             # Admin panel (Phase 2)
│   └── api/               # API routes
├── components/
│   ├── ui/                # shadcn/ui components
│   ├── agents/            # Agent cards, download buttons
│   └── layout/            # Navigation, footer
├── lib/
│   ├── supabase.ts        # Supabase client
│   ├── api.ts             # API helpers
│   └── utils.ts           # Utilities
├── hooks/                 # Custom React hooks
└── styles/
    └── globals.css        # Tailwind base styles
```

#### 6.1.2 Design System
- **Color Palette:**
  - Primary: `#3B82F6` (Blue-500) - Modern, trustworthy
  - Secondary: `#8B5CF6` (Violet-500) - Creative, AI-related
  - Accent: `#10B981` (Emerald-500) - Success states
  - Neutral: Tailwind Gray scale
  - Background: `#F9FAFB` (Gray-50) for light mode
  
- **Typography:**
  - Headings: `Inter` font, weights 600-800
  - Body: `Inter` font, weights 400-500
  - Code: `JetBrains Mono`

- **Components:**
  - Buttons: Rounded (`rounded-lg`), with hover states, loading spinners
  - Cards: Subtle shadows, hover elevations
  - Forms: Floating labels, inline validation
  - Modals: Overlay with backdrop blur

- **Animations:**
  - Page transitions: Fade-in (300ms)
  - Button interactions: Scale (100ms)
  - Skeleton loaders for async content

#### 6.1.3 Performance Targets
- **Lighthouse Score:** >90 in all categories
- **First Contentful Paint (FCP):** <1.5s
- **Time to Interactive (TTI):** <3s
- **Bundle Size:** <500KB initial JS bundle

### 6.2 Desktop Agent Technical Details

#### 6.2.1 Agent Architecture
```
pm-minions-agent-1/
├── src/
│   ├── main.py                # Entry point, GUI initialization
│   ├── config/
│   │   ├── config_manager.py  # Load/save JSON config
│   │   └── wizard.py          # First-run setup GUI
│   ├── core/
│   │   ├── email_parser.py    # Parse .msg/.eml files
│   │   ├── code_extractor.py  # Regex for AEMA codes
│   │   ├── file_manager.py    # Network drive operations
│   │   └── ai_handler.py      # OpenAI API calls
│   ├── ui/
│   │   ├── main_window.py     # Drag-and-drop interface
│   │   └── notifications.py   # Toast notifications
│   ├── utils/
│   │   ├── logger.py          # Logging setup
│   │   ├── updater.py         # Check for updates
│   │   └── license.py         # License verification
│   └── tests/
│       ├── test_email_parser.py
│       ├── test_file_manager.py
│       └── fixtures/          # Sample .msg files
├── config.json                # Local user configuration
├── requirements.txt
├── build.spec                 # PyInstaller config
└── README.md
```

#### 6.2.2 Configuration File Schema (config.json)
```json
{
  "version": "1.0.0",
  "user": {
    "agent_id": "uuid-generated-on-install",
    "email": "user@example.com"
  },
  "openai": {
    "api_key": "sk-...",
    "model": "gpt-4",
    "max_tokens": 500
  },
  "email_recognition": {
    "sender_whitelist": [
      "project-assignments@company.com",
      "pm-team@company.com"
    ],
    "subject_keywords": ["project assignment", "new project"],
    "code_patterns": ["AEMA-\\d{5}", "PROJ-\\d{4}"]
  },
  "network": {
    "proposal_folder_path": "\\\\server\\proposals",
    "retry_attempts": 3,
    "timeout_seconds": 30
  },
  "updates": {
    "check_on_startup": true,
    "auto_download": false,
    "channel": "stable"
  },
  "analytics": {
    "enabled": true,
    "usage_tracking": true
  }
}
```

#### 6.2.3 Email Parsing Logic
1. **File Format Detection:**
   - `.msg` (Outlook): Use `extract_msg` library
   - `.eml` (standard): Use built-in `email` library
   
2. **Content Extraction:**
   - Subject line
   - Sender email
   - Body (plain text + HTML, strip to plain text)
   - Attachments (save to temp directory)
   - Metadata (date, to/cc/bcc)

3. **AEMA Code Extraction:**
   ```python
   import re
   
   def extract_aema_codes(email_content, patterns):
       codes = []
       for pattern in patterns:
           matches = re.findall(pattern, email_content, re.IGNORECASE)
           codes.extend(matches)
       return list(set(codes))  # Remove duplicates
   ```

4. **AI Validation:**
   - Send email content to OpenAI API
   - Prompt: "Is this email a project assignment? Extract: client name, project manager assigned, deadline."
   - Parse structured response (use JSON mode)

#### 6.2.4 File System Operations
1. **Network Path Validation:**
   - Check if path exists: `os.path.exists(network_path)`
   - Check write permissions: Try creating a temp file
   - Retry with exponential backoff if network is slow

2. **Folder Creation:**
   ```python
   import os
   import shutil
   
   def create_project_folder(base_path, aema_code, attachments):
       folder_path = os.path.join(base_path, aema_code)
       
       # Check if folder exists
       if os.path.exists(folder_path):
           # Prompt user: overwrite, rename, or cancel
           pass
       
       # Create folder
       os.makedirs(folder_path, exist_ok=True)
       
       # Copy attachments
       for attachment in attachments:
           dest = os.path.join(folder_path, attachment.name)
           shutil.copy(attachment.path, dest)
       
       # Create metadata file
       metadata = {
           "created_at": datetime.now().isoformat(),
           "email_sender": email.sender,
           "pm_assigned": extracted_pm_name
       }
       with open(os.path.join(folder_path, "_metadata.json"), "w") as f:
           json.dump(metadata, f, indent=2)
   ```

3. **Error Recovery:**
   - Log all operations
   - Rollback on failure (delete partially created folders)
   - Notify user with actionable error messages

#### 6.2.5 Auto-Update Flow
1. On startup, call `GET /api/agents/1/version`
2. Compare remote version with local version
3. If update available:
   - Display notification with changelog
   - User clicks "Update"
   - Download new `.exe` to temp directory
   - Verify checksum (SHA-256)
   - Replace current executable (OS-specific logic)
   - Restart agent

4. **Update Package Format:**
   ```json
   {
     "version": "1.1.0",
     "release_date": "2025-12-01",
     "download_url": "https://storage.supabase.io/agents/agent-1-v1.1.0.exe",
     "checksum": "sha256-hash",
     "changelog": "- Fixed AEMA code parsing\n- Improved network retry logic",
     "required": false  // Force update if true
   }
   ```

#### 6.2.6 PyInstaller Build Configuration (build.spec)
```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets', 'assets'),  # Icons, images
        ('config.example.json', '.')
    ],
    hiddenimports=[
        'tkinter',
        'PIL._tkinter_finder',
        'openai'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PM_Minions_Agent_1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico'
)
```

---

## 7. Database Schema

### 7.1 Supabase PostgreSQL Schema

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table (handled by Supabase Auth, extended here)
CREATE TABLE public.users (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  organization_id UUID REFERENCES organizations(id),
  role TEXT DEFAULT 'user' CHECK (role IN ('user', 'admin', 'super_admin')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Organizations table (Phase 2)
CREATE TABLE public.organizations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL,
  domain TEXT, -- e.g., company.com (for auto-join)
  license_key TEXT UNIQUE,
  max_seats INTEGER DEFAULT 0,
  active_seats INTEGER DEFAULT 0,
  plan_type TEXT, -- 'free', 'starter', 'professional', 'enterprise'
  billing_email TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Agents table
CREATE TABLE public.agents (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name TEXT NOT NULL, -- 'Project Booking and Initiation'
  slug TEXT UNIQUE NOT NULL, -- 'project-booking-initiation'
  description TEXT,
  version TEXT NOT NULL, -- '1.0.0'
  changelog TEXT,
  download_url TEXT NOT NULL, -- Supabase Storage URL
  checksum TEXT NOT NULL, -- SHA-256
  file_size_mb NUMERIC,
  is_active BOOLEAN DEFAULT TRUE,
  requires_update BOOLEAN DEFAULT FALSE,
  release_date TIMESTAMPTZ DEFAULT NOW(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Agent versions (historical tracking)
CREATE TABLE public.agent_versions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  agent_id UUID NOT NULL REFERENCES agents(id) ON DELETE CASCADE,
  version TEXT NOT NULL,
  download_url TEXT NOT NULL,
  checksum TEXT NOT NULL,
  changelog TEXT,
  release_date TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(agent_id, version)
);

-- Downloads table (tracking user downloads)
CREATE TABLE public.downloads (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  agent_id UUID NOT NULL REFERENCES agents(id) ON DELETE CASCADE,
  version TEXT NOT NULL,
  downloaded_at TIMESTAMPTZ DEFAULT NOW(),
  ip_address TEXT,
  user_agent TEXT
);

-- Agent installations (track active installations)
CREATE TABLE public.agent_installations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  agent_id UUID NOT NULL REFERENCES agents(id) ON DELETE CASCADE,
  installation_id TEXT UNIQUE NOT NULL, -- Generated on agent install
  version TEXT NOT NULL,
  machine_name TEXT,
  os_version TEXT,
  installed_at TIMESTAMPTZ DEFAULT NOW(),
  last_seen TIMESTAMPTZ DEFAULT NOW(), -- Updated on license verification
  is_active BOOLEAN DEFAULT TRUE
);

-- Agent usage analytics
CREATE TABLE public.agent_usage (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  installation_id TEXT NOT NULL REFERENCES agent_installations(installation_id),
  agent_id UUID NOT NULL REFERENCES agents(id) ON DELETE CASCADE,
  action_type TEXT, -- 'email_processed', 'folder_created', 'error_occurred'
  metadata JSONB, -- Flexible field for action-specific data
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Agent configuration presets (Phase 2 - org-level configs)
CREATE TABLE public.agent_configs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  agent_id UUID NOT NULL REFERENCES agents(id) ON DELETE CASCADE,
  config_json JSONB NOT NULL, -- Pre-configured settings
  created_by UUID REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Licenses table (Phase 2)
CREATE TABLE public.licenses (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  license_key TEXT UNIQUE NOT NULL,
  agent_id UUID REFERENCES agents(id), -- NULL = all agents
  max_activations INTEGER NOT NULL,
  current_activations INTEGER DEFAULT 0,
  expires_at TIMESTAMPTZ,
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Payments table (Phase 2 - Stripe integration)
CREATE TABLE public.payments (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  stripe_payment_id TEXT UNIQUE,
  amount_cents INTEGER NOT NULL,
  currency TEXT DEFAULT 'USD',
  status TEXT NOT NULL, -- 'pending', 'completed', 'failed', 'refunded'
  payment_method TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_users_org ON users(organization_id);
CREATE INDEX idx_downloads_user ON downloads(user_id);
CREATE INDEX idx_downloads_agent ON downloads(agent_id);
CREATE INDEX idx_installations_user ON agent_installations(user_id);
CREATE INDEX idx_installations_agent ON agent_installations(agent_id);
CREATE INDEX idx_usage_installation ON agent_usage(installation_id);
CREATE INDEX idx_usage_created_at ON agent_usage(created_at);
CREATE INDEX idx_licenses_org ON licenses(organization_id);

-- Row Level Security (RLS) policies
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.downloads ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_installations ENABLE ROW LEVEL SECURITY;

-- Users can only see their own data
CREATE POLICY "Users can view own profile" ON users
  FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON users
  FOR UPDATE USING (auth.uid() = id);

-- Users can view their organization
CREATE POLICY "Users can view own organization" ON organizations
  FOR SELECT USING (
    id IN (SELECT organization_id FROM users WHERE id = auth.uid())
  );

-- Users can view their downloads
CREATE POLICY "Users can view own downloads" ON downloads
  FOR SELECT USING (user_id = auth.uid());

-- Users can insert their downloads
CREATE POLICY "Users can create downloads" ON downloads
  FOR INSERT WITH CHECK (user_id = auth.uid());

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$ LANGUAGE plpgsql;

-- Triggers for updated_at
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_organizations_updated_at BEFORE UPDATE ON organizations
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_agents_updated_at BEFORE UPDATE ON agents
  FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### 7.2 Supabase Storage Buckets

```sql
-- Create storage bucket for agent executables
INSERT INTO storage.buckets (id, name, public)
VALUES ('agent-executables', 'agent-executables', false);

-- Storage policy: Authenticated users can download
CREATE POLICY "Authenticated users can download agents"
ON storage.objects FOR SELECT
TO authenticated
USING (bucket_id = 'agent-executables');

-- Only service role can upload (admin uploads)
CREATE POLICY "Service role can upload agents"
ON storage.objects FOR INSERT
TO service_role
WITH CHECK (bucket_id = 'agent-executables');
```

---

## 8. API Specifications

### 8.1 REST API Endpoints

**Base URL:** `https://pminions.vercel.app/api`

#### 8.1.1 Authentication

**POST /api/auth/signup**
```json
Request:
{
  "email": "user@example.com",
  "password": "securePassword123",
  "full_name": "John Doe"
}

Response (201):
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe"
  },
  "session": {
    "access_token": "jwt-token",
    "refresh_token": "refresh-token"
  }
}

Errors:
400 - Invalid email format
409 - Email already exists
```

**POST /api/auth/login**
```json
Request:
{
  "email": "user@example.com",
  "password": "securePassword123"
}

Response (200):
{
  "user": { "id": "uuid", "email": "user@example.com" },
  "session": { "access_token": "jwt-token" }
}

Errors:
401 - Invalid credentials
```

**POST /api/auth/logout**
```json
Headers: Authorization: Bearer {access_token}

Response (200):
{ "message": "Logged out successfully" }
```

#### 8.1.2 Agents

**GET /api/agents**
```json
Response (200):
{
  "agents": [
    {
      "id": "uuid",
      "name": "Project Booking and Initiation",
      "slug": "project-booking-initiation",
      "description": "Automates email-based project workflows...",
      "version": "1.0.0",
      "file_size_mb": 45.2,
      "release_date": "2025-11-01T00:00:00Z",
      "changelog": "- Initial release\n- Email parsing\n- Folder creation"
    }
  ]
}
```

**GET /api/agents/:slug**
```json
Response (200):
{
  "agent": {
    "id": "uuid",
    "name": "Project Booking and Initiation",
    "slug": "project-booking-initiation",
    "version": "1.0.0",
    "description": "Full description...",
    "features": ["Email parsing", "AI-powered recognition", "Folder automation"],
    "requirements": {
      "os": "Windows 10+",
      "python": "Not required (bundled)",
      "disk_space_mb": 100
    },
    "changelog": "...",
    "documentation_url": "https://docs.pm-minions.com/agents/project-booking"
  }
}

Errors:
404 - Agent not found
```

**GET /api/agents/:id/download**
```json
Headers: Authorization: Bearer {access_token}

Response (200):
{
  "download_url": "https://storage.supabase.io/agent-executables/agent-1-v1.0.0.exe",
  "checksum": "sha256-hash",
  "expires_at": "2025-11-21T12:00:00Z"  // Signed URL, expires in 1 hour
}

Side Effects:
- Creates record in downloads table
- Increments download counter

Errors:
401 - Unauthorized
403 - License required (Phase 2)
```

**GET /api/agents/:id/version**
```json
Request Query Params:
?current_version=1.0.0

Response (200):
{
  "latest_version": "1.1.0",
  "update_available": true,
  "required": false,
  "download_url": "https://...",
  "checksum": "sha256-hash",
  "changelog": "- Bug fixes\n- Performance improvements",
  "release_date": "2025-12-01T00:00:00Z"
}

Response (200) - No update:
{
  "latest_version": "1.0.0",
  "update_available": false
}
```

#### 8.1.3 License Verification (Phase 2)

**POST /api/license/verify**
```json
Request:
{
  "installation_id": "uuid-from-agent",
  "agent_id": "uuid",
  "version": "1.0.0"
}

Response (200):
{
  "valid": true,
  "license_type": "professional",
  "expires_at": "2026-01-01T00:00:00Z"
}

Side Effects:
- Updates last_seen timestamp in agent_installations

Errors:
403 - Invalid or expired license
```

#### 8.1.4 Analytics

**POST /api/analytics/usage**
```json
Request:
{
  "installation_id": "uuid",
  "agent_id": "uuid",
  "action_type": "email_processed",
  "metadata": {
    "aema_code": "AEMA-12345",
    "attachments_count": 3,
    "processing_time_ms": 2500
  }
}

Response (201):
{ "message": "Usage logged" }

Note: This endpoint accepts anonymous data (no auth required)
Rate limit: 100 requests per hour per installation_id
```

**GET /api/analytics/dashboard**
```json
Headers: Authorization: Bearer {access_token}

Response (200):
{
  "total_downloads": 150,
  "active_installations": 120,
  "usage_stats": {
    "total_actions": 5420,
    "actions_this_week": 320,
    "most_used_agent": "project-booking-initiation"
  },
  "user_downloads": [
    {
      "agent_name": "Project Booking and Initiation",
      "version": "1.0.0",
      "downloaded_at": "2025-11-15T10:30:00Z"
    }
  ]
}

Errors:
401 - Unauthorized
```

#### 8.1.5 User Profile

**GET /api/user/profile**
```json
Headers: Authorization: Bearer {access_token}

Response (200):
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe",
    "organization": {
      "id": "uuid",
      "name": "Acme Corp"
    },
    "created_at": "2025-11-01T00:00:00Z"
  }
}
```

**PUT /api/user/profile**
```json
Headers: Authorization: Bearer {access_token}

Request:
{
  "full_name": "John Smith",
  "preferences": {
    "email_notifications": true,
    "update_notifications": true
  }
}

Response (200):
{
  "user": { "id": "uuid", "full_name": "John Smith", ... }
}
```

---

## 9. UI/UX Design System

### 9.1 Design Principles

1. **Clarity over cleverness** - Prioritize user understanding
2. **Speed and efficiency** - Minimize clicks to complete tasks
3. **Progressive disclosure** - Show advanced features when needed
4. **Consistency** - Uniform patterns across all pages
5. **Accessibility** - WCAG 2.1 AA compliance

### 9.2 Color Palette

```css
/* Primary Colors */
--color-primary-50: #EFF6FF;
--color-primary-100: #DBEAFE;
--color-primary-500: #3B82F6;  /* Main brand color */
--color-primary-600: #2563EB;
--color-primary-700: #1D4ED8;

/* Secondary Colors */
--color-secondary-50: #FAF5FF;
--color-secondary-500: #8B5CF6;  /* Accent for AI features */
--color-secondary-600: #7C3AED;

/* Success/Error/Warning */
--color-success: #10B981;
--color-error: #EF4444;
--color-warning: #F59E0B;

/* Neutral */
--color-gray-50: #F9FAFB;
--color-gray-100: #F3F4F6;
--color-gray-500: #6B7280;
--color-gray-900: #111827;
```

### 9.3 Typography Scale

```css
/* Font Family */
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--font-mono: 'JetBrains Mono', monospace;

/* Font Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
--text-5xl: 3rem;      /* 48px */
```

### 9.4 Component Specifications

#### 9.4.1 Navigation Bar
```
Desktop:
- Height: 64px
- Background: White with subtle shadow
- Logo: Left (40px height)
- Nav items: Center (Products, Pricing, Docs, About)
- CTA buttons: Right (Login, Get Started)

Mobile:
- Hamburger menu
- Full-screen overlay navigation
```

#### 9.4.2 Hero Section (Landing Page)
```
Layout:
- 60/40 split (text left, visual right)
- Heading: text-5xl, font-bold, gradient text
- Subheading: text-xl, color-gray-600
- CTA buttons: Primary (Get Started), Secondary (Watch Demo)
- Hero image/animation: 3D illustration of agents working

Key Message:
"Automate Your PM Workflow with AI-Powered Agents"
"Download intelligent assistants that handle repetitive tasks,
so you can focus on what matters."
```

#### 9.4.3 Agent Cards
```
Card Structure:
┌─────────────────────────────┐
│  [Agent Icon]               │
│  Agent Name                 │
│  Brief description...       │
│                             │
│  Features:                  │
│  • Feature 1                │
│  • Feature 2                │
│                             │
│  Version 1.0.0  |  45.2 MB  │
│  [Download Button]          │
└─────────────────────────────┘

Interactions:
- Hover: Lift effect (shadow increase)
- Click card: Navigate to agent detail page
- Download button: Show progress modal
```

#### 9.4.4 Download Modal
```
Steps:
1. Confirm download
2. Show progress bar (downloading from Supabase)
3. Success state with next steps:
   - "Installation Guide" link
   - "Configuration Guide" link
   - "Open folder" button

Loading State:
- Animated progress bar
- File size and speed (e.g., "23.5 MB / 45.2 MB - 2.3 MB/s")
```

#### 9.4.5 Dashboard Layout
```
Sidebar (Left):
- User avatar + name
- Navigation:
  * Dashboard (home icon)
  * My Agents (grid icon)
  * Downloads (download icon)
  * Settings (gear icon)
  * Support (help icon)

Main Content:
- Page title
- Stats cards (Total Downloads, Active Agents, Usage This Week)
- Agent list with actions
- Recent activity feed
```

### 9.5 Responsive Breakpoints

```css
/* Mobile First Approach */
--breakpoint-sm: 640px;   /* Small devices */
--breakpoint-md: 768px;   /* Tablets */
--breakpoint-lg: 1024px;  /* Desktops */
--breakpoint-xl: 1280px;  /* Large screens */
```

### 9.6 Animation Guidelines

```css
/* Transitions */
--transition-fast: 100ms ease-in-out;
--transition-base: 200ms ease-in-out;
--transition-slow: 300ms ease-in-out;

/* Common Animations */
.fade-in {
  animation: fadeIn 300ms ease-in;
}

.slide-up {
  animation: slideUp 400ms cubic-bezier(0.16, 1, 0.3, 1);
}

.scale-hover:hover {
  transform: scale(1.02);
  transition: transform 100ms ease-in-out;
}
```

### 9.7 Accessibility Requirements

- **Keyboard Navigation:** All interactive elements must be keyboard accessible
- **Focus Indicators:** Visible focus rings (2px solid primary-500)
- **ARIA Labels:** All icons and buttons must have descriptive labels
- **Color Contrast:** Minimum 4.5:1 for normal text, 3:1 for large text
- **Screen Reader:** Test with NVDA/JAWS
- **Skip Links:** "Skip to main content" link at top

---

## 10. Security & Compliance

### 10.1 Web Application Security

#### 10.1.1 Authentication & Authorization
- **Password Requirements:**
  - Minimum 8 characters
  - At least 1 uppercase, 1 lowercase, 1 number
  - Hashed with bcrypt (cost factor 12)
- **Session Management:**
  - JWT tokens with 1-hour expiration
  - Refresh tokens with 30-day expiration (stored in httpOnly cookies)
  - Token rotation on refresh
- **Rate Limiting:**
  - Login attempts: 5 per 15 minutes per IP
  - API requests: 100 per minute per user
  - Download requests: 10 per hour per user

#### 10.1.2 Data Protection
- **Encryption:**
  - All data in transit: TLS 1.3
  - Database: Encryption at rest (Supabase default)
  - Sensitive fields: Additional encryption (OpenAI API keys)
- **Data Minimization:**
  - Collect only necessary user data
  - Anonymous analytics (no PII in usage logs)
- **GDPR Compliance:**
  - User data export functionality
  - Right to deletion (cascade deletes in DB)
  - Cookie consent banner
  - Privacy policy and terms of service

#### 10.1.3 Input Validation
- **Frontend:** Client-side validation with Zod schemas
- **Backend:** Server-side validation (never trust client)
- **SQL Injection:** Use parameterized queries (Supabase client)
- **XSS Prevention:** Sanitize all user inputs, CSP headers

#### 10.1.4 Content Security Policy (CSP)
```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://vercel.live;
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: https://storage.supabase.co;
  connect-src 'self' https://api.supabase.co;
  font-src 'self';
```

### 10.2 Desktop Agent Security

#### 10.2.1 Code Signing
- **Windows:** Sign executables with EV Code Signing Certificate
- **Purpose:** Prevents "Unknown Publisher" warnings
- **Certificate Authority:** DigiCert or Sectigo

#### 10.2.2 Secure Configuration Storage
- **OpenAI API Keys:**
  - Stored in config.json with file permissions (read-only for user)
  - Optionally encrypt with Windows DPAPI (Data Protection API)
- **Network Credentials:**
  - Never store passwords in config
  - Use Windows Credential Manager if needed

#### 10.2.3 Network Communication
- **HTTPS Only:** All API calls to web app
- **Certificate Pinning:** Validate server certificates
- **Timeout & Retry:** Prevent hanging connections

#### 10.2.4 File System Access
- **Sandboxing:** Agent only accesses configured network paths
- **Permission Checks:** Validate write access before operations
- **Path Traversal Prevention:** Sanitize all file paths

#### 10.2.5 Update Verification
- **Checksum Validation:** SHA-256 hash verification before installing updates
- **Signed Updates:** Verify update packages are signed
- **Rollback Mechanism:** Keep previous version for rollback

### 10.3 Third-Party Dependencies

#### 10.3.1 Supply Chain Security
- **Dependency Scanning:** GitHub Dependabot for vulnerability alerts
- **Lock Files:** Use package-lock.json (npm) and requirements.txt (Python)
- **Minimal Dependencies:** Regularly audit and remove unused packages
- **Trusted Sources:** Only install from official package registries

#### 10.3.2 License Compliance
- **Audit:** Ensure all dependencies use compatible licenses (MIT, Apache 2.0)
- **Attribution:** Include licenses in About section

### 10.4 Incident Response Plan

#### 10.4.1 Security Breach Protocol
1. **Detection:** Monitor logs, error tracking (Sentry)
2. **Containment:** Revoke compromised tokens, disable affected accounts
3. **Investigation:** Identify root cause, affected users
4. **Notification:** Email affected users within 72 hours (GDPR)
5. **Remediation:** Patch vulnerability, force password resets if needed
6. **Post-Mortem:** Document incident, improve monitoring

#### 10.4.2 Vulnerability Disclosure
- **Security Email:** security@pm-minions.com
- **Response Time:** Acknowledge within 48 hours
- **Responsible Disclosure:** 90-day window before public disclosure

---

## 11. Testing Strategy

### 11.1 Testing Methodologies

#### 11.1.1 Test-Driven Development (TDD)
- **Process:**
  1. Write failing test for new feature
  2. Write minimum code to pass test
  3. Refactor code while keeping tests green
- **Application:**
  - All API endpoints
  - Business logic functions (email parsing, code extraction)
  - Database operations

#### 11.1.2 Shift-Left Testing
- **Principles:**
  - Test early in development cycle
  - Automate tests in CI/CD pipeline
  - Developers write tests alongside code
- **Implementation:**
  - Pre-commit hooks run linters and unit tests
  - PR checks require passing tests before merge
  - Daily automated test runs

#### 11.1.3 Agile/DevOps Testing
- **Continuous Testing:**
  - Unit tests: On every commit
  - Integration tests: On PR merge to main
  - E2E tests: On deployment to staging
- **Fast Feedback:**
  - Test results in <5 minutes
  - Slack notifications for failures

### 11.2 Web Application Testing

#### 11.2.1 Unit Tests (Jest + React Testing Library)
```javascript
// Example: Agent card component
describe('AgentCard', () => {
  it('renders agent information correctly', () => {
    const agent = {
      name: 'Project Booking',
      version: '1.0.0',
      file_size_mb: 45.2
    };
    render(<AgentCard agent={agent} />);
    expect(screen.getByText('Project Booking')).toBeInTheDocument();
    expect(screen.getByText('Version 1.0.0')).toBeInTheDocument();
  });

  it('triggers download on button click', async () => {
    const mockDownload = jest.fn();
    render(<AgentCard onDownload={mockDownload} />);
    await userEvent.click(screen.getByRole('button', { name: /download/i }));
    expect(mockDownload).toHaveBeenCalledTimes(1);
  });
});
```

**Coverage Target:** >80% for critical paths

#### 11.2.2 Integration Tests
```javascript
// Example: Download flow
describe('Agent Download Flow', () => {
  it('downloads agent after authentication', async () => {
    // Mock API responses
    server.use(
      rest.get('/api/agents/:id/download', (req, res, ctx) => {
        return res(ctx.json({ download_url: 'https://...' }));
      })
    );

    // Simulate user flow
    await loginUser('user@example.com', 'password');
    await navigateToAgentPage('project-booking-initiation');
    await clickDownloadButton();
    
    expect(screen.getByText(/downloading/i)).toBeInTheDocument();
    await waitFor(() => {
      expect(screen.getByText(/download complete/i)).toBeInTheDocument();
    });
  });
});
```

#### 11.2.3 End-to-End Tests (Playwright)
```javascript
// Example: Full user journey
test('new user can sign up and download agent', async ({ page }) => {
  // Sign up
  await page.goto('https://pm-minions.com/signup');
  await page.fill('[name="email"]', 'newuser@example.com');
  await page.fill('[name="password"]', 'SecurePass123');
  await page.click('button[type="submit"]');
  
  // Verify email (mock)
  await mockEmailVerification(page);
  
  // Navigate to agents
  await page.click('text=Browse Agents');
  
  // Download agent
  await page.click('text=Project Booking and Initiation');
  await page.click('button:has-text("Download")');
  
  // Assert download started
  const download = await page.waitForEvent('download');
  expect(download.suggestedFilename()).toContain('PM_Minions_Agent');
});
```

**Test Environments:**
- **Local:** Run against local dev server
- **Staging:** Run against Vercel preview deployments
- **Production:** Smoke tests only (non-destructive)

#### 11.2.4 API Testing (Supertest)
```javascript
// Example: API endpoint tests
describe('POST /api/auth/signup', () => {
  it('creates user with valid data', async () => {
    const response = await request(app)
      .post('/api/auth/signup')
      .send({
        email: 'test@example.com',
        password: 'SecurePass123',
        full_name: 'Test User'
      })
      .expect(201);
    
    expect(response.body).toHaveProperty('user.id');
    expect(response.body).toHaveProperty('session.access_token');
  });

  it('returns 409 for duplicate email', async () => {
    // First signup
    await createUser('duplicate@example.com');
    
    // Second signup with same email
    const response = await request(app)
      .post('/api/auth/signup')
      .send({ email: 'duplicate@example.com', password: 'pass123' })
      .expect(409);
    
    expect(response.body.error).toContain('already exists');
  });
});
```

### 11.3 Desktop Agent Testing

#### 11.3.1 Unit Tests (pytest)
```python
# test_email_parser.py
import pytest
from src.core.email_parser import EmailParser

def test_parse_msg_file():
    parser = EmailParser()
    email_data = parser.parse('tests/fixtures/sample.msg')
    
    assert email_data['subject'] == 'New Project Assignment'
    assert 'project-assignments@company.com' in email_data['sender']
    assert len(email_data['attachments']) == 2

def test_extract_aema_code():
    parser = EmailParser()
    content = "Please see AEMA-12345 for details"
    codes = parser.extract_codes(content, patterns=[r'AEMA-\d{5}'])
    
    assert 'AEMA-12345' in codes

def test_extract_multiple_codes():
    content = "Projects AEMA-12345 and AEMA-67890 need attention"
    codes = parser.extract_codes(content, patterns=[r'AEMA-\d{5}'])
    
    assert len(codes) == 2
    assert 'AEMA-12345' in codes
    assert 'AEMA-67890' in codes
```

#### 11.3.2 Integration Tests (File System)
```python
# test_file_manager.py
import tempfile
import os
from src.core.file_manager import FileManager

def test_create_project_folder():
    with tempfile.TemporaryDirectory() as tmpdir:
        fm = FileManager(base_path=tmpdir)
        
        # Create folder with attachments
        attachments = [
            {'name': 'doc1.pdf', 'content': b'fake pdf content'}
        ]
        result = fm.create_project_folder('AEMA-12345', attachments)
        
        assert result['success'] == True
        assert os.path.exists(os.path.join(tmpdir, 'AEMA-12345'))
        assert os.path.exists(os.path.join(tmpdir, 'AEMA-12345', 'doc1.pdf'))

def test_handle_duplicate_folder():
    with tempfile.TemporaryDirectory() as tmpdir:
        fm = FileManager(base_path=tmpdir)
        
        # Create folder first time
        fm.create_project_folder('AEMA-12345', [])
        
        # Try creating again
        result = fm.create_project_folder('AEMA-12345', [])
        
        assert result['success'] == False
        assert 'already exists' in result['error']
```

#### 11.3.3 Mock Testing (OpenAI API)
```python
# test_ai_handler.py
from unittest.mock import patch, Mock
from src.core.ai_handler import AIHandler

@patch('openai.ChatCompletion.create')
def test_analyze_email(mock_openai):
    # Mock OpenAI response
    mock_openai.return_value = Mock(
        choices=[Mock(message=Mock(content='{"is_project_assignment": true}'))]
    )
    
    handler = AIHandler(api_key='test-key')
    result = handler.analyze_email('Email content here...')
    
    assert result['is_project_assignment'] == True
    mock_openai.assert_called_once()
```

#### 11.3.4 User Acceptance Testing (UAT)
**Manual Test Cases:**

1. **Email Parsing:**
   - Drag `.msg` file → Agent recognizes AEMA code
   - Drag `.eml` file → Agent recognizes AEMA code
   - Drag email with no AEMA code → Agent prompts user

2. **Folder Creation:**
   - First project → Folder created successfully
   - Duplicate AEMA code → Agent asks user action (overwrite/rename/cancel)
   - Network drive unavailable → Agent shows error, offers retry

3. **Configuration:**
   - First run → Setup wizard guides user
   - Change network path → Agent validates new path
   - Add email sender → Agent recognizes new sender

4. **Edge Cases:**
   - Very large attachments (>100MB) → Progress indicator works
   - Special characters in AEMA code → Folder created with safe name
   - Network interruption during copy → Agent resumes or rolls back

**UAT Participants:**
- 3-5 actual project managers
- Conduct in real work environments
- Observe and record issues

### 11.4 Performance Testing

#### 11.4.1 Load Testing (k6)
```javascript
// load-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },  // Ramp up to 100 users
    { duration: '5m', target: 100 },  // Stay at 100 users
    { duration: '2m', target: 0 },    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% of requests under 500ms
    http_req_failed: ['rate<0.01'],    // Error rate under 1%
  },
};

export default function () {
  const response = http.get('https://pm-minions.com/api/agents');
  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time OK': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

**Performance Targets:**
- **API Response Time:** p95 < 500ms
- **Page Load Time:** p95 < 3s
- **Agent Download:** Start within 1s (signed URL generation)
- **Agent Startup:** < 5s cold start

#### 11.4.2 Agent Performance Testing
```python
# test_performance.py
import time
from src.core.email_parser import EmailParser

def test_email_parsing_performance():
    parser = EmailParser()
    
    start = time.time()
    for _ in range(100):
        parser.parse('tests/fixtures/sample.msg')
    end = time.time()
    
    avg_time = (end - start) / 100
    assert avg_time < 0.1,  # Should parse in <100ms
```

### 11.5 Security Testing

#### 11.5.1 Automated Security Scanning
- **SAST (Static):** 
  - Web: ESLint security plugins, Semgrep
  - Agent: Bandit (Python security linter)
- **DAST (Dynamic):** OWASP ZAP on staging environment
- **Dependency Scanning:** Snyk, GitHub Dependabot

#### 11.5.2 Penetration Testing
- **Frequency:** Annually or after major releases
- **Scope:** Web app authentication, API endpoints, agent-server communication
- **Third-Party:** Hire external security firm (recommendations: Bishop Fox, NCC Group)
- **Focus Areas:**
  - Authentication bypass attempts
  - SQL injection, XSS, CSRF vulnerabilities
  - API rate limit bypass
  - Agent executable reverse engineering
  - Session hijacking
  - Authorization flaws (horizontal/vertical privilege escalation)
  - File upload vulnerabilities
  - Business logic flaws

**Penetration Testing Checklist:**
- [ ] OWASP Top 10 coverage
- [ ] API security testing (OWASP API Security Top 10)
- [ ] Agent-server communication security
- [ ] License verification bypass attempts
- [ ] Payment integration security (Phase 2)
- [ ] Data exposure in error messages
- [ ] Rate limiting effectiveness
- [ ] SSL/TLS configuration
- [ ] Subdomain takeover risks
- [ ] Third-party dependencies audit

### 11.6 Test Automation Strategy

#### 11.6.1 CI/CD Test Pipeline
```yaml
# .github/workflows/test.yml
name: Test Suite

on: [push, pull_request]

jobs:
  web-app-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run lint
      - run: npm run test:unit
      - run: npm run test:integration
      - run: npm run build
      
  agent-tests:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pip install pytest pytest-cov
      - run: pytest --cov=src tests/
      - run: python -m bandit -r src/
      
  e2e-tests:
    runs-on: ubuntu-latest
    needs: web-app-tests
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npx playwright install
      - run: npm run test:e2e
      - uses: actions/upload-artifact@v3
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
```

#### 11.6.2 Test Coverage Goals
- **Web App:**
  - Unit tests: >80% coverage
  - Integration tests: All critical user flows
  - E2E tests: 10-15 happy path scenarios
- **Desktop Agent:**
  - Unit tests: >85% coverage (higher due to complexity)
  - Integration tests: All file system and network operations
  - Manual UAT: Before each release

#### 11.6.3 Test Data Management
- **Fixtures:** Store sample emails, config files in `tests/fixtures/`
- **Factories:** Use factory pattern for generating test data
- **Database:** Use separate test database (Supabase project)
- **Cleanup:** Reset test data after each test run

---

## 12. Deployment & CI/CD

### 12.1 Repository Structure

```
pm-minions/
├── web-app/                 # Main web application
│   ├── .github/
│   │   └── workflows/
│   │       ├── test.yml
│   │       ├── deploy-preview.yml
│   │       └── deploy-production.yml
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vercel.json
│
├── agent-1-project-booking/  # Agent #1 repository
│   ├── .github/
│   │   └── workflows/
│   │       ├── test.yml
│   │       └── build-release.yml
│   ├── src/
│   ├── tests/
│   ├── requirements.txt
│   └── build.spec
│
├── agent-shared/            # Shared utilities for all agents
│   ├── src/
│   │   ├── license_verification.py
│   │   ├── auto_updater.py
│   │   └── analytics.py
│   └── tests/
│
└── docs/                    # Documentation site
    ├── user-guides/
    ├── api-reference/
    └── developer-docs/
```

### 12.2 Web App Deployment (Vercel)

#### 12.2.1 Environment Configuration

**Development (.env.local)**
```bash
NEXT_PUBLIC_SUPABASE_URL=https://dev-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...dev-key
SUPABASE_SERVICE_ROLE_KEY=eyJ...service-key
NEXT_PUBLIC_API_URL=http://localhost:3000/api
NEXT_PUBLIC_ENV=development
```

**Staging (.env.staging)**
```bash
NEXT_PUBLIC_SUPABASE_URL=https://staging-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...staging-key
SUPABASE_SERVICE_ROLE_KEY=eyJ...service-key
NEXT_PUBLIC_API_URL=https://staging.pminions.com/api
NEXT_PUBLIC_ENV=staging
```

**Production (.env.production)**
```bash
NEXT_PUBLIC_SUPABASE_URL=https://prod-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...prod-key
SUPABASE_SERVICE_ROLE_KEY=eyJ...service-key
NEXT_PUBLIC_API_URL=https://pminions.com/api
NEXT_PUBLIC_ENV=production
SENTRY_DSN=https://...
```

#### 12.2.2 Deployment Pipeline

```yaml
# .github/workflows/deploy-production.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm run lint
      - run: npm run test
      - run: npm run build
      
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: amondnet/vercel-action@v20
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
      
  notify:
    needs: deploy
    runs-on: ubuntu-latest
    steps:
      - name: Slack Notification
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: 'Production deployment completed!'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

#### 12.2.3 Vercel Configuration (vercel.json)

```json
{
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "regions": ["iad1"],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        { "key": "Access-Control-Allow-Methods", "value": "GET,POST,PUT,DELETE,OPTIONS" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" }
      ]
    }
  ],
  "rewrites": [
    { "source": "/docs/:path*", "destination": "https://docs.pm-minions.com/:path*" }
  ]
}
```

### 12.3 Desktop Agent Build & Release

#### 12.3.1 Build Process (PyInstaller)

**Build Script (build.py)**
```python
import PyInstaller.__main__
import os
import hashlib

VERSION = "1.0.0"
AGENT_NAME = "PMinions_Agent_1"

def build_executable():
    PyInstaller.__main__.run([
        'src/main.py',
        '--name', f'{AGENT_NAME}_v{VERSION}',
        '--onefile',
        '--windowed',
        '--icon=assets/icon.ico',
        '--add-data', 'assets;assets',
        '--add-data', 'config.example.json;.',
        '--hidden-import', 'tkinter',
        '--hidden-import', 'openai',
        '--clean',
        '--noconfirm'
    ])
    
    exe_path = f'dist/{AGENT_NAME}_v{VERSION}.exe'
    
    # Generate checksum
    with open(exe_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    print(f"\nBuild Complete!")
    print(f"Executable: {exe_path}")
    print(f"SHA-256: {file_hash}")
    
    # Save checksum
    with open(f'dist/{AGENT_NAME}_v{VERSION}.sha256', 'w') as f:
        f.write(file_hash)

if __name__ == '__main__':
    build_executable()
```

#### 12.3.2 Release Pipeline

```yaml
# .github/workflows/build-release.yml
name: Build and Release Agent

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pyinstaller
      
      - name: Run tests
        run: pytest tests/
      
      - name: Build executable
        run: python build.py
      
      - name: Sign executable
        uses: azure/code-sign-action@v1
        with:
          certificate: ${{ secrets.CODE_SIGNING_CERT }}
          password: ${{ secrets.CERT_PASSWORD }}
          files: 'dist/*.exe'
      
      - name: Upload to Supabase Storage
        run: |
          python scripts/upload_to_supabase.py \
            --file dist/PMinions_Agent_1_v${{ github.ref_name }}.exe \
            --bucket agent-executables \
            --version ${{ github.ref_name }}
        env:
          SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
          SUPABASE_SERVICE_KEY: ${{ secrets.SUPABASE_SERVICE_KEY }}
      
      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            dist/*.exe
            dist/*.sha256
          body_path: CHANGELOG.md
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Update database
        run: |
          python scripts/update_agent_version.py \
            --version ${{ github.ref_name }} \
            --changelog "$(cat CHANGELOG.md)"
        env:
          SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
          SUPABASE_SERVICE_KEY: ${{ secrets.SUPABASE_SERVICE_KEY }}
```

#### 12.3.3 Upload Script (upload_to_supabase.py)

```python
import argparse
import os
from supabase import create_client, Client

def upload_agent(file_path, bucket, version):
    supabase: Client = create_client(
        os.getenv('SUPABASE_URL'),
        os.getenv('SUPABASE_SERVICE_KEY')
    )
    
    filename = f"agent-1-{version}.exe"
    
    # Upload to storage
    with open(file_path, 'rb') as f:
        supabase.storage.from_(bucket).upload(
            path=filename,
            file=f,
            file_options={"content-type": "application/octet-stream"}
        )
    
    # Get public URL
    url = supabase.storage.from_(bucket).get_public_url(filename)
    
    print(f"Uploaded to: {url}")
    return url

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--bucket', required=True)
    parser.add_argument('--version', required=True)
    args = parser.parse_args()
    
    upload_agent(args.file, args.bucket, args.version)
```

### 12.4 Database Migrations

#### 12.4.1 Migration Strategy
- **Tool:** Supabase CLI with SQL migrations
- **Versioning:** Sequential numbered migrations (001_initial_schema.sql)
- **Testing:** Run migrations on staging before production
- **Rollback:** Keep rollback scripts for each migration

**Example Migration (002_add_usage_analytics.sql)**
```sql
-- Up migration
CREATE TABLE IF NOT EXISTS agent_usage (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  installation_id TEXT NOT NULL,
  agent_id UUID NOT NULL REFERENCES agents(id),
  action_type TEXT,
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_usage_installation ON agent_usage(installation_id);
CREATE INDEX idx_usage_created_at ON agent_usage(created_at);

-- Down migration (stored in 002_rollback.sql)
-- DROP TABLE IF EXISTS agent_usage;
```

#### 12.4.2 Migration Workflow
```bash
# Create new migration
supabase migration new add_usage_analytics

# Apply to local dev
supabase db reset

# Test locally
npm run test:integration

# Apply to staging
supabase db push --db-url $STAGING_DB_URL

# Verify on staging
npm run test:e2e -- --env=staging

# Apply to production (with backup)
supabase db dump --db-url $PROD_DB_URL > backup_$(date +%Y%m%d).sql
supabase db push --db-url $PROD_DB_URL
```

### 12.5 Monitoring & Observability

#### 12.5.1 Application Monitoring

**Sentry (Error Tracking)**
```javascript
// sentry.client.config.js
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NEXT_PUBLIC_ENV,
  tracesSampleRate: 0.1,
  beforeSend(event, hint) {
    // Filter out sensitive data
    if (event.request) {
      delete event.request.cookies;
    }
    return event;
  },
});
```

**Vercel Analytics**
- Built-in Web Vitals tracking
- Real User Monitoring (RUM)
- Deployment analytics

**Custom Metrics (Datadog)**
```javascript
// lib/metrics.ts
import { datadogRum } from '@datadog/browser-rum';

export function trackAgentDownload(agentId: string, version: string) {
  datadogRum.addAction('agent_download', {
    agent_id: agentId,
    version: version,
    timestamp: Date.now()
  });
}

export function trackAPILatency(endpoint: string, duration: number) {
  datadogRum.addTiming(`api.${endpoint}`, duration);
}
```

#### 12.5.2 Infrastructure Monitoring

**Vercel Metrics:**
- Function execution time
- Edge network latency
- Bandwidth usage
- Build times

**Supabase Metrics:**
- Database connections
- Query performance
- Storage usage
- API request volume

**Alert Thresholds:**
- Error rate > 1% for 5 minutes → PagerDuty alert
- API response time p95 > 1s for 10 minutes → Slack notification
- Database CPU > 80% for 15 minutes → Email alert
- Storage > 90% capacity → Slack notification

#### 12.5.3 Logging Strategy

**Log Levels:**
- **ERROR:** System failures, exceptions
- **WARN:** Recoverable issues, deprecations
- **INFO:** Significant events (user signup, agent download)
- **DEBUG:** Detailed diagnostic info (dev/staging only)

**Log Structure (JSON)**
```json
{
  "timestamp": "2025-11-20T15:30:45Z",
  "level": "INFO",
  "service": "web-app",
  "message": "Agent downloaded",
  "user_id": "uuid",
  "agent_id": "uuid",
  "version": "1.0.0",
  "metadata": {
    "ip": "192.168.1.1",
    "user_agent": "Mozilla/5.0..."
  }
}
```

**Log Aggregation:**
- Vercel Logs (built-in)
- Export to Datadog for long-term retention
- Retention: 30 days in Vercel, 90 days in Datadog

### 12.6 Rollback & Disaster Recovery

#### 12.6.1 Web App Rollback
```bash
# Rollback to previous Vercel deployment
vercel rollback

# Or rollback to specific deployment
vercel rollback [deployment-url]
```

**Automatic Rollback Triggers:**
- Error rate > 5% within 10 minutes of deployment
- Critical security vulnerability detected
- Database connection failures

#### 12.6.2 Database Backup & Recovery

**Automated Backups:**
- Supabase automated daily backups (retained 30 days)
- Weekly full backups to S3 (retained 1 year)
- Point-in-time recovery available (7 days)

**Recovery Procedure:**
```bash
# Restore from Supabase backup
supabase db restore --backup-id [backup-id]

# Restore from S3
aws s3 cp s3://pm-minions-backups/backup_20251120.sql .
psql $DATABASE_URL < backup_20251120.sql
```

**Recovery Time Objective (RTO):** < 4 hours  
**Recovery Point Objective (RPO):** < 24 hours

#### 12.6.3 Agent Rollback

**User-Initiated:**
- Users can download previous versions from dashboard
- Agent includes "Restore Previous Version" feature

**Emergency Killswitch:**
- Set `requires_update: true` in database for problematic version
- Agent checks on startup, forces update before use
- Display critical alert to users

---

## 13. Success Metrics

### 13.1 Key Performance Indicators (KPIs)

#### 13.1.1 Adoption Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| Total Signups | 1,000 in 12 months | Monthly growth rate: 15% |
| Activated Users | 70% of signups | Users who download at least 1 agent |
| Daily Active Users (DAU) | 500 within 12 months | Users running agents daily |
| Agent Downloads | 1,500 total | Tracked via downloads table |

#### 13.1.2 Engagement Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| Average Agent Runs/Week | 20+ per user | Via usage analytics |
| Retention Rate (30-day) | >60% | Users active after 30 days |
| Stickiness (DAU/MAU) | >30% | Daily active / Monthly active |
| Feature Adoption | >50% use AI features | Track OpenAI API calls |

#### 13.1.3 Quality Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| Agent Success Rate | >99% | Successful operations / total |
| Error Rate | <0.1% | Errors / total operations |
| Crash Rate | <0.01% | Agent crashes / sessions |
| Bug Report Rate | <5 per 100 users/month | Support tickets |

#### 13.1.4 Performance Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| API Response Time (p95) | <500ms | Vercel Analytics |
| Agent Startup Time | <5s | Instrumented timing |
| Email Processing Time | <10s average | Usage analytics |
| Page Load Time (p95) | <3s | Web Vitals |

#### 13.1.5 Business Metrics (Phase 2)
| Metric | Target | Measurement |
|--------|--------|-------------|
| Monthly Recurring Revenue (MRR) | TBD | Stripe dashboard |
| Customer Acquisition Cost (CAC) | TBD | Marketing spend / new customers |
| Lifetime Value (LTV) | TBD | Average revenue per customer |
| Churn Rate | <5% monthly | Cancelled subscriptions |

### 13.2 User Satisfaction Metrics

#### 13.2.1 Net Promoter Score (NPS)
- **Target:** >50 (Excellent)
- **Survey:** Quarterly, in-app survey to random sample
- **Question:** "How likely are you to recommend PM Minions to a colleague?" (0-10)

#### 13.2.2 Customer Satisfaction (CSAT)
- **Target:** >4.5/5
- **Survey:** Post-download, after 1 week of usage
- **Questions:**
  - How satisfied are you with the agent's performance?
  - How easy was setup?
  - How helpful is the time saved?

#### 13.2.3 Time Saved
- **Target:** 5+ hours/week per user
- **Measurement:** 
  - Baseline survey (time spent before)
  - Post-usage survey (time spent now)
  - Calculated metrics (operations * avg time saved)

### 13.3 Analytics Dashboard

**Real-Time Dashboard (Datadog/Custom)**
```
┌─────────────────────────────────────────────────────────┐
│  PMinions - Live Analytics                              │
├─────────────────────────────────────────────────────────┤
│  Total Users: 1,234    |  Active Now: 89                │
│  Agents Downloaded: 2,345  |  Running: 67               │
├─────────────────────────────────────────────────────────┤
│  Today's Activity:                                      │
│  • Email Processed: 1,456                               │
│  • Folders Created: 1,234                               │
│  • Errors: 12 (0.8%)                                    │
├─────────────────────────────────────────────────────────┤
│  [Usage Over Time Chart]                                │
│                                                          │
│  [Error Rate Trend]                                     │
│                                                          │
│  [Top User Actions]                                     │
└─────────────────────────────────────────────────────────┘
```

### 13.4 Reporting Schedule

**Daily:**
- Active users (DAU)
- Error rate
- Critical failures (automated alerts)

**Weekly:**
- New signups
- Agent downloads
- Top support issues
- Performance metrics summary

**Monthly:**
- Retention cohort analysis
- Feature adoption trends
- NPS/CSAT results
- Product roadmap review

**Quarterly:**
- Business review (revenue, costs)
- Strategic goal assessment
- Competitive analysis
- Roadmap planning

---

## 14. Risks & Mitigations

### 14.1 Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Agent incompatibility with user systems** (Windows versions, antivirus) | High | High | Extensive testing on multiple Windows versions, code signing, clear system requirements |
| **OpenAI API rate limits** | Medium | Medium | Implement exponential backoff, user API key model (users bring own keys), caching |
| **Network drive access issues** (permissions, VPNs) | High | High | Comprehensive error handling, retry logic, detailed setup documentation, test connection wizard |
| **Agent crashes due to edge cases** | Medium | High | Extensive testing, crash reporting (Sentry), automatic error recovery, rollback mechanism |
| **Database performance degradation** | Low | High | Query optimization, proper indexing, connection pooling, monitoring alerts, Supabase scaling |
| **Supabase/Vercel outages** | Low | High | Status page monitoring, failover plan, cached downloads, graceful degradation |

### 14.2 Security Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Agent executable flagged as malware** | Medium | High | Code signing certificate, VirusTotal checks, whitepaper explaining safety, reputation building |
| **OpenAI API key theft** | Medium | High | Encrypt keys with Windows DPAPI, user education, key rotation guidance, detect unusual usage |
| **Unauthorized agent distribution** | Medium | Medium | Checksum verification, signed executables, license verification, DMCA takedown process |
| **Data breach (user emails, files)** | Low | Critical | Encryption at rest/transit, regular security audits, penetration testing, incident response plan |
| **Supply chain attack (dependency compromise)** | Low | High | Lock files, SCA tools (Snyk), minimal dependencies, regular updates, verify package integrity |

### 14.3 Business Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Low user adoption** | Medium | Critical | Beta testing with real PMs, iterate based on feedback, strong marketing, free trial period |
| **High support burden** | High | Medium | Comprehensive documentation, video tutorials, in-app help, FAQ, community forum |
| **Competitor launches similar product** | Medium | High | Focus on differentiation (agent collaboration, ease of use), build brand loyalty, rapid iteration |
| **Licensing/monetization model fails** | Medium | High | Multiple pricing experiments, user feedback, flexible plans, freemium option |
| **Scope creep (50 agents)** | High | Medium | Phased roadmap, MVP focus, prioritization framework, regular scope reviews |

### 14.4 Compliance & Legal Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **GDPR violations** | Low | Critical | Privacy policy, data minimization, user consent, right to deletion, DPO if needed |
| **OpenAI Terms of Service violations** | Low | High | Review ToS, ensure compliant usage, educate users, monitor for abuse |
| **Software licensing issues (dependencies)** | Low | Medium | License audit, use permissive licenses (MIT, Apache), legal review |
| **Intellectual property disputes** | Low | High | Trademark search, clear ownership policies, open-source contribution agreements |

### 14.5 User Experience Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Confusing setup process** | High | High | User testing, step-by-step wizard, video walkthrough, pre-configuration templates |
| **Agent doesn't match expectations** | Medium | High | Clear marketing messaging, demo videos, realistic use cases, 30-day money-back guarantee |
| **Poor error messages (technical jargon)** | Medium | Medium | UX writing guidelines, user-friendly messages, actionable next steps, context-sensitive help |
| **Performance issues on older hardware** | Medium | Medium | System requirements page, performance optimization, lightweight mode, graceful degradation |

---

## 15. Roadmap

### 15.1 Phase 1: MVP (Months 1-3)

**Month 1: Foundation**
- ✅ Set up repositories (web app, agent-1)
- ✅ Design database schema
- ✅ Build landing page (marketing)
- ✅ Implement authentication (Supabase Auth)
- ✅ Create basic dashboard UI

**Month 2: Core Development**
- ✅ Build Agent #1 core functionality
  - Email parsing
  - AEMA code extraction
  - Folder creation logic
- ✅ Implement OpenAI integration
- ✅ Build agent GUI (drag-and-drop interface)
- ✅ Create download API endpoints

**Month 3: Testing & Launch**
- ✅ Comprehensive testing (unit, integration, E2E)
- ✅ Beta testing with 10-20 project managers
- ✅ Documentation (user guides, API docs)
- ✅ Code signing certificate
- ✅ Soft launch to early adopters

**Deliverables:**
- Functional web app with auth + download
- Agent #1 executable (Windows)
- Basic analytics dashboard
- Documentation site

---

### 15.2 Phase 2: Licensing & Monetization (Months 4-6)

**Month 4: Organization Features**
- Organization accounts
- Admin dashboard (manage team, view usage)
- License key system
- Seat management

**Month 5: Payment Integration**
- Stripe integration (subscriptions)
- Pricing page with multiple tiers
- Invoice generation
- Payment webhooks and handling

**Month 6: Polish & Marketing**
- Agent configuration presets (org-level)
- Usage analytics per user
- Marketing campaign launch
- Customer onboarding flow
- Support system (ticketing)

**Deliverables:**
- Fully functional licensing system
- Payment processing
- Organization management
- Marketing materials

---

### 15.3 Phase 3: Agent Expansion (Months 7-12)

**Month 7-8: Agent #2 Development**
- Design Agent #2 (TBD use case)
- Build agent with inter-agent communication
- Shared data store (SQLite)
- Dependency management

**Month 9-10: Agent #3-5 Development**
- Develop 3 more agents based on user feedback
- Build agent marketplace UI
- Agent bundling and discounts

**Month 11-12: Advanced Features**
- Agent collaboration workflows
- Workflow builder (visual UI)
- Advanced analytics and insights
- Mobile app (view analytics, trigger agents remotely)

**Deliverables:**
- 5 total agents in marketplace
- Inter-agent communication framework
- Workflow orchestration
- Mobile app (iOS/Android)

---

### 15.4 Phase 4: Enterprise & Scale (Year 2)

**Q1 Year 2:**
- Enterprise features (SSO, custom SLAs)
- API for third-party integrations
- White-label options
- Advanced security (SOC 2 compliance)

**Q2 Year 2:**
- Agent SDK for custom agent development
- Community marketplace (user-contributed agents)
- Advanced AI features (custom models, fine-tuning)

**Q3 Year 2:**
- International expansion (multi-language)
- Partnerships with PM tool vendors (Jira, Asana)
- Cross-platform agents (macOS, Linux)

**Q4 Year 2:**
- 50 agents in marketplace
- Enterprise customer success team
- Annual user conference

---

### 15.5 Feature Prioritization Framework

**MoSCoW Method:**

**Must Have (MVP):**
- User authentication
- Agent #1 download
- Email parsing and folder creation
- Basic error handling
- Documentation

**Should Have (Phase 2):**
- Organization licensing
- Payment integration
- Admin dashboard
- Auto-updates

**Could Have (Phase 3):**
- Inter-agent communication
- Workflow builder
- Advanced analytics
- Mobile app

**Won't Have (Future):**
- Custom AI model fine-tuning
- White-label solutions
- Enterprise SSO (until Phase 4)

---

## 16. Appendices

### 16.1 Glossary

- **Agent:** A standalone executable that automates specific PM tasks
- **AEMA Code:** Project identifier format (e.g., AEMA-12345)
- **Organization:** A company/entity that purchases licenses
- **Seat:** A licensed user within an organization
- **Installation ID:** Unique identifier for each agent installation
- **Shift-Left Testing:** Testing earlier in development lifecycle
- **TDD:** Test-Driven Development
- **Artifact:** Downloadable agent executable file
- **RLS:** Row Level Security (database access control)
- **JWT:** JSON Web Token (authentication)
- **CSP:** Content Security Policy (security header)

### 16.2 Technical Dependencies

**Web Application:**
```json
{
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "@supabase/supabase-js": "^2.38.0",
    "@supabase/auth-helpers-nextjs": "^0.8.0",
    "tailwindcss": "^3.3.0",
    "@radix-ui/react-dialog": "^1.0.5",
    "lucide-react": "^0.292.0",
    "zod": "^3.22.0",
    "react-hook-form": "^7.48.0"
  },
  "devDependencies": {
    "@testing-library/react": "^14.1.0",
    "@playwright/test": "^1.40.0",
    "jest": "^29.7.0",
    "eslint": "^8.54.0",
    "typescript": "^5.3.0"
  }
}
```

**Desktop Agent:**
```
# requirements.txt
openai==1.3.0
pyinstaller==6.2.0
extract-msg==0.46.0
beautifulsoup4==4.12.2
requests==2.31.0
pillow==10.1.0
pytest==7.4.3
pytest-cov==4.1.0
bandit==1.7.5
```

### 16.3 API Rate Limits

**Rate Limiting Strategy:**
All rate limits are enforced at the API Gateway level (Vercel Edge Middleware) and use a sliding window algorithm with Redis/Upstash for distributed rate limiting.

| Endpoint | Rate Limit | Window | Applies To |
|----------|-----------|--------|------------|
| POST /api/auth/login | 5 requests | 15 minutes | Per IP address |
| POST /api/auth/signup | 3 requests | 1 hour | Per IP address |
| POST /api/auth/reset-password | 3 requests | 1 hour | Per email |
| GET /api/agents | 100 requests | 1 minute | Per authenticated user |
| GET /api/agents/:id | 100 requests | 1 minute | Per authenticated user |
| GET /api/agents/:id/download | 10 requests | 1 hour | Per authenticated user |
| POST /api/analytics/usage | 100 requests | 1 hour | Per installation_id |
| GET /api/user/profile | 60 requests | 1 minute | Per authenticated user |
| PUT /api/user/profile | 10 requests | 1 minute | Per authenticated user |
| POST /api/license/verify | 1000 requests | 1 hour | Per installation_id |

**Rate Limit Headers:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000
```

**Rate Limit Response (429):**
```json
{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again later.",
  "retry_after": 60
}
```

### 16.4 System Requirements

**Desktop Agent Minimum Requirements:**
- **Operating System:** Windows 10 (64-bit) or later
- **RAM:** 4 GB minimum, 8 GB recommended
- **Disk Space:** 200 MB for agent + 500 MB for operations
- **Network:** Internet connection required for license verification and updates
- **Other:** 
  - Microsoft Outlook (for email drag-and-drop)
  - Network drive access permissions
  - OpenAI API key (user-provided)

**Web Application Browser Support:**
- Chrome/Edge 100+
- Firefox 100+
- Safari 15+
- Mobile: iOS Safari 15+, Chrome Mobile 100+

### 16.5 Code Style Guidelines

**JavaScript/TypeScript (Web App):**
```javascript
// Use Prettier + ESLint
// .prettierrc
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}

// Naming conventions
const userName = 'john'; // camelCase for variables
const UserProfile = () => {}; // PascalCase for components
const API_BASE_URL = '...'; // UPPER_SNAKE_CASE for constants

// File naming
user-profile.tsx // kebab-case for files
UserProfile.tsx // PascalCase for component files
```

**Python (Desktop Agent):**
```python
# PEP 8 compliant
# Use black formatter + pylint

# Naming conventions
user_name = "john"  # snake_case for variables
class EmailParser:  # PascalCase for classes
API_KEY = "..."  # UPPER_SNAKE_CASE for constants

# File naming
email_parser.py  # snake_case for modules
```

### 16.6 Documentation Structure

**Documentation Structure (docs.pminions.com):**
```
/getting-started
  /signup-and-download
  /first-agent-setup
  /basic-usage
  
/user-guides
  /agent-1-project-booking
    /email-configuration
    /network-path-setup
    /troubleshooting
  /dashboard-overview
  /managing-downloads
  
/faqs
  /general
  /technical
  /billing (Phase 2)
  
/api-reference
  /authentication
  /agents
  /analytics
  
  /developer-docs
  /architecture
  /contributing
  /building-custom-agents
```

### 16.7 Support & Feedback Channels

**User Support:**
- **Email:** support@pminions.com (Response SLA: 24 hours)
- **Documentation:** docs.pminions.com
- **Community Forum:** community.pminions.com (Discord/Discourse)
- **Status Page:** status.pminions.com (uptime monitoring)

**Feature Requests & Bugs:**
- **GitHub Issues:** github.com/pminions/web-app/issues (public)
- **In-App Feedback:** Feedback widget in dashboard
- **User Interviews:** Monthly sessions with power users

**Release Communications:**
- **Changelog:** changelog.pminions.com
- **Email Newsletter:** Monthly product updates
- **Social Media:** 
  - Primary: @pminions (Twitter/X, LinkedIn)
  - Alternative handles: @pminionshq (if primary unavailable)
  - Recommendation: Secure handles before public launch

### 16.8 Competitive Analysis

| Feature | PMinions | Competitor A | Competitor B |
|---------|-----------|--------------|--------------|
| **AI-Powered Automation** | ✅ ChatGPT | ❌ Rules-based | ✅ Custom AI |
| **Local Execution** | ✅ Desktop agent | ❌ Cloud-only | ✅ Desktop |
| **Email Integration** | ✅ Drag-and-drop | ✅ Full Outlook | ⚠️ Gmail only |
| **Network Drive Access** | ✅ Native Windows | ❌ Cloud storage | ✅ Windows |
| **Multi-Agent Collaboration** | ✅ (Phase 3) | ❌ Single tools | ❌ Separate |
| **Pricing** | TBD | $49/mo per user | $99/mo org |
| **Setup Time** | <10 minutes | ~30 minutes | ~1 hour |
| **Code Signing** | ✅ EV Certificate | ⚠️ Standard | ✅ EV |

**Key Differentiators:**
1. **Ease of Use:** Minimal setup, no admin permissions needed
2. **AI Intelligence:** ChatGPT-powered decision making (not just rules)
3. **Agent Collaboration:** 50 agents working together (future)
4. **Local Privacy:** Data stays on user's machine (network drives)

### 16.9 Marketing & Go-to-Market Strategy

**Target Audience:**
- **Primary:** Mid-size consulting firms (50-200 employees)
- **Secondary:** Enterprise PM teams (200+ employees)
- **Tertiary:** Freelance/solo PMs (long-tail)

**Marketing Channels:**
- **Content Marketing:** Blog posts on PM productivity, SEO optimization
- **Product Hunt:** Launch on Product Hunt (aim for #1 product of the day)
- **LinkedIn Ads:** Target project managers, decision-makers
- **PM Communities:** Reddit (r/projectmanagement), PM forums
- **Partnerships:** Integrate with Asana, Jira (co-marketing)
- **YouTube:** Demo videos, tutorials, case studies
- **Referral Program:** Give $50 credit for successful referrals

**Launch Plan (Month 3):**
1. **Week 1:** Beta user testimonials, press kit
2. **Week 2:** Product Hunt launch, email blast to waitlist
3. **Week 3:** LinkedIn campaign, PM community posts
4. **Week 4:** Webinar "10x Your PM Productivity with AI Agents"

**Growth Metrics:**
- Month 1-3: 100 signups (organic + early adopters)
- Month 4-6: 500 signups (marketing ramp-up)
- Month 7-12: 1,000+ signups (product-led growth)

### 16.10 Customer Success & Onboarding

**Onboarding Email Sequence:**
1. **Day 0 (Signup):** Welcome email + link to download Agent #1
2. **Day 1:** "Getting Started" guide + setup video
3. **Day 3:** "Pro Tips" for maximizing efficiency
4. **Day 7:** Check-in email "How's it going?" + feedback request
5. **Day 14:** Feature announcement + invite to community
6. **Day 30:** Case study showcase + referral program

**In-App Onboarding:**
- **First Login:** Interactive tutorial (Intro.js or similar)
- **First Download:** Step-by-step agent setup wizard
- **First Run:** Success celebration + next steps

**Customer Health Scores:**
- **Green (Healthy):** 10+ agent runs per week, no support tickets
- **Yellow (At Risk):** <5 runs per week, 1-2 support tickets
- **Red (Churning):** No activity in 7 days, multiple tickets

**Proactive Outreach:**
- Yellow: Automated "Need help?" email + resource links
- Red: Personal email from customer success manager

### 16.11 Legal & Compliance Checklist

**Before Launch:**
- ✅ Terms of Service (reviewed by lawyer)
- ✅ Privacy Policy (GDPR + CCPA compliant)
- ✅ Cookie Policy and consent banner
- ✅ Acceptable Use Policy (prevent abuse)
- ✅ OpenAI API Terms compliance review
- ✅ Code signing certificate purchased
- ✅ Trademark search for "PMinions"
- ✅ Domain ownership (pminions.com)

**Ongoing Compliance:**
- Quarterly privacy policy review
- Annual security audit
- GDPR data processing agreements (Phase 2 - enterprise)
- SOC 2 Type II certification (Year 2)

### 16.12 Budget Estimates (MVP - Phase 1)

**Development Costs (3 months):**
- Engineering (2 full-time developers @ $30/hr): $60,000
- Product Management (1 part-time @ $50/hr): $12,000
- Design (UI/UX contractor): $10,000
- QA/Testing (contractor): $8,000
- **Subtotal: $90,000**

**Infrastructure (Monthly):**
- Vercel Pro: $20/month
- Supabase Pro: $25/month
- Domain + SSL (annual): ~$4/month
- Code Signing Certificate (annual): ~$33/month
- **Subtotal: $82/month**

**Development Tools & Services (Monthly):**
- GitHub Team (2 users @ $4/user): $8/month
- Sentry (Team plan): $26/month
- Datadog (Starter): $15/month
- Design tools (Figma Professional): $15/month
- OpenAI API (testing): $50/month (estimated)
- Postman/Insomnia (API testing): $15/month
- **Subtotal: $129/month**

**Marketing & Launch:**
- Landing page copywriting: $500
- Demo videos (professional): $2,000
- Product Hunt launch prep: $500
- Initial ad budget (testing): $1,000
- **Subtotal: $4,000**

**Legal & Compliance:**
- Terms of Service review: $1,500
- Privacy Policy (GDPR compliant): $1,500
- Trademark search & filing: $1,000
- **Subtotal: $4,000**

**Total Phase 1 Budget:**
- **One-time costs:** ~$98,000
- **Monthly recurring:** ~$211/month
- **3-month total:** ~$98,633

**Phase 2 (Licensing & Monetization) - Additional Costs:**
- Stripe integration development: $5,000
- Payment processing fees: 2.9% + $0.30 per transaction
- Customer support tool (Intercom/Zendesk): $79/month
- **Estimated additional:** $10,000 + ongoing fees

**Cost Optimization Notes:**
- Consider remote/international developers for cost savings
- Use free tiers for initial testing (Vercel Hobby, Supabase Free)
- Delay premium tools until after revenue validation
- Bootstrap marketing with organic content initially

### 16.13 Team Structure & Roles

**Phase 1 (MVP):**
- **1x Full-Stack Developer** (Web app, API)
- **1x Python Developer** (Desktop agent)
- **1x Product Manager** (PRD owner, user research)
- **1x UI/UX Designer** (part-time contractor)
- **1x QA Engineer** (part-time, testing)

**Phase 2 (Growth):**
- Add: 1x Backend Developer (licensing, payments)
- Add: 1x Customer Success Manager
- Add: 1x Marketing Manager

**Phase 3 (Scale):**
- Add: 2x Agent Developers
- Add: 1x DevOps Engineer
- Add: 1x Technical Writer (documentation)

### 16.14 Assumptions & Dependencies

**Key Assumptions:**
1. Project managers spend 8+ hours/week on manual setup tasks
2. Organizations willing to pay for productivity tools
3. Windows remains dominant OS in enterprise environments
4. OpenAI API remains accessible and affordable
5. Users have OpenAI API keys or willing to purchase

**External Dependencies:**
- **OpenAI API:** Pricing stability, uptime, terms of service
- **Vercel:** Platform availability, pricing model
- **Supabase:** Database performance, storage limits
- **Microsoft Outlook:** Email format compatibility (.msg)
- **Windows OS:** File system APIs, network drive access

**Risk Mitigation:**
- OpenAI: Consider alternative LLMs (Anthropic Claude, local models)
- Vercel: Have migration plan to AWS/GCP if needed
- Supabase: Database backups, self-hosting option available
- Outlook: Support .eml format (universal)
- Windows: Plan macOS/Linux versions (Phase 4)

### 16.15 Frequently Asked Questions (Internal)

**Q: Why desktop agents instead of cloud-based?**
A: Security and privacy. Enterprise users prefer data staying on their network drives. Also eliminates our liability for handling sensitive customer files, and reduces infrastructure costs significantly.

**Q: Why user-provided OpenAI API keys?**
A: Cost control and scalability. OpenAI usage can be unpredictable and expensive at scale. Users bringing their own keys means:
- We avoid API cost surprises
- Users have full control over their AI spending
- Enterprise customers can use their existing OpenAI agreements
- May offer bundled pricing option in Phase 2 based on demand

**Q: Why focus on Windows first?**
A: Market prioritization. 85-90% of enterprise PM workstations run Windows. macOS is more common in tech startups but smaller overall market. Linux is niche for desktop PM work. We'll expand to macOS in Phase 4 based on demand.

**Q: How do we prevent piracy?**
A: Balanced approach:
- Code signing (prevents malware warnings, builds trust)
- License verification (phone home periodically)
- NOT using aggressive DRM (creates friction)
- Focus: Provide so much value that piracy isn't worth the hassle
- Enterprise customers need proper licenses for compliance anyway

**Q: What if users don't have OpenAI API keys?**
A: Multi-pronged strategy:
- Clear setup guide with screenshots
- Partner with OpenAI for potential discounted keys
- Offer bundled pricing option (Phase 2)
- Consider alternative: We provide API access, charge premium
- Reality: Most enterprise users can expense $20/month easily

**Q: How do agents work offline?**
A: Limited offline capability:
- Core file operations work (folder creation, file copying)
- AI features require internet (OpenAI API)
- License verification: Grace period of 7 days / 50 uses before re-check
- Cached data can enable some features temporarily
- Full offline mode not a priority (network drives require connectivity anyway)

**Q: Can agents work with Gmail/Google Workspace?**
A: Yes, planned for Phase 3:
- Gmail uses .eml format (already supported for parsing)
- Drag-and-drop works same way
- Full integration (no drag-and-drop) needs Gmail API + OAuth
- Enterprise Google Workspace is major opportunity
- Will require separate authentication flow

**Q: What about mobile devices?**
A: Mobile app is Phase 3 feature:
- Mobile app lets users trigger agents remotely
- View analytics and agent status
- Manage configurations
- Agents still run on desktop (file system access required)
- Think: Mobile as remote control, not replacement

**Q: How do we handle agent updates without breaking user workflows?**
A: Careful update strategy:
- Semantic versioning (major.minor.patch)
- Backwards compatible minor/patch updates
- User control: Auto-update for patches, prompt for major versions
- Rollback feature (keep previous version)
- Beta channel for early adopters
- Clear changelog with breaking changes highlighted

**Q: What if OpenAI changes their pricing or API?**
A: Mitigation plan:
- Monitor OpenAI announcements closely
- Build abstraction layer (swap LLM providers easily)
- Alternative providers ready: Anthropic Claude, local models (Ollama)
- User-provided keys means users absorb price changes
- Our code works with any OpenAI-compatible API

**Q: How do we compete with Microsoft Copilot or similar built-in tools?**
A: Differentiation strategy:
- Specialized for PM workflows (not generic)
- 50+ purpose-built agents vs one general assistant
- Works across all tools (not locked to Microsoft ecosystem)
- Local execution (more control, privacy)
- Agent collaboration (unique feature)
- Better at niche PM tasks than general AI

**Q: What's our data retention policy?**
A: Privacy-first approach:
- User data: Retained as long as account active
- Usage analytics: Anonymized, 90 days detailed, 2 years aggregated
- Logs: 30 days operational logs, deleted after
- Email content: NEVER stored on our servers (stays local)
- GDPR: Right to deletion honored within 30 days
- Backups: 30 days, encrypted

**Q: How do we ensure agent quality with 50 agents?**
A: Quality framework:
- Standardized testing requirements for all agents
- Shared codebase for common functions (agent-shared repo)
- Code review process (2 approvers minimum)
- Beta testing period for each agent (30 days minimum)
- Success rate monitoring (must maintain >95%)
- User feedback loop and rapid iteration
- Agent certification process before marketplace listing

---

## 17. Conclusion & Next Steps

### 17.1 Summary

PMinions is positioned to revolutionize project management workflows through intelligent, locally-running AI agents. By combining:

- **AI-powered automation** (ChatGPT integration)
- **Enterprise-grade security** (local execution, code signing)
- **Seamless user experience** (drag-and-drop, minimal setup)
- **Scalable architecture** (50+ agents, inter-agent collaboration)

We create a unique value proposition that reduces PM administrative burden by 60% while respecting data privacy and enterprise requirements.

**Key Success Factors:**
1. Laser focus on user experience (setup in <10 minutes)
2. Robust error handling and recovery (99%+ success rate)
3. Clear documentation and support
4. Rapid iteration based on user feedback
5. Building trust through transparency and security

**Market Opportunity:**
- 3M+ project managers globally
- Growing adoption of AI automation tools
- Enterprise appetite for productivity enhancement
- Gap in specialized PM automation vs generic AI tools

### 17.2 Immediate Next Steps (Week 1-2)

**Technical Setup:**
- [ ] Create GitHub organization and repositories
  - web-app (Next.js + Supabase)
  - agent-1-project-booking (Python)
  - agent-shared (Common utilities)
  - docs (Documentation site)
- [ ] Set up Vercel project (connect to GitHub)
- [ ] Create Supabase projects (dev, staging, prod)
- [ ] Initialize Next.js app with TypeScript + Tailwind + shadcn/ui
- [ ] Set up Python project structure for Agent #1
- [ ] Configure CI/CD pipelines (GitHub Actions)
- [ ] Set up development environments for team

**Design:**
- [ ] Create design system in Figma (colors, typography, components)
- [ ] Design landing page mockups (desktop + mobile)
- [ ] Design dashboard wireframes and user flows
- [ ] Design agent UI (drag-and-drop interface)
- [ ] Create brand assets (logo, favicon, social media graphics)
- [ ] Design email templates (onboarding sequence)

**Product:**
- [ ] Finalize MVP feature set (review and lock PRD)
- [ ] Create detailed user stories with acceptance criteria
- [ ] Set up project management tool (Linear, Jira, or GitHub Projects)
- [ ] Recruit 5-10 PMs for user research interviews
- [ ] Draft user documentation outline and structure
- [ ] Create product demo script

**Business:**
- [ ] Register domain (pminions.com + variations)
- [ ] Secure social media handles (@pminions or alternatives)
- [ ] Set up company email (Google Workspace)
- [ ] Draft and review Terms of Service and Privacy Policy
- [ ] Purchase EV Code Signing Certificate (DigiCert/Sectigo)
- [ ] Set up analytics accounts (Vercel, Sentry, PostHog)
- [ ] Create pitch deck for potential stakeholders/investors

### 17.3 Development Sprints (2-Week Cycles)

**Sprint 1-2 (Weeks 1-4): Foundation**
- Authentication system (Supabase Auth)
- Database schema implementation and testing
- Landing page (hero, features, CTA)
- Agent #1 basic project structure
- Email parsing proof of concept
- CI/CD pipeline setup

**Sprint 3-4 (Weeks 5-8): Core Features**
- Complete email parsing logic (.msg and .eml)
- AEMA code extraction with regex
- File system operations (folder creation, file copying)
- OpenAI integration and prompt engineering
- Agent GUI (Tkinter drag-and-drop interface)
- Download functionality and signed URLs

**Sprint 5-6 (Weeks 9-12): Polish & Testing**
- Agent GUI refinement and error states
- Comprehensive error handling and recovery
- Auto-update mechanism
- Security hardening (penetration testing)
- Unit + Integration + E2E tests (achieve >80% coverage)
- Documentation (user guides, API reference)
- Beta testing with recruited users (20+ participants)
- Bug fixes and performance optimization

**Post-MVP (Month 4+): Phase 2 Development**
- See Roadmap section for detailed Phase 2-4 plans

### 17.4 Decision Points & Gates

**Gate 1: Proceed to Full Development (Week 2)**
- ✅ PRD reviewed and approved by stakeholders
- ✅ Technical feasibility confirmed (PyInstaller testing completed)
- ✅ Budget approved and allocated
- ✅ Team assembled (developers, designer, PM)
- ✅ OpenAI API access confirmed and tested
- ✅ Initial user research completed (5+ interviews)

**Gate 2: Enter Beta Testing (Month 3)**
- All automated tests passing (unit, integration, E2E)
- Security audit completed (basic vulnerability scan)
- Code signing working (no Windows warnings)
- Documentation complete (80%+ of user guides)
- At least 20 beta users recruited and onboarded
- Agent success rate >90% in internal testing
- No P0/P1 bugs remaining

**Gate 3: Public Launch (Month 3-4)**
- Beta feedback incorporated (major issues resolved)
- Performance targets met (API <500ms p95, agent startup <5s)
- Support system ready (email, docs, community forum)
- Marketing materials prepared (videos, case studies, social posts)
- Legal documents finalized and reviewed
- Payment system tested (if Phase 2 ready)
- Monitoring and alerting configured
- 3+ customer testimonials secured

**Gate 4: Phase 2 Launch (Month 6)**
- 100+ active users from Phase 1
- Licensing system tested with pilot customers
- Payment integration fully functional
- Organization management features complete
- Positive cash flow or funding secured
- Team scaled appropriately

### 17.5 Success Definition

**Phase 1 will be considered successful if (within 3 months of public launch):**
- ✅ 100+ active users (running agents at least weekly)
- ✅ Agent #1 success rate >95% (successful operations / total attempts)
- ✅ NPS score >40 (calculated from user surveys)
- ✅ <5 critical bugs reported (P0/P1 severity)
- ✅ 3+ positive case studies/testimonials collected
- ✅ Technical foundation proven (can support 50 agents architecturally)
- ✅ 60%+ user activation rate (signups → downloads → active usage)
- ✅ <5% churn rate (users stopping usage within first month)
- ✅ Average 5+ hours/week time saved per user (self-reported)

**Additional Success Indicators:**
- Product Hunt launch: Top 5 product of the day
- Media coverage: 2+ tech blog mentions
- Community growth: 200+ Discord/Forum members
- Support burden: <10% of users require support contact
- Performance: 99%+ uptime for web app and API

### 17.6 Risk Review & Contingency Plans

**If adoption is slower than expected (<50 users in Month 3):**
- Conduct user research to identify friction points
- Offer extended free trial or freemium tier
- Increase marketing spend on proven channels
- Pivot messaging based on user feedback
- Consider different target market (freelancers vs enterprise)

**If technical issues prevent launch:**
- Fall back to manual beta testing period extension
- Reduce scope: Launch with limited features
- Hire additional QA/engineering resources
- Consider off-the-shelf solutions for problematic components

**If competitor launches similar product:**
- Double down on differentiation (agent collaboration, ease of use)
- Accelerate Phase 2-3 development
- Build stronger community and brand loyalty
- Consider strategic partnerships

**If budget exceeds projections:**
- Seek additional funding (angel, VC, or revenue-based financing)
- Reduce team size or use contractors
- Delay non-critical features
- Prioritize revenue-generating Phase 2 features

### 16.16 Open Questions & Decision Timeline

**To Be Resolved Before Development (Week 1-2):**

1. **Agent Naming Convention**
   - Option A: Descriptive names (e.g., "Project Booking Agent", "Status Reporter")
   - Option B: Code names (e.g., "Agent Alpha", "Agent Beta") + descriptive tagline
   - Option C: Minion themed names (e.g., "Bob the Booking Minion")
   - **Decision needed by:** Sprint 1 kickoff
   - **Owner:** Product Manager + Marketing

2. **OpenAI Model Default**
   - Current plan: GPT-4 (best quality, higher cost)
   - Alternative: GPT-3.5-Turbo (faster, cheaper, good enough?)
   - Hybrid: GPT-3.5 by default, GPT-4 optional upgrade
   - **Decision needed by:** Agent development start
   - **Owner:** Engineering Lead

3. **Installation Method**
   - Option A: Direct .exe download (simplest)
   - Option B: Installer package with auto-update built-in
   - Option C: Microsoft Store distribution (trusted, but complex approval)
   - **Decision needed by:** Month 2
   - **Owner:** Engineering Lead

**To Be Resolved Before Beta Launch (Month 3):**

4. **Beta Program Structure**
   - Free beta for X months with feedback requirement?
   - Paid beta at discounted rate?
   - Invitation-only or open signup?
   - How many beta testers (target: 20-50)?
   - **Decision needed by:** Week 8
   - **Owner:** Product Manager

5. **Community Platform Choice**
   - Discord (popular with developers, real-time)
   - Discourse (forum-style, better for long-term knowledge)
   - Slack (familiar to enterprise, but paid for support)
   - GitHub Discussions (integrated with development)
   - **Decision needed by:** Week 10
   - **Owner:** Product Manager + Community Lead

6. **Documentation Platform**
   - GitBook (beautiful, expensive)
   - Docusaurus (free, developer-friendly)
   - Notion (easy to use, less technical feel)
   - Custom built with Next.js
   - **Decision needed by:** Week 8
   - **Owner:** Technical Writer + Engineering

**To Be Resolved Before Phase 2 (Month 4):**

7. **Licensing Model** ⚠️ HIGH PRIORITY
   - Per-user subscription ($X/month per user)
   - Per-organization unlimited users ($Y/month flat)
   - Tiered: Starter (1-10 users), Professional (11-50), Enterprise (51+)
   - Per-agent pricing or bundled?
   - **Decision needed by:** End of Month 3
   - **Owner:** Founder/CEO + Product Manager

8. **Payment Processor**
   - Stripe (most popular, 2.9% + $0.30)
   - Paddle (merchant of record, handles VAT, 5% + $0.50)
   - Both (Stripe for US, Paddle for international)?
   - **Decision needed by:** Start of Month 4
   - **Owner:** Engineering Lead + Finance

9. **Freemium Strategy**
   - Free tier with limited features?
   - Free trial period (14 days, 30 days)?
   - Free forever for Agent #1, paid for additional agents?
   - No free tier (paid only)?
   - **Decision needed by:** End of Month 3
   - **Owner:** Product Manager + Founder

**Future Considerations (Year 1):**

10. **Enterprise Sales Strategy**
    - Self-service only (PLG - Product-Led Growth)
    - Hybrid: Self-service + sales assist for >100 users
    - Full enterprise sales team
    - **Decision needed by:** Month 9
    - **Owner:** Founder/CEO

11. **Internationalization Priority**
    - English-only initially?
    - Which languages second? (Spanish, German, French, Japanese?)
    - Machine translation acceptable or human translation required?
    - **Decision needed by:** End of Year 1
    - **Owner:** Product Manager

12. **White-Label / Reseller Program**
    - Allow partners to rebrand and resell?
    - Revenue share model?
    - **Decision needed by:** Year 2
    - **Owner:** Founder/CEO

---

## Document Metadata

**Version:** 1.0  
**Last Updated:** November 20, 2025  
**Next Review:** December 20, 2025 (post-Sprint 2)  
**Owner:** Product Team  
**Contributors:** Engineering, Design, QA  
**Status:** ✅ Approved for Development  
**Document Type:** Product Requirements Document (PRD)

**Distribution:**
- Internal: All team members
- External: Select stakeholders, beta testers (redacted version)

**Revision History:**
| Version | Date | Author | Changes | Approvers |
|---------|------|--------|---------|-----------|
| 0.1 | 2025-11-20 | Product Team | Initial draft | - |
| 1.0 | 2025-11-20 | Product Team | Complete PRD with all sections | Pending |

**Change Log:**
- v1.0 (2025-11-20): Initial PRD created based on product brief
  - Added comprehensive architecture diagrams
  - Detailed database schema with RLS policies
  - Complete API specifications with examples
  - Testing strategy aligned with TDD/Shift-Left/Agile
  - Modern UI/UX design system specifications
  - Security and compliance framework
  - Deployment and CI/CD pipelines
  - Success metrics and KPIs
  - Risk analysis and mitigation strategies
  - 3-phase roadmap with timeline
  - Budget estimates and team structure
  - Extensive FAQs and decision framework

**Related Documents:**
- Technical Architecture Document (TBD)
- User Research Summary (TBD)
- Competitive Analysis Deep-Dive (TBD)
- Go-to-Market Strategy (TBD)
- Brand Guidelines (TBD)

**Contact Information:**
- Product Questions: product@pminions.com
- Technical Questions: engineering@pminions.com
- Design Questions: design@pminions.com
- Document Feedback: Use inline comments or email product@pminions.com

---

## Approval Signatures

**Product Manager:** ___________________ Date: ___________

**Engineering Lead:** ___________________ Date: ___________

**Design Lead:** ___________________ Date: ___________

**Stakeholder/Founder:** ___________________ Date: ___________

---

*This PRD is a living document and will be updated as we learn from users, market conditions change, and technical constraints evolve. All major changes require approval from the Product Manager and should be tracked in the Change Log.*

---

**Ready to build something amazing? Let's go! 🚀**