# PMinions Web Application

The web application for PMinions - a marketplace for downloading and managing AI-powered desktop agents.

## Tech Stack

- **Framework:** Next.js 16 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS 4
- **UI Components:** shadcn/ui
- **Database:** Supabase (PostgreSQL)
- **Authentication:** Supabase Auth
- **Hosting:** Vercel
- **Analytics:** Vercel Analytics

## Getting Started

### Prerequisites

- Node.js 20+ 
- npm or yarn
- Supabase account
- Vercel account (for deployment)

### Local Development

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment variables:**
   
   Copy `.env.local.template` to `.env.local`:
   ```bash
   cp .env.local.template .env.local
   ```
   
   Fill in your Supabase credentials:
   ```env
   NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
   SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here
   NEXT_PUBLIC_ENV=development
   ```

3. **Run development server:**
   ```bash
   npm run dev
   ```
   
   Open [http://localhost:3000](http://localhost:3000) in your browser.

4. **Build for production:**
   ```bash
   npm run build
   npm start
   ```

### Project Structure

```
web-app/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── (auth)/            # Auth routes (login, signup)
│   │   ├── (marketing)/       # Public pages (landing)
│   │   ├── dashboard/         # Protected user dashboard
│   │   ├── api/               # API routes
│   │   │   └── health/        # Health check endpoint
│   │   ├── layout.tsx         # Root layout
│   │   └── page.tsx           # Landing page
│   ├── components/
│   │   ├── ui/                # shadcn/ui components
│   │   └── layout/            # Layout components
│   ├── lib/
│   │   ├── supabase/          # Supabase clients
│   │   │   ├── client.ts      # Client-side
│   │   │   └── server.ts      # Server-side
│   │   └── utils.ts           # Utility functions
│   └── styles/
│       └── globals.css        # Global styles
├── public/                    # Static assets
├── .env.local.template        # Environment variables template
├── components.json            # shadcn/ui config
├── next.config.ts             # Next.js config
├── tailwind.config.ts         # Tailwind config
├── tsconfig.json              # TypeScript config
├── vercel.json                # Vercel deployment config
└── package.json
```

## Available Scripts

- `npm run dev` - Start development server (port 3000)
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

## API Routes

### Health Check

**Endpoint:** `GET /api/health`

Returns the health status of the application and its services.

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2025-11-22T12:00:00.000Z",
  "environment": "development",
  "version": "1.0.0",
  "services": {
    "supabase": {
      "configured": true,
      "url": "your-project.supabase.co"
    },
    "api": {
      "status": "operational"
    }
  },
  "deployment": {
    "vercel": false,
    "region": "local",
    "url": "localhost:3000"
  }
}
```

## Deployment

### Deploy to Vercel

See [VERCEL-SETUP.md](../VERCEL-SETUP.md) for detailed deployment instructions.

**Quick Deploy:**

1. Push to GitHub
2. Connect repository to Vercel
3. Configure environment variables
4. Deploy automatically on push to `main`

**Manual Deploy:**

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Deploy to production
vercel --prod
```

### Environment Variables

Required environment variables for deployment:

| Variable | Description | Where to Get |
|----------|-------------|--------------|
| `NEXT_PUBLIC_SUPABASE_URL` | Supabase project URL | Supabase Dashboard → Settings → API |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Supabase anonymous key | Supabase Dashboard → Settings → API |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase service role key (server-only) | Supabase Dashboard → Settings → API |
| `NEXT_PUBLIC_ENV` | Environment name | `development`, `staging`, or `production` |

## Features

### Current (MVP)

- ✅ Modern landing page
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Supabase integration (client & server)
- ✅ shadcn/ui components
- ✅ Health check API
- ✅ Vercel deployment configuration
- ✅ GitHub Actions CI/CD

### Planned (Phase 1)

- ⏭️ User authentication (sign up, login, logout)
- ⏭️ User dashboard
- ⏭️ Agent marketplace
- ⏭️ Agent download functionality
- ⏭️ Download history
- ⏭️ Profile management

### Planned (Phase 2)

- ⏭️ Organization accounts
- ⏭️ License management
- ⏭️ Payment integration (Stripe)
- ⏭️ Admin dashboard
- ⏭️ Usage analytics

## Development Guidelines

### Code Style

- Use TypeScript for all new files
- Follow ESLint rules
- Use Prettier for formatting
- Use functional components with hooks
- Prefer server components over client components

### Component Guidelines

- Place reusable UI components in `src/components/ui/`
- Place layout components in `src/components/layout/`
- Use shadcn/ui components when available
- Create custom components in feature-specific directories

### API Route Guidelines

- Use Next.js App Router API routes (`src/app/api/`)
- Return proper HTTP status codes
- Use TypeScript for type safety
- Validate input data
- Handle errors gracefully

### Supabase Guidelines

- Use server-side client for server components and API routes
- Use client-side client for client components
- Never expose service role key to client
- Use Row Level Security (RLS) policies

## Testing

### Local Testing

1. **Test build:**
   ```bash
   npm run build
   ```

2. **Test health endpoint:**
   ```bash
   curl http://localhost:3000/api/health
   ```

3. **Test in browser:**
   - Open http://localhost:3000
   - Check console for errors (F12)
   - Test responsive design (F12 → Device toolbar)

### Production Testing

1. **Test health endpoint:**
   ```bash
   curl https://your-site.vercel.app/api/health
   ```

2. **Test in browser:**
   - Visit production URL
   - Verify all pages load
   - Check browser console
   - Test on mobile device

## Troubleshooting

### Build Errors

**Error:** `Module not found`

**Solution:**
```bash
rm -rf node_modules package-lock.json .next
npm install
npm run build
```

### Environment Variables Not Working

**Problem:** `undefined` when accessing env vars

**Solution:**
- Ensure `.env.local` exists and has correct values
- Restart dev server after changing env vars
- Client-side vars must start with `NEXT_PUBLIC_`
- Server-side vars don't need prefix

### Supabase Connection Issues

**Problem:** Can't connect to Supabase

**Solution:**
- Verify `NEXT_PUBLIC_SUPABASE_URL` is correct
- Verify `NEXT_PUBLIC_SUPABASE_ANON_KEY` is correct
- Check Supabase project is active
- Check network connectivity

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [Supabase Documentation](https://supabase.com/docs)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [shadcn/ui Documentation](https://ui.shadcn.com)
- [Vercel Documentation](https://vercel.com/docs)

## Support

For issues or questions:
- Create an issue in the GitHub repository
- Check existing documentation
- Contact the development team

---

**Version:** 1.0.0  
**Last Updated:** November 22, 2025
