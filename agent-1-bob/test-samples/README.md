# Test Samples for Bob Agent

This directory contains sample email files for testing Bob's functionality.

## Sample Files

### sample-project-email.eml
A simple test email containing:
- Project code: AEMA-12345
- Client name: ABC Corporation
- Project Manager: Sarah Johnson
- Deadline information

**How to use:**
1. Run Bob: `python src/main.py`
2. Drag `sample-project-email.eml` into Bob's window
3. Bob should:
   - Parse the email
   - Find code AEMA-12345
   - Analyze with AI
   - Create a project folder (if network path is configured)

## Creating Your Own Test Emails

### EML Format (Universal)
```
From: sender@example.com
To: recipient@example.com
Subject: Your Subject Here
Date: Thu, 21 Nov 2025 10:30:00 -0500
Content-Type: text/plain; charset=UTF-8

Your email body here with project codes like AEMA-12345
```

Save as `.eml` file and test!

### MSG Format (Outlook)
- Create an email in Outlook
- Drag it to a folder to save as `.msg`
- Use that file for testing

## Test Scenarios

### Scenario 1: Single Project Code
- Email contains one AEMA code
- Bob should find it and create folder

### Scenario 2: Multiple Project Codes
- Email contains AEMA-12345 and AEMA-67890
- Bob should find both and ask which to use

### Scenario 3: No Project Code
- Email has no AEMA codes
- Bob should report "No project codes found"

### Scenario 4: With Attachments
- Email has PDF/DOCX attachments
- Bob should copy them to project folder

## Notes

- Test emails don't need real attachments
- Network path must be configured for folder creation
- AI analysis requires valid OpenAI API key

