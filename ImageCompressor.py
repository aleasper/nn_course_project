from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui_module import Ui_MainWindow
import sys

class main_window(QMainWindow, Ui_MainWindow):
   def __init__(self):
      QMainWindow.__init__(self)
      self.setupUi(self)

app = QApplication(sys.argv)
main = main_window()
main.show()
sys.exit(app.exec_())