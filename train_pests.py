# File: train_pests.py (This is run once, locally, to create the model)
from ultralytics import YOLO

# 1. Load a pre-trained base model. 'yolov8n.pt' is the smallest and fastest version.
model = YOLO('yolov8n.pt')

# 2. Train the model on your custom dataset.
#    You need a 'data.yaml' file that points to your image folders and lists the pest names.
results = model.train(
    data='/Users/darshanmonpara/pest project/pest.v2i.yolov8/data.yaml',   # Path to dataset configuration
    epochs=50,                      # How many times to review the entire dataset
    imgsz=640,                      # Standardize image size for consistency
    project='pest_detection_project', # Folder to save results
    name='first_run'                  # Subfolder for this specific training session
)

# 3. After training, the best model is saved in:
#    'pest_detection_project/first_run/weights/best.pt'
#    This is the file you'll use in the backend server.
        