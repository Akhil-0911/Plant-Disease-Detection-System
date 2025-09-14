// Plant Disease Detection - JavaScript Functions

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in');
    });

    // File upload validation
    const fileInput = document.getElementById('file');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                // Validate file size (16MB max)
                if (file.size > 16 * 1024 * 1024) {
                    alert('File size too large. Please select a file under 16MB.');
                    this.value = '';
                    return;
                }

                // Validate file type
                const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif'];
                if (!allowedTypes.includes(file.type)) {
                    alert('Invalid file type. Please select a JPG, PNG, or GIF image.');
                    this.value = '';
                    return;
                }

                // Show file size
                const fileSize = (file.size / 1024 / 1024).toFixed(2);
                const fileInfo = document.createElement('small');
                fileInfo.className = 'text-muted';
                fileInfo.innerHTML = `<i class="fas fa-file-image"></i> ${file.name} (${fileSize} MB)`;
                
                // Remove existing file info
                const existingInfo = document.querySelector('.file-info');
                if (existingInfo) {
                    existingInfo.remove();
                }
                
                fileInfo.className += ' file-info d-block mt-1';
                fileInput.parentNode.appendChild(fileInfo);
            }
        });
    }

    // Form submission handling
    const uploadForm = document.getElementById('uploadForm');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            const fileInput = document.getElementById('file');
            if (!fileInput.files[0]) {
                e.preventDefault();
                alert('Please select an image file.');
                return;
            }
            
            // Show loading state
            showLoadingState();
        });
    }

    // Location autocomplete (basic implementation)
    const locationInput = document.getElementById('location');
    if (locationInput) {
        const commonLocations = [
            'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
            'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
            'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte',
            'London', 'Paris', 'Tokyo', 'Mumbai', 'Delhi', 'Sydney', 'Toronto'
        ];

        locationInput.addEventListener('input', function() {
            const value = this.value.toLowerCase();
            if (value.length > 1) {
                const suggestions = commonLocations.filter(location => 
                    location.toLowerCase().includes(value)
                );
                showLocationSuggestions(suggestions, this);
            }
        });
    }
});

// Show loading state during form submission
function showLoadingState() {
    const submitBtn = document.getElementById('submitBtn');
    const loadingDiv = document.getElementById('loadingDiv');
    
    if (submitBtn && loadingDiv) {
        submitBtn.style.display = 'none';
        loadingDiv.style.display = 'block';
        
        // Animate progress bar
        const progressBar = loadingDiv.querySelector('.progress-bar');
        if (progressBar) {
            let width = 0;
            const interval = setInterval(() => {
                width += Math.random() * 10;
                if (width > 90) {
                    clearInterval(interval);
                    width = 95; // Stop at 95% until actual completion
                }
                progressBar.style.width = width + '%';
            }, 500);
        }
    }
}

// Image preview functionality
function previewImage(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById('preview');
            const previewContainer = document.getElementById('imagePreview');
            
            if (preview && previewContainer) {
                preview.src = e.target.result;
                previewContainer.style.display = 'block';
                
                // Add loading animation
                preview.style.opacity = '0';
                preview.onload = function() {
                    preview.style.transition = 'opacity 0.3s ease';
                    preview.style.opacity = '1';
                };
            }
        };
        reader.readAsDataURL(input.files[0]);
    }
}

// Location suggestions
function showLocationSuggestions(suggestions, input) {
    // Remove existing suggestions
    const existingSuggestions = document.querySelector('.location-suggestions');
    if (existingSuggestions) {
        existingSuggestions.remove();
    }

    if (suggestions.length === 0) return;

    // Create suggestions dropdown
    const suggestionsList = document.createElement('div');
    suggestionsList.className = 'location-suggestions list-group position-absolute w-100';
    suggestionsList.style.zIndex = '1000';
    suggestionsList.style.maxHeight = '200px';
    suggestionsList.style.overflowY = 'auto';

    suggestions.slice(0, 5).forEach(location => {
        const item = document.createElement('button');
        item.className = 'list-group-item list-group-item-action';
        item.textContent = location;
        item.type = 'button';
        
        item.addEventListener('click', function() {
            input.value = location;
            suggestionsList.remove();
        });
        
        suggestionsList.appendChild(item);
    });

    // Position and show suggestions
    input.parentNode.style.position = 'relative';
    input.parentNode.appendChild(suggestionsList);

    // Remove suggestions when clicking outside
    document.addEventListener('click', function(e) {
        if (!input.contains(e.target) && !suggestionsList.contains(e.target)) {
            suggestionsList.remove();
        }
    });
}

// Confidence level indicator
function updateConfidenceIndicator(confidence) {
    const indicators = document.querySelectorAll('.confidence-indicator');
    indicators.forEach(indicator => {
        if (confidence > 0.8) {
            indicator.className = 'confidence-indicator confidence-high';
        } else if (confidence > 0.6) {
            indicator.className = 'confidence-indicator confidence-medium';
        } else {
            indicator.className = 'confidence-indicator confidence-low';
        }
    });
}

// Copy result link functionality
function copyResultLink(resultId) {
    const url = `${window.location.origin}/results/${resultId}`;
    
    if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(() => {
            showToast('Link copied to clipboard!', 'success');
        });
    } else {
        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = url;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        showToast('Link copied to clipboard!', 'success');
    }
}

// Toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    toast.style.top = '20px';
    toast.style.right = '20px';
    toast.style.zIndex = '9999';
    toast.style.minWidth = '300px';
    
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(toast);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        if (toast.parentNode) {
            toast.parentNode.removeChild(toast);
        }
    }, 3000);
}

// Download result as PDF (future enhancement)
function downloadResultPDF(resultId) {
    showToast('PDF download feature coming soon!', 'info');
    // Future implementation: generate PDF report
}

// Share result on social media (future enhancement)
function shareResult(resultId, platform) {
    const url = `${window.location.origin}/results/${resultId}`;
    const text = 'Check out my plant disease analysis result!';
    
    let shareUrl = '';
    switch(platform) {
        case 'twitter':
            shareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`;
            break;
        case 'facebook':
            shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
            break;
        case 'whatsapp':
            shareUrl = `https://wa.me/?text=${encodeURIComponent(text + ' ' + url)}`;
            break;
    }
    
    if (shareUrl) {
        window.open(shareUrl, '_blank', 'width=600,height=400');
    }
}

// Dark mode toggle (future enhancement)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDark);
    showToast(`Dark mode ${isDark ? 'enabled' : 'disabled'}`, 'info');
}

// Load dark mode preference
document.addEventListener('DOMContentLoaded', function() {
    const darkMode = localStorage.getItem('darkMode') === 'true';
    if (darkMode) {
        document.body.classList.add('dark-mode');
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Lazy loading for images
function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading if images exist
if (document.querySelectorAll('img[data-src]').length > 0) {
    lazyLoadImages();
}

// API call example for external integration
async function analyzeImageAPI(imageFile, location = '') {
    const formData = new FormData();
    formData.append('file', imageFile);
    formData.append('location', location);

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Analysis API error:', error);
        throw error;
    }
}
