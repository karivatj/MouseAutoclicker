import sys
import csv
import time
import pyHook
import win32api
import win32con
from PyQt4 import QtCore, QtGui, uic

class WorkThread(QtCore.QThread):
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)

        self.exiting = False
        self.sequence = list()
        self.reruncount = 1
        self.rerundelay = 0

    def __del__(self):
        self.exiting = True
        self.wait()

    def startclicking(self, seq, rerun, delay):
        self.exiting = False
        self.sequence = seq
        self.reruncount = rerun
        self.rerundelay = delay
        self.start()

    def stopclicking(self):
        self.exiting = True

    def run(self):

        for i in range(self.reruncount):
            counter = 0            
            while counter < len(self.sequence) and self.exiting != True:
                self.emit(QtCore.SIGNAL("output(int)"), counter / 5)

                clicktype = self.sequence[counter][0]
                x = int(self.sequence[counter][1])
                y = int(self.sequence[counter][2])
                duration = float(self.sequence[counter][3])
                repeat = int(self.sequence[counter][4])

                win32api.SetCursorPos((x,y))

                for j in range(repeat):
                    if clicktype == "Left Click":
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
                    elif clicktype == "Middle Click":
                        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,x,y,0,0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,x,y,0,0)
                    elif clicktype == "Right Click":
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
                    time.sleep(duration / 1000)

                counter += 1

            if self.exiting == True:
                break
            if self.reruncount == 6: #Reruncount of 6 means that the user chose to run this indefinitely
                i = 0

            time.sleep(self.rerundelay)


autoclicker_ui = uic.loadUiType("AutoClicker.ui")[0]

#Self declared exceptions:
class InvalidComboBoxValue(Exception):
    pass

class AutoClicker(QtGui.QMainWindow, autoclicker_ui):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        # member variables
        self.title = "AutoClicker v.1.0"
        self.selectedRow  = -1
        self.selectedCol  = -1
        self.recording    = False
        self.picking      = False
        self.savePending  = False

        # create the hook mananger, register callbacks and hook to mouse and keyboard events
        hm = pyHook.HookManager()
        hm.MouseAllButtonsDown = self.OnMouseEvent
        hm.MouseAllButtonsUp = self.OnMouseEvent
        hm.KeyDown = self.OnKeyboardEvent
        hm.HookKeyboard()
        hm.HookMouse()

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

        self.thread = WorkThread()
        self.thread.finished.connect(self.updateUI)
        self.thread.terminated.connect(self.updateUI)
        self.connect(self.thread, QtCore.SIGNAL("output(int)"), self.highlightRow)

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
        
    def OnKeyboardEvent(self, event):
        if event.Key == "F12" and self.thread.isRunning() == True:
            self.thread.stopclicking()
            win32api.SetCursorPos((self.x() + self.width() / 2, self.y() + self.height() / 2))

        if event.Key == "F12" and self.recording == True:
            self.stopRecording()

        return True

    def highlightRow(self, index):
        self.table.selectRow(index)

    def aboutActionTriggered(self):
        QtGui.QMessageBox.about(self, "About", "Mouse Autoclicker v1.0\nA tool to automatize mouse clicks.\nAuthor: Kari Vatjus-Anttila\nEmail: kari.vatjusanttila@gmail.com")

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
            QtGui.QMessageBox.question(self, 'Error', "Invalid values given. Please check your parameters.", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
            return
        except InvalidComboBoxValue:
            QtGui.QMessageBox.question(self, 'Error', "Please choose a click type.", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
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

        filename = QtGui.QFileDialog.getOpenFileName(self, "Load Autoclick Sequence", "", "Sequence files (*.seq)", "Sequence files (*.seq)")

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
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save sequence", "", "Sequence files (*.seq)", "Sequence files (*.seq)")

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
                self.table.setItem(i , j, QtGui.QTableWidgetItem(str(list[0][i][j])))
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
        self.table.setItem(row , 1, QtGui.QTableWidgetItem(str(xcoord)))
        self.table.setItem(row , 2, QtGui.QTableWidgetItem(str(ycoord)))
        self.table.setItem(row , 4, QtGui.QTableWidgetItem(str(repeat)))
        self.table.setItem(row , 3, QtGui.QTableWidgetItem(str(duration)))
        self.table.setItem(row , 0, QtGui.QTableWidgetItem(str(clicktype)))
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
        for w in self.findChildren(QtGui.QPushButton):
            w.setEnabled(False)
        for w in self.findChildren(QtGui.QLineEdit):
            w.setEnabled(False)            

        self.cmbClickType.setEnabled(False)
        self.cmbRerun.setEnabled(False)
        self.table.setEnabled(False)

    def enableUI(self):
        for w in self.findChildren(QtGui.QPushButton):
            w.setEnabled(True)
        for w in self.findChildren(QtGui.QLineEdit):
            w.setEnabled(True)            

        self.cmbClickType.setEnabled(True)
        self.cmbRerun.setEnabled(True)
        self.table.setEnabled(True)

    def updateUI(self):
        self.enableUI()
        self.setWindowState(QtCore.Qt.WindowActive)
        self.setWindowTitle(self.title)
        self.btnStartStopSequence.setText("Start")
        win32api.SetCursorPos((self.x() + self.width() / 2, self.y() + self.height() / 2))

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
        reply = QtGui.QMessageBox.question(self, 'Confirmation Required', question, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            return True    
        else:
            return False

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = AutoClicker(None)
    myWindow.show()
    app.exec_()