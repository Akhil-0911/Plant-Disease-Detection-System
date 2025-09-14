# 🌱 Plant Disease Detection System

[![GitHub Repository](https://img.shields.io/badge/GitHub-Plant--Disease--Detection--System-blue?logo=github)](https://github.com/Akhil-0911/Plant-Disease-Detection-System)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-green?logo=flask)](https://flask.palletsprojects.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?logo=pytorch)](https://pytorch.org/)

A comprehensive AI-powered web application for detecting plant diseases using deep learning, providing treatment recommendations, weather analysis, and Wikipedia-sourced disease information.

## 🌟 Demo

![Plant Disease Detection Demo](https://img.shields.io/badge/Live%20Demo-Coming%20Soon-yellow?style=for-the-badge)

**🎯 Key Capabilities:**
- Upload plant images and get instant disease detection
- 99.66% accuracy AI classification across 38 plant diseases  
- Real-time weather analysis for disease risk assessment
- Wikipedia-sourced educational content about diseases
- Detailed treatment recommendations and care instructions

## ⚡ Quick Start

```bash
# 1. Navigate to project directory
cd Plant-Disease-Detection-System

# 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open browser to http://localhost:5000
```

## 🚀 Features

- **🤖 AI Disease Detection**: 99.66% accuracy plant disease classifier
- **🌤️ Weather Integration**: Real-time weather data for disease risk assessment
- **📚 Educational Content**: Wikipedia-sourced disease information
- **💊 Treatment Recommendations**: Detailed care instructions for detected diseases
- **📱 Web Interface**: User-friendly upload and analysis interface
- **📊 Analysis History**: Track previous diagnoses and results
- **🔄 Real-time Processing**: Instant image analysis and results

## 📋 Prerequisites

- **Python 3.8+** (Recommended: Python 3.9 or 3.10)
- **Git** (for cloning the repository)
- **Internet Connection** (for weather data and Wikipedia information)

## 🛠️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/Akhil-0911/Plant-Disease-Detection-System.git
cd Plant-Disease-Detection-System
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
# Test if the disease analyzer imports correctly
python -c "from src.disease_analyzer import SimpleEnhancedPlantCare; print('✅ Installation successful!')"

# Test Flask app readiness
python -c "from app import app; print('✅ Flask app ready!')"

# Check Python and virtual environment
python -c "import sys; print('✅ Python version:', sys.version[:5])"
```

**Expected Output:**
```
✅ Installation successful!
✅ Flask app ready!
✅ Python version: 3.x.x
```

## 🏃‍♂️ Running the Application

### Method 1: Web Application (Recommended)
```bash
# Make sure you're in the project directory and virtual environment is activated
python app.py
```

The application will start on `http://localhost:5000`

**Web Interface Features:**
- 🖼️ **Upload Images**: Drag & drop or click to upload plant images
- 🔍 **Instant Analysis**: Real-time disease detection with confidence scores
- 📖 **Disease Information**: Detailed Wikipedia-sourced disease descriptions
- 🌡️ **Weather Analysis**: Current weather conditions affecting plant health
- 💊 **Treatment Plans**: Step-by-step care recommendations
- 📈 **History Tracking**: View previous analysis results

### Method 2: Direct Analysis (Command Line)
```bash
# Run disease analysis directly
python src/disease_analyzer.py
```

## 📁 Project Structure

```
Plant-Disease-Detection-System/
├── 🌐 app.py                          # Flask web application (main entry point)
├── 📦 requirements.txt                # Python dependencies
├── ⚙️ setup.py                       # Package configuration
├── 📖 README.md                      # This file
├── 🔒 .gitignore                     # Git ignore rules
├── 📂 src/
│   ├── __init__.py                   # Package initialization
│   ├── plant_care_system.py         # Core plant care system
│   └── disease_analyzer.py          # Main disease analysis engine
├── 🧠 model/
│   └── plant_disease_classifier.pth # Trained ML model (99.66% accuracy)
├── 💾 data/
│   ├── analysis_cache.json          # Cached analysis results
│   └── care_recommendations.json    # Treatment recommendations database
├── 🎨 templates/                     # HTML templates for web interface
│   ├── base.html                    # Base template
│   ├── index.html                   # Upload page
│   ├── results.html                 # Analysis results page
│   ├── history.html                 # Analysis history
│   └── about.html                   # About page
├── 🎯 static/                       # Static web assets
│   ├── css/                         # Stylesheets
│   ├── js/                          # JavaScript files
│   └── images/                      # Static images
├── 🧪 tests/                        # Test configuration
├── 📤 uploads/                      # User uploaded images (auto-created)
└── 📊 results/                      # Analysis results (auto-created)
```

## 🎯 Usage Guide

### Web Application Usage

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Open Your Browser**
   - Navigate to `http://localhost:5000`

3. **Upload Plant Image**
   - Click "Choose File" or drag & drop an image
   - Supported formats: JPG, JPEG, PNG
   - Maximum file size: 16MB

4. **View Results**
   - **Disease Detection**: See detected disease with confidence percentage
   - **Disease Information**: Read about the disease from Wikipedia
   - **Weather Analysis**: Current conditions affecting plant health
   - **Treatment Recommendations**: Follow step-by-step care instructions

5. **Explore Features**
   - **History**: View previous analyses
   - **About**: Learn about the system capabilities

### Command Line Usage

```bash
# Direct analysis with specific image
python src/disease_analyzer.py

# The system will provide:
# - Disease classification
# - Confidence score
# - Wikipedia disease information
# - Weather-based recommendations
# - Treatment suggestions
```

## 🧠 Supported Plant Diseases

The system can detect **38 different plant diseases** including:

- **Apple Diseases**: Apple Scab, Black Rot, Cedar Apple Rust
- **Cherry Diseases**: Powdery Mildew, Healthy Cherry
- **Corn Diseases**: Cercospora Leaf Spot, Common Rust, Northern Leaf Blight
- **Grape Diseases**: Black Rot, Esca, Leaf Blight
- **Peach Diseases**: Bacterial Spot, Healthy Peach
- **Pepper Diseases**: Bacterial Spot, Healthy Pepper
- **Potato Diseases**: Early Blight, Late Blight, Healthy Potato
- **Strawberry Diseases**: Leaf Scorch, Healthy Strawberry
- **Tomato Diseases**: Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Mosaic Virus, and more

## 🔧 Configuration

### Optional: API Keys (Enhanced Features)

For enhanced weather data and additional features, you can add API keys:

1. Create a `.env` file in the project root:
   ```bash
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   ```

2. Get API keys:
   - **OpenWeatherMap**: https://openweathermap.org/api (Free tier available)

*Note: The application works without API keys using fallback weather data.*

## 🚨 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure virtual environment is activated
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

2. **Model Loading Issues**
   ```bash
   # Verify model file exists
   ls model/plant_disease_classifier.pth
   
   # Check if model path is correct in app.py
   ```

3. **Port Already in Use**
   ```bash
   # Change port in app.py (line ~320)
   app.run(debug=True, port=5001)  # Use different port
   ```

4. **File Upload Issues**
   ```bash
   # Ensure uploads directory exists and has write permissions
   mkdir uploads
   ```

### Performance Tips

- **Image Size**: Resize large images (>5MB) for faster processing
- **Browser**: Use modern browsers (Chrome, Firefox, Safari, Edge)
- **Memory**: Ensure at least 4GB RAM available for model inference

## 🔄 Development

### Running in Development Mode
```bash
# Enable debug mode for development
export FLASK_ENV=development  # Linux/macOS
set FLASK_ENV=development     # Windows

python app.py
```

### Testing
```bash
# Test disease analyzer import
python -c "from src.disease_analyzer import SimpleEnhancedPlantCare; print('✅ Success')"

# Test Flask app
python -c "from app import app; print('✅ Flask app ready')"
```

## 📊 Model Information

- **Architecture**: ResNet-based Convolutional Neural Network
- **Accuracy**: 99.66% on validation dataset
- **Training Data**: 54,303 images across 38 plant disease classes
- **Input Size**: 224x224 pixels
- **Format**: PyTorch (.pth) model file

## 🤝 Contributing

1. Fork the repository: https://github.com/Akhil-0911/Plant-Disease-Detection-System
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Acknowledgments

- **Dataset**: PlantVillage Dataset
- **Framework**: PyTorch, Flask
- **APIs**: OpenWeatherMap, Wikipedia
- **UI**: Bootstrap 5, Font Awesome

## 📞 Support

For issues, questions, or contributions:
- � **Issues**: [GitHub Issues](https://github.com/Akhil-0911/Plant-Disease-Detection-System/issues)
- � **Discussions**: [GitHub Discussions](https://github.com/Akhil-0911/Plant-Disease-Detection-System/discussions)
- � **Repository**: https://github.com/Akhil-0911/Plant-Disease-Detection-System

---

**🌱 Happy Plant Care!** 🌿