"""
Test Configuration and Utilities
================================
"""

import sys
import os

# Add src directory to Python path for testing
src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.insert(0, src_path)

# Test data paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'model')

# Model path
MODEL_PATH = os.path.join(MODEL_DIR, "plant_disease_classifier.pth")

def get_test_config():
    """Return test configuration"""
    return {
        "data_dir": DATA_DIR,
        "model_dir": MODEL_DIR,
        "model_path": MODEL_PATH
    }
