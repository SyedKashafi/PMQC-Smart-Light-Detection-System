import sys
import os
from pathlib import Path
import cProfile
import pstats

# Add yolov5 into PATH. This is to avoid referencing issue
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
ROOT = Path(str(ROOT) + '/yolov5')
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
# print(ROOT)

from Perodua.settings import settings
import Perodua.detect_video as dvp
# from Perodua.config.light_config import check_lights_dictionary, open_file
# from Perodua.operation.GridBox import create_list_of_GridCoordinates
from Perodua.operation.stm import STM
from Perodua.operation.ui import UI


def main():
    stm = STM()
    # arg from terminal
    args = sys.argv
    if len(args) > 1:
        # # print(args)
        # # Source location
        source = args[1]
        # # Detect Setup
        model_weight = args[2]
        # # True for Front side, False for rear
        front_side = True if args[3].lower() == 'true' else False
        debug = True if args[4].lower() == 'true' else False
    else:
        # arg from settings.py
        source = settings.SOURCE  # initialize camera
        model_weight = settings.YOLO_WEIGHT
        front_side = settings.FRONT

    # frame size duration
    frame_duration = settings.FRAME_DURATION

    # Setting if you want to enable object tracking or not
    obj_tracking_status = settings.OBJECT_TRACKING

    # Dict of model's class id and the class name to be detected by object tracking
    list_of_classes = {0: 'Car'}  # {class_id:class_name}

    # Live view image size
    # imgsz = (800, 648)  # 640,480 | 800, 648
    imgsz = settings.IMGSZ

    view = "front_lights" if front_side else "rear_lights"
    final_ui = UI(view)

    # TODO: For multi weights implementation, load general weight on startup
    input_param = dvp.detect_init_args(weights=model_weight, source=source, live_view=True,
                                       imgsz=imgsz, conf_thres=0.1, iou_thres=0.15, frame_wait_time=1,
                                       lab_frame_path='', video_save_dir='', frame_duration=frame_duration,
                                       list_of_classes=list_of_classes, list_of_gc=stm.list_of_gc)

    dvp.run(input_param, obj_tracking_status, front_side, stm=stm, final_ui=final_ui)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename="profiling.prof")
