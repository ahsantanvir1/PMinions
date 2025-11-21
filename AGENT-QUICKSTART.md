# 🤖 Bob Agent - Quick Start Guide

**Agent #1: Project Booking & Initiation**

Bob is your friendly minion that automates project booking tasks! He can parse emails, extract project codes, and organize your network folders automatically.

---

## 🚀 Getting Started (5 Minutes)

### Step 1: Install Dependencies

```bash
cd agent-1-bob
pip install -r requirements.txt
```

**What gets installed:**
- `openai` - For AI-powered email analysis
- `extract-msg` - To parse Outlook .msg files
- `beautifulsoup4` - For HTML email parsing
- `tkinterdnd2` - For drag-and-drop functionality
- `colorlog` - Pretty colored logs
- Plus testing and security tools

### Step 2: Run Bob for the First Time

```bash
python src/main.py
```

**What happens:**
1. Bob detects it's the first run
2. A configuration wizard appears
3. You'll need to provide:
   - ✅ **OpenAI API Key** (get from https://platform.openai.com/api-keys)
   - ✅ **Network Folder Path** (where Bob should create project folders)
   - ⚪ Your email (optional)

### Step 3: Use Bob!

Once configured:
1. Bob's window opens with a drag-and-drop zone
2. Drag an email file (.msg or .eml) onto the window
3. Bob automatically:
   - Parses the email
   - Finds project codes (like AEMA-12345)
   - Analyzes with AI
   - Creates a project folder
   - Copies attachments
   - Saves metadata

---

## 📧 Supported Email Formats

### Outlook MSG Files (.msg)
- Native Outlook format
- Drag from Outlook or file explorer
- Preserves all attachments

### EML Files (.eml)
- Universal email format
- Works with Gmail, Thunderbird, etc.
- Export from any email client

---

## 🎯 How Bob Works

### 1. Email Processing
```
📧 Email File
    ↓
🔍 Parse email (subject, body, attachments)
    ↓
🔎 Search for project codes (AEMA-xxxxx)
    ↓
🧠 AI Analysis (is this a project assignment?)
    ↓
📁 Create folder on network drive
    ↓
📎 Copy attachments
    ↓
✅ Done!
```

### 2. Project Code Patterns

Bob looks for codes matching these patterns (configurable):
- **Default**: `AEMA-12345` (AEMA- followed by 5 digits)
- **Custom**: Edit `config.json` to add your own patterns

Example:
```json
"code_patterns": [
  "AEMA-\\d{5}",
  "PROJ-\\d{4}",
  "WO-\\d{6}"
]
```

### 3. Folder Structure

Bob creates folders like this:
```
\\network\proposals\
├── AEMA-12345/
│   ├── attachment1.pdf
│   ├── attachment2.docx
│   └── _bob_metadata.json  ← Bob's tracking file
├── AEMA-67890/
│   └── ...
```

### 4. Metadata File

Each folder gets a `_bob_metadata.json`:
```json
{
  "created_at": "2025-11-21T10:30:00",
  "project_code": "AEMA-12345",
  "email_subject": "New Project Assignment",
  "email_sender": "pm@company.com",
  "attachments_copied": ["proposal.pdf", "specs.docx"],
  "agent_version": "0.1.0"
}
```

---

## 🛠️ Configuration

### Config File Location
`agent-1-bob/config.json`

### Full Configuration Options

```json
{
  "version": "1.0.0",
  "user": {
    "agent_id": "auto-generated-uuid",
    "email": "your@email.com"
  },
  "openai": {
    "api_key": "sk-...",
    "model": "gpt-3.5-turbo",  // or "gpt-4" for better quality
    "max_tokens": 500
  },
  "email_recognition": {
    "sender_whitelist": [
      "pm@company.com",
      "projects@company.com"
    ],
    "subject_keywords": [
      "project assignment",
      "new project"
    ],
    "code_patterns": [
      "AEMA-\\d{5}"
    ]
  },
  "network": {
    "proposal_folder_path": "\\\\server\\proposals",
    "retry_attempts": 3,
    "timeout_seconds": 30
  },
  "analytics": {
    "enabled": true,
    "usage_tracking": true
  }
}
```

### Reconfigure Bob

To change settings:
1. Delete `config.json`
2. Run `python src/main.py` again
3. Wizard will reappear

Or edit `config.json` directly.

---

## 🧪 Testing Bob

### Quick Test (No Email Required)

```bash
python test_bob.py
```

This tests:
- ✅ All modules import correctly
- ✅ Code extraction works
- ✅ Dependencies are installed

### Test with Sample Email

Create a test email file:

**test-email.eml:**
```
Subject: New Project AEMA-12345
From: pm@company.com
To: you@company.com

Hi,

Please work on project AEMA-12345 for Client ABC.

Thanks!
```

Save as `test-email.eml` and drag it into Bob!

---

## 🐛 Troubleshooting

### "OpenAI API Error"
**Problem**: Invalid API key or no credits

**Solution**:
1. Check your API key at https://platform.openai.com/api-keys
2. Verify you have credits in your OpenAI account
3. Update `config.json` with correct key

### "Network Path Not Found"
**Problem**: Can't access network drive

**Solution**:
1. Check the path in `config.json`
2. Make sure you're connected to VPN (if needed)
3. Try accessing the path manually in File Explorer
4. Verify you have write permissions

### "No Project Codes Found"
**Problem**: Bob can't find AEMA codes in email

**Solution**:
1. Check the email actually contains codes
2. Verify code pattern in `config.json` matches your format
3. Codes must match exactly (e.g., `AEMA-12345`)

### "Drag-and-Drop Not Working"
**Problem**: tkinterdnd2 not installed properly

**Solution**:
```bash
pip install --force-reinstall tkinterdnd2
```

Or use the "Browse" button instead of drag-and-drop.

### "Permission Denied"
**Problem**: Can't write to network folder

**Solution**:
1. Check folder permissions
2. Try creating a folder manually in that location
3. Contact IT if needed

---

## 📊 What Bob Logs

Bob creates detailed logs in `agent-1-bob/logs/`:

**Console Output:**
- 🟢 INFO: Normal operations
- 🟡 WARNING: Non-critical issues
- 🔴 ERROR: Problems that need attention

**Log Files:**
- `bob_YYYYMMDD.log` - Daily log file
- Rotates at 10MB (keeps last 5 files)
- Includes timestamps and full error details

---

## 🎨 Bob's Personality

Bob is:
- 🤖 **Friendly**: Uses emojis and clear language
- 🎯 **Focused**: Does one thing really well
- 🔒 **Trustworthy**: Logs everything, never loses data
- 🚀 **Fast**: Processes emails in seconds
- 🧠 **Smart**: Uses AI to understand context

---

## 🔮 Coming Soon

Bob's future upgrades:
- ⏳ Direct Outlook integration (no drag-and-drop needed)
- ⏳ Automatic email monitoring
- ⏳ Custom AI prompts
- ⏳ Integration with Jira/Asana
- ⏳ Multiple project code formats
- ⏳ Batch processing

---

## 💡 Pro Tips

1. **Use GPT-4 for Better Analysis**
   - Edit `config.json`: `"model": "gpt-4"`
   - More accurate but slower and more expensive

2. **Add Multiple Code Patterns**
   - Support different project formats
   - Bob finds all matches

3. **Whitelist Senders**
   - Only process emails from specific senders
   - Reduces false positives

4. **Check Logs for Issues**
   - All operations are logged
   - Great for debugging

5. **Backup Your Config**
   - Save `config.json` somewhere safe
   - Easy to restore if needed

---

## 📞 Need Help?

- **Documentation**: See `agent-1-bob/README.md`
- **Test Script**: Run `python test_bob.py`
- **Logs**: Check `logs/bob_YYYYMMDD.log`
- **Config**: Review `config.json`

---

## 🎉 Success!

If you see this in Bob's window:
```
✅ Bob is ready! Waiting for email files...
📁 Network folder: \\server\proposals
```

**You're all set!** Bob is ready to automate your project booking! 🚀

---

**Version**: 0.1.0  
**Agent**: Bob (Project Booking Specialist)  
**Status**: 🟢 Ready for Use

