import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import PyQt5
import warnings
warnings.simplefilter("ignore")

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

app = QApplication(sys.argv)

class Render(QWebEngineView):
    def closeEvent(self, event):
        # do stuff
        if True:
            event.accept()

    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            sys.exit()



def showUrl(url):
        web = Render()
        web.setWindowState(Qt.WindowMaximized)
        web.load(QUrl(url))
        web.show()
        web.activateWindow()
        sys.exit(app.exec_())  

def Visit_site(web):
        sites = {'ytb': 'http://youtube.com', 'ggl': 'http://google.com','ghb':'http://github.com/',}
        return sites.get(web, web)
         


try:
    if  len(sys.argv) >1 :
        website = (sys.argv[1]).lower()
        showUrl(Visit_site(website))
    else:
        showUrl('http://google.com')
except:
    print("\nBrowser closed !!!")
    sys.exit()

