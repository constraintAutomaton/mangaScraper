from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import os
from mangaScraping import mangaFinder
from PyQt5.QtMultimedia import QSound
from interface import Ui_MainWindow

class interface(Ui_MainWindow):
    def __init__(self, w):
        self.setupUi(w)
        self.mangaScraper = mangaFinder()
        
        self.btnGo.clicked.connect(self.download)
    def download(self):
        
        self.mangaScraper.setVariable(self.leUrl.text(),float(self.leStart.text()),float(self.leEnd.text()),self.leFolder.text())
        
        self.mangaScraper.domainSplitter()
        
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    prog = interface(w)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 