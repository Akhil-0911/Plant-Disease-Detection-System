"""
Plant Disease Treatment and Fertilizer Recommendation System
This system uses your trained disease classification model and provides
specific fertilizer and manure recommendations based on plant type and disease.
"""

import json

class PlantCareRecommendationSystem:
    def __init__(self):
        self.recommendations = self._build_recommendation_database()
    
    def _build_recommendation_database(self):
        """
        Comprehensive database of fertilizer and manure recommendations
        for each plant type and disease condition.
        """
        recommendations = {
            # APPLE RECOMMENDATIONS
            "Apple___Apple_scab": {
                "disease_info": "Fungal disease causing dark spots on leaves and fruit",
                "immediate_treatment": [
                    "Remove infected leaves and fruit immediately",
                    "Apply copper-based fungicide spray",
                    "Improve air circulation around tree"
                ],
                "fertilizer_recommendations": [
                    "Balanced NPK fertilizer (10-10-10) in early spring",
                    "Potassium sulfate to boost disease resistance",
                    "Calcium supplement to strengthen cell walls"
                ],
                "organic_manure": [
                    "Well-composted cow manure (2-3 inches around tree base)",
                    "Bone meal for phosphorus",
                    "Wood ash for potassium (small amounts)"
                ],
                "soil_amendments": [
                    "Ensure good drainage",
                    "Maintain soil pH 6.0-7.0",
                    "Add organic compost to improve soil health"
                ],
                "prevention": [
                    "Plant disease-resistant apple varieties",
                    "Prune for good air circulation",
                    "Fall cleanup of fallen leaves"
                ]
            },
            
            "Apple___Black_rot": {
                "disease_info": "Fungal disease causing fruit rot and cankers",
                "immediate_treatment": [
                    "Remove all infected fruit and wood",
                    "Apply copper fungicide during dormant season",
                    "Prune out cankers below infection point"
                ],
                "fertilizer_recommendations": [
                    "Balanced fertilizer (12-12-12) in spring",
                    "Avoid high nitrogen in late season",
                    "Magnesium sulfate if leaves show yellowing"
                ],
                "organic_manure": [
                    "Aged horse manure",
                    "Compost tea applications",
                    "Fish emulsion for nitrogen"
                ],
                "soil_amendments": [
                    "Improve soil drainage",
                    "Add perlite if soil is heavy clay",
                    "Maintain soil pH 6.5-7.0"
                ],
                "prevention": [
                    "Choose resistant rootstocks",
                    "Avoid overhead watering",
                    "Regular pruning for air flow"
                ]
            },
            
            "Apple___Cedar_apple_rust": {
                "disease_info": "Fungal disease alternating between apple and cedar trees",
                "immediate_treatment": [
                    "Apply preventive fungicide in early spring",
                    "Remove nearby cedar trees if possible",
                    "Use systemic fungicides for severe cases"
                ],
                "fertilizer_recommendations": [
                    "Low nitrogen fertilizer to reduce susceptibility",
                    "Phosphorus and potassium emphasis",
                    "Zinc and iron supplements"
                ],
                "organic_manure": [
                    "Well-aged chicken manure (low nitrogen)",
                    "Kelp meal for trace minerals",
                    "Rock phosphate for phosphorus"
                ],
                "soil_amendments": [
                    "Ensure excellent drainage",
                    "Add sand to heavy soils",
                    "Maintain slightly acidic soil (pH 6.0-6.5)"
                ],
                "prevention": [
                    "Plant resistant apple varieties",
                    "Remove alternate hosts (cedar trees)",
                    "Spring fungicide applications"
                ]
            },
            
            "Apple___healthy": {
                "disease_info": "Healthy apple tree - maintain optimal nutrition",
                "immediate_treatment": [
                    "Continue regular maintenance",
                    "Monitor for early disease signs",
                    "Maintain proper pruning schedule"
                ],
                "fertilizer_recommendations": [
                    "Balanced NPK (10-10-10) in early spring",
                    "Calcium for strong fruit development",
                    "Boron for good fruit set"
                ],
                "organic_manure": [
                    "Composted cow manure annually",
                    "Bone meal in spring",
                    "Kelp meal for micronutrients"
                ],
                "soil_amendments": [
                    "Maintain soil pH 6.0-7.0",
                    "Add compost annually",
                    "Mulch around base with organic matter"
                ],
                "prevention": [
                    "Regular soil testing",
                    "Proper pruning and spacing",
                    "Integrated pest management"
                ]
            },
            
            # TOMATO RECOMMENDATIONS
            "Tomato___Bacterial_spot": {
                "disease_info": "Bacterial infection causing leaf spots and fruit lesions",
                "immediate_treatment": [
                    "Remove infected plant parts immediately",
                    "Apply copper-based bactericide",
                    "Improve air circulation",
                    "Avoid overhead watering"
                ],
                "fertilizer_recommendations": [
                    "Reduce nitrogen to slow bacterial growth",
                    "Increase potassium for disease resistance",
                    "Calcium to strengthen cell walls",
                    "Use 5-10-15 NPK ratio"
                ],
                "organic_manure": [
                    "Well-composted manure only (avoid fresh)",
                    "Worm castings for gentle nutrition",
                    "Fish bone meal for phosphorus"
                ],
                "soil_amendments": [
                    "Improve drainage immediately",
                    "Add perlite to heavy soils",
                    "Maintain soil pH 6.2-6.8",
                    "Avoid waterlogged conditions"
                ],
                "prevention": [
                    "Use disease-resistant varieties",
                    "Drip irrigation instead of sprinklers",
                    "Crop rotation with non-solanaceous plants",
                    "Sterilize tools between plants"
                ]
            },
            
            "Tomato___Early_blight": {
                "disease_info": "Fungal disease causing dark spots with concentric rings",
                "immediate_treatment": [
                    "Remove affected lower leaves",
                    "Apply fungicide containing chlorothalonil",
                    "Improve plant spacing",
                    "Mulch to prevent soil splash"
                ],
                "fertilizer_recommendations": [
                    "Balanced NPK (8-8-8) with emphasis on potassium",
                    "Avoid excess nitrogen which promotes disease",
                    "Calcium and magnesium supplements",
                    "Phosphorus for root strength"
                ],
                "organic_manure": [
                    "Aged cow manure",
                    "Compost with good C:N ratio",
                    "Bone meal for phosphorus",
                    "Greensand for potassium"
                ],
                "soil_amendments": [
                    "Ensure good drainage",
                    "Add organic matter to improve soil structure",
                    "Maintain soil pH 6.0-6.8",
                    "Apply mulch to reduce soil splash"
                ],
                "prevention": [
                    "Stake and prune for air circulation",
                    "Water at soil level, not leaves",
                    "Rotate crops annually",
                    "Choose resistant varieties"
                ]
            },
            
            "Tomato___Late_blight": {
                "disease_info": "Devastating fungal disease, same pathogen as Irish potato famine",
                "immediate_treatment": [
                    "URGENT: Remove entire infected plants",
                    "Apply systemic fungicide immediately",
                    "Increase air circulation dramatically",
                    "Reduce humidity around plants"
                ],
                "fertilizer_recommendations": [
                    "Stop nitrogen fertilization immediately",
                    "High potassium fertilizer for disease resistance",
                    "Calcium chloride foliar spray",
                    "Phosphorus for root health"
                ],
                "organic_manure": [
                    "No fresh manure - use only well-aged compost",
                    "Worm castings for gentle feeding",
                    "Rock phosphate",
                    "Granite dust for potassium"
                ],
                "soil_amendments": [
                    "Improve drainage urgently",
                    "Add sand/perlite to heavy soils",
                    "Ensure soil pH 6.5-7.0",
                    "Remove all plant debris"
                ],
                "prevention": [
                    "Plant only certified disease-free seeds",
                    "Use resistant varieties",
                    "Avoid overhead irrigation",
                    "Monitor weather for favorable disease conditions"
                ]
            },
            
            "Tomato___Leaf_Mold": {
                "disease_info": "Fungal disease common in greenhouse conditions",
                "immediate_treatment": [
                    "Increase ventilation immediately",
                    "Reduce humidity below 85%",
                    "Remove infected leaves",
                    "Apply fungicide spray"
                ],
                "fertilizer_recommendations": [
                    "Reduce nitrogen levels",
                    "Increase potassium and calcium",
                    "Use 4-8-12 NPK ratio",
                    "Magnesium sulfate foliar spray"
                ],
                "organic_manure": [
                    "Well-composted manure with good drainage",
                    "Avoid high-nitrogen sources",
                    "Kelp meal for potassium",
                    "Bone meal for phosphorus"
                ],
                "soil_amendments": [
                    "Improve air circulation at soil level",
                    "Add perlite for drainage",
                    "Maintain soil pH 6.0-6.8",
                    "Use raised beds if possible"
                ],
                "prevention": [
                    "Ensure excellent ventilation",
                    "Control humidity levels",
                    "Space plants adequately",
                    "Use resistant varieties in greenhouses"
                ]
            },
            
            "Tomato___healthy": {
                "disease_info": "Healthy tomato plant - maintain optimal growing conditions",
                "immediate_treatment": [
                    "Continue regular monitoring",
                    "Maintain consistent watering",
                    "Regular pruning of suckers"
                ],
                "fertilizer_recommendations": [
                    "Balanced NPK (10-10-10) for vegetative growth",
                    "Switch to high potassium (5-10-15) when fruiting",
                    "Calcium supplement for blossom end rot prevention",
                    "Magnesium for chlorophyll production"
                ],
                "organic_manure": [
                    "Compost-enriched cow manure",
                    "Worm castings throughout season",
                    "Fish emulsion for quick nitrogen",
                    "Bone meal at planting"
                ],
                "soil_amendments": [
                    "Maintain soil pH 6.0-6.8",
                    "Add compost regularly",
                    "Mulch with organic matter",
                    "Ensure consistent moisture"
                ],
                "prevention": [
                    "Regular soil testing",
                    "Proper plant spacing",
                    "Consistent watering schedule",
                    "Integrated pest management"
                ]
            }
        }
        
        # Add more plant types (this is a starting template)
        # You can expand this database with all 38 classes
        return recommendations
    
    def get_recommendations(self, predicted_class, confidence_score=None):
        """
        Get treatment recommendations for a predicted plant disease class
        
        Args:
            predicted_class (str): The class predicted by your model
            confidence_score (float): Model confidence (optional)
            
        Returns:
            dict: Complete recommendation package
        """
        if predicted_class not in self.recommendations:
            return self._get_generic_recommendations(predicted_class)
        
        recommendations = self.recommendations[predicted_class].copy()
        
        # Add confidence information
        if confidence_score:
            recommendations['model_confidence'] = f"{confidence_score:.2%}"
            if confidence_score < 0.7:
                recommendations['confidence_warning'] = "Low confidence - consider manual verification"
        
        # Add general care tips
        recommendations['general_care'] = self._get_general_care_tips(predicted_class)
        
        return recommendations
    
    def _get_generic_recommendations(self, predicted_class):
        """
        Provide generic recommendations for classes not in detailed database
        """
        plant_type = predicted_class.split('___')[0] if '___' in predicted_class else predicted_class
        is_healthy = 'healthy' in predicted_class.lower()
        
        if is_healthy:
            return {
                "disease_info": f"Healthy {plant_type} - maintain current care",
                "immediate_treatment": ["Continue current care routine", "Monitor regularly"],
                "fertilizer_recommendations": ["Balanced NPK fertilizer", "Seasonal adjustments as needed"],
                "organic_manure": ["Well-composted organic matter", "Seasonal compost applications"],
                "soil_amendments": ["Maintain proper pH", "Regular soil testing"],
                "prevention": ["Continue good practices", "Regular monitoring"]
            }
        else:
            return {
                "disease_info": f"Disease detected in {plant_type} - general treatment needed",
                "immediate_treatment": ["Remove infected plant parts", "Improve air circulation", "Apply appropriate fungicide/bactericide"],
                "fertilizer_recommendations": ["Reduce nitrogen", "Increase potassium for disease resistance", "Ensure adequate calcium"],
                "organic_manure": ["Well-aged compost only", "Avoid fresh manure during disease"],
                "soil_amendments": ["Improve drainage", "Maintain optimal pH", "Add organic matter"],
                "prevention": ["Use resistant varieties", "Improve growing conditions", "Regular monitoring"]
            }
    
    def _get_general_care_tips(self, predicted_class):
        """
        Get general care tips based on plant type
        """
        plant_type = predicted_class.split('___')[0] if '___' in predicted_class else predicted_class
        
        care_tips = {
            "Apple": {
                "watering": "Deep, infrequent watering - avoid wetting leaves",
                "pruning": "Prune in late winter for air circulation",
                "harvest": "Harvest when fruit comes off easily with upward twist"
            },
            "Tomato": {
                "watering": "Consistent moisture - 1-2 inches per week",
                "pruning": "Remove suckers, lower leaves touching ground",
                "harvest": "Pick when fully colored but still firm"
            },
            "Potato": {
                "watering": "Consistent moisture, especially during tuber formation",
                "hilling": "Hill soil around plants as they grow",
                "harvest": "Harvest after plant dies back naturally"
            }
        }
        
        return care_tips.get(plant_type, {
            "watering": "Maintain consistent moisture levels",
            "care": "Follow best practices for this plant type",
            "monitoring": "Regular inspection for pests and diseases"
        })
    
    def generate_care_schedule(self, predicted_class, season="spring"):
        """
        Generate a seasonal care schedule
        """
        recommendations = self.get_recommendations(predicted_class)
        
        schedule = {
            "immediate_actions": recommendations.get('immediate_treatment', []),
            "weekly_tasks": [
                "Monitor plant health",
                "Check soil moisture",
                "Apply organic fertilizer if scheduled"
            ],
            "monthly_tasks": [
                "Soil pH testing",
                "Apply compost or manure as recommended",
                "Disease prevention treatments"
            ],
            "seasonal_tasks": self._get_seasonal_tasks(predicted_class, season)
        }
        
        return schedule
    
    def _get_seasonal_tasks(self, predicted_class, season):
        """
        Get season-specific tasks
        """
        plant_type = predicted_class.split('___')[0] if '___' in predicted_class else predicted_class
        
        seasonal_tasks = {
            "spring": ["Apply base fertilizer", "Begin regular watering", "Start disease monitoring"],
            "summer": ["Increase watering frequency", "Apply potassium fertilizer", "Harvest as ready"],
            "fall": ["Reduce watering", "Apply phosphorus fertilizer", "Prepare for dormancy"],
            "winter": ["Minimal watering", "Plan for next season", "Equipment maintenance"]
        }
        
        return seasonal_tasks.get(season, seasonal_tasks["spring"])

