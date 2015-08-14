import time
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

    def runsequence(self):
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

    def run(self):
        if self.reruncount == 0:
            while(True):
                self.runsequence()
                if self.exiting == True:
                    break
                else:
                    time.sleep(self.rerundelay)
        else:
            for i in range(self.reruncount):
                self.runsequence()

                if self.exiting == True:
                    break
                elif i == self.reruncount:
                    break
                else:
                    time.sleep(self.rerundelay)
