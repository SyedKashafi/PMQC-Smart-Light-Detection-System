import sys
import os
from pathlib import Path
import time
import glob
import logging
from datetime import datetime

import numpy as np
from shapely.geometry import Polygon

# Add yolov5 into PATH. This is to avoid referencing issue
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
ROOT = Path(str(ROOT) + '/yolov5')
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
# print(ROOT)


import py3nvml.py3nvml as nvml
import time
import json
from PIL import Image

from extra_utils.frame_extraction import extract, extraction_per_clip, extraction_per_parts, copy_files
from extra_utils.generate_labels import pregenerate_label_files
from extra_utils.dataset_pp import train_batch_review

# from extra_utils.voc_to_yolo import convert_annotation, getImagesInDir

# extract(
#     r"D:\Perodua\dataset from Perodua\[--------- Raw Rear Dataset\MYVI\LAVA RED\Without\1 fps",
#     r"D:\Perodua\dataset from Perodua\[--------- Training Rear Dataset\Myvi\Lava Red\Without\images",
#     ["export-Rear_ALL_22.08.2022_DAY.mp4-20220825-095402-025"],
#     frames_count=1, extract_method=extraction_per_clip
# )

# pregenerate_label_files(
#     r"D:\Perodua\dataset from Perodua\[--------- Training Rear Dataset\Aruz\DEFAULT_ARUZ_REAR.xml",
#     r"D:\Perodua\dataset from Perodua\[--------- Training Rear Dataset\Aruz\Granite Grey\images",
#     r"D:\Perodua\dataset from Perodua\[--------- Training Rear Dataset\Aruz\Granite Grey\labels",
#     ext="xml"
# )


# ========================= VOC TO YOLO =========================
# # classes = ['SL', 'DRL', 'HL', 'HB', 'FL', 'BL']
# classes = ["MYVI", "PERODUA", "DRL", "SL", "SSL", "HL", "CL"]
#
# folder_path = 'D:\Perodua\dataset from Perodua\[--------- Training Front Dataset_2022-9-6\Myvi\Cranberry Red\With DRL/'
# label_folder_path = folder_path + 'labels'
# image_folder_path = folder_path + 'images'
# output_path = folder_path + 'labels-txt/'
#
# Path.mkdir(Path(output_path), parents=True, exist_ok=True)
#
# print("image_folder_path: ", image_folder_path)
# image_paths = getImagesInDir(image_folder_path)
# print(image_paths)
# list_file = open(image_folder_path + '.txt', 'w')
# print(list_file)
#
# for image_path in image_paths:
#     list_file.write(image_path + '\n')
#     convert_annotation(label_folder_path, output_path, image_path)
# list_file.close()
#
# print("Finished processing: " + folder_path)

# ========================= TRAIN BATCH REVIEW =========================

# class_names = ["MYVI", "PERODUA", "DRL", "SL", "SSL", "HL", "CL"]   # MYVI front
# class_names = ["MYVI", "PERODUA", "HM", "WL", "RL", "BL", "LP", "SL"]  # MYVI rear
# class_names = ["ARUZ", "PERODUA", "FL", "HL", "CL", "SL", "SSL"]  # ARUZ front
# class_names = ["ARUZ", "PERODUA", "WL", "RL", "BL", "LP", "SL"]  # ARUZ rear
# class_names = ["RUSH", "TOYOTA", "FL", "HLF", "HLH", "CL", "SL", "SSL"]  # RUSH front
# class_names = ["RUSH", "TOYOTA", "WL", "RL", "BL", "LP", "SL"]  # RUSH rear
# class_names = ["ALZA_X", "PERODUA", "SL", "SSL", "HL", "CL"]  # ALZA_X front
# class_names = ["ALZA_AV", "PERODUA", "FL", "SEQ", "SSL", "HL", "CL"]  # ALZA_AV front
# class_names = ["VELOZ", "TOYOTA", "DRL", "SEQ", "SSL", "HB", "LB", "CL"]  # VELOZ front
# class_names = ["VELOZ", "TOYOTA", "HM", "FWL", "WL", "RL", "BL", "LP", "SL"]  # VELOZ rear
# class_names = ["ALZA_X", "PERODUA", "HM", "WL", "RL", "BL", "LP", "SL"]  # ALZA_X rear
# class_names = ["ALZA", "PERODUA", "HM", "FWL", "WL", "RL", "BL", "LP", "SL"]  # ALZA_X rear

