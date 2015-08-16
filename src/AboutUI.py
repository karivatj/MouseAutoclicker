# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created: Sun Aug 16 22:14:37 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(250, 130)
        About.setMinimumSize(QtCore.QSize(250, 130))
        About.setMaximumSize(QtCore.QSize(250, 130))
        self.verticalLayout = QtGui.QVBoxLayout(About)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblHeadline = QtGui.QLabel(About)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHeadline.sizePolicy().hasHeightForWidth())
        self.lblHeadline.setSizePolicy(sizePolicy)
        self.lblHeadline.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeadline.setWordWrap(True)
        self.lblHeadline.setObjectName(_fromUtf8("lblHeadline"))
        self.verticalLayout.addWidget(self.lblHeadline)
        self.lblSummary = QtGui.QLabel(About)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSummary.sizePolicy().hasHeightForWidth())
        self.lblSummary.setSizePolicy(sizePolicy)
        self.lblSummary.setScaledContents(False)
        self.lblSummary.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSummary.setObjectName(_fromUtf8("lblSummary"))
        self.verticalLayout.addWidget(self.lblSummary)
        self.lblInfo = QtGui.QLabel(About)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInfo.sizePolicy().hasHeightForWidth())
        self.lblInfo.setSizePolicy(sizePolicy)
        self.lblInfo.setScaledContents(False)
        self.lblInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblInfo.setObjectName(_fromUtf8("lblInfo"))
        self.verticalLayout.addWidget(self.lblInfo)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.lblHeadline.setText(_translate("About", "Mouse Autoclicker v1.0b", None))
        self.lblSummary.setText(_translate("About", "A tool to automatize mouse clicks.", None))
        self.lblInfo.setText(_translate("About", "Author: Kari Vatjus-Anttila\n"
"Email: kari.vatjusanttila@gmail.com", None))

import resources_rc
