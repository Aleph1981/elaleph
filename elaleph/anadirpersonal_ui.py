# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anadirpersonal_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AnadirPersonal_Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(210, 210, 210);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.aceptcancel = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.aceptcancel.setGeometry(QtCore.QRect(150, 540, 193, 28))
        self.aceptcancel.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.aceptcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.aceptcancel.setObjectName("aceptcancel")
        self.anadirperso = QtWidgets.QLabel(self.centralwidget)
        self.anadirperso.setGeometry(QtCore.QRect(80, 40, 231, 61))
        self.anadirperso.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.anadirperso.setObjectName("anadirperso")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(82, 125, 310, 305))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nombre = QtWidgets.QLabel(self.layoutWidget)
        self.nombre.setObjectName("nombre")
        self.horizontalLayout_2.addWidget(self.nombre)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.entryNOMBRE = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryNOMBRE.setMinimumSize(QtCore.QSize(200, 0))
        self.entryNOMBRE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryNOMBRE.setText("")
        self.entryNOMBRE.setObjectName("entryNOMBRE")
        self.horizontalLayout_2.addWidget(self.entryNOMBRE)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.apellidos = QtWidgets.QLabel(self.layoutWidget)
        self.apellidos.setObjectName("apellidos")
        self.horizontalLayout_3.addWidget(self.apellidos)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.entryAPELL = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryAPELL.setMinimumSize(QtCore.QSize(200, 0))
        self.entryAPELL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryAPELL.setObjectName("entryAPELL")
        self.horizontalLayout_3.addWidget(self.entryAPELL)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dni = QtWidgets.QLabel(self.layoutWidget)
        self.dni.setObjectName("dni")
        self.horizontalLayout_4.addWidget(self.dni)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.entryDNI = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryDNI.setMinimumSize(QtCore.QSize(200, 0))
        self.entryDNI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryDNI.setObjectName("entryDNI")
        self.horizontalLayout_4.addWidget(self.entryDNI)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.telefono = QtWidgets.QLabel(self.layoutWidget)
        self.telefono.setObjectName("telefono")
        self.horizontalLayout_5.addWidget(self.telefono)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.entryTFN = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryTFN.setMinimumSize(QtCore.QSize(200, 0))
        self.entryTFN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryTFN.setObjectName("entryTFN")
        self.horizontalLayout_5.addWidget(self.entryTFN)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.email = QtWidgets.QLabel(self.layoutWidget)
        self.email.setObjectName("email")
        self.horizontalLayout_6.addWidget(self.email)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.entryEMAIL = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryEMAIL.setMinimumSize(QtCore.QSize(200, 0))
        self.entryEMAIL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryEMAIL.setObjectName("entryEMAIL")
        self.horizontalLayout_6.addWidget(self.entryEMAIL)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.direccion = QtWidgets.QLabel(self.layoutWidget)
        self.direccion.setObjectName("direccion")
        self.horizontalLayout_7.addWidget(self.direccion)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.entryDIRECCION = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryDIRECCION.setMinimumSize(QtCore.QSize(200, 0))
        self.entryDIRECCION.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryDIRECCION.setText("")
        self.entryDIRECCION.setObjectName("entryDIRECCION")
        self.horizontalLayout_7.addWidget(self.entryDIRECCION)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cp = QtWidgets.QLabel(self.layoutWidget)
        self.cp.setObjectName("cp")
        self.horizontalLayout_8.addWidget(self.cp)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.entryCP = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryCP.setMinimumSize(QtCore.QSize(200, 0))
        self.entryCP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryCP.setText("")
        self.entryCP.setObjectName("entryCP")
        self.horizontalLayout_8.addWidget(self.entryCP)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ciudad = QtWidgets.QLabel(self.layoutWidget)
        self.ciudad.setObjectName("ciudad")
        self.horizontalLayout_9.addWidget(self.ciudad)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.entryCIUDAD = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryCIUDAD.setMinimumSize(QtCore.QSize(200, 0))
        self.entryCIUDAD.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryCIUDAD.setText("")
        self.entryCIUDAD.setObjectName("entryCIUDAD")
        self.horizontalLayout_9.addWidget(self.entryCIUDAD)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.iban = QtWidgets.QLabel(self.layoutWidget)
        self.iban.setObjectName("iban")
        self.horizontalLayout_10.addWidget(self.iban)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.entryIBAN = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryIBAN.setMinimumSize(QtCore.QSize(200, 0))
        self.entryIBAN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryIBAN.setObjectName("entryIBAN")
        self.horizontalLayout_10.addWidget(self.entryIBAN)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.autonomo = QtWidgets.QLabel(self.layoutWidget)
        self.autonomo.setStyleSheet("")
        self.autonomo.setObjectName("autonomo")
        self.horizontalLayout_11.addWidget(self.autonomo)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioSI = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioSI.setObjectName("radioSI")
        self.horizontalLayout.addWidget(self.radioSI)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.radioNO = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioNO.setObjectName("radioNO")
        self.horizontalLayout.addWidget(self.radioNO)
        self.horizontalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 440, 311, 89))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.notas_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.notas_2.setObjectName("notas_2")
        self.verticalLayout_2.addWidget(self.notas_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.textNOTAS = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textNOTAS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textNOTAS.setObjectName("textNOTAS")
        self.horizontalLayout_12.addWidget(self.textNOTAS)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(490, 130, 280, 451))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.entryNOMBRE, self.entryAPELL)
        MainWindow.setTabOrder(self.entryAPELL, self.entryDNI)
        MainWindow.setTabOrder(self.entryDNI, self.entryTFN)
        MainWindow.setTabOrder(self.entryTFN, self.entryEMAIL)
        MainWindow.setTabOrder(self.entryEMAIL, self.entryDIRECCION)
        MainWindow.setTabOrder(self.entryDIRECCION, self.entryCP)
        MainWindow.setTabOrder(self.entryCP, self.entryCIUDAD)
        MainWindow.setTabOrder(self.entryCIUDAD, self.entryIBAN)
        MainWindow.setTabOrder(self.entryIBAN, self.radioSI)
        MainWindow.setTabOrder(self.radioSI, self.radioNO)
        MainWindow.setTabOrder(self.radioNO, self.textNOTAS)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.anadirperso.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">AÑADIR PERSONAL</p></body></html>"))
        self.nombre.setText(_translate("MainWindow", "Nombre"))
        self.apellidos.setText(_translate("MainWindow", "Apellidos"))
        self.dni.setText(_translate("MainWindow", "DNI"))
        self.telefono.setText(_translate("MainWindow", "Teléfono"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.direccion.setText(_translate("MainWindow", "Dirección"))
        self.cp.setText(_translate("MainWindow", "C.P."))
        self.ciudad.setText(_translate("MainWindow", "Ciudad"))
        self.iban.setText(_translate("MainWindow", "IBAN"))
        self.autonomo.setText(_translate("MainWindow", "Autónomo"))
        self.radioSI.setText(_translate("MainWindow", "Sí"))
        self.radioNO.setText(_translate("MainWindow", "No"))
        self.notas_2.setText(_translate("MainWindow", "Notas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AnadirPersonal_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
