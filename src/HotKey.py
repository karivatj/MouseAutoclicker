import re
import Keys

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

# import UI files created with pyuic4
from MainUI import *
from HotkeyUI import *
from AboutUI import *

class HotKeyDialog(QtGui.QDialog, Ui_HotKey):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.hotkey = 'S'
        self.ctrlActivated = False
        self.altActivated = False
        self.shiftActivated = False
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.rejected)
        self.destroyed.connect(self.rejected)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def keyPressEvent(self, event):
        if event.modifiers() & QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Control:
            if self.ctrlActivated:
                self.lblCTRL.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/ctrl_inactive.png")))
                self.ctrlActivated = False
            else:
                self.lblCTRL.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/ctrl_active.png")))
                self.ctrlActivated = True

        if event.modifiers() & QtCore.Qt.AltModifier and event.key() == QtCore.Qt.Key_Alt:
            if self.altActivated:
                self.lblAlt.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/alt_inactive.png")))
                self.altActivated = False
            else:
                self.lblAlt.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/alt_active.png")))
                self.altActivated = True

        if event.modifiers() & QtCore.Qt.ShiftModifier and event.key() == QtCore.Qt.Key_Shift:
            if self.shiftActivated:
                self.lblShift.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/shift_inactive.png")))
                self.shiftActivated = False
            else:
                self.lblShift.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/shift_active.png")))        
                self.shiftActivated = True

        try:
            key = Keys.getKey(event.key())
            if key is not None and re.match('^[A-Z0-9]+$', key) is not None:
                self.lblKey.setText(key)
                self.hotkey = key
        except UnicodeEncodeError:
            pass

    def getHotKey(self):
        list = []
        list.append(self.ctrlActivated)
        list.append(self.altActivated)
        list.append(self.shiftActivated)
        list.append(self.hotkey)
        return list

    def setHotkey(self, configuration):
        self.ctrlActivated  = configuration[0]
        self.altActivated   = configuration[1]
        self.shiftActivated = configuration[2]
        self.hotkey         = configuration[3]    

        if self.ctrlActivated:
            self.lblCTRL.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/ctrl_active.png")))
        if self.altActivated:
            self.lblAlt.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/alt_active.png")))
        if self.shiftActivated:
            self.lblShift.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/shift_active.png")))

        self.lblKey.setText(self.hotkey)

    def accepted(self):
        self.accept()

    def rejected(self):
        self.reject()

    def closeEvent(self, event):
        self.rejected()