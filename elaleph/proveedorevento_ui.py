# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proveedorevento_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ProveedorEvento_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(458, 624)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 100, 301, 378))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNotas = QtWidgets.QLabel(self.layoutWidget)
        self.labelNotas.setObjectName("labelNotas")
        self.verticalLayout.addWidget(self.labelNotas)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 9, 0, 1, 1)
        self.inputEmpresa = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputEmpresa.setEnabled(False)
        self.inputEmpresa.setObjectName("inputEmpresa")
        self.gridLayout.addWidget(self.inputEmpresa, 1, 2, 1, 1)
        self.labelContacto = QtWidgets.QLabel(self.layoutWidget)
        self.labelContacto.setObjectName("labelContacto")
        self.gridLayout.addWidget(self.labelContacto, 4, 0, 1, 1)
        self.comboServicio = QtWidgets.QComboBox(self.layoutWidget)
        self.comboServicio.setObjectName("comboServicio")
        self.gridLayout.addWidget(self.comboServicio, 2, 2, 1, 1)
        self.inputContacto = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputContacto.setObjectName("inputContacto")
        self.gridLayout.addWidget(self.inputContacto, 4, 2, 1, 1)
        self.inputFecha = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputFecha.setEnabled(False)
        self.inputFecha.setObjectName("inputFecha")
        self.gridLayout.addWidget(self.inputFecha, 3, 2, 1, 1)
        self.labelFecha = QtWidgets.QLabel(self.layoutWidget)
        self.labelFecha.setObjectName("labelFecha")
        self.gridLayout.addWidget(self.labelFecha, 3, 0, 1, 1)
        self.labelNombre = QtWidgets.QLabel(self.layoutWidget)
        self.labelNombre.setObjectName("labelNombre")
        self.gridLayout.addWidget(self.labelNombre, 1, 0, 1, 1)
        self.labelCodigo = QtWidgets.QLabel(self.layoutWidget)
        self.labelCodigo.setObjectName("labelCodigo")
        self.gridLayout.addWidget(self.labelCodigo, 0, 0, 1, 1)
        self.inputCodigo = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputCodigo.setEnabled(False)
        self.inputCodigo.setObjectName("inputCodigo")
        self.gridLayout.addWidget(self.inputCodigo, 0, 2, 1, 1)
        self.labelCargo = QtWidgets.QLabel(self.layoutWidget)
        self.labelCargo.setObjectName("labelCargo")
        self.gridLayout.addWidget(self.labelCargo, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 9, 1, 1, 1)
        self.labelEmail = QtWidgets.QLabel(self.layoutWidget)
        self.labelEmail.setObjectName("labelEmail")
        self.gridLayout.addWidget(self.labelEmail, 6, 0, 1, 1)
        self.labelTelefono = QtWidgets.QLabel(self.layoutWidget)
        self.labelTelefono.setObjectName("labelTelefono")
        self.gridLayout.addWidget(self.labelTelefono, 5, 0, 1, 1)
        self.inputNotas = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.inputNotas.setObjectName("inputNotas")
        self.gridLayout.addWidget(self.inputNotas, 9, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 1, 1, 1)
        self.inputTelefono = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputTelefono.setObjectName("inputTelefono")
        self.gridLayout.addWidget(self.inputTelefono, 5, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 1, 1, 1)
        self.inputEmail = QtWidgets.QLineEdit(self.layoutWidget)
        self.inputEmail.setObjectName("inputEmail")
        self.gridLayout.addWidget(self.inputEmail, 6, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 510, 231, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonGuardar = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonGuardar.setObjectName("buttonGuardar")
        self.horizontalLayout.addWidget(self.buttonGuardar)
        self.buttonCancelar = QtWidgets.QPushButton(self.layoutWidget1)
        self.buttonCancelar.setObjectName("buttonCancelar")
        self.horizontalLayout.addWidget(self.buttonCancelar)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 50, 341, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelProject = QtWidgets.QLabel(self.widget)
        self.labelProject.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelProject.setObjectName("labelProject")
        self.horizontalLayout_2.addWidget(self.labelProject)
        self.inputEvento = QtWidgets.QLineEdit(self.widget)
        self.inputEvento.setEnabled(False)
        self.inputEvento.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.inputEvento.setText("")
        self.inputEvento.setObjectName("inputEvento")
        self.horizontalLayout_2.addWidget(self.inputEvento)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboServicio, self.inputContacto)
        Dialog.setTabOrder(self.inputContacto, self.inputTelefono)
        Dialog.setTabOrder(self.inputTelefono, self.inputEmail)
        Dialog.setTabOrder(self.inputEmail, self.inputNotas)
        Dialog.setTabOrder(self.inputNotas, self.buttonGuardar)
        Dialog.setTabOrder(self.buttonGuardar, self.buttonCancelar)
        Dialog.setTabOrder(self.buttonCancelar, self.inputEvento)
        Dialog.setTabOrder(self.inputEvento, self.inputCodigo)
        Dialog.setTabOrder(self.inputCodigo, self.inputEmpresa)
        Dialog.setTabOrder(self.inputEmpresa, self.inputFecha)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelNotas.setText(_translate("Dialog", "Notas"))
        self.labelContacto.setText(_translate("Dialog", "Contacto\n"
"On-site"))
        self.labelFecha.setText(_translate("Dialog", "Fecha"))
        self.labelNombre.setText(_translate("Dialog", "Empresa"))
        self.labelCodigo.setText(_translate("Dialog", "Código"))
        self.labelCargo.setText(_translate("Dialog", "Servicio"))
        self.labelEmail.setText(_translate("Dialog", "Email\n"
"On-site"))
        self.labelTelefono.setText(_translate("Dialog", "Teléfono\n"
"On-site"))
        self.buttonGuardar.setText(_translate("Dialog", "Aceptar"))
        self.buttonCancelar.setText(_translate("Dialog", "Cancelar"))
        self.labelProject.setText(_translate("Dialog", "Proveedor del evento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ProveedorEvento_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

