from flask import Flask, render_template, request
import os
import shutil
from ultralytics import YOLO
from werkzeug.utils import secure_filename
import glob
import time
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
PREDICTION_FOLDER = 'static/predictions'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PREDICTION_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

model = YOLO('best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Create unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        original_filename = secure_filename(file.filename)
        name, ext = os.path.splitext(original_filename)
        unique_filename = f"{name}_{timestamp}{ext}"
        
        upload_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(upload_path)

        # Create unique prediction folder for this request
        prediction_session = f"predict_{timestamp}"
        
        # Run prediction with unique folder name
        results = model.predict(
            source=upload_path, 
            save=True, 
            project=PREDICTION_FOLDER, 
            name=prediction_session, 
            exist_ok=True
        )

        # Find the predicted image in the unique session folder
        session_folder = os.path.join(PREDICTION_FOLDER, prediction_session)
        predicted_files = glob.glob(os.path.join(session_folder, '*'))
        
        if predicted_files:
            # Get the predicted file (should be only one)
            predicted_file = predicted_files[0]
            predicted_filename = os.path.basename(predicted_file)
            
            # Copy the predicted image to results folder with unique name
            result_filename = f"result_{timestamp}_{predicted_filename}"
            result_path = os.path.join(RESULT_FOLDER, result_filename)
            shutil.copy2(predicted_file, result_path)
            
            return render_template("index.html",
                                   uploaded_image_path=unique_filename,
                                   predicted_image=result_filename)
        else:
            return "Prediction failed", 500

if __name__ == '__main__':
    app.run(debug=True)