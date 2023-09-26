import os
import cv2
from utils.logger import logging

def extract():

    logging.info("Instantiated extraction object.")
    extract_obj = cv2.VideoCapture("data\\sample.mp4")
    frame_num = 0
    os.makedirs("frames", exist_ok=True)

    logging.info("Started extraction.")
    while(True):
        state, frame = extract_obj.read()
        if state:
            name = str(frame_num) + ".png"
            print("New frame captured:", name)
            cv2.imwrite(os.path.join("frames", name), frame)
            frame_num += 1
        else:
            break

    extract_obj.release()
    logging.info("Released extraction object.")

    cv2.destroyAllWindows()

    logging.info(f"Collected {frame_num} images.")
    logging.info("Finished.")

if __name__ == "__main__":
    extract()