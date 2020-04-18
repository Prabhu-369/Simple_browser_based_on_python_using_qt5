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
        return app.exec_()

def Visit_site(web):
        sites = {'ytb': 'http://youtube.com', 'ggl': 'http://google.com','ghb':'http://github.com/',}
        return sites.get(web, 'http://' + web)
         


try:
    if  len(sys.argv) >1 :
        website = str(sys.argv[1]).lower()
        window_status = showUrl(Visit_site(website)) 
    else:
        window_status = showUrl(Visit_site('ggl'))

    while window_status == 0:
        print("\nOpen new website - Y. Exit - N ?")
        if str(input()).lower() == 'y':
            print("\nEnter new website url Ex - 'example.com'  or for frequent websites like google, youtube, github just type ggl, ytb, ghb")
            website = str(input()).lower()
            window_status = showUrl(Visit_site(website))
        else:
            print("\nClosing browser!")
            break      
finally:
    print("\nBrowser closed !!!")
    sys.exit()

