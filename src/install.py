from distutils.core import setup
import py2exe

setup(windows=['AutoClicker.py'], options={"py2exe": {'bundle_files': 1, 'compressed': True, "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"], "includes": ["sip", "PyQt5.QtGui"]}}, zipfile = None,)
