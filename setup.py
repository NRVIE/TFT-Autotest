# import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["PySide2", "pyautogui", "pydirectinput",
                                  "time", "threading", "sys"],
                     "include_files": []
                     }

# GUI applications require a different base on Windows (the default is for
# a console application).
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(
    name="TFT Helper",
    version="1.2.1",
    description="Adding auto play mode, and setting button",
    options={"build_exe": build_exe_options},
    executables=[Executable("Run.py", base="Win32GUI")]
)
