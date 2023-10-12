import cv2
import numpy as np
from ultralytics import YOLO

from tracker import Tracker

video_out = ".\\out.mp4"

capture_obj = cv2.VideoCapture("data\\sample.mp4")

state, frame = capture_obj.read()

capture_out = cv2.VideoWriter(video_out, 
                              cv2.VideoWriter_fourcc("m", "p", "4", "v"), 
                              capture_obj.get(cv2.CAP_PROP_FPS),
                              (frame.shape[1], frame.shape[0]))

# Load YOLO model:
best_weights = "runs\\detect\\yolo_trial_1\\weights\\best.pt"
model = YOLO(best_weights)

# Instantiate tracker:
tracker = Tracker()

while state:

    # Compute prediction results:
    results = model(frame)

    # Collect list of all detections:
    for result in results:
        detections = []

        for det in result.boxes.data.tolist():
            x1, y1, x2, y2, score, cls_id = det
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            cls_id = int(cls_id)
            detections.append([x1, y1, x2, y2, score])
            
            # Update tracking information:
            tracker.update(frame, detections)

            # Extract updated tracks:
            updated_tracks = tracker.tracks

            # Extract bbox coordinates and track ids:
            for track in updated_tracks:
                x1, y1, x2, y2 = track.bbox
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

    capture_out.write(frame)
    state, frame = capture_obj.read()

capture_obj.release()
capture_out.release()
cv2.destroyAllWindows()