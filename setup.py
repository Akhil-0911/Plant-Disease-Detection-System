#!/usr/bin/env python3
"""
Project Setup Script
===================
Sets up the plant disease detection system for development and deployment.
"""

import os
import sys
import subprocess
import json

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False
    return True

def verify_project_structure():
    """Verify all necessary files and directories exist"""
    required_dirs = ["src", "tests", "data", "docs", "model"]
    required_files = [
        "requirements.txt",
        "README.md", 
        ".gitignore",
        "src/__init__.py",
        "src/plant_care_system.py",
        "src/disease_analyzer.py",
        "tests/__init__.py",
        "data/care_recommendations.json"
    ]
    
    print("🔍 Verifying project structure...")
    
    # Check directories
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"  ✅ {dir_name}/")
        else:
            print(f"  ❌ {dir_name}/ - MISSING")
            return False
    
    # Check files
    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"  ✅ {file_name}")
        else:
            print(f"  ❌ {file_name} - MISSING")
            return False
    
    print("✅ Project structure verified")
    return True

def test_system():
    """Run basic system tests"""
    print("🧪 Testing system components...")
    
    try:
        # Test imports
        sys.path.insert(0, 'src')
        from plant_care_system import PlantCareRecommendationSystem
        
        # Test basic functionality
        care_system = PlantCareRecommendationSystem()
        test_recs = care_system.get_recommendations("Apple___Apple_scab", 0.95)
        
        if test_recs and "fertilizer_recommendations" in test_recs:
            print("  ✅ Plant care system working")
        else:
            print("  ❌ Plant care system test failed")
            return False
            
    except Exception as e:
        print(f"  ❌ System test failed: {e}")
        return False
    
    print("✅ System tests passed")
    return True

def generate_project_info():
    """Generate project information file"""
    info = {
        "name": "Plant Disease Detection & Treatment System",
        "version": "1.0.0",
        "description": "AI-powered agricultural system for disease detection and treatment recommendations",
        "accuracy": "99.66%",
        "supported_plants": 14,
        "disease_classes": 38,
        "features": [
            "Real-time disease detection",
            "Treatment recommendations", 
            "Weather integration",
            "Organic alternatives",
            "Confidence-based advice"
        ],
        "structure": {
            "src/": "Core system code",
            "tests/": "Test scripts and analysis", 
            "data/": "Training data and results",
            "docs/": "Documentation",
            "model/": "Trained AI model"
        }
    }
    
    with open("project_info.json", "w") as f:
        json.dump(info, f, indent=2)
    
    print("✅ Project info generated: project_info.json")

def main():
    """Main setup function"""
    print("🌱 PLANT DISEASE SYSTEM SETUP")
    print("="*50)
    
    # Check Python version
    check_python_version()
    
    # Verify project structure
    if not verify_project_structure():
        print("❌ Setup failed - project structure incomplete")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed - could not install requirements")
        sys.exit(1)
    
    # Test system
    if not test_system():
        print("❌ Setup failed - system tests failed")
        sys.exit(1)
    
    # Generate project info
    generate_project_info()
    
    print("\n🎉 SETUP COMPLETE!")
    print("="*50)
    print("Your plant disease detection system is ready to use!")
    print("\n📋 Quick Start:")
    print("  1. Test the system: cd tests && python fixed_analysis.py")
    print("  2. Use in code: from src.plant_care_system import PlantCareRecommendationSystem")
    print("  3. Read docs: check docs/ folder for detailed information")
    print("\n🚀 Ready for deployment!")

if __name__ == "__main__":
    main()
