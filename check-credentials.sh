#!/bin/bash

# PMinions - Credentials Checker
# This script checks if all required credentials are filled in

echo "🔐 PMinions Credentials Checker"
echo "================================"
echo ""

CREDENTIALS_DIR=".credentials"
ALL_GOOD=true

# Check GitHub token
if [ -f "$CREDENTIALS_DIR/github-token.txt" ]; then
    if grep -q "ghp_" "$CREDENTIALS_DIR/github-token.txt"; then
        echo "✅ GitHub token found"
    else
        echo "❌ GitHub token missing or invalid"
        ALL_GOOD=false
    fi
else
    echo "❌ GitHub token file not found"
    ALL_GOOD=false
fi

# Check Vercel token
if [ -f "$CREDENTIALS_DIR/vercel-token.txt" ]; then
    VERCEL_CONTENT=$(grep -v "^#" "$CREDENTIALS_DIR/vercel-token.txt" | grep -v "^$")
    if [ ! -z "$VERCEL_CONTENT" ]; then
        echo "✅ Vercel token found"
    else
        echo "❌ Vercel token missing"
        ALL_GOOD=false
    fi
else
    echo "❌ Vercel token file not found"
    ALL_GOOD=false
fi

# Check Supabase credentials
if [ -f "$CREDENTIALS_DIR/supabase-credentials.txt" ]; then
    if grep -q "PROJECT_URL=https://" "$CREDENTIALS_DIR/supabase-credentials.txt" && \
       grep -q "ANON_KEY=eyJ" "$CREDENTIALS_DIR/supabase-credentials.txt" && \
       grep -q "SERVICE_ROLE_KEY=eyJ" "$CREDENTIALS_DIR/supabase-credentials.txt"; then
        echo "✅ Supabase credentials found"
    else
        echo "❌ Supabase credentials incomplete"
        ALL_GOOD=false
    fi
else
    echo "❌ Supabase credentials file not found"
    ALL_GOOD=false
fi

# Check OpenAI key
if [ -f "$CREDENTIALS_DIR/openai-key.txt" ]; then
    if grep -q "sk-" "$CREDENTIALS_DIR/openai-key.txt"; then
        echo "✅ OpenAI API key found"
    else
        echo "❌ OpenAI API key missing or invalid"
        ALL_GOOD=false
    fi
else
    echo "❌ OpenAI API key file not found"
    ALL_GOOD=false
fi

echo ""
echo "================================"

if [ "$ALL_GOOD" = true ]; then
    echo "✅ All credentials are ready!"
    echo ""
    echo "You can now continue with:"
    echo "  - GitHub repository creation"
    echo "  - Vercel deployment"
    echo "  - Supabase setup"
    echo ""
    echo "Tell the AI: 'credentials ready' to continue"
else
    echo "❌ Some credentials are missing"
    echo ""
    echo "Please fill in the missing credentials in:"
    echo "  .credentials/ directory"
    echo ""
    echo "See SETUP-STATUS.md for detailed instructions"
fi

echo ""

