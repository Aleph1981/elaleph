# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectmanagers_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ProjectManagers_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1186, 550)
        self.tableManagers = QtWidgets.QTableWidget(Dialog)
        self.tableManagers.setGeometry(QtCore.QRect(40, 90, 761, 391))
        self.tableManagers.setObjectName("tableManagers")
        self.tableManagers.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableManagers.setItem(0, 6, item)
        self.labelProject = QtWidgets.QLabel(Dialog)
        self.labelProject.setGeometry(QtCore.QRect(40, 30, 181, 31))
        self.labelProject.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelProject.setObjectName("labelProject")
        self.buttonAnadir = QtWidgets.QPushButton(Dialog)
        self.buttonAnadir.setGeometry(QtCore.QRect(890, 340, 93, 28))
        self.buttonAnadir.setObjectName("buttonAnadir")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(830, 93, 317, 241))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelNombre = QtWidgets.QLabel(self.widget)
        self.labelNombre.setObjectName("labelNombre")
        self.gridLayout.addWidget(self.labelNombre, 0, 0, 1, 2)
        self.inputNombre = QtWidgets.QLineEdit(self.widget)
        self.inputNombre.setObjectName("inputNombre")
        self.gridLayout.addWidget(self.inputNombre, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.labelApellidos = QtWidgets.QLabel(self.widget)
        self.labelApellidos.setObjectName("labelApellidos")
        self.gridLayout.addWidget(self.labelApellidos, 1, 0, 1, 2)
        self.inputApellidos = QtWidgets.QLineEdit(self.widget)
        self.inputApellidos.setObjectName("inputApellidos")
        self.gridLayout.addWidget(self.inputApellidos, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.labelTelefono = QtWidgets.QLabel(self.widget)
        self.labelTelefono.setObjectName("labelTelefono")
        self.gridLayout.addWidget(self.labelTelefono, 2, 0, 1, 2)
        self.inputTelefono = QtWidgets.QLineEdit(self.widget)
        self.inputTelefono.setObjectName("inputTelefono")
        self.gridLayout.addWidget(self.inputTelefono, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.labelDni = QtWidgets.QLabel(self.widget)
        self.labelDni.setObjectName("labelDni")
        self.gridLayout.addWidget(self.labelDni, 3, 0, 1, 1)
        self.inputDni = QtWidgets.QLineEdit(self.widget)
        self.inputDni.setObjectName("inputDni")
        self.gridLayout.addWidget(self.inputDni, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        self.labelEmail = QtWidgets.QLabel(self.widget)
        self.labelEmail.setObjectName("labelEmail")
        self.gridLayout.addWidget(self.labelEmail, 4, 0, 1, 1)
        self.inputEmail = QtWidgets.QLineEdit(self.widget)
        self.inputEmail.setObjectName("inputEmail")
        self.gridLayout.addWidget(self.inputEmail, 4, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 3, 1, 1)
        self.labelNotas = QtWidgets.QLabel(self.widget)
        self.labelNotas.setObjectName("labelNotas")
        self.gridLayout.addWidget(self.labelNotas, 5, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 101, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 1, 2, 1)
        self.inputNotas = QtWidgets.QPlainTextEdit(self.widget)
        self.inputNotas.setObjectName("inputNotas")
        self.gridLayout.addWidget(self.inputNotas, 5, 2, 2, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(40, 490, 241, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonGuardar = QtWidgets.QPushButton(self.widget1)
        self.buttonGuardar.setObjectName("buttonGuardar")
        self.horizontalLayout.addWidget(self.buttonGuardar)
        self.buttonEliminar = QtWidgets.QPushButton(self.widget1)
        self.buttonEliminar.setObjectName("buttonEliminar")
        self.horizontalLayout.addWidget(self.buttonEliminar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableManagers.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableManagers.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nombre"))
        item = self.tableManagers.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Apellidos"))
        item = self.tableManagers.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Teléfono"))
        item = self.tableManagers.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Email"))
        item = self.tableManagers.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "DNI"))
        item = self.tableManagers.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Notas"))
        __sortingEnabled = self.tableManagers.isSortingEnabled()
        self.tableManagers.setSortingEnabled(False)
        self.tableManagers.setSortingEnabled(__sortingEnabled)
        self.labelProject.setText(_translate("Dialog", "Project Managers"))
        self.buttonAnadir.setText(_translate("Dialog", "Añadir"))
        self.labelNombre.setText(_translate("Dialog", "Nombre"))
        self.labelApellidos.setText(_translate("Dialog", "Apellidos"))
        self.labelTelefono.setText(_translate("Dialog", "Teléfono"))
        self.labelDni.setText(_translate("Dialog", "DNI"))
        self.labelEmail.setText(_translate("Dialog", "Email"))
        self.labelNotas.setText(_translate("Dialog", "Notas"))
        self.buttonGuardar.setText(_translate("Dialog", "Guardar cambios"))
        self.buttonEliminar.setText(_translate("Dialog", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ProjectManagers_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

