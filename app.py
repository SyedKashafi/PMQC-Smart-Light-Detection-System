import sys
import os
from pathlib import Path
from datetime import datetime
import subprocess

# Add yolov5 into PATH. This is to avoid referencing issue
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
ROOT = Path(str(ROOT) + '/yolov5')
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
# print(ROOT)

from Perodua.util.collage_util import draw_grid_from_cv2
# from yolo_wrapper import detect_video as dv
from extra_utils.dataset_pp import train_batch_review, annotation_to_labels

# folder_1 = r'C:\DSB - Work\JKR\testing'
# sample_1 = r'/home/amirarshadaziz/Full_video_trimmed.mp4'
# weight_1 = r'/home/amirarshadaziz/PycharmProjects/yolo-service/Perodua/files/best_weight_v2.pt'
# weight_2 = r'/home/amirarshadaziz/PycharmProjects/yolo-service/Perodua/files/best_lamp_triggerless_v3.pt'

# dv.exec_detect(
#     model_weight=weight_1,
#     video_path=sample_1,
#     live_view=True, frame_wait_time=1, video_save_dir='', lab_frame_path='',
#     iou_thres=0.25,
#     conf_thres=0.25,
#     imgsz=(640, 640)
# )

# train_batch_review(['Car', 'SL', 'FL', 'DRL', 'HL', 'SL_Lamp', 'FL_Lamp', 'DRL_Lamp', 'HL_Lamp', 'SSL', 'SSL_Lamp'],
#                    img_folder=r'/home/amirarshadaziz/Downloads/new_triggerless_train/images/train/',
#                    lab_folder=r'/home/amirarshadaziz/Downloads/new_triggerless_train/labels/train/',
#                    dest_folder=r'/home/amirarshadaziz/Downloads/new_triggerless_train/review/',
#                    review=True, crop=True, labeled=True, ori=False,
#                    img_filter=[],
#                    lab_filter=[],
#                    img_exclude=[])

# raw_dataset_folder_1 = r'/home/amirarshadaziz/Labelled data/'
# dest_folder = r'/home/amirarshadaziz/Downloads/new_triggerless_train/'
# for f in os.listdir(raw_dataset_folder_1):
#     annotation_to_labels(raw_dataset_folder_1 + f, f, dest_folder, do_split=False, copy_files=True,
#                          pos_split_mod=10, neg_split_mod=10, pos_sample_mod=1, neg_sample_mod=1)


import cv2

img = cv2.imread(
    r"D:\Perodua\multi models - new labels\BMW_E60\images\BMW_E60_BMW_E60_BMW_E60_BMW_E60_BMW_E60_BMW_E60_BMW_E60_00005.jpeg")
img = draw_grid_from_cv2(
    img,
    5, 5)
cv2.imshow("asdas", img)
cv2.waitKey(0)
exit()
# ----------------------------- Single Core Implementation -----------------------------
source1 = 'C:\\Users\\Discoverix PC\\Downloads\\Lights_only.mp4'  # '/home/amirarshadaziz/Lights_only.mp4'
source2 = 'C:\\Users\\Discoverix PC\\Downloads\\Lights_only (copy).mp4'  # '/home/amirarshadaziz/Full_video_trimmed (copy).mp4'
model_weight = r'C:\Users\Discoverix PC\PycharmProjects\Yolo-Service\Perodua\files\new_lamp_triggerless_s6.pt'

p1 = subprocess.Popen(["python", "sub_app.py", source1, model_weight, "True"])
# p2 = subprocess.Popen(["python", "sub_app.py", source2, model_weight, "False"])

print("Subprocess Starts!")
start_time = datetime.now()

p1.wait()
print("Subprocess 1 Ends! Time taken: ", (datetime.now() - start_time))
# p2.wait()
# print("Subprocess 2 Ends! Time taken: ", (datetime.now() - start_time))
