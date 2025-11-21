"""
Project Code Extractor
Extracts AEMA codes and other project identifiers from text
"""

import re
from typing import List

class CodeExtractor:
    """Extract project codes from text"""
    
    def __init__(self, config_manager):
        """
        Initialize code extractor
        
        Args:
            config_manager: ConfigManager instance
        """
        self.config_manager = config_manager
        self.patterns = config_manager.get('email_recognition.code_patterns', [r'AEMA-\d{5}'])
    
    def extract_codes(self, text: str) -> List[str]:
        """
        Extract project codes from text
        
        Args:
            text: Text to search
        
        Returns:
            List of found codes (unique)
        """
        if not text:
            return []
        
        codes = []
        
        for pattern in self.patterns:
            try:
                matches = re.findall(pattern, text, re.IGNORECASE)
                codes.extend(matches)
            except re.error as e:
                print(f"Invalid regex pattern '{pattern}': {e}")
        
        # Remove duplicates while preserving order
        seen = set()
        unique_codes = []
        for code in codes:
            code_upper = code.upper()
            if code_upper not in seen:
                seen.add(code_upper)
                unique_codes.append(code_upper)
        
        return unique_codes
    
    def validate_code(self, code: str) -> bool:
        """
        Validate if a code matches any pattern
        
        Args:
            code: Code to validate
        
        Returns:
            True if valid, False otherwise
        """
        for pattern in self.patterns:
            try:
                if re.match(pattern, code, re.IGNORECASE):
                    return True
            except re.error:
                continue
        
        return False

