#!/usr/bin/env python3
"""
Quick test script for Bob agent
Run this to test if everything is set up correctly
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """Test if all modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        from config.config_manager import ConfigManager
        print("✅ ConfigManager imported")
    except Exception as e:
        print(f"❌ ConfigManager failed: {e}")
        return False
    
    try:
        from core.email_parser import EmailParser
        print("✅ EmailParser imported")
    except Exception as e:
        print(f"❌ EmailParser failed: {e}")
        return False
    
    try:
        from core.code_extractor import CodeExtractor
        print("✅ CodeExtractor imported")
    except Exception as e:
        print(f"❌ CodeExtractor failed: {e}")
        return False
    
    try:
        from core.file_manager import FileManager
        print("✅ FileManager imported")
    except Exception as e:
        print(f"❌ FileManager failed: {e}")
        return False
    
    try:
        from core.ai_handler import AIHandler
        print("✅ AIHandler imported")
    except Exception as e:
        print(f"❌ AIHandler failed: {e}")
        return False
    
    try:
        from utils.logger import setup_logger
        print("✅ Logger imported")
    except Exception as e:
        print(f"❌ Logger failed: {e}")
        return False
    
    return True

def test_code_extraction():
    """Test code extraction"""
    print("\n🧪 Testing code extraction...")
    
    from config.config_manager import ConfigManager
    from core.code_extractor import CodeExtractor
    
    config = ConfigManager()
    config.load()
    
    extractor = CodeExtractor(config)
    
    test_text = "Please work on project AEMA-12345 and also AEMA-67890"
    codes = extractor.extract_codes(test_text)
    
    if codes == ['AEMA-12345', 'AEMA-67890']:
        print(f"✅ Code extraction works: {codes}")
        return True
    else:
        print(f"❌ Code extraction failed: expected ['AEMA-12345', 'AEMA-67890'], got {codes}")
        return False

def main():
    """Run tests"""
    print("🤖 Bob Agent - Quick Test\n")
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test code extraction
    if not test_code_extraction():
        all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("✅ All tests passed! Bob is ready to go!")
        print("\nTo run Bob:")
        print("  python src/main.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\nMake sure you've installed dependencies:")
        print("  pip install -r requirements.txt")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

