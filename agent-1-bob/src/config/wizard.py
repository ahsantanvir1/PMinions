"""
Configuration Wizard for first-time setup
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from .config_manager import ConfigManager

class ConfigWizard:
    """Interactive configuration wizard"""
    
    def __init__(self):
        self.config_manager = ConfigManager()
        self.config_manager.load()
        self.root = None
        self.completed = False
    
    def run(self) -> bool:
        """
        Run the configuration wizard
        
        Returns:
            True if configuration completed, False if cancelled
        """
        self.root = tk.Tk()
        self.root.title("🤖 Bob - First Time Setup")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"600x500+{x}+{y}")
        
        self._create_ui()
        
        self.root.mainloop()
        
        return self.completed
    
    def _create_ui(self):
        """Create wizard UI"""
        
        # Header
        header_frame = tk.Frame(self.root, bg="#3B82F6", height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🤖 Welcome to Bob!",
            font=("Arial", 20, "bold"),
            bg="#3B82F6",
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Main content
        content_frame = tk.Frame(self.root, padx=30, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Instructions
        instructions = tk.Label(
            content_frame,
            text="Let's set up Bob to automate your project booking tasks.\nPlease provide the following information:",
            font=("Arial", 10),
            justify=tk.LEFT,
            wraplength=500
        )
        instructions.pack(anchor=tk.W, pady=(0, 20))
        
        # OpenAI API Key
        tk.Label(content_frame, text="OpenAI API Key:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        self.api_key_entry = tk.Entry(content_frame, width=60, show="*")
        self.api_key_entry.pack(anchor=tk.W, pady=(5, 15))
        
        # Network Folder Path
        tk.Label(content_frame, text="Network Folder Path:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        path_frame = tk.Frame(content_frame)
        path_frame.pack(anchor=tk.W, pady=(5, 15), fill=tk.X)
        
        self.folder_path_entry = tk.Entry(path_frame, width=50)
        self.folder_path_entry.pack(side=tk.LEFT)
        
        browse_btn = tk.Button(
            path_frame,
            text="Browse...",
            command=self._browse_folder
        )
        browse_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Email (optional)
        tk.Label(content_frame, text="Your Email (optional):", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        self.email_entry = tk.Entry(content_frame, width=60)
        self.email_entry.pack(anchor=tk.W, pady=(5, 15))
        
        # Buttons
        button_frame = tk.Frame(self.root, pady=20)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        cancel_btn = tk.Button(
            button_frame,
            text="Cancel",
            command=self._cancel,
            width=15
        )
        cancel_btn.pack(side=tk.RIGHT, padx=(5, 30))
        
        save_btn = tk.Button(
            button_frame,
            text="Save & Continue",
            command=self._save_config,
            width=15,
            bg="#3B82F6",
            fg="white",
            font=("Arial", 10, "bold")
        )
        save_btn.pack(side=tk.RIGHT, padx=(5, 5))
    
    def _browse_folder(self):
        """Open folder browser dialog"""
        folder = filedialog.askdirectory(
            title="Select Network Folder Path",
            initialdir=Path.home()
        )
        
        if folder:
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(0, folder)
    
    def _save_config(self):
        """Save configuration and close wizard"""
        
        # Get values
        api_key = self.api_key_entry.get().strip()
        folder_path = self.folder_path_entry.get().strip()
        email = self.email_entry.get().strip()
        
        # Validate
        if not api_key:
            messagebox.showerror("Error", "OpenAI API Key is required!")
            return
        
        if not folder_path:
            messagebox.showerror("Error", "Network Folder Path is required!")
            return
        
        # Check if path exists
        if not Path(folder_path).exists():
            result = messagebox.askyesno(
                "Warning",
                f"The path '{folder_path}' does not exist.\nDo you want to continue anyway?"
            )
            if not result:
                return
        
        # Save to config
        self.config_manager.set("openai.api_key", api_key)
        self.config_manager.set("network.proposal_folder_path", folder_path)
        
        if email:
            self.config_manager.set("user.email", email)
        
        # Save to file
        if self.config_manager.save():
            messagebox.showinfo("Success", "Configuration saved successfully!\n\nBob is ready to help you! 🎉")
            self.completed = True
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Failed to save configuration. Please try again.")
    
    def _cancel(self):
        """Cancel wizard"""
        result = messagebox.askyesno(
            "Cancel Setup",
            "Are you sure you want to cancel? Bob won't work without configuration."
        )
        
        if result:
            self.completed = False
            self.root.destroy()

