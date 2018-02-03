from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from mangaScraping import mangaFinder
from PyQt5.QtMultimedia import QSound
from interface import Ui_MainWindow
import threading
import queue

global downloadQueue
global mangaScraper
global booleanStopDownload

booleanStopDownload = False
mangaScraper = mangaFinder()
downloadQueue = queue.Queue()  # a queue to limit one download at the time


class downloadingThread(QtCore.QThread):
    new_operation = QtCore.pyqtSignal()
    taskProgressBar = QtCore.pyqtSignal(tuple)

    def __init__(self):

        QtCore.QThread.__init__(self)
        self.percentageCompleted = 0
        self.pageDownloaded = 0

    def run(self):

        while not downloadQueue.empty():  # start to download everything that is in the queue
            if booleanStopDownload == True:
                break
            infoDownload = downloadQueue.get()
            mangaScraper.set_variable(
                infoDownload[0], infoDownload[1], infoDownload[2], infoDownload[3])

            for pageDownloaded in mangaScraper.mangafoxDownload():
                if booleanStopDownload == True:
                    break                
                try:

                    self.percentageCompleted = (
                        pageDownloaded / mangaScraper.totalPage) * 100
                    self.pageDownloaded = pageDownloaded
                except:
                    self.percentageCompleted = 0

                completed_dowloaded = (self.percentageCompleted, self.pageDownloaded)
                self.taskProgressBar.emit(completed_dowloaded)
        self.new_operation.emit()
    def stop(self):
        self.terminate()    


class interface(Ui_MainWindow):

    def __init__(self, w):
        self.setupUi(w)
        self.downloadingThread = None

        with open('lastUsed.txt', 'r') as file:
            lastUsed = file.readlines()

        self.leFolder.setText(lastUsed[0][0:-1])
        self.leUrl.setText(lastUsed[1][0:-1])
        self.leStart.setText(lastUsed[2][0:-1])
        self.leEnd.setText(lastUsed[3])

        self.btnGo.clicked.connect(self.btnDownload)
        self.btnAddQueue.clicked.connect(self.addToQueue)
        self.btnStopDownload.clicked.connect(self.stop_download)
        self.btnStopDownload.setEnabled(False)
    def addToQueue(self):

        if self.leUrl.text() == '' or self.leStart.text() == '' or self.leEnd.text() == '' or self.leFolder.text() == '':
            pass

        else:

            tupleInfoDownload = (self.leUrl.text(), float(self.leStart.text()), float(
                self.leEnd.text()), self.leFolder.text())  # data to download the chapter
            downloadQueue.put(tupleInfoDownload)

            self.tbQueueDownload.setText(self.tbQueueDownload.toPlainText() + ' {} from chapter {} to chapter {} to {}\n'.format(mangaScraper.mangafoxGetTitle(tupleInfoDownload[0]),
                                                                                                                                 tupleInfoDownload[1], tupleInfoDownload[2], tupleInfoDownload[3]))

        # write on the label the queue
    def btnDownload(self):
        booleanStopDownload = False
        self.addToQueue()

        self.downloadingThread = downloadingThread()
        self.downloadingThread.start()

        self.downloadingThread.new_operation.connect(self.new_operation)
        self.downloadingThread.taskProgressBar.connect(self.taskProgressBar)

        self.btnAddQueue.setEnabled(False)
        self.btnGo.setEnabled(False)
        self.btnStopDownload.setEnabled(True)
        with open('lastUsed.txt', 'w') as file:
            file.write("{}\n{}\n{}\n{}".format(self.leFolder.text(),self.leUrl.text(),self.leStart.text(),self.leEnd.text()))     

    def taskProgressBar(self, completed_dowloaded):
        try:
            self.lblProgressBarResult.setText('{} downloaded out of {}'.format(completed_dowloaded[1],
                                                                               mangaScraper.totalPage))
        except:
            self.lblProgressBarResult.setText('0 downloaded out of 0')
        self.progressBar.setValue(completed_dowloaded[0])

    def new_operation(self):
        self.btnAddQueue.setEnabled(True)
        self.btnGo.setEnabled(True)
        self.btnStopDownload.setEnabled(False)
        self.progressBar.setValue(0)
        self.lblProgressBarResult.setText('0 downloaded out of 0')
        downloadQueue.queue.clear()
        self.tbQueueDownload.setText("")
        self.downloadingThread.stop()
        mangaScraper.restart()
        
    def stop_download(self):
        booleanStopDownload = True
        self.new_operation()
    def highligthText(self):
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = interface(w)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
