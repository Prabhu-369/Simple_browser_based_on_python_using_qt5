import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import PyQt5
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

app = QApplication(sys.argv)

class customWebView(QWebEngineView):

    def closeEvent(self, event):
        # do stuff
        if True:
            event.accept()

    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            sys.exit()



def showUrl(url):
    web = customWebView()
    web.setWindowState(Qt.WindowMaximized)
    web.load(QUrl(url))
    web.show()
    web.activateWindow()
    sys.exit(app.exec_())



url = 'http://google.com'
if  len(sys.argv) >1 :
    url = sys.argv[1]
    showUrl(sys.argv[1])
else:
    showUrl(url)
