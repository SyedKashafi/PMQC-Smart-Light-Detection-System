import sys
import os
from pathlib import Path
from datetime import datetime
import subprocess

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

# Add yolov5 into PATH. This is to avoid referencing issue
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
ROOT = Path(str(ROOT) + '/yolov5')
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

widgets = {
    "logo": [],
    "button": []
}

logo_loc = r'Perodua\files\perodua-logo-vector.png'

app = QApplication(sys.argv)
app.setStyle('Windows')
window = QWidget()
window.setWindowTitle("PERODUA Light Detection")
window.setFixedWidth(1000)
window.setStyleSheet("background: #FAF9F6;")  # 161219

grid = QGridLayout()


def clear_widgets():
    for widget in widgets:
        if widgets[widget]:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


# Running Python Subprocess. This will block the UI until it is done
def start_process():
    # clear_widgets()
    # frame2()

    # Put your source video/rtsp ip here
    source1 = r'Perodua\files\Lights_only.mp4'  # '/home/amirarshadaziz/Lights_only.mp4'
    # source1 = '0' # Webcam/camera IP
    source2 = r'Perodua\files\Lights_only - Copy.mp4'  # '/home/amirarshadaziz/Full_video_trimmed (copy).mp4'
    model_weight = r'Perodua\files\new_lamp_triggerless_s6.pt'

    # python sub_app.py Perodua\files\Lights_only.mp4 Perodua\files\new_lamp_triggerless_s6.pt True
    p1 = subprocess.Popen(["python", "sub_app.py", source1, model_weight, "True"], shell=True)
    p2 = subprocess.Popen(["python", "sub_app.py", source1, model_weight, "False"], shell=True)

    print("Subprocess Starts!")
    start_time = datetime.now()

    p1.wait()
    print("Subprocess 1 Ends! Time taken: ", (datetime.now() - start_time))
    p2.wait()
    print("Subprocess 2 Ends! Time taken: ", (datetime.now() - start_time))


def stop_process():
    clear_widgets()
    frame1()


def frame1():
    # Display Logo
    image = QPixmap(logo_loc)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "margin-top: 20px;"
    )
    widgets["logo"].append(logo)

    # Button Widget
    button = QPushButton("Start Process")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{background-color: '#C0C0C0';" +
        "border: 2px solid '#FFFFF';" +
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: '#black';" +
        "padding: 10px 0;" +
        "margin: 100px 300px;}" +
        "*:hover{background: '#32CD32';}"
    )
    button.clicked.connect(start_process)
    widgets["button"].append(button)

    # Report Button
    report_button = QPushButton("Report")
    report_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    report_button.setStyleSheet(
        "*{background-color: '#C0C0C0';" +
        "border: 2px solid '#FFFFF';" +
        "border-width: 2px;" +
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: '#black';" +
        "padding: 10px 0;" +
        "margin: 100px 300px;}" +
        "*:hover{background: '#32CD32';}"
    )
    # report_button.clicked.connect(start_process)
    widgets["button"].append(report_button)

    grid.addWidget(widgets["logo"][-1], 0, 1)
    grid.addWidget(widgets["button"][0], 1, 0)  # Start Process
    grid.addWidget(widgets["button"][-1], 1, 2)  # Report Button


def frame2():
    # Display Logo
    image = QPixmap(logo_loc)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50px;")
    widgets["logo"].append(logo)

    # Button Widget
    button = QPushButton("Stop Process")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet("*{border 4px solid '#BC006C';" +
                         "border-radius: 45px;" +
                         "font-size: 35px;" +
                         "color: 'white';" +
                         "padding: 25px 0;" +
                         "margin: 100px 200px;}" +
                         "*:hover{background: '#D22B2B';}"
                         )
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid.addWidget(widgets["button"][-1], 1, 0)


start_process()

# frame1()
#
# window.setLayout(grid)
#
# window.show()
# sys.exit(app.exec())
