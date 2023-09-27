import cv2
import numpy as np
from ultralytics import YOLO

# from deep_sort.deep_sort.tracker import Tracker

capture_obj = cv2.VideoCapture("data\\sample.mp4")

state, frame = capture_obj.read()

# Load YOLO model:
best_weights = "runs\\detect\\yolo_trial_1\\weights\\best.pt"
model = YOLO(best_weights)

# tracker = Tracker()
while state:

    results = model(frame)

    for result in results:
        detections = []
        if result.data.tolist():
            x, y, w, h, score, cls_id = result.data.tolist()
            detections.append(x, y, w, h, score)
        if not result.data.tolist():
            detections.append(np.empty(0, 5))

    # tracker.update(frame, detections)

    # for track in tracker.tracks:
    #     bbox = track.bbox
    #     x, w, y, h = bbox
    #     track_id = track.track_id

    #     cv2.rectangle(frame, (x, w), (y, h))
    
    cv2.imshow("frame", frame)
    cv2.waitKey(25)

    state, frame = capture_obj.read()

capture_obj.release()
cv2.destroyAllWindows()