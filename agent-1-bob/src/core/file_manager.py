"""
File Manager for network folder operations
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class FileManager:
    """Manage network folders and file operations"""
    
    def __init__(self, config_manager):
        """
        Initialize file manager
        
        Args:
            config_manager: ConfigManager instance
        """
        self.config_manager = config_manager
        self.base_path = Path(config_manager.get('network.proposal_folder_path'))
        self.retry_attempts = config_manager.get('network.retry_attempts', 3)
    
    def create_project_folder(self, project_code: str, email_data: Dict) -> Dict[str, Any]:
        """
        Create project folder and copy attachments
        
        Args:
            project_code: Project code (e.g., AEMA-12345)
            email_data: Email data dictionary
        
        Returns:
            Dictionary with success status and details
        """
        try:
            # Validate base path
            if not self.base_path.exists():
                return {
                    'success': False,
                    'error': f"Network path does not exist: {self.base_path}"
                }
            
            # Create folder path
            folder_path = self.base_path / project_code
            
            # Check if folder already exists
            if folder_path.exists():
                return {
                    'success': False,
                    'error': f"Folder already exists: {folder_path}",
                    'folder_path': str(folder_path)
                }
            
            # Create folder
            folder_path.mkdir(parents=True, exist_ok=True)
            
            # Copy attachments
            copied_files = []
            for attachment in email_data.get('attachments', []):
                try:
                    filename = attachment['filename']
                    file_path = folder_path / filename
                    
                    # Write attachment data
                    with open(file_path, 'wb') as f:
                        f.write(attachment['data'])
                    
                    copied_files.append(filename)
                
                except Exception as e:
                    print(f"Warning: Failed to copy attachment '{attachment.get('filename')}': {e}")
            
            # Create metadata file
            metadata = {
                'created_at': datetime.now().isoformat(),
                'project_code': project_code,
                'email_subject': email_data.get('subject', ''),
                'email_sender': email_data.get('sender', ''),
                'email_date': email_data.get('date', ''),
                'attachments_copied': copied_files,
                'agent_version': '0.1.0'
            }
            
            metadata_path = folder_path / '_bob_metadata.json'
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            return {
                'success': True,
                'folder_path': str(folder_path),
                'files_copied': len(copied_files),
                'metadata': metadata
            }
        
        except PermissionError as e:
            return {
                'success': False,
                'error': f"Permission denied: {e}"
            }
        
        except Exception as e:
            return {
                'success': False,
                'error': f"Unexpected error: {e}"
            }
    
    def folder_exists(self, project_code: str) -> bool:
        """
        Check if project folder exists
        
        Args:
            project_code: Project code
        
        Returns:
            True if exists, False otherwise
        """
        folder_path = self.base_path / project_code
        return folder_path.exists()
    
    def get_folder_path(self, project_code: str) -> Path:
        """
        Get full path for project folder
        
        Args:
            project_code: Project code
        
        Returns:
            Path object
        """
        return self.base_path / project_code
    
    def validate_network_path(self) -> bool:
        """
        Validate network path is accessible
        
        Returns:
            True if accessible, False otherwise
        """
        try:
            return self.base_path.exists() and os.access(self.base_path, os.W_OK)
        except:
            return False

