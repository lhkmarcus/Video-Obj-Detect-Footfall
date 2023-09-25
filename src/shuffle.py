import os
import random
import shutil

def shuffle():
    annotated_dir = ".\\data\\obj_train_data\\w_annotation"
    non_annotated_dir = ".\\data\\obj_train_data\\wout_annotation"

    train_label_dir = ".\\data\\labels\\train"
    valid_label_dir = ".\\data\\labels\\valid"

    annotated_f_list = os.listdir(annotated_dir)
    annotated_sampled = random.sample(annotated_f_list, len(annotated_f_list))

    non_annotated_f_list = os.listdir(non_annotated_dir)
    non_annotated_sampled = random.sample(non_annotated_f_list, len(non_annotated_f_list))

    for f in annotated_sampled[:160]:
        shutil.move(os.path.join(annotated_dir, f), train_label_dir)

    for f in annotated_sampled[160:]:
        shutil.move(os.path.join(annotated_dir, f), valid_label_dir)

    for f in non_annotated_sampled[:160]:
        shutil.move(os.path.join(non_annotated_dir, f), train_label_dir)

    for f in non_annotated_sampled[160:len(annotated_f_list)]:
        shutil.move(os.path.join(non_annotated_dir, f), valid_label_dir)

if __name__ == "__main__":
    shuffle()