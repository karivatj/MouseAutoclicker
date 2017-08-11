import sys
import csv
import pyHook

from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# import UI files created with pyuic4
from MainUI import *
from HotkeyUI import *
from AboutUI import *
import HotKey
import Keys

# workthread which executes click sequences
from WorkThread import *

# class for used for stdout redirecting
class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))
    def writelines(self, l): 
        map(self.write, l) 

# self declared exceptions:
class InvalidComboBoxValue(Exception):
    pass

# main program
class AutoClicker(QtWidgets.QMainWindow, Ui_AutoClicker_Window):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        # redirect stdout
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)        

        # member variables
        self.title = "Mouse Autoclicker v.1.1"
        self.selectedRow  = -1
        self.selectedCol  = -1
        self.recording    = False
        self.picking      = False
        self.hotkeychange = False
        self.savePending  = False
        self.timer        = QtCore.QTimer()

        #Hotkey options
        self.ctrlModifier  = True
        self.altModifier   = False
        self.shiftModifier = False
        self.hotkey        = 'S'

        # create the hook mananger, register callbacks and hook to mouse and keyboard events
        hm = pyHook.HookManager()
        hm.MouseAllButtonsDown = self.OnMouseEvent
        hm.MouseAllButtonsUp = self.OnMouseEvent
        hm.KeyDown = self.OnKeyboardPressEvent
        hm.KeyUp = self.OnKeyboardReleaseEvent
        hm.HookKeyboard()
        hm.HookMouse()
        self.ctrlPressed = False
        self.altPressed = False
        self.shiftPressed = False

        # connect signals / slots of UI controls
        self.btnAdd.clicked.connect(self.buttonAddPressed)
        self.btnLoad.clicked.connect(self.buttonLoadPressed)
        self.btnPick.clicked.connect(self.buttonPickPressed)
        self.btnSave.clicked.connect(self.buttonSavePressed)
        self.btnClear.clicked.connect(self.buttonClearPressed)
        self.btnDelete.clicked.connect(self.buttonDeletePressed)
        self.btnMoveUp.clicked.connect(self.buttonMoveUpPressed)
        self.btnRecord.clicked.connect(self.buttonRecordPressed)
        self.btnUpdate.clicked.connect(self.buttonUpdatePressed)
        self.btnMoveDown.clicked.connect(self.buttonMoveDownPressed)
        self.actionAbout.triggered.connect(self.aboutActionTriggered)
        self.btnStartStopSequence.clicked.connect(self.buttonStartStopPressed)
        self.table.itemClicked.connect(self.cellClicked)
        self.timer.timeout.connect(self.updateMouseCoordstoStatusBar)

        self.btnHotkey.clicked.connect(self.hotkeyChangeRequested)

        self.thread = WorkThread()
        self.thread.finished.connect(self.updateUI)
        #self.thread.terminated.connect(self.updateUI)
        self.thread.progress.connect(self.highlightRow)
        #self.connect(self.thread, QtCore.SIGNAL("output(int)"), self.highlightRow)

        self.updateHotkeyButton()
        
        self.timer.start(100)

    def __del__(self):
        sys.stdout = sys.__stdout__

    #Triggered by pyhook library
    def OnMouseEvent(self, event):
        if self.picking == True:
            self.picking = False
            self.txtXcoord.setText(str(event.Position[0]))
            self.txtYcoord.setText(str(event.Position[1]))

            if event.Message == 513:
                self.cmbClickType.setCurrentIndex(1)
            elif event.Message == 519:
                self.cmbClickType.setCurrentIndex(2)
            elif event.Message == 516:
                self.cmbClickType.setCurrentIndex(3)

            self.setWindowState(QtCore.Qt.WindowActive)
            return False
        if self.recording == True:
            xcoord = event.Position[0]
            ycoord = event.Position[1]
            delay  = self.spinDelay.value()
            click  = 0

            if event.Message == 513:
                click = 1
            elif event.Message == 519:
                click = 2
            elif event.Message == 516:
                click = 3
            if click != 0:
                self.addTableEntry(click, xcoord, ycoord, delay, 1)

        return True   

    def OnKeyboardPressEvent(self, event):
        #Update modifier key status
        if event.Key == "Lcontrol" or event.Key == "Rcontrol":
            self.ctrlPressed = True
        if event.Key == "Lmenu" or event.Key == "Rmenu":
            self.altPressed = True
        if event.Key == "Lshift" or event.Key == "Rshift":
            self.shiftPressed = True

        #Check if mathching hotkey was pressed
        if self.ctrlModifier == True and self.ctrlPressed == False:
            return True
        if self.altModifier == True and self.altPressed == False:
            return True
        if self.shiftModifier == True and self.shiftPressed == False:
            return True
        if event.Key.upper() != self.hotkey.upper():
            return True

        #Hotkey matched. Do proper actions
        if self.recording == True:
            self.stopRecording()
        if self.thread.isRunning() == True:
            self.thread.stopclicking()
            win32api.SetCursorPos((self.x() + self.width() / 2, self.y() + self.height() / 2))   

        return True

    def OnKeyboardReleaseEvent(self, event):
        if event.Key == "Lcontrol" or event.Key == "Rcontrol":
            self.ctrlPressed = False
        if event.Key == "Lmenu" or event.Key == "Rmenu":
            self.altPressed = False
        if event.Key == "Lshift" or event.Key == "Rshift":
            self.shiftPressed = False
        return True

    def normalOutputWritten(self, text):       
        if len(text) == 1 and ord(str(text)) == 10:
            return
        self.statusBar.showMessage(text, 0)

    def updateHotkeyButton(self):
        hotkeytext = ""
        if self.ctrlModifier == True:
            hotkeytext += "CTRL+"
        if self.altModifier == True:
            hotkeytext += "ALT+"
        if self.shiftModifier == True:
            hotkeytext += "SHIFT+"
        hotkeytext += self.hotkey

        self.btnHotkey.setText(hotkeytext)

    def highlightRow(self, index):
        self.table.selectRow(index)

    def updateMouseCoordstoStatusBar(self):
        pos = QPoint(QCursor.pos())
        print("Mouse Position: (%d, %d)" % (pos.x(), pos.y()))

    def hotkeyChangeRequested(self):
        dialog = HotKey.HotKeyDialog()
        dialog.setHotkey([self.ctrlModifier, self.altModifier, self.shiftModifier, self.hotkey])
        if dialog.exec_():
            result = dialog.getHotKey()
            self.ctrlModifier  = result[0]
            self.altModifier   = result[1]
            self.shiftModifier = result[2]
            self.hotkey        = result[3]
            self.updateHotkeyButton()

    def aboutActionTriggered(self):
        dialog = QDialog()
        dialog.ui = Ui_About()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    def buttonPickPressed(self):
        self.setWindowState(QtCore.Qt.WindowMinimized)
        self.picking = True

    def buttonAddPressed(self):
        try:
            xcoord = int(self.txtXcoord.text())
            ycoord = int(self.txtYcoord.text())
            repeat = self.spinRepeat.value()
            duration = self.spinDelay.value()
            click = self.cmbClickType.currentIndex()

            if click == 0:
                raise InvalidComboBoxValue

            self.addTableEntry(click, xcoord, ycoord, duration, repeat)

            #Reset fields
            self.txtXcoord.setText("0")
            self.txtYcoord.setText("0")
            self.spinDelay.setValue(500)
            self.spinRepeat.setValue(1)
            self.cmbClickType.setCurrentIndex(0)

            self.btnStartStopSequence.setEnabled(True)
            self.btnClear.setEnabled(True)
            self.btnMoveDown.setEnabled(False)
            self.btnMoveUp.setEnabled(False)
            self.btnDelete.setEnabled(False)

            self.savePending = True
        except ValueError:
            QtWidgets.QMessageBox.question(self, 'Error', "Invalid values given. Please check your parameters.", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return
        except InvalidComboBoxValue:
            QtWidgets.QMessageBox.question(self, 'Error', "Please choose a click type.", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

    def buttonUpdatePressed(self):
        if self.selectedRow != -1 and self.selectedCol != -1:
            repeat = self.spinRepeat.value()
            duration = self.spinDelay.value()
            xcoord = int(self.txtXcoord.text())
            ycoord = int(self.txtYcoord.text())
            click = self.cmbClickType.currentIndex()

            self.updateTableEntry(self.selectedRow, click, xcoord, ycoord, duration, repeat)
            self.selectedRow = -1
            self.selectedCol = -1
            self.btnMoveDown.setEnabled(False)
            self.btnMoveUp.setEnabled(False)
            self.btnDelete.setEnabled(False)

    def buttonLoadPressed(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Load Autoclick Sequence", "", "Sequence files (*.seq)", "Sequence files (*.seq)")
        if filename == "":
            return
        if self.savePending == True or self.table.rowCount() != 0:
            if self.confirm("About to clear the current sequence. Are you sure?") == True:
                self.clearTable()
            else:
                return

        self.load(filename)
        self.enableUI()

    def buttonSavePressed(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save sequence", "", "Sequence files (*.seq)", "Sequence files (*.seq)")

        if filename == "":
            return
        else:
            self.save(filename)

    def buttonRecordPressed(self):
        if "Record Sequence" in self.btnRecord.text():
            self.startRecording()
        else:
            self.table.removeRow(self.table.rowCount() - 1)
            self.stopRecording()

    def startRecording(self):
        if self.savePending == True or self.table.rowCount() != 0:
            if self.confirm("About to clear the current sequence. Are you sure?") == True:
                self.clearTable()
            else:
                return

        self.disableUI()
        self.btnRecord.setText("Stop Recording")
        self.btnRecord.setEnabled(True)

        self.recording = True
        self.savePending = True
        self.setWindowState(QtCore.Qt.WindowMinimized)
        self.setWindowTitle("Press F12 to stop")

    def stopRecording(self):
        self.enableUI()
        self.setWindowState(QtCore.Qt.WindowActive)
        self.setWindowTitle(self.title)
        self.btnRecord.setText("Record Sequence")

        self.btnMoveDown.setEnabled(False)
        self.btnMoveUp.setEnabled(False)
        self.btnDelete.setEnabled(False)

        if self.table.rowCount() == 0:
            self.savePending = False
            self.btnStartStopSequence.setEnabled(False)

        self.recording = False

    def buttonStartStopPressed(self):
        if "Start" in self.btnStartStopSequence.text():
            self.disableUI()
            self.table.selectRow(0)
            self.btnStartStopSequence.setText("Stop")
            self.btnStartStopSequence.setEnabled(True)
            self.setWindowState(QtCore.Qt.WindowMinimized)
            self.setWindowTitle("Press F12 to stop")
            self.thread.startclicking(self.tableToList(), self.spinRerun.value(), self.spinRerunDelay.value())
        else:
            self.thread.stopclicking()

    def buttonMoveUpPressed(self):
        row = self.table.currentRow()

        if row != 0:
            self.table.insertRow(row - 1)
            for i in range(self.table.columnCount()):
                self.table.setItem(row - 1, i, self.table.takeItem(row + 1, i))
            self.table.removeRow(row + 1)
            self.table.setCurrentCell(row - 1, 0)
            self.table.selectRow(self.table.currentRow())

    def buttonMoveDownPressed(self):
        row = self.table.currentRow()

        if row != self.table.rowCount() - 1:
            self.table.insertRow(row + 2)
            for i in range(self.table.columnCount()):
                self.table.setItem(row + 2, i, self.table.takeItem(row, i))
            self.table.removeRow(row)
            self.table.setCurrentCell(row + 1, 0)
            self.table.selectRow(self.table.currentRow())

    def buttonDeletePressed(self):
        self.table.removeRow(self.table.currentRow())

        if self.table.rowCount() == 0:
            self.btnStartStopSequence.setEnabled(False)
            self.btnMoveDown.setEnabled(False)
            self.btnMoveUp.setEnabled(False)
            self.btnDelete.setEnabled(False)
            self.btnClear.setEnabled(False)
            self.savePending = False

    def buttonClearPressed(self):
        if self.confirm("About to clear the current sequence. Are you sure?") == True:
            self.clearTable()
            self.savePending = False
        else:
            return

    def cellClicked(self, item):
        self.selectedRow = item.row()
        self.selectedCol = item.column()

        clicktype = self.table.item(self.selectedRow, 0).text()
        xcoord    = self.table.item(self.selectedRow, 1).text()
        ycoord    = self.table.item(self.selectedRow, 2).text()
        duration  = int(self.table.item(self.selectedRow, 3).text())
        repeat    = int(self.table.item(self.selectedRow, 4).text())

        self.txtXcoord.setText(xcoord)
        self.txtYcoord.setText(ycoord)
        self.spinDelay.setValue(duration)
        self.spinRepeat.setValue(repeat)

        self.btnMoveDown.setEnabled(True)
        self.btnMoveUp.setEnabled(True)
        self.btnDelete.setEnabled(True)

        if clicktype == "Left Click":
            self.cmbClickType.setCurrentIndex(1)
        elif clicktype == "Middle Click":
            self.cmbClickType.setCurrentIndex(2)
        else:
            self.cmbClickType.setCurrentIndex(3)

    def clearTable(self):
        while self.table.rowCount() > 0:
            self.table.removeRow(0)

        self.btnStartStopSequence.setEnabled(False)
        self.btnMoveUp.setEnabled(False)
        self.btnMoveDown.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.btnClear.setEnabled(False)

    def tableToList(self):
        list = []

        for i in range(self.table.rowCount()):
            templist = []
            for j in range(self.table.columnCount()):
                templist.append(str(self.table.item(i, j).text()))
            list.append(templist)

        return list

    def listToTable(self, list):
        for i in range(len(list[0])):
            self.table.insertRow(i)
            for j in range(len(list[0][i])):
                self.table.setItem(i , j, QtWidgets.QTableWidgetItem(str(list[0][i][j])))
                self.table.item(i, j).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

    def updateTableEntry(self, row, click, xcoord, ycoord, duration, repeat):
        clicktype = self.clickTypetoAscii(click)
        self.insertRow(row, clicktype, xcoord, ycoord, duration, repeat)

    def addTableEntry(self, click, xcoord, ycoord, duration, repeat):
        clicktype = self.clickTypetoAscii(click)
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.insertRow(row, clicktype, xcoord, ycoord, duration, repeat)

    def insertRow(self, row, clicktype, xcoord, ycoord, duration, repeat):
        self.table.setItem(row , 1, QtWidgets.QTableWidgetItem(str(xcoord)))
        self.table.setItem(row , 2, QtWidgets.QTableWidgetItem(str(ycoord)))
        self.table.setItem(row , 4, QtWidgets.QTableWidgetItem(str(repeat)))
        self.table.setItem(row , 3, QtWidgets.QTableWidgetItem(str(duration)))
        self.table.setItem(row , 0, QtWidgets.QTableWidgetItem(str(clicktype)))
        self.table.item(row, 0).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.table.item(row, 1).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.table.item(row, 2).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.table.item(row, 3).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
        self.table.item(row, 4).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)

    def clickTypetoAscii(self, click):
        try:
            if click == 1:
                return "Left Click"
            elif click == 2:
                return "Middle Click"
            else:
                return "Right Click"
        except ValueError:
            return "Left Click"

    def disableUI(self):
        for w in self.findChildren(QtWidgets.QPushButton):
            w.setEnabled(False)
        for w in self.findChildren(QtWidgets.QLineEdit):
            w.setEnabled(False)

        self.cmbClickType.setEnabled(False)
        self.table.setEnabled(False)

    def enableUI(self):
        for w in self.findChildren(QtWidgets.QPushButton):
            w.setEnabled(True)
        for w in self.findChildren(QtWidgets.QLineEdit):
            w.setEnabled(True)

        self.cmbClickType.setEnabled(True)
        self.table.setEnabled(True)

    def updateUI(self):
        self.enableUI()
        self.setWindowState(QtCore.Qt.WindowActive)
        self.setWindowTitle(self.title)
        self.btnStartStopSequence.setText("Start")
        win32api.SetCursorPos((int((self.x() + self.width() / 2)), int((self.y() + self.height() / 2))))

    def load(self, fileName):
        list = []

        with open(fileName, "rb") as fileInput:
            reader = csv.reader(fileInput)
            templist = []
            for row in reader:
                items = [ str(field) for field in row ]
                templist.append(items)
            list.append(templist)

        self.listToTable(list)

    def save(self, fileName):
        list = self.tableToList()

        with open(fileName, "wb") as fileOutput:
            writer = csv.writer(fileOutput)
            writer.writerows(list)

        self.savePending = False

    def confirm(self, question):
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation Required', question, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = AutoClicker(None)
    myWindow.show()
    app.exec_()