# Example usage function
def save_recommendations_database():
    """
    Save the recommendations to a JSON file for easy editing and expansion
    """
    care_system = PlantCareRecommendationSystem()
    
    # Save to JSON for easy editing
    with open('care_recommendations.json', 'w') as f:
        json.dump(care_system.recommendations, f, indent=2)
    
    print("Recommendations database saved to 'care_recommendations.json'")
    print("You can edit this file to add more detailed recommendations for all 38 classes")

if __name__ == "__main__":
    # Example usage
    care_system = PlantCareRecommendationSystem()
    
    # Test with a few classes
    test_classes = [
        "Apple___Apple_scab",
        "Tomato___Early_blight", 
        "Tomato___healthy",
        "Apple___healthy"
    ]
    
    for class_name in test_classes:
        print(f"\n{'='*60}")
        print(f"RECOMMENDATIONS FOR: {class_name}")
        print('='*60)
        
        recommendations = care_system.get_recommendations(class_name, confidence_score=0.95)
        
        for key, value in recommendations.items():
            if key != 'general_care':
                print(f"\n{key.upper().replace('_', ' ')}:")
                if isinstance(value, list):
                    for item in value:
                        print(f"  • {item}")
                else:
                    print(f"  {value}")
    
    # Save database for expansion
    save_recommendations_database()
