# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hotkey.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HotKey(object):
    def setupUi(self, HotKey):
        HotKey.setObjectName(_fromUtf8("HotKey"))
        HotKey.resize(511, 196)
        self.verticalLayout = QtGui.QVBoxLayout(HotKey)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(HotKey)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblCTRL = QtGui.QLabel(HotKey)
        self.lblCTRL.setText(_fromUtf8(""))
        self.lblCTRL.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/ctrl_inactive.png")))
        self.lblCTRL.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCTRL.setObjectName(_fromUtf8("lblCTRL"))
        self.horizontalLayout.addWidget(self.lblCTRL)
        self.label_2 = QtGui.QLabel(HotKey)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.lblAlt = QtGui.QLabel(HotKey)
        self.lblAlt.setText(_fromUtf8(""))
        self.lblAlt.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/alt_inactive.png")))
        self.lblAlt.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAlt.setObjectName(_fromUtf8("lblAlt"))
        self.horizontalLayout.addWidget(self.lblAlt)
        self.label_3 = QtGui.QLabel(HotKey)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.lblShift = QtGui.QLabel(HotKey)
        self.lblShift.setText(_fromUtf8(""))
        self.lblShift.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/shift_inactive.png")))
        self.lblShift.setAlignment(QtCore.Qt.AlignCenter)
        self.lblShift.setObjectName(_fromUtf8("lblShift"))
        self.horizontalLayout.addWidget(self.lblShift)
        self.label_4 = QtGui.QLabel(HotKey)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.lblKey = QtGui.QLabel(HotKey)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lblKey.setFont(font)
        self.lblKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKey.setObjectName(_fromUtf8("lblKey"))
        self.horizontalLayout.addWidget(self.lblKey)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(HotKey)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HotKey)
        QtCore.QMetaObject.connectSlotsByName(HotKey)

    def retranslateUi(self, HotKey):
        HotKey.setWindowTitle(_translate("HotKey", "Dialog", None))
        self.label_5.setText(_translate("HotKey", "Input your hotkey to stop script execution after which press OK to save", None))
        self.label_2.setText(_translate("HotKey", "+", None))
        self.label_3.setText(_translate("HotKey", "+", None))
        self.label_4.setText(_translate("HotKey", "+", None))
        self.lblKey.setText(_translate("HotKey", "A", None))

import resources_rc
