#!/usr/bin/env python3
"""
PCAP Course Setup Verification Script
Run this script to verify your Python environment is properly configured.
"""

import sys
import platform
import os

def print_header():
    """Print a formatted header for the verification script."""
    print("=" * 60)
    print("🐍 PCAP Course Setup Verification")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version meets requirements."""
    print("📋 Python Version Check")
    print("-" * 30)
    
    version = sys.version_info
    print(f"Current Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version meets requirements (3.8+)")
        return True
    else:
        print("❌ Python version too old. Please install Python 3.8 or higher.")
        return False

def check_platform():
    """Display platform information."""
    print("\n💻 Platform Information")
    print("-" * 30)
    
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python Executable: {sys.executable}")
    
    # Check if running in virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Running in virtual environment")
    else:
        print("ℹ️  Running in system Python (consider using a virtual environment)")

def check_basic_imports():
    """Test basic Python imports."""
    print("\n📚 Basic Import Test")
    print("-" * 30)
    
    basic_modules = [
        'os', 'sys', 'math', 'datetime', 'json', 'random'
    ]
    
    failed_imports = []
    
    for module in basic_modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n⚠️  Failed to import: {', '.join(failed_imports)}")
        return False
    else:
        print("\n✅ All basic modules imported successfully")
        return True

def test_basic_operations():
    """Test basic Python operations."""
    print("\n🧮 Basic Operations Test")
    print("-" * 30)
    
    try:
        # Arithmetic
        result = 2 + 2
        print(f"✅ Basic arithmetic: 2 + 2 = {result}")
        
        # String operations
        text = "Hello, Python!"
        print(f"✅ String operations: {text}")
        
        # List operations
        numbers = [1, 2, 3, 4, 5]
        print(f"✅ List operations: {numbers}")
        
        # Dictionary operations
        data = {"name": "Student", "course": "PCAP"}
        print(f"✅ Dictionary operations: {data}")
        
        print("\n✅ All basic operations working correctly")
        return True
        
    except Exception as e:
        print(f"❌ Error in basic operations: {e}")
        return False

def test_file_operations():
    """Test basic file operations."""
    print("\n📁 File Operations Test")
    print("-" * 30)
    
    test_file = "test_setup.txt"
    
    try:
        # Write to file
        with open(test_file, 'w') as f:
            f.write("PCAP Course Setup Test\n")
            f.write("If you can see this file, file operations are working!\n")
        print("✅ File write operation successful")
        
        # Read from file
        with open(test_file, 'r') as f:
            content = f.read()
        print("✅ File read operation successful")
        
        # Clean up
        os.remove(test_file)
        print("✅ File cleanup successful")
        
        print("\n✅ All file operations working correctly")
        return True
        
    except Exception as e:
        print(f"❌ Error in file operations: {e}")
        # Try to clean up if file was created
        if os.path.exists(test_file):
            try:
                os.remove(test_file)
            except:
                pass
        return False

def check_ide_recommendations():
    """Provide IDE recommendations."""
    print("\n🛠️  IDE Recommendations")
    print("-" * 30)
    
    print("For the best learning experience, consider using:")
    print("1. VS Code (Free) - Excellent for beginners")
    print("2. PyCharm Community (Free) - Full-featured IDE")
    print("3. IDLE (Built-in) - Simple but functional")
    
    print("\nMake sure to install the Python extension for your chosen IDE!")

def print_next_steps():
    """Print next steps for the student."""
    print("\n🎯 Next Steps")
    print("-" * 30)
    
    print("1. ✅ Complete this setup verification")
    print("2. 📚 Review the course introduction materials")
    print("3. 🚀 Move to Module 1: Python Fundamentals")
    print("4. 💻 Start coding your first Python programs")
    print("5. 📝 Complete the module exercises")
    
    print("\n" + "=" * 60)
    print("🎉 Setup verification complete! You're ready to learn Python!")
    print("=" * 60)

def main():
    """Main verification function."""
    print_header()
    
    # Run all checks
    version_ok = check_python_version()
    check_platform()
    imports_ok = check_basic_imports()
    operations_ok = test_basic_operations()
    files_ok = test_file_operations()
    
    # Summary
    print("\n📊 Setup Summary")
    print("-" * 30)
    
    checks = [
        ("Python Version", version_ok),
        ("Basic Imports", imports_ok),
        ("Basic Operations", operations_ok),
        ("File Operations", files_ok)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, status in checks:
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {check_name}")
        if status:
            passed += 1
    
    print(f"\nResults: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 All checks passed! Your setup is ready for the PCAP course!")
    else:
        print("⚠️  Some checks failed. Please review the errors above.")
        print("Contact support if you need help resolving these issues.")
    
    check_ide_recommendations()
    print_next_steps()

if __name__ == "__main__":
    main()
