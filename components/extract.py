import os
import cv2

def extract():

    extract_obj = cv2.VideoCapture("data\\sample.mp4")
    frame_num = 0
    os.makedirs("frames", exist_ok=True)

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

    cv2.destroyAllWindows()

if __name__ == "__main__":
    extract()