# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MegaDashboard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../figs/AssinaturaPython-2022.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 291, 221))
        self.frame.setStyleSheet("background-color: rgb(213, 235, 151);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(310, 10, 291, 221))
        self.frame_2.setStyleSheet("background-color: rgb(213, 235, 151);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 250, 291, 221))
        self.frame_3.setStyleSheet("background-color: rgb(213, 235, 151);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_3)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(310, 250, 291, 221))
        self.frame_4.setStyleSheet("background-color: rgb(213, 235, 151);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView_4.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(609, 9, 201, 461))
        self.frame_5.setStyleSheet("background-color: rgb(213, 235, 151);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 20))
        self.label.setStyleSheet("font: 700 12pt \"Dark Crystal Outline\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Programa Mega Sena"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

