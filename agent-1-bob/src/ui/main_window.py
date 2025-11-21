"""
Main GUI window for Bob agent
Drag-and-drop interface for email files
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinterdnd2 import DND_FILES, TkinterDnD
from pathlib import Path
import threading
from typing import Optional

class MainWindow:
    """Main application window with drag-and-drop"""
    
    def __init__(self, config_manager):
        """
        Initialize main window
        
        Args:
            config_manager: ConfigManager instance
        """
        self.config_manager = config_manager
        self.root = None
        self.processing = False
    
    def run(self):
        """Start the application"""
        try:
            self.root = TkinterDnD.Tk()
        except:
            # Fallback if tkinterdnd2 not available
            self.root = tk.Tk()
            messagebox.showwarning(
                "Limited Functionality",
                "Drag-and-drop not available. Please install tkinterdnd2.\nYou can still use file selection."
            )
        
        self.root.title("🤖 Bob - Project Booking Agent")
        self.root.geometry("700x600")
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (700 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"700x600+{x}+{y}")
        
        self._create_ui()
        
        self.root.mainloop()
    
    def _create_ui(self):
        """Create main UI"""
        
        # Header
        header_frame = tk.Frame(self.root, bg="#3B82F6", height=100)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🤖 Bob - Project Booking Agent",
            font=("Arial", 18, "bold"),
            bg="#3B82F6",
            fg="white"
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Drag and drop email files (.msg or .eml) here",
            font=("Arial", 10),
            bg="#3B82F6",
            fg="white"
        )
        subtitle_label.pack()
        
        # Main content
        content_frame = tk.Frame(self.root, padx=20, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Drop zone
        self.drop_zone = tk.Frame(
            content_frame,
            bg="#EFF6FF",
            relief=tk.RIDGE,
            borderwidth=2
        )
        self.drop_zone.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Try to enable drag-and-drop
        try:
            self.drop_zone.drop_target_register(DND_FILES)
            self.drop_zone.dnd_bind('<<Drop>>', self._on_drop)
        except:
            pass  # Drag-and-drop not available
        
        drop_label = tk.Label(
            self.drop_zone,
            text="📧\n\nDrag email file here\n\nor click Browse to select",
            font=("Arial", 14),
            bg="#EFF6FF",
            fg="#3B82F6",
            justify=tk.CENTER
        )
        drop_label.pack(expand=True)
        
        # Browse button
        browse_btn = tk.Button(
            content_frame,
            text="📁 Browse for Email File",
            command=self._browse_file,
            font=("Arial", 11),
            bg="#3B82F6",
            fg="white",
            padx=20,
            pady=10
        )
        browse_btn.pack(pady=(0, 10))
        
        # Status area
        status_frame = tk.LabelFrame(
            content_frame,
            text="Status",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=10
        )
        status_frame.pack(fill=tk.BOTH, expand=True)
        
        self.status_text = scrolledtext.ScrolledText(
            status_frame,
            height=10,
            font=("Courier", 9),
            state=tk.DISABLED,
            bg="#F9FAFB"
        )
        self.status_text.pack(fill=tk.BOTH, expand=True)
        
        # Initial status
        self._log_status("✅ Bob is ready! Waiting for email files...")
        self._log_status(f"📁 Network folder: {self.config_manager.get('network.proposal_folder_path')}")
    
    def _on_drop(self, event):
        """Handle file drop event"""
        files = self.root.tk.splitlist(event.data)
        
        if files:
            file_path = Path(files[0])
            self._process_email(file_path)
    
    def _browse_file(self):
        """Open file browser"""
        from tkinter import filedialog
        
        file_path = filedialog.askopenfilename(
            title="Select Email File",
            filetypes=[
                ("Email files", "*.msg *.eml"),
                ("Outlook MSG", "*.msg"),
                ("EML files", "*.eml"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self._process_email(Path(file_path))
    
    def _process_email(self, file_path: Path):
        """
        Process email file
        
        Args:
            file_path: Path to email file
        """
        if self.processing:
            messagebox.showwarning("Busy", "Bob is already processing an email. Please wait...")
            return
        
        self._log_status(f"\n📧 Processing: {file_path.name}")
        
        # Validate file
        if not file_path.exists():
            self._log_status("❌ Error: File does not exist")
            messagebox.showerror("Error", "File does not exist!")
            return
        
        if file_path.suffix.lower() not in ['.msg', '.eml']:
            self._log_status("❌ Error: Invalid file type")
            messagebox.showerror("Error", "Please select a .msg or .eml file")
            return
        
        # Process in background thread
        self.processing = True
        thread = threading.Thread(target=self._process_email_thread, args=(file_path,))
        thread.daemon = True
        thread.start()
    
    def _process_email_thread(self, file_path: Path):
        """Process email in background thread"""
        try:
            # Import here to avoid circular imports
            from core.email_parser import EmailParser
            from core.code_extractor import CodeExtractor
            from core.file_manager import FileManager
            from core.ai_handler import AIHandler
            
            # Parse email
            self._log_status("📖 Parsing email...")
            parser = EmailParser()
            email_data = parser.parse(file_path)
            
            if not email_data:
                self._log_status("❌ Failed to parse email")
                return
            
            self._log_status(f"✅ Email parsed: {email_data['subject']}")
            self._log_status(f"   From: {email_data['sender']}")
            self._log_status(f"   Attachments: {len(email_data['attachments'])}")
            
            # Extract AEMA codes
            self._log_status("\n🔍 Searching for project codes...")
            extractor = CodeExtractor(self.config_manager)
            codes = extractor.extract_codes(email_data['body'] + " " + email_data['subject'])
            
            if not codes:
                self._log_status("❌ No project codes found")
                messagebox.showwarning("No Codes Found", "Bob couldn't find any project codes in this email.")
                return
            
            self._log_status(f"✅ Found codes: {', '.join(codes)}")
            
            # Use first code (or let user choose if multiple)
            project_code = codes[0]
            if len(codes) > 1:
                self._log_status(f"⚠️  Multiple codes found, using: {project_code}")
            
            # AI analysis (optional)
            self._log_status("\n🧠 Analyzing with AI...")
            ai_handler = AIHandler(self.config_manager)
            analysis = ai_handler.analyze_email(email_data)
            
            if analysis:
                self._log_status(f"✅ AI Analysis:")
                self._log_status(f"   Is project assignment: {analysis.get('is_project_assignment', 'Unknown')}")
                if analysis.get('client_name'):
                    self._log_status(f"   Client: {analysis.get('client_name')}")
            
            # Create folder
            self._log_status(f"\n📁 Creating project folder: {project_code}")
            file_manager = FileManager(self.config_manager)
            result = file_manager.create_project_folder(project_code, email_data)
            
            if result['success']:
                self._log_status(f"✅ Success! Folder created: {result['folder_path']}")
                self._log_status(f"   Copied {len(email_data['attachments'])} attachments")
                messagebox.showinfo("Success", f"Project folder created successfully!\n\n{result['folder_path']}")
            else:
                self._log_status(f"❌ Error: {result['error']}")
                messagebox.showerror("Error", f"Failed to create folder:\n{result['error']}")
        
        except Exception as e:
            self._log_status(f"❌ Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
        
        finally:
            self.processing = False
            self._log_status("\n✅ Bob is ready for the next email!")
    
    def _log_status(self, message: str):
        """
        Add message to status log
        
        Args:
            message: Status message
        """
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
        self.root.update()

