from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from mangaScraping import mangaFinder
from PyQt5.QtMultimedia import QSound
from interface import Ui_MainWindow
import threading
import queue

class interface(Ui_MainWindow):
    def __init__(self, w):
        self.setupUi(w)
        self.mangaScraper = mangaFinder()
        self.downloadQueue = queue.Queue() # a queue to limit one download at the time
        self.task = None # the thread of the download
        self.progress = None # the thread of thr progress bar
        
        self.btnGo.clicked.connect(self.threadDownload)
        self.btnAddQueue.clicked.connect(self.addToQueue)
        
    def addToQueue(self):
        tupleInfoDownload = (self.leUrl.text(),float(self.leStart.text()),float(self.leEnd.text()),self.leFolder.text()) # data to download the chapter
        self.downloadQueue.put(tupleInfoDownload) 
        self.tbQueueDownload.setText(self.tbQueueDownload.toPlainText()+ ' {} from chapter {} to chapter {} to {}\n'.format(self.mangaScraper.mangafoxGetTitle(tupleInfoDownload[0]), 
                                                                                                                            tupleInfoDownload[1],tupleInfoDownload[2],tupleInfoDownload[3])) 
        # write on the label the queue
    def download(self):
        
        while not self.downloadQueue.empty():
            infoDownload = self.downloadQueue.get()
            self.mangaScraper.setVariable(infoDownload[0],infoDownload[1],infoDownload[2],infoDownload[3])
            self.mangaScraper.domainSplitter()
                
    
        
    def threadDownload(self,queue):
    
        self.task = threading.Thread(target = self.download)
        self.task.start()
        
        self.progress = threading.Thread(target = self.taskProgressBar)
        self.progress.start()
        
    def taskProgressBar(self):
        while self.task.isAlive():
            try: # at the begining completed = 0/0
                completed = (self.mangaScraper.pageDownloaded/self.mangaScraper.totalPage)*100
            except:
                
                completed = 0
                
            self.lblProgressBarResult.setText('{} downloaded out of {}'.format(self.mangaScraper.pageDownloaded,
                                                                               self.mangaScraper.totalPage))
            self.progressBar.setValue(completed)
           
        self.progressBar.setValue(100)
        self.lblProgressBarResult.setText('all done')

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = interface(w)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 