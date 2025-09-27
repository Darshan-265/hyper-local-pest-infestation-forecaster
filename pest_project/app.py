import os
import uuid
from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO

app = Flask(__name__)

# Folders
UPLOAD_FOLDER = 'static/uploads/'
RESULTS_FOLDER = 'static/results/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "weights", "best.pt")
model = YOLO(model_path)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Detection API
@app.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files["image"]
    ext = os.path.splitext(file.filename)[1]
    filename = str(uuid.uuid4()) + ext
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Run inference
    results = model(filepath)
    pest_count = len(results[0].boxes)

    # Save result image
    result_filename = 'result_' + filename
    result_filepath = os.path.join(RESULTS_FOLDER, result_filename)
    results[0].save(filename=result_filepath)  # This saves the image with boxes

    # Determine risk
    if pest_count > 10:
        risk = "red"
    elif pest_count > 5:
        risk = "yellow"
    else:
        risk = "green"

    # Example Gujarat hotspots
    hotspots = [
        {"lat": 22.3, "lon": 70.8, "risk": risk},
        {"lat": 23.0, "lon": 72.5, "risk": risk},
        {"lat": 21.7, "lon": 73.0, "risk": risk}
    ]

    return jsonify({
        "pest_count": pest_count,
        "result_image_url": f"/static/results/{result_filename}",
        "predicted_hotspots": hotspots
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
