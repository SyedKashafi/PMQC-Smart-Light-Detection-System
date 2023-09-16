import streamlit as st

import sys
import os
from pathlib import Path

# Add yolov5 into PATH. This is to avoid referencing issue
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
ROOT = Path(str(ROOT) + '/yolov5')
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

# import Perodua.config.config_page as config
import Perodua.operation.Operation_Page as operation
import Perodua.result.result_page as result


PAGES = {
    # "Config Page": config,
    "Operation Page": operation,
    "Result Page": result
}

st.sidebar.title('Navigation')
selection = st.sidebar.selectbox('Go to', list(PAGES.keys()))
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

page.app()
