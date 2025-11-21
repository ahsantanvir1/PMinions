# 🤖 Bob - Project Booking & Initiation Agent

**Agent #1 of the PMinions Suite**

Bob is your friendly minion that automates project booking and initiation tasks. He monitors your emails, extracts project codes, and organizes your network folders automatically.

## 🎯 What Bob Does

- **Email Processing**: Drag-and-drop `.msg` or `.eml` files
- **Smart Recognition**: AI-powered project assignment detection
- **Code Extraction**: Automatically finds AEMA-xxxxx project codes
- **Folder Management**: Creates and organizes network folders
- **Attachment Handling**: Copies email attachments to project folders

## 🚀 Quick Start

### First-Time Setup

1. **Run Bob**:
   ```bash
   python src/main.py
   ```

2. **Configuration Wizard** will guide you through:
   - OpenAI API key
   - Network folder path
   - Email sender whitelist
   - Project code patterns

3. **Start Using**:
   - Drag an email file onto Bob's window
   - Bob analyzes it and creates the project folder
   - Done! ✨

## 📋 Requirements

- **OS**: Windows 10+ (64-bit)
- **Python**: 3.11+ (for development)
- **Network**: Access to network drives
- **API**: OpenAI API key

## 🛠️ Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run in Development Mode

```bash
python src/main.py
```

### Run Tests

```bash
pytest tests/
```

### Build Executable

```bash
python build.py
```

## 📁 Project Structure

```
agent-1-bob/
├── src/
│   ├── main.py              # Entry point
│   ├── config/
│   │   ├── config_manager.py
│   │   └── wizard.py
│   ├── core/
│   │   ├── email_parser.py
│   │   ├── code_extractor.py
│   │   ├── file_manager.py
│   │   └── ai_handler.py
│   ├── ui/
│   │   ├── main_window.py
│   │   └── notifications.py
│   └── utils/
│       ├── logger.py
│       └── validator.py
├── tests/
├── config.json              # User configuration
├── requirements.txt
└── build.py                 # PyInstaller build script
```

## 🎨 Features

### Current Version (v0.1.0)

- ✅ Email drag-and-drop interface
- ✅ MSG and EML file support
- ✅ AEMA code extraction
- ✅ Network folder creation
- ✅ AI-powered email analysis
- ✅ Configuration wizard
- ✅ Error handling and logging

### Coming Soon

- ⏳ Direct Outlook integration
- ⏳ Automatic email monitoring
- ⏳ Custom AI prompts
- ⏳ Integration with project management tools

## 🐛 Troubleshooting

### Bob can't access network drives
- Check network path in configuration
- Ensure you have write permissions
- Try accessing the path manually first

### OpenAI API errors
- Verify your API key is valid
- Check your OpenAI account has credits
- Review rate limits

### Email parsing fails
- Ensure file is `.msg` or `.eml` format
- Check file isn't corrupted
- Try with a different email

## 📄 License

Proprietary - Part of PMinions Suite

---

**Version**: 0.1.0  
**Status**: 🟡 In Development  
**Minion Name**: Bob (Project Booking Specialist)

