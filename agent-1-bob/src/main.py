"""
PMinions Agent #1: Bob - Project Booking & Initiation
Main entry point for the agent
"""

import sys
import os
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config.config_manager import ConfigManager
from config.wizard import ConfigWizard
from ui.main_window import MainWindow
from utils.logger import setup_logger

# Version
__version__ = "0.1.0"
__agent_name__ = "Bob"

def main():
    """Main entry point for Bob agent"""
    
    # Setup logging
    logger = setup_logger("bob")
    logger.info(f"🤖 Starting {__agent_name__} v{__version__}")
    
    # Initialize configuration
    config_manager = ConfigManager()
    
    # Check if first run (no config file)
    if not config_manager.config_exists():
        logger.info("First run detected - launching configuration wizard")
        wizard = ConfigWizard()
        
        if not wizard.run():
            logger.error("Configuration wizard cancelled or failed")
            sys.exit(1)
        
        # Reload config after wizard
        config_manager.load()
    else:
        # Load existing configuration
        config_manager.load()
        logger.info("Configuration loaded successfully")
    
    # Validate configuration
    if not config_manager.validate():
        logger.error("Configuration validation failed")
        logger.info("Please run configuration wizard again")
        
        wizard = ConfigWizard()
        if not wizard.run():
            sys.exit(1)
        
        config_manager.load()
    
    # Launch main GUI
    logger.info("Launching main window...")
    try:
        app = MainWindow(config_manager)
        app.run()
    except KeyboardInterrupt:
        logger.info("Agent stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)
    
    logger.info(f"👋 {__agent_name__} shutting down")

if __name__ == "__main__":
    main()

