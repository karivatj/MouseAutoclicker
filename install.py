from distutils.core import setup
import py2exe

setup(windows=['AutoClicker.py'], options={"py2exe": {"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"], "includes": ["sip", "PyQt4.QtGui"]}})
