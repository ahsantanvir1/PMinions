import { NextResponse } from 'next/server';

export const dynamic = 'force-dynamic'; // Always run dynamically

export async function GET() {
  const health = {
    status: 'ok',
    timestamp: new Date().toISOString(),
    environment: process.env.NEXT_PUBLIC_ENV || 'development',
    version: '1.0.0',
    services: {
      supabase: {
        configured: !!process.env.NEXT_PUBLIC_SUPABASE_URL,
        url: process.env.NEXT_PUBLIC_SUPABASE_URL ? 
          process.env.NEXT_PUBLIC_SUPABASE_URL.replace(/https?:\/\//, '').split('.')[0] + '.supabase.co' : 
          'not configured'
      },
      api: {
        status: 'operational'
      }
    },
    deployment: {
      vercel: !!process.env.VERCEL,
      region: process.env.VERCEL_REGION || 'local',
      url: process.env.VERCEL_URL || 'localhost:3000'
    }
  };

  return NextResponse.json(health, {
    status: 200,
    headers: {
      'Cache-Control': 'no-store, must-revalidate',
      'Content-Type': 'application/json'
    }
  });
}

