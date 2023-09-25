import os
import shutil

def sort():
    src_dir = ".\\data\\frames"

    train_out_dir = ".\\data\\images\\train"
    valid_out_dir = ".\\data\\images\\valid"

    train_labels_patterns = [str(f[:-4]) for f in os.listdir(".\\data\\labels\\train")]
    valid_labels_patterns = [str(f[:-4]) for f in os.listdir(".\\data\\labels\\valid")]

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