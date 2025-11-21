"""
Email Parser for MSG and EML files
"""

import email
from email import policy
from pathlib import Path
from typing import Dict, List, Optional
import tempfile
import os

try:
    import extract_msg
    HAS_EXTRACT_MSG = True
except ImportError:
    HAS_EXTRACT_MSG = False

from bs4 import BeautifulSoup

class EmailParser:
    """Parse email files (.msg and .eml)"""
    
    def parse(self, file_path: Path) -> Optional[Dict]:
        """
        Parse email file
        
        Args:
            file_path: Path to email file
        
        Returns:
            Dictionary with email data or None if failed
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            return None
        
        suffix = file_path.suffix.lower()
        
        if suffix == '.msg':
            return self._parse_msg(file_path)
        elif suffix == '.eml':
            return self._parse_eml(file_path)
        else:
            return None
    
    def _parse_msg(self, file_path: Path) -> Optional[Dict]:
        """Parse Outlook MSG file"""
        
        if not HAS_EXTRACT_MSG:
            print("Error: extract_msg library not installed")
            return None
        
        try:
            msg = extract_msg.Message(str(file_path))
            
            # Extract body (prefer plain text, fall back to HTML)
            body = msg.body
            if not body and msg.htmlBody:
                body = self._html_to_text(msg.htmlBody)
            
            # Extract attachments
            attachments = []
            for attachment in msg.attachments:
                attachments.append({
                    'filename': attachment.longFilename or attachment.shortFilename,
                    'data': attachment.data,
                    'size': len(attachment.data) if attachment.data else 0
                })
            
            email_data = {
                'subject': msg.subject or '',
                'sender': msg.sender or '',
                'to': msg.to or '',
                'cc': msg.cc or '',
                'date': str(msg.date) if msg.date else '',
                'body': body or '',
                'attachments': attachments
            }
            
            msg.close()
            return email_data
        
        except Exception as e:
            print(f"Error parsing MSG file: {e}")
            return None
    
    def _parse_eml(self, file_path: Path) -> Optional[Dict]:
        """Parse EML file"""
        
        try:
            with open(file_path, 'rb') as f:
                msg = email.message_from_binary_file(f, policy=policy.default)
            
            # Extract body
            body = ''
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        body = part.get_content()
                        break
                    elif content_type == 'text/html' and not body:
                        html_body = part.get_content()
                        body = self._html_to_text(html_body)
            else:
                content_type = msg.get_content_type()
                if content_type == 'text/plain':
                    body = msg.get_content()
                elif content_type == 'text/html':
                    body = self._html_to_text(msg.get_content())
            
            # Extract attachments
            attachments = []
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_disposition() == 'attachment':
                        filename = part.get_filename()
                        if filename:
                            attachments.append({
                                'filename': filename,
                                'data': part.get_content(),
                                'size': len(part.get_content())
                            })
            
            email_data = {
                'subject': msg.get('Subject', ''),
                'sender': msg.get('From', ''),
                'to': msg.get('To', ''),
                'cc': msg.get('Cc', ''),
                'date': msg.get('Date', ''),
                'body': body,
                'attachments': attachments
            }
            
            return email_data
        
        except Exception as e:
            print(f"Error parsing EML file: {e}")
            return None
    
    def _html_to_text(self, html: str) -> str:
        """
        Convert HTML to plain text
        
        Args:
            html: HTML string
        
        Returns:
            Plain text
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text()
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
        except Exception as e:
            print(f"Error converting HTML to text: {e}")
            return html

