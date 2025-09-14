#!/usr/bin/env python3
"""
Flask Web Application for Plant Disease Detection
=================================================
A complete web interface for uploading plant images and getting disease analysis
with treatment recommendations, weather analysis, and Wikipedia information.
"""

from flask import Flask, request, render_template, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import json
import uuid
from datetime import datetime
import torch
import torchvision.models as models
from PIL import Image
from torchvision import transforms
import sys

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.plant_care_system import PlantCareRecommendationSystem
from src.disease_analyzer import SimpleEnhancedPlantCare

app = Flask(__name__)
app.secret_key = 'plant_disease_secret_key_2025'  # Change in production

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global variables for model and systems
model = None
class_names = None
care_system = None
enhanced_system = None

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_model_and_systems():
    """Load the disease detection model and care systems"""
    global model, class_names, care_system, enhanced_system
    
    try:
        # Load model
        model_path = os.path.join("model", "plant_disease_classifier.pth")
        checkpoint = torch.load(model_path, map_location="cpu")
        
        # Get class names and create model
        class_names = checkpoint['class_names']
        num_classes = len(class_names)
        
        # Create model architecture
        model = models.resnet50(pretrained=False)
        model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
        
        # Load weights
        if 'model_state_dict' in checkpoint:
            model.load_state_dict(checkpoint['model_state_dict'])
        else:
            model = checkpoint['model']
        
        model.eval()
        
        # Load care systems
        care_system = PlantCareRecommendationSystem()
        enhanced_system = SimpleEnhancedPlantCare()
        
        print("✅ Model and systems loaded successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error loading model: {str(e)}")
        return False

def preprocess_image(image_path):
    """Preprocess image for model prediction"""
    try:
        # Define transforms (same as training)
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                               std=[0.229, 0.224, 0.225])
        ])
        
        # Load and transform image
        image = Image.open(image_path).convert('RGB')
        image_tensor = transform(image).unsqueeze(0)
        
        return image_tensor
        
    except Exception as e:
        print(f"❌ Error preprocessing image: {str(e)}")
        return None

def predict_disease(image_path):
    """Predict disease from image"""
    global model, class_names
    
    try:
        # Preprocess image
        image_tensor = preprocess_image(image_path)
        if image_tensor is None:
            return None, 0.0
        
        # Make prediction
        with torch.no_grad():
            outputs = model(image_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            confidence, predicted_idx = torch.max(probabilities, 0)
            
            predicted_class = class_names[predicted_idx.item()]
            confidence_score = confidence.item()
            
            return predicted_class, confidence_score
            
    except Exception as e:
        print(f"❌ Error predicting disease: {str(e)}")
        return None, 0.0

@app.route('/')
def index():
    """Main page with upload form"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and disease analysis"""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['file']
    location = request.form.get('location', 'Unknown')
    
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Save uploaded file
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        # Also save to static/uploads for web display
        static_filepath = os.path.join('static', 'uploads', unique_filename)
        file.save(filepath)
        
        # Copy to static directory for web display
        import shutil
        shutil.copy2(filepath, static_filepath)
        
        # Predict disease
        predicted_class, confidence = predict_disease(filepath)
        
        if predicted_class is None:
            flash('Error analyzing image. Please try again.')
            return redirect(url_for('index'))
        
        # Get enhanced analysis
        try:
            enhanced_analysis = enhanced_system.get_complete_enhanced_diagnosis(
                predicted_class, confidence, location
            )
        except Exception as e:
            print(f"Enhanced analysis error: {e}")
            enhanced_analysis = {"error": str(e)}
        
        # Create result data
        result_data = {
            'filename': unique_filename,
            'original_filename': filename,
            'predicted_class': predicted_class,
            'confidence': confidence,
            'location': location,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'enhanced_analysis': enhanced_analysis
        }
        
        # Save result to JSON file for persistence
        result_id = str(uuid.uuid4())
        result_file = os.path.join('results', f'{result_id}.json')
        os.makedirs('results', exist_ok=True)
        
        with open(result_file, 'w') as f:
            json.dump(result_data, f, indent=2)
        
        return render_template('results.html', 
                             result=result_data, 
                             result_id=result_id)
    
    flash('Invalid file type. Please upload PNG, JPG, JPEG, or GIF files.')
    return redirect(url_for('index'))

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """API endpoint for disease analysis"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        location = request.form.get('location', 'Unknown')
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'}), 400
        
        # Save temporary file
        filename = secure_filename(file.filename)
        temp_filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"temp_{uuid.uuid4()}_{filename}")
        file.save(temp_filepath)
        
        try:
            # Predict disease
            predicted_class, confidence = predict_disease(temp_filepath)
            
            if predicted_class is None:
                return jsonify({'error': 'Error analyzing image'}), 500
            
            # Get enhanced analysis
            enhanced_analysis = enhanced_system.get_complete_enhanced_diagnosis(
                predicted_class, confidence, location
            )
            
            result = {
                'predicted_class': predicted_class,
                'confidence': confidence,
                'location': location,
                'timestamp': datetime.now().isoformat(),
                'enhanced_analysis': enhanced_analysis
            }
            
            return jsonify(result)
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)
                
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/results/<result_id>')
def view_result(result_id):
    """View saved result by ID"""
    try:
        result_file = os.path.join('results', f'{result_id}.json')
        
        if not os.path.exists(result_file):
            flash('Result not found')
            return redirect(url_for('index'))
        
        with open(result_file, 'r') as f:
            result_data = json.load(f)
        
        return render_template('results.html', 
                             result=result_data, 
                             result_id=result_id)
        
    except Exception as e:
        flash(f'Error loading result: {str(e)}')
        return redirect(url_for('index'))

@app.route('/history')
def history():
    """View analysis history"""
    try:
        results_dir = 'results'
        if not os.path.exists(results_dir):
            return render_template('history.html', results=[])
        
        results = []
        for filename in os.listdir(results_dir):
            if filename.endswith('.json'):
                try:
                    with open(os.path.join(results_dir, filename), 'r') as f:
                        data = json.load(f)
                        data['result_id'] = filename[:-5]  # Remove .json extension
                        results.append(data)
                except:
                    continue
        
        # Sort by timestamp (newest first)
        results.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        
        return render_template('history.html', results=results)
        
    except Exception as e:
        flash(f'Error loading history: {str(e)}')
        return render_template('history.html', results=[])

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    print("🌱 PLANT DISEASE DETECTION WEB APPLICATION")
    print("="*50)
    
    # Load model and systems
    if load_model_and_systems():
        print("🚀 Starting Flask application...")
        print("📱 Access the web interface at: http://localhost:5000")
        print("🔌 API endpoint available at: http://localhost:5000/api/analyze")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("❌ Failed to load model. Please check your model file.")
