from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import img_editing_module as img_process
import neural_network as nn

#default paths
default_path_img_before = r".\IMGBEFORE.jpg"
default_path_img_after = r".\IMGAFTER.jpg"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # bg color
        bg_color = self.palette()
        bg_color.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                            QtGui.QColor("#464451"))
        self.setPalette(bg_color)
        #
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 1150, 657))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ImageBefore = QtWidgets.QLabel(self.widget)
        self.ImageBefore.setObjectName("ImageBefore")
        self.horizontalLayout.addWidget(self.ImageBefore)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ImageAfter = QtWidgets.QLabel(self.widget)
        self.ImageAfter.setObjectName("ImageAfter")
        self.horizontalLayout.addWidget(self.ImageAfter)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.OpenLabel = QtWidgets.QLabel(self.widget)
        self.OpenLabel.setObjectName("OpenLabel")
        self.horizontalLayout_3.addWidget(self.OpenLabel)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.SaveLabel = QtWidgets.QLabel(self.widget)
        self.SaveLabel.setObjectName("SaveLabel")
        self.horizontalLayout_3.addWidget(self.SaveLabel)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)

        self.OpenFileWindowButton = QtWidgets.QToolButton(self.widget)
        self.OpenFileWindowButton.setObjectName("OpenFileWindowButton")
        self.OpenFileWindowButton.setStyleSheet("background-color: #817DA6")

        self.horizontalLayout_2.addWidget(self.OpenFileWindowButton)
        self.OpenPathEdit = QtWidgets.QLineEdit(self.widget)
        self.OpenPathEdit.setObjectName("OpenPathEdit")
        self.horizontalLayout_2.addWidget(self.OpenPathEdit)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)

        self.CompressButton = QtWidgets.QPushButton(self.widget)
        self.CompressButton.setObjectName("CompressButton")
        self.CompressButton.setStyleSheet("background-color: #817DA6")

        self.horizontalLayout_2.addWidget(self.CompressButton)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)

        self.SaveFileWindowButton = QtWidgets.QToolButton(self.widget)
        self.SaveFileWindowButton.setObjectName("SaveFileWindowButton")
        self.SaveFileWindowButton.setStyleSheet("background-color: #817DA6")

        self.horizontalLayout_2.addWidget(self.SaveFileWindowButton)
        self.SavePathEdit = QtWidgets.QLineEdit(self.widget)
        self.SavePathEdit.setObjectName("SavePathEdit")
        self.horizontalLayout_2.addWidget(self.SavePathEdit)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionoption_1 = QtWidgets.QAction(MainWindow)
        self.actionoption_1.setObjectName("trainMode")
        self.actionAbout_program = QtWidgets.QAction(MainWindow)
        self.actionAbout_program.setObjectName("actionAbout_program")
        self.actionHelp = QtWidgets.QAction(MainWindow)#
        self.actionHelp.setObjectName("actionHelp")#
        self.menuOptions.addAction(self.actionoption_1)
        #self.menuOptions.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuHelp.addAction(self.actionAbout_program)
        self.menuHelp.addAction(self.actionHelp)#
        self.menubar.addAction(self.menuHelp.menuAction())

        #self.menubar.addAction(self.actionoption_1.menuAction())
        self.boolTrain = False
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #connect!!!
        self.OpenFileWindowButton.clicked.connect(self.OpenFileDialog)
        self.SaveFileWindowButton.clicked.connect(self.SaveFileDialog)
        self.CompressButton.clicked.connect(self.Compress)
        self.actionAbout_program.triggered.connect(self.AboutBar)
        self.actionHelp.triggered.connect(self.HelbBar)
        self.actionoption_1.triggered.connect(self.TrainOnOff)
        #connect!!!

    def TrainOnOff(self):
        self.boolTrain = not self.boolTrain
        if self.boolTrain:
            print("Neural net train mode: on")
            self.CompressButton.setText("Train and compress")
        else:
            print("Neural net train mode: off")
            self.CompressButton.setText("Compress")

    def AboutBar(self):
        QtWidgets.QMessageBox.critical(self, 'About programm',
                                       "Autor: Vasilchenko Alexandr, student of 484 group, STPGTI(TU).\
                                       \nCourse work on the topic \"Adaptive compress of images with neural network\" \
                                       \n\nThis programm can adaptively compress 500x500 jpeg images,\
                                       \nusing already trained neural network", QtWidgets.QMessageBox.Ok)

    def HelbBar(self):
        QtWidgets.QMessageBox.critical(self, 'Help',
                                       "To get support: alexidest@gmail.com", QtWidgets.QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ImageBefore.setPixmap(QPixmap(default_path_img_before)) #заменить на дефолтные из папки
        self.ImageAfter.setPixmap(QPixmap(default_path_img_after))
        self.OpenLabel.setText(_translate("MainWindow", "Open file to compress"))
        self.SaveLabel.setText(_translate("MainWindow", "Save compressed file as"))
        self.OpenFileWindowButton.setText(_translate("MainWindow", "..."))
        self.CompressButton.setText(_translate("MainWindow", "Compress"))
        self.SaveFileWindowButton.setText(_translate("MainWindow", "..."))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionAbout_program.setText(_translate("MainWindow", "About program"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionoption_1.setText(_translate("MainWindow", "On/Off train mode"))

    def OpenFileDialog(self):
        print('OpenFileDialog open')
        PathToFile = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "", "Images (*.jpeg *.jpg);")[0]
        if img_process.verify_open_path(PathToFile):
            print("path is ", PathToFile)
            self.OpenPathEdit.setText(PathToFile)
            self.ImageBefore.setPixmap(QPixmap(PathToFile))
            #path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

    def SaveFileDialog(self):
        print("SaveFileDialog open")
        PathToFile = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", "", "Image (*.jpeg *jpg);")[0]
        print("path is ", PathToFile)
        self.SavePathEdit.setText(PathToFile)

    def Compress(self):
        if img_process.verify_open_path(self.OpenPathEdit.text() and self.OpenPathEdit.text() != ''):
            if self.boolTrain:
                weights = nn.train_mode()
            else:
                weights = nn.get_default_weights()
            img_before_code = nn.get_input_for_analyse(self.OpenPathEdit.text())
            ratio_vector = nn.analyse_by_nn(img_before_code, weights[0], weights[1]) #input, weight0, weight1
            compress_lvl = nn.get_compress_ratio(ratio_vector)
            print("compress lvl: ", compress_lvl)
            print("path to open file is correct")
            img_process.compress_image(self.OpenPathEdit.text(), self.SavePathEdit.text(), compress_lvl)
            self.ImageAfter.setPixmap(QPixmap(self.SavePathEdit.text()))
        else:
            print("incorrect open path")
        #nn.clear_temp()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())