import os
import shutil

def sort():
    src_dir = "frames"

    train_out_dir = "data\\train\\images"
    valid_out_dir = "data\\valid\\images"

    train_labels_patterns = [str(f[:-4]) for f in os.listdir("data\\train\\labels")]
    valid_labels_patterns = [str(f[:-4]) for f in os.listdir("data\\valid\\labels")]

    for f in os.listdir(src_dir):

        if str(f[:-4]) in train_labels_patterns:
            src_f = os.path.join(src_dir, f)
            out_p = os.path.join(train_out_dir, f)
            shutil.copy(src_f, out_p)

    for f in os.listdir(src_dir):

        if str(f[:-4]) in valid_labels_patterns:
            src_f = os.path.join(src_dir, f)
            out_p = os.path.join(valid_out_dir, f)
            shutil.copy(src_f, out_p)

if __name__ == "__main__":
    sort()