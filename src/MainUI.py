# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoClicker.ui'
#
# Created: Sun Aug 16 22:15:52 2015
#      by: PyQt5 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_AutoClicker_Window(object):
    def setupUi(self, AutoClicker_Window):
        AutoClicker_Window.setObjectName(_fromUtf8("AutoClicker_Window"))
        AutoClicker_Window.setEnabled(True)
        AutoClicker_Window.resize(880, 500)
        AutoClicker_Window.setMinimumSize(QtCore.QSize(880, 500))
        AutoClicker_Window.setWindowOpacity(1.0)
        AutoClicker_Window.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(AutoClicker_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupAddEdit = QtWidgets.QGroupBox(self.centralwidget)
        self.groupAddEdit.setObjectName(_fromUtf8("groupAddEdit"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupAddEdit)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnRecord = QtWidgets.QPushButton(self.groupAddEdit)
        self.btnRecord.setEnabled(True)
        self.btnRecord.setObjectName(_fromUtf8("btnRecord"))
        self.gridLayout_2.addWidget(self.btnRecord, 2, 3, 1, 3)
        self.btnPick = QtWidgets.QPushButton(self.groupAddEdit)
        self.btnPick.setObjectName(_fromUtf8("btnPick"))
        self.gridLayout_2.addWidget(self.btnPick, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupAddEdit)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.txtXcoord = QtWidgets.QLineEdit(self.groupAddEdit)
        self.txtXcoord.setObjectName(_fromUtf8("txtXcoord"))
        self.gridLayout_2.addWidget(self.txtXcoord, 0, 1, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.groupAddEdit)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout_2.addWidget(self.btnSave, 1, 5, 1, 1)
        self.lblYcoord = QtWidgets.QLabel(self.groupAddEdit)
        self.lblYcoord.setObjectName(_fromUtf8("lblYcoord"))
        self.gridLayout_2.addWidget(self.lblYcoord, 1, 0, 1, 1)
        self.lblClicktype = QtWidgets.QLabel(self.groupAddEdit)
        self.lblClicktype.setObjectName(_fromUtf8("lblClicktype"))
        self.gridLayout_2.addWidget(self.lblClicktype, 2, 0, 1, 1)
        self.cmbClickType = QtWidgets.QComboBox(self.groupAddEdit)
        self.cmbClickType.setObjectName(_fromUtf8("cmbClickType"))
        self.cmbClickType.addItem(_fromUtf8(""))
        self.cmbClickType.addItem(_fromUtf8(""))
        self.cmbClickType.addItem(_fromUtf8(""))
        self.cmbClickType.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cmbClickType, 2, 1, 1, 1)
        self.lblXcoord = QtWidgets.QLabel(self.groupAddEdit)
        self.lblXcoord.setObjectName(_fromUtf8("lblXcoord"))
        self.gridLayout_2.addWidget(self.lblXcoord, 0, 0, 1, 1)
        self.btnLoad = QtWidgets.QPushButton(self.groupAddEdit)
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.gridLayout_2.addWidget(self.btnLoad, 0, 5, 1, 1)
        self.txtYcoord = QtWidgets.QLineEdit(self.groupAddEdit)
        self.txtYcoord.setObjectName(_fromUtf8("txtYcoord"))
        self.gridLayout_2.addWidget(self.txtYcoord, 1, 1, 1, 1)
        self.btnUpdate = QtWidgets.QPushButton(self.groupAddEdit)
        self.btnUpdate.setObjectName(_fromUtf8("btnUpdate"))
        self.gridLayout_2.addWidget(self.btnUpdate, 1, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.spinDelay = QtWidgets.QSpinBox(self.groupAddEdit)
        self.spinDelay.setEnabled(True)
        self.spinDelay.setMinimum(100)
        self.spinDelay.setMaximum(10000)
        self.spinDelay.setSingleStep(50)
        self.spinDelay.setProperty("value", 500)
        self.spinDelay.setObjectName(_fromUtf8("spinDelay"))
        self.horizontalLayout.addWidget(self.spinDelay)
        self.lblMs = QtWidgets.QLabel(self.groupAddEdit)
        self.lblMs.setObjectName(_fromUtf8("lblMs"))
        self.horizontalLayout.addWidget(self.lblMs)
        self.lblRepeat = QtWidgets.QLabel(self.groupAddEdit)
        self.lblRepeat.setObjectName(_fromUtf8("lblRepeat"))
        self.horizontalLayout.addWidget(self.lblRepeat)
        self.spinRepeat = QtWidgets.QSpinBox(self.groupAddEdit)
        self.spinRepeat.setMinimum(1)
        self.spinRepeat.setObjectName(_fromUtf8("spinRepeat"))
        self.horizontalLayout.addWidget(self.spinRepeat)
        self.label_2 = QtWidgets.QLabel(self.groupAddEdit)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(self.groupAddEdit)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.gridLayout_2.addWidget(self.btnAdd, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupAddEdit)
        self.groupClickSequence = QtWidgets.QGroupBox(self.centralwidget)
        self.groupClickSequence.setObjectName(_fromUtf8("groupClickSequence"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupClickSequence)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnStartStopSequence = QtWidgets.QPushButton(self.groupClickSequence)
        self.btnStartStopSequence.setEnabled(False)
        self.btnStartStopSequence.setObjectName(_fromUtf8("btnStartStopSequence"))
        self.verticalLayout_3.addWidget(self.btnStartStopSequence)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.btnMoveUp = QtWidgets.QPushButton(self.groupClickSequence)
        self.btnMoveUp.setEnabled(False)
        self.btnMoveUp.setObjectName(_fromUtf8("btnMoveUp"))
        self.verticalLayout_3.addWidget(self.btnMoveUp)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.btnMoveDown = QtWidgets.QPushButton(self.groupClickSequence)
        self.btnMoveDown.setEnabled(False)
        self.btnMoveDown.setObjectName(_fromUtf8("btnMoveDown"))
        self.verticalLayout_3.addWidget(self.btnMoveDown)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.btnDelete = QtWidgets.QPushButton(self.groupClickSequence)
        self.btnDelete.setEnabled(False)
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.verticalLayout_3.addWidget(self.btnDelete)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.btnClear = QtWidgets.QPushButton(self.groupClickSequence)
        self.btnClear.setEnabled(False)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.verticalLayout_3.addWidget(self.btnClear)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.table = QtWidgets.QTableWidget(self.groupClickSequence)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setProperty("showDropIndicator", False)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table.setWordWrap(True)
        self.table.setCornerButtonEnabled(False)
        self.table.setColumnCount(5)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(75)
        self.table.horizontalHeader().setMinimumSectionSize(30)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.verticalHeader().setHighlightSections(True)
        self.gridLayout_3.addWidget(self.table, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtWidgets.QLabel(self.groupClickSequence)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spinRerun = QtWidgets.QSpinBox(self.groupClickSequence)
        self.spinRerun.setMaximum(1000)
        self.spinRerun.setProperty("value", 1)
        self.spinRerun.setObjectName(_fromUtf8("spinRerun"))
        self.horizontalLayout_2.addWidget(self.spinRerun)
        self.label_3 = QtWidgets.QLabel(self.groupClickSequence)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinRerunDelay = QtWidgets.QSpinBox(self.groupClickSequence)
        self.spinRerunDelay.setMaximum(1000)
        self.spinRerunDelay.setObjectName(_fromUtf8("spinRerunDelay"))
        self.horizontalLayout_2.addWidget(self.spinRerunDelay)
        self.label_5 = QtWidgets.QLabel(self.groupClickSequence)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.btnHotkey = QtWidgets.QPushButton(self.groupClickSequence)
        self.btnHotkey.setEnabled(True)
        self.btnHotkey.setDefault(False)
        self.btnHotkey.setFlat(False)
        self.btnHotkey.setObjectName(_fromUtf8("btnHotkey"))
        self.horizontalLayout_2.addWidget(self.btnHotkey)
        self.lblHotkey = QtWidgets.QLabel(self.groupClickSequence)
        self.lblHotkey.setObjectName(_fromUtf8("lblHotkey"))
        self.horizontalLayout_2.addWidget(self.lblHotkey)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupClickSequence)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        AutoClicker_Window.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(AutoClicker_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 880, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        AutoClicker_Window.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(AutoClicker_Window)
        self.statusBar.setEnabled(False)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        AutoClicker_Window.setStatusBar(self.statusBar)
        self.actionAbout = QtWidgets.QAction(AutoClicker_Window)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionBind_Script_Abort_Hotkey = QtWidgets.QAction(AutoClicker_Window)
        self.actionBind_Script_Abort_Hotkey.setObjectName(_fromUtf8("actionBind_Script_Abort_Hotkey"))
        self.menuMenu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(AutoClicker_Window)
        QtCore.QMetaObject.connectSlotsByName(AutoClicker_Window)
        AutoClicker_Window.setTabOrder(self.txtXcoord, self.txtYcoord)
        AutoClicker_Window.setTabOrder(self.txtYcoord, self.cmbClickType)
        AutoClicker_Window.setTabOrder(self.cmbClickType, self.btnAdd)
        AutoClicker_Window.setTabOrder(self.btnAdd, self.btnLoad)
        AutoClicker_Window.setTabOrder(self.btnLoad, self.btnUpdate)
        AutoClicker_Window.setTabOrder(self.btnUpdate, self.btnSave)
        AutoClicker_Window.setTabOrder(self.btnSave, self.table)
        AutoClicker_Window.setTabOrder(self.table, self.btnStartStopSequence)
        AutoClicker_Window.setTabOrder(self.btnStartStopSequence, self.btnMoveUp)
        AutoClicker_Window.setTabOrder(self.btnMoveUp, self.btnMoveDown)
        AutoClicker_Window.setTabOrder(self.btnMoveDown, self.btnDelete)
        AutoClicker_Window.setTabOrder(self.btnDelete, self.btnClear)

    def retranslateUi(self, AutoClicker_Window):
        AutoClicker_Window.setWindowTitle(_translate("AutoClicker_Window", "Mouse Autoclicker v.1.1", None))
        self.groupAddEdit.setTitle(_translate("AutoClicker_Window", "Add / Edit mouse clicks", None))
        self.btnRecord.setText(_translate("AutoClicker_Window", "Record Sequence", None))
        self.btnPick.setText(_translate("AutoClicker_Window", "Pick", None))
        self.label.setText(_translate("AutoClicker_Window", "Duration:", None))
        self.txtXcoord.setText(_translate("AutoClicker_Window", "0", None))
        self.btnSave.setText(_translate("AutoClicker_Window", "Save Clicks", None))
        self.lblYcoord.setText(_translate("AutoClicker_Window", "Y Coordinate:", None))
        self.lblClicktype.setText(_translate("AutoClicker_Window", "Click Type:", None))
        self.cmbClickType.setItemText(0, _translate("AutoClicker_Window", "None", None))
        self.cmbClickType.setItemText(1, _translate("AutoClicker_Window", "Left Click", None))
        self.cmbClickType.setItemText(2, _translate("AutoClicker_Window", "Middle Click", None))
        self.cmbClickType.setItemText(3, _translate("AutoClicker_Window", "Right Click", None))
        self.lblXcoord.setText(_translate("AutoClicker_Window", "X Coordinate:", None))
        self.btnLoad.setText(_translate("AutoClicker_Window", "Load Clicks", None))
        self.txtYcoord.setText(_translate("AutoClicker_Window", "0", None))
        self.btnUpdate.setText(_translate("AutoClicker_Window", "Update", None))
        self.lblMs.setText(_translate("AutoClicker_Window", "milliseconds", None))
        self.lblRepeat.setText(_translate("AutoClicker_Window", "Repeat", None))
        self.label_2.setText(_translate("AutoClicker_Window", "time(s)", None))
        self.btnAdd.setText(_translate("AutoClicker_Window", "Add", None))
        self.groupClickSequence.setTitle(_translate("AutoClicker_Window", "Current mouse click sequence", None))
        self.btnStartStopSequence.setText(_translate("AutoClicker_Window", "Start", None))
        self.btnMoveUp.setText(_translate("AutoClicker_Window", "Move Up", None))
        self.btnMoveDown.setText(_translate("AutoClicker_Window", "Move Down", None))
        self.btnDelete.setText(_translate("AutoClicker_Window", "Delete", None))
        self.btnClear.setText(_translate("AutoClicker_Window", "Clear", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("AutoClicker_Window", "Type", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("AutoClicker_Window", "X", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("AutoClicker_Window", "Y", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("AutoClicker_Window", "Duration", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("AutoClicker_Window", "Repeat", None))
        self.label_4.setText(_translate("AutoClicker_Window", "Rerun sequence (0 = infinite)", None))
        self.label_3.setText(_translate("AutoClicker_Window", "time(s). Delay between reruns:", None))
        self.label_5.setText(_translate("AutoClicker_Window", "sec", None))
        self.btnHotkey.setText(_translate("AutoClicker_Window", "F12", None))
        self.lblHotkey.setText(_translate("AutoClicker_Window", "stops execution. Click to change hotkey", None))
        self.menuMenu.setTitle(_translate("AutoClicker_Window", "Menu", None))
        self.actionAbout.setText(_translate("AutoClicker_Window", "About", None))
        self.actionBind_Script_Abort_Hotkey.setText(_translate("AutoClicker_Window", "Bind Script Abort Hotkey", None))

