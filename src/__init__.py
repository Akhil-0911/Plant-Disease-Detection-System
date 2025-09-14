"""
Plant Disease Detection & Treatment System
==========================================
Main package initialization file
"""

__version__ = "1.0.0"
__author__ = "Plant Disease Detection Team"
__description__ = "AI-powered agricultural system for disease detection and treatment recommendations"

# Import main classes for easy access
try:
    from .plant_care_system import PlantCareRecommendationSystem
    from .disease_analyzer import SimpleEnhancedPlantCare
    
    __all__ = [
        'PlantCareRecommendationSystem',
        'SimpleEnhancedPlantCare'
    ]
except ImportError:
    # Handle case where dependencies aren't installed
    __all__ = []

# Package metadata
SUPPORTED_PLANT_TYPES = [
    "Apple", "Blueberry", "Cherry", "Corn", "Grape", "Orange", 
    "Peach", "Pepper", "Potato", "Raspberry", "Soybean", 
    "Squash", "Strawberry", "Tomato"
]

DISEASE_CLASSES = 38
MODEL_ACCURACY = 0.9966

def get_version():
    """Return the current version of the package"""
    return __version__

def get_info():
    """Return package information"""
    return {
        "name": "Plant Disease Detection System",
        "version": __version__,
        "description": __description__,
        "supported_plants": len(SUPPORTED_PLANT_TYPES),
        "disease_classes": DISEASE_CLASSES,
        "model_accuracy": f"{MODEL_ACCURACY:.2%}"
    }