# folder_path = r"D:\Perodua\dataset from Perodua\check - Valid Rear Rush_19-9-2022\Valid Rear Rush_19-9-2022\Rush/"
# for (root, dirs, files) in os.walk(folder_path):
#     if "images" in dirs:
#         variant_name = root.split("/")[-1]
#         train_batch_review(class_names,
#                            img_folder=f"{root}\\images/",
#                            lab_folder=f"{root}\\labels-txt/",
#                            img_filter=[], img_exclude=[], lab_filter=[],
#                            dest_folder=f'D:\\Perodua\\dataset from Perodua\\Review\\Rush Rear - Valid\\{variant_name}\\',
#                            empty=False, pos=False, neg=False, review=True, crop=True, labeled=True, ori=True)

# path = r"D:\Perodua\dataset from Perodua\check - Valid Rear Alza X Dataset_14-9-2022_labelled\Alza X\Ivory White (Solid)"
# train_batch_review(class_names,
#                    img_folder=f"{path}\\images/",
#                    lab_folder=f"{path}\\labels-txt/",
#                    img_filter=[], img_exclude=[], lab_filter=[],
#                    dest_folder=r'D:\Perodua\dataset from Perodua\Review\(Review) Alza X Rear - Valid\Ivory White (Solid)/',
#                    empty=False, pos=False, neg=False, review=True, crop=True, labeled=True, ori=False)

# # ========================= EXTRACT PARENT =========================
# folder_path = r"D:\Perodua\dataset from Perodua\[--------- Training Front Dataset_2022-9-8\Myvi\Cranberry Red\With DRL"
# img_folder = "images"
# label_folder = "labels"
# dest_folder = r"D:\Perodua\dataset from Perodua\[--------- Training Front Dataset_2022-9-8\Parent"
#
# images = glob.glob(f"{folder_path}\\{img_folder}\\*.jpeg")
# labels = glob.glob(f"{folder_path}\\{img_folder}\\*.xml")
#
# print("len: ", len(images))
# selected_images = images[: int(len(images) * 0.2)]
# selected_images.extend(images[int(len(images) * 0.2):])
#
# for image in selected_images:
#     img_name = image.split("\\")[-1]
#     print("source: ", image)
#     print(f"dest -> {dest_folder}\\images\\{img_name}")
#     copy_files(image, f"{dest_folder}\\images\\{img_name}")


# with open(
#         r"C:\Users\Aiman\Documents\IDE Workspace\PyCharm Projects\Yolo-Service\perodua_configurations\car_configs_v2022_7_15\Lights_Dict.json",
#         "r") as f:
#     file_json = json.load(f)
#
# print(file_json)
# exit()
#
# nvml.nvmlInit()
# h = nvml.nvmlDeviceGetHandleByIndex(0)
#
# while True:
#     t1 = time.time()
#     t = nvml.nvmlDeviceGetTemperature(h, nvml.NVML_TEMPERATURE_GPU)
#     print(t, str(time.time() - t1))


import cv2
import torch
import torchvision.ops.boxes as bops


def aggregate_by_union(bbox_list):
    """
    Aggregate by getting the minimum of x1 and y1, and the maximum of x2 and y2 between boxes
    :param bbox_list: list of bbox in the format of (x1, y1, x2, y2)
    :return:
    """
    x1 = sys.maxsize
    y1 = sys.maxsize
    x2 = -sys.maxsize - 1
    y2 = -sys.maxsize - 1
    for bbox in bbox_list:
        if bbox[0] < x1:
            x1 = bbox[0]
        if bbox[1] < y1:
            y1 = bbox[1]
        if bbox[2] > x2:
            x2 = bbox[2]
        if bbox[3] > y2:
            y2 = bbox[3]
    return x1, y1, x2, y2


# # Read image
# im = cv2.imread("C:\\Users\\Aiman\\Pictures\\myvi rear.png")
# default_area = 10000
# rois = []
# for i in range(3):
#     # Select ROI
#     x, y, w, h = cv2.selectROI(im)
#     x2 = x + w
#     y2 = y + h
#     rois.append((x, y, x2, y2))
#     im = cv2.rectangle(im, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0))
#
# st = time.time()

