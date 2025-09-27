# 🐛 Pest Infestation Forecaster

A web application that uses **YOLOv8 (Ultralytics)** to detect pests in images and forecast potential spread zones on a map of Gujarat.  
Built with **Flask, OpenCV, Leaflet.js, and PyTorch**.

---

## 🚀 Features
- 🔍 Pest Detection using a custom-trained YOLOv8 model  
- 🌍 Interactive Gujarat Map with predicted pest hotspots  
- 🖼️ Instant Image Upload & Detection Results  
- 🟥🟨🟩 Risk Zones (Red = High, Yellow = Medium, Green = Low)  
- ✨ Modern UI with smooth animations  

---

## 🏗️ Project Architecture


pest_project/
- app.py                # Flask backend
- weights/              # Trained YOLOv8 model weights
  - best.pt
  - last.pt
- static/               # CSS, JS, and uploaded/result images
  - uploads/
  - results/
- templates/
  - index.html          # Frontend (map + upload UI)
- requirements.txt
- README.md

## ⚙️ Installation & Setup




### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/pest_project.git
cd pest_project
```


### 2️⃣ Create Virtual Environment
```bash
python3 -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```


### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```


### 4️⃣ Run the Application

```bash
python app.py
Open in browser: http://127.0.0.1:5000
```

## 📊 How It Works

Upload an image of crops/pests

YOLOv8 detects pests and generates bounding boxes

Flask saves results in /static/results/

Gujarat map displays predicted risk zones:

🟥 Red = High risk

🟨 Yellow = Medium risk

🟩 Green = Low risk

## 👨‍💻 Author

Darshan Monpara
~ Passionate about AI, Data Science & Real-world Applications
