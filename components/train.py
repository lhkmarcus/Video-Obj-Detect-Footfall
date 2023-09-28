from ultralytics import YOLO

# Load YOLO model:
model = YOLO("yolov8n.pt")

# Run model:
results = model.train(data="data_config.yaml", imgsz=960, batch=32, epochs=50, name="yolo_trial_1")

# yolo task=detect mode=predict model=runs/detect/yolo_trial_1/weights/best.pt source=data/sample.mp4 show=True imgsz=960