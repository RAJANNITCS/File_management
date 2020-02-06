import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\rajan\AppData\Local\Programs\Python\Python37-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\rajan\AppData\Local\Programs\Python\Python37-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("File_Management.py", base=base, icon="file.ico")]


cx_Freeze.setup(
    name = "File Management",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["file.ico",'tcl86t.dll','tk86t.dll']}},
    version = "2.0",
    description = "Tkinter Application",
    executables = executables
    )