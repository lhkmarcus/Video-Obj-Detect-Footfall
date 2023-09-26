from ultralytics import YOLO

# Load YOLO model:
model = YOLO("yolov8n.pt")

# Run model:
results = model.train(data="yolo_config.yaml", imgsz=960, batch=32, epochs=300, name="yolo_trial_1")

