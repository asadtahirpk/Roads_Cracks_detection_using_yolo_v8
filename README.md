# AI Vision - Crack Detection System

A modern, web-based crack detection system powered by YOLO (You Only Look Once) deep learning model. This application provides an intuitive interface for uploading images and detecting cracks using advanced computer vision techniques.

## 🚀 Features

- **Modern UI/UX**: Sleek, futuristic interface with animations and glassmorphism effects
- **AI-Powered Detection**: Uses YOLO model for accurate crack detection
- **Real-time Processing**: Fast image analysis with visual feedback
- **Drag & Drop**: Intuitive file upload with drag-and-drop support
- **Responsive Design**: Mobile-friendly interface
- **Visual Results**: Side-by-side comparison of original and analyzed images

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **AI Model**: YOLO (Ultralytics)
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: OpenCV (via YOLO)
- **File Handling**: Werkzeug

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- pip (Python package installer)
- A trained YOLO model file (`best.pt`)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd ai-vision-crack-detection
   ```

2. **Install required packages**
   ```bash
   pip install flask ultralytics opencv-python pillow werkzeug
   ```

3. **Set up the project structure**
   ```
   project/
   ├── app.py
   ├── best.pt (your trained YOLO model)
   ├── templates/
   │   └── index.html
   └── static/
       ├── uploads/
       ├── predictions/
       └── results/
   ```

4. **Place your trained model**
   - Put your trained YOLO model file (`best.pt`) in the root directory
   - If your model has a different name, update the model loading line in `app.py`

## 🚀 Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:5000`
   - The application will be running in debug mode

3. **Upload and analyze images**
   - Click on the upload area or drag and drop an image
   - Supported formats: JPG, PNG, GIF (up to 10MB)
   - Click "ANALYZE WITH AI" to process the image

## 📁 Project Structure

```
ai-vision-crack-detection/
├── app.py                 # Main Flask application
├── best.pt               # Trained YOLO model
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── uploads/          # Uploaded original images
│   ├── predictions/      # YOLO prediction outputs
│   └── results/          # Processed result images
└── README.md            # This file
```

## 🔍 How It Works

1. **Image Upload**: Users upload images through the web interface
2. **Preprocessing**: The system saves uploaded images with unique timestamps
3. **AI Analysis**: YOLO model processes the image to detect cracks
4. **Result Generation**: Processed images with detected cracks are generated
5. **Display**: Both original and analyzed images are displayed side-by-side

## ⚙️ Configuration

### Model Configuration
- The application uses a YOLO model file named `best.pt`
- To use a different model, update this line in `app.py`:
  ```python
  model = YOLO('best.pt')
  ```

### File Size Limits
- Default maximum file size: 10MB
- Supported formats: JPG, PNG, GIF
- To change limits, modify the HTML file upload constraints

### Folder Structure
The application automatically creates necessary folders:
- `static/uploads/` - Stores uploaded images
- `static/predictions/` - Temporary YOLO output
- `static/results/` - Final processed images

## 🎨 UI Features

- **Animated Background**: Dynamic particle effects and grid overlay
- **Glassmorphism Design**: Modern translucent interface elements
- **Responsive Layout**: Works on desktop and mobile devices
- **Interactive Elements**: Hover effects and smooth animations
- **Loading States**: Visual feedback during processing
- **Status Indicators**: Real-time system status display

## 🚨 Troubleshooting

### Common Issues

1. **Model file not found**
   - Ensure `best.pt` is in the root directory
   - Check file permissions

2. **Import errors**
   - Install missing packages: `pip install ultralytics flask`
   - Verify Python version compatibility

3. **Upload failures**
   - Check file size (must be under 10MB)
   - Verify file format (JPG, PNG, GIF only)
   - Ensure upload folder exists and is writable

4. **Prediction errors**
   - Verify model file integrity
   - Check if CUDA is available (for GPU acceleration)

### Performance Tips

- **GPU Acceleration**: Install PyTorch with CUDA support for faster processing
- **Model Optimization**: Use quantized or pruned models for better performance
- **Memory Management**: Clear prediction folders periodically

## 🔒 Security Considerations

- File upload validation is implemented
- Unique filenames prevent conflicts
- Consider adding authentication for production use
- Implement rate limiting for API endpoints

## 📈 Future Enhancements

- [ ] Batch processing for multiple images
- [ ] Real-time camera feed analysis
- [ ] API endpoints for programmatic access
- [ ] Database integration for result storage
- [ ] User authentication and session management
- [ ] Advanced filtering and image preprocessing options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support, please contact:
- Email: asadtahirpkoutlook.com
- Issues: [GitHub Issues](https://github.com/asadtahirpk/Roads_Cracks_detection_using_yolo_v8)

## 🙏 Acknowledgments

- YOLO (Ultralytics) for the object detection framework
- Flask community for the web framework
- Contributors and testers