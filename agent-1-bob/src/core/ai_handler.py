"""
AI Handler for OpenAI integration
"""

import json
from typing import Dict, Optional

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

class AIHandler:
    """Handle OpenAI API interactions"""
    
    def __init__(self, config_manager):
        """
        Initialize AI handler
        
        Args:
            config_manager: ConfigManager instance
        """
        self.config_manager = config_manager
        self.api_key = config_manager.get('openai.api_key')
        self.model = config_manager.get('openai.model', 'gpt-3.5-turbo')
        self.max_tokens = config_manager.get('openai.max_tokens', 500)
        
        if HAS_OPENAI and self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None
    
    def analyze_email(self, email_data: Dict) -> Optional[Dict]:
        """
        Analyze email using AI
        
        Args:
            email_data: Email data dictionary
        
        Returns:
            Analysis results or None if failed
        """
        if not self.client:
            print("OpenAI client not initialized")
            return None
        
        try:
            # Prepare prompt
            prompt = self._create_analysis_prompt(email_data)
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an AI assistant that analyzes project management emails. Respond with JSON only."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=self.max_tokens,
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            # Parse response
            result = response.choices[0].message.content
            analysis = json.loads(result)
            
            return analysis
        
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return None
    
    def _create_analysis_prompt(self, email_data: Dict) -> str:
        """
        Create analysis prompt
        
        Args:
            email_data: Email data
        
        Returns:
            Prompt string
        """
        prompt = f"""Analyze this email and determine if it's a project assignment.

Subject: {email_data.get('subject', 'N/A')}
From: {email_data.get('sender', 'N/A')}
Body: {email_data.get('body', 'N/A')[:1000]}

Provide a JSON response with:
- is_project_assignment: boolean (true if this is a project assignment email)
- client_name: string (extracted client name if found, or null)
- project_manager: string (PM name if mentioned, or null)
- deadline: string (deadline if mentioned, or null)
- confidence: number (0-1, how confident you are)
- notes: string (any additional observations)
"""
        return prompt
    
    def is_available(self) -> bool:
        """Check if AI handler is available"""
        return self.client is not None

