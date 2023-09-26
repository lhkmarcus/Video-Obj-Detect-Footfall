import os
import random
import shutil

def shuffle():
    data_dir = "cvat_artifacts\\obj_train_data"

    with_annot_dir = os.path.join(data_dir, "with_annot")
    wout_annot_dir = os.path.join(data_dir, "wout_annot")

    train_label_dir = "data\\train\\labels"
    valid_label_dir = "data\\valid\\labels"

    # Get list of annotated files:
    f_list_with_annot = os.listdir(with_annot_dir)

    # Randomly sample from list:
    with_annot_sample = random.sample(f_list_with_annot, len(f_list_with_annot))

    f_list_wout_annot = os.listdir(wout_annot_dir)
    wout_annot_sample = random.sample(f_list_wout_annot, len(f_list_wout_annot))

    # Copy files to training and validation labels folders:
    for f in with_annot_sample[:160]:
        shutil.copy(os.path.join(with_annot_dir, f), train_label_dir)

    for f in with_annot_sample[160:]:
        shutil.copy(os.path.join(with_annot_dir, f), valid_label_dir)

    for f in wout_annot_sample[:160]:
        shutil.copy(os.path.join(wout_annot_dir, f), train_label_dir)

    for f in wout_annot_sample[160:len(with_annot_sample)]:
        shutil.copy(os.path.join(wout_annot_dir, f), valid_label_dir)

if __name__ == "__main__":
    shuffle()