# rois = sorted(rois, key=lambda k: [k[0], k[1]])
# last_bbox = []
# new_bbox = []
# change = False
# for idx, roi in enumerate(rois):
#     if not change:
#         last_bbox = roi
#     change = False
#     x1, y1, x2, y2 = last_bbox
#     # bbox_1 = [x1, y1, x2, y2]
#     polygon1 = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
#     polygon1_shape = Polygon(polygon1)
#     try:
#         new_bbox = rois[idx]
#         # bbox_2 = rois[idx]
#         x1, y1, x2, y2 = rois[idx]
#         polygon2 = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
#         polygon2_shape = Polygon(polygon2)
#     except IndexError:
#         break
#
#     polygon_intersection = polygon1_shape.intersection(polygon2_shape).area
#     area1 = polygon1_shape.area
#     conf = polygon_intersection / area1
#     polygon_intersection = polygon2_shape.intersection(polygon1_shape).area
#     area2 = polygon2_shape.area
#     conf += polygon_intersection / area2
#     conf /= 2
#
#     if conf > 0.4:
#         x1, y1, x2, y2 = aggregate_by_union([last_bbox, new_bbox])
#         change = True
#     else:
#         diff1 = abs(area1 - default_area)
#         diff2 = abs(area2 - default_area)
#         if diff1 < diff2:
#             x1, y1, x2, y2 = last_bbox
#         else:
#             x1, y1, x2, y2 = new_bbox
#     last_bbox = [x1, y1, x2, y2]
#
# print("conf: ", conf)
# print("time using sorted: ", time.time() - st)
# im = cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), thickness=2)
# cv2.imshow("image", im)
# cv2.waitKey(0)

# ##### 2nd Method ####
# change = True
# while change:
#     for idx, roi in enumerate(rois):
#         last_bbox = roi
#         for j, r in enumerate(rois):
#             if idx == j:
#                 continue
#             x1, y1, x2, y2 = last_bbox
#             # bbox_1 = [x1, y1, x2, y2]
#             polygon1 = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
#             polygon1_shape = Polygon(polygon1)
#             try:
#                 new_bbox = r
#                 # bbox_2 = rois[idx]
#                 x1, y1, x2, y2 = new_bbox
#                 polygon2 = [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
#                 polygon2_shape = Polygon(polygon2)
#             except IndexError:
#                 break
#
#             polygon_intersection = polygon1_shape.intersection(polygon2_shape).area
#             area1 = polygon1_shape.area
#             conf = polygon_intersection / area1
#             polygon_intersection = polygon2_shape.intersection(polygon1_shape).area
#             area2 = polygon2_shape.area
#             conf += polygon_intersection / area2
#             conf /= 2
#
#             if conf > 0.4:
#                 x1, y1, x2, y2 = aggregate_by_union([last_bbox, new_bbox])
#                 change = True
#             else:
#                 diff1 = abs(area1 - default_area)
#                 diff2 = abs(area2 - default_area)
#                 if diff1 < diff2:
#                     x1, y1, x2, y2 = last_bbox
#                 else:
#                     x1, y1, x2, y2 = new_bbox
#                 change = False
#
#             last_bbox = [x1, y1, x2, y2]
# print("conf: ", conf)
# print("time using nested loop: ", time.time() - st)
# im = cv2.rectangle(im, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), thickness=2)
# cv2.imshow("image", im)
# cv2.waitKey(0)

# image = Image.open("C:\\Users\\Aiman\\Pictures\\myvi rear.png")
#
# pil_time = time.perf_counter()
# image.resize((400, 400))
# print("pillow resize: ", time.perf_counter() - pil_time)
#
# im = cv2.imread("C:\\Users\\Aiman\\Pictures\\myvi rear.png")
# cv2_time = time.perf_counter()
# im = cv2.resize(im, (400, 400), interpolation=cv2.INTER_AREA)
# print("cv2 resize: ", time.perf_counter() - cv2_time)
#
# cv2.imshow("pil resize", np.asarray(image))
# cv2.imshow("cv2 resize", im)
#
# cv2.waitKey(0)


# # ========================= EXTRACT TEST LABELS =========================
import xml.etree.ElementTree as ET


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


images = glob.glob(
    r"D:\Perodua\dataset from Perodua\check - Test labeled Front Alza AV_20-9-2022\Garnet Red\images\*.jpeg")
labels = glob.glob(
    r"D:\Perodua\dataset from Perodua\check - Test labeled Front Alza AV_20-9-2022\Garnet Red\labels\*.xml")
for label in labels:
    file_name = ".".join(label.split("\\")[-1].split(".")[:-1])
    image = next((i for i in images if file_name in i), None)
    img = cv2.imread(image)
    in_file = open(label, "r")
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        print("cls: ", cls)
        # if cls not in classes or int(difficult) == 1:
        #     continue
        # cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymin').text),
             int(xmlbox.find('ymax').text))
        img = cv2.rectangle(img, (b[0], b[2]), (b[1], b[3]), (255, 255, 0), 1)
        bb = convert((w, h), b)
        print("b: ", b)
        # out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    cv2.imshow("img", img)
    cv2.waitKey(0)
    break
