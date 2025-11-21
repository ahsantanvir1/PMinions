"""
Configuration Manager for Bob agent
Handles loading, saving, and validating configuration
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
import uuid

class ConfigManager:
    """Manages agent configuration"""
    
    DEFAULT_CONFIG_PATH = Path("config.json")
    
    DEFAULT_CONFIG = {
        "version": "1.0.0",
        "user": {
            "agent_id": "",  # Generated on first run
            "email": ""
        },
        "openai": {
            "api_key": "",
            "model": "gpt-3.5-turbo",  # Default to cheaper model
            "max_tokens": 500
        },
        "email_recognition": {
            "sender_whitelist": [],
            "subject_keywords": ["project assignment", "new project"],
            "code_patterns": [r"AEMA-\d{5}"]
        },
        "network": {
            "proposal_folder_path": "",
            "retry_attempts": 3,
            "timeout_seconds": 30
        },
        "updates": {
            "check_on_startup": True,
            "auto_download": False,
            "channel": "stable"
        },
        "analytics": {
            "enabled": True,
            "usage_tracking": True
        }
    }
    
    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize configuration manager
        
        Args:
            config_path: Path to config file (defaults to config.json)
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self.config: Dict[str, Any] = {}
    
    def config_exists(self) -> bool:
        """Check if configuration file exists"""
        return self.config_path.exists()
    
    def load(self) -> bool:
        """
        Load configuration from file
        
        Returns:
            True if loaded successfully, False otherwise
        """
        try:
            if not self.config_exists():
                # Create default config
                self.config = self.DEFAULT_CONFIG.copy()
                # Generate agent ID
                self.config["user"]["agent_id"] = str(uuid.uuid4())
                return False
            
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
            
            # Ensure agent_id exists
            if not self.config.get("user", {}).get("agent_id"):
                self.config["user"]["agent_id"] = str(uuid.uuid4())
                self.save()
            
            return True
        
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = self.DEFAULT_CONFIG.copy()
            return False
    
    def save(self) -> bool:
        """
        Save configuration to file
        
        Returns:
            True if saved successfully, False otherwise
        """
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def validate(self) -> bool:
        """
        Validate configuration
        
        Returns:
            True if valid, False otherwise
        """
        try:
            # Check required fields
            if not self.config.get("openai", {}).get("api_key"):
                return False
            
            if not self.config.get("network", {}).get("proposal_folder_path"):
                return False
            
            # Validate network path exists
            network_path = Path(self.config["network"]["proposal_folder_path"])
            if not network_path.exists():
                print(f"Warning: Network path does not exist: {network_path}")
                # Don't fail validation - might be network drive not mounted
            
            return True
        
        except Exception as e:
            print(f"Validation error: {e}")
            return False
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get configuration value by dot-notation path
        
        Args:
            key_path: Dot-separated path (e.g., "openai.api_key")
            default: Default value if key not found
        
        Returns:
            Configuration value or default
        """
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path: str, value: Any) -> None:
        """
        Set configuration value by dot-notation path
        
        Args:
            key_path: Dot-separated path (e.g., "openai.api_key")
            value: Value to set
        """
        keys = key_path.split('.')
        config = self.config
        
        # Navigate to the parent dict
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        # Set the value
        config[keys[-1]] = value
    
    def get_all(self) -> Dict[str, Any]:
        """Get entire configuration"""
        return self.config.copy()
    
    def reset_to_defaults(self) -> None:
        """Reset configuration to defaults"""
        self.config = self.DEFAULT_CONFIG.copy()
        self.config["user"]["agent_id"] = str(uuid.uuid4())

