# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anadirpersonalwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AnadirPersonal_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1239, 837)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.entryTFN = QtWidgets.QLineEdit(Form)
        self.entryTFN.setMinimumSize(QtCore.QSize(200, 22))
        self.entryTFN.setObjectName("entryTFN")
        self.gridLayout.addWidget(self.entryTFN, 3, 2, 1, 4)
        self.email = QtWidgets.QLabel(Form)
        self.email.setMinimumSize(QtCore.QSize(75, 22))
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 4, 0, 1, 2)
        self.dni = QtWidgets.QLabel(Form)
        self.dni.setMinimumSize(QtCore.QSize(75, 22))
        self.dni.setObjectName("dni")
        self.gridLayout.addWidget(self.dni, 2, 0, 1, 2)
        self.entryNOMBRE = QtWidgets.QLineEdit(Form)
        self.entryNOMBRE.setMinimumSize(QtCore.QSize(200, 22))
        self.entryNOMBRE.setText("")
        self.entryNOMBRE.setObjectName("entryNOMBRE")
        self.gridLayout.addWidget(self.entryNOMBRE, 0, 2, 1, 4)
        self.entryEMAIL = QtWidgets.QLineEdit(Form)
        self.entryEMAIL.setMinimumSize(QtCore.QSize(200, 22))
        self.entryEMAIL.setObjectName("entryEMAIL")
        self.gridLayout.addWidget(self.entryEMAIL, 4, 2, 1, 4)
        self.direccion = QtWidgets.QLabel(Form)
        self.direccion.setMinimumSize(QtCore.QSize(75, 22))
        self.direccion.setObjectName("direccion")
        self.gridLayout.addWidget(self.direccion, 5, 0, 1, 2)
        self.apellidos = QtWidgets.QLabel(Form)
        self.apellidos.setMinimumSize(QtCore.QSize(75, 22))
        self.apellidos.setObjectName("apellidos")
        self.gridLayout.addWidget(self.apellidos, 1, 0, 1, 2)
        self.nombre = QtWidgets.QLabel(Form)
        self.nombre.setMinimumSize(QtCore.QSize(75, 22))
        self.nombre.setObjectName("nombre")
        self.gridLayout.addWidget(self.nombre, 0, 0, 1, 2)
        self.entryAPELL = QtWidgets.QLineEdit(Form)
        self.entryAPELL.setMinimumSize(QtCore.QSize(200, 22))
        self.entryAPELL.setObjectName("entryAPELL")
        self.gridLayout.addWidget(self.entryAPELL, 1, 2, 1, 4)
        self.entryDNI = QtWidgets.QLineEdit(Form)
        self.entryDNI.setMinimumSize(QtCore.QSize(200, 22))
        self.entryDNI.setObjectName("entryDNI")
        self.gridLayout.addWidget(self.entryDNI, 2, 2, 1, 4)
        self.telefono = QtWidgets.QLabel(Form)
        self.telefono.setMinimumSize(QtCore.QSize(75, 22))
        self.telefono.setObjectName("telefono")
        self.gridLayout.addWidget(self.telefono, 3, 0, 1, 2)
        self.entryDIRECCION = QtWidgets.QLineEdit(Form)
        self.entryDIRECCION.setMinimumSize(QtCore.QSize(200, 22))
        self.entryDIRECCION.setText("")
        self.entryDIRECCION.setObjectName("entryDIRECCION")
        self.gridLayout.addWidget(self.entryDIRECCION, 5, 2, 1, 4)
        self.cp = QtWidgets.QLabel(Form)
        self.cp.setMinimumSize(QtCore.QSize(75, 22))
        self.cp.setObjectName("cp")
        self.gridLayout.addWidget(self.cp, 6, 0, 1, 2)
        self.entryCP = QtWidgets.QLineEdit(Form)
        self.entryCP.setMinimumSize(QtCore.QSize(200, 22))
        self.entryCP.setText("")
        self.entryCP.setObjectName("entryCP")
        self.gridLayout.addWidget(self.entryCP, 6, 2, 1, 4)
        self.iban = QtWidgets.QLabel(Form)
        self.iban.setMinimumSize(QtCore.QSize(75, 22))
        self.iban.setObjectName("iban")
        self.gridLayout.addWidget(self.iban, 8, 0, 1, 2)
        self.entryIBAN = QtWidgets.QLineEdit(Form)
        self.entryIBAN.setMinimumSize(QtCore.QSize(200, 22))
        self.entryIBAN.setObjectName("entryIBAN")
        self.gridLayout.addWidget(self.entryIBAN, 8, 2, 1, 4)
        self.radioNO = QtWidgets.QRadioButton(Form)
        self.radioNO.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.radioNO.setObjectName("radioNO")
        self.gridLayout.addWidget(self.radioNO, 9, 5, 1, 1)
        self.entryCIUDAD = QtWidgets.QLineEdit(Form)
        self.entryCIUDAD.setMinimumSize(QtCore.QSize(200, 22))
        self.entryCIUDAD.setText("")
        self.entryCIUDAD.setObjectName("entryCIUDAD")
        self.gridLayout.addWidget(self.entryCIUDAD, 7, 2, 1, 4)
        self.radioSI = QtWidgets.QRadioButton(Form)
        self.radioSI.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.radioSI.setObjectName("radioSI")
        self.gridLayout.addWidget(self.radioSI, 9, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 9, 1, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.notas_2 = QtWidgets.QLabel(Form)
        self.notas_2.setMinimumSize(QtCore.QSize(75, 22))
        self.notas_2.setObjectName("notas_2")
        self.verticalLayout_2.addWidget(self.notas_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_2, 10, 0, 1, 2)
        self.ciudad = QtWidgets.QLabel(Form)
        self.ciudad.setMinimumSize(QtCore.QSize(75, 22))
        self.ciudad.setObjectName("ciudad")
        self.gridLayout.addWidget(self.ciudad, 7, 0, 1, 2)
        self.autonomo = QtWidgets.QLabel(Form)
        self.autonomo.setMinimumSize(QtCore.QSize(75, 22))
        self.autonomo.setStyleSheet("")
        self.autonomo.setObjectName("autonomo")
        self.gridLayout.addWidget(self.autonomo, 9, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 9, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 9, 6, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 11, 2, 1, 1)
        self.textNOTAS = QtWidgets.QPlainTextEdit(Form)
        self.textNOTAS.setObjectName("textNOTAS")
        self.gridLayout.addWidget(self.textNOTAS, 10, 2, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.buttonAceptar = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAceptar.sizePolicy().hasHeightForWidth())
        self.buttonAceptar.setSizePolicy(sizePolicy)
        self.buttonAceptar.setObjectName("buttonAceptar")
        self.horizontalLayout_2.addWidget(self.buttonAceptar)
        self.buttonCancelar = QtWidgets.QPushButton(Form)
        self.buttonCancelar.setObjectName("buttonCancelar")
        self.horizontalLayout_2.addWidget(self.buttonCancelar)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(275, 450))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.entryNOMBRE, self.entryAPELL)
        Form.setTabOrder(self.entryAPELL, self.entryDNI)
        Form.setTabOrder(self.entryDNI, self.entryTFN)
        Form.setTabOrder(self.entryTFN, self.entryEMAIL)
        Form.setTabOrder(self.entryEMAIL, self.entryDIRECCION)
        Form.setTabOrder(self.entryDIRECCION, self.entryCP)
        Form.setTabOrder(self.entryCP, self.entryCIUDAD)
        Form.setTabOrder(self.entryCIUDAD, self.entryIBAN)
        Form.setTabOrder(self.entryIBAN, self.radioSI)
        Form.setTabOrder(self.radioSI, self.radioNO)
        Form.setTabOrder(self.radioNO, self.buttonAceptar)
        Form.setTabOrder(self.buttonAceptar, self.buttonCancelar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitle.setText(_translate("Form", "<html><head/><body><p>AÑADIR PERSONAL</p></body></html>"))
        self.email.setText(_translate("Form", "Email"))
        self.dni.setText(_translate("Form", "DNI"))
        self.direccion.setText(_translate("Form", "Dirección"))
        self.apellidos.setText(_translate("Form", "Apellidos"))
        self.nombre.setText(_translate("Form", "Nombre"))
        self.telefono.setText(_translate("Form", "Teléfono"))
        self.cp.setText(_translate("Form", "C.P."))
        self.iban.setText(_translate("Form", "IBAN"))
        self.radioNO.setText(_translate("Form", "No"))
        self.radioSI.setText(_translate("Form", "Sí"))
        self.notas_2.setText(_translate("Form", "Notas"))
        self.ciudad.setText(_translate("Form", "Ciudad"))
        self.autonomo.setText(_translate("Form", "Autónomo"))
        self.buttonAceptar.setText(_translate("Form", "Aceptar"))
        self.buttonCancelar.setText(_translate("Form", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = AnadirPersonal_Ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

