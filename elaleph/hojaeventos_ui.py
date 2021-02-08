# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hojaeventos_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class HojaRuta_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 528)
        self.comboAnyo = QtWidgets.QComboBox(Dialog)
        self.comboAnyo.setGeometry(QtCore.QRect(30, 100, 91, 22))
        self.comboAnyo.setObjectName("comboAnyo")
        self.labelAnyo = QtWidgets.QLabel(Dialog)
        self.labelAnyo.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.labelAnyo.setObjectName("labelAnyo")
        self.comboMes = QtWidgets.QComboBox(Dialog)
        self.comboMes.setGeometry(QtCore.QRect(30, 180, 141, 22))
        self.comboMes.setObjectName("comboMes")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.labelMes = QtWidgets.QLabel(Dialog)
        self.labelMes.setGeometry(QtCore.QRect(30, 160, 55, 16))
        self.labelMes.setObjectName("labelMes")
        self.tableEventos = QtWidgets.QTableWidget(Dialog)
        self.tableEventos.setGeometry(QtCore.QRect(210, 100, 301, 381))
        self.tableEventos.setObjectName("tableEventos")
        self.tableEventos.setColumnCount(0)
        self.tableEventos.setRowCount(0)
        self.labelEventos = QtWidgets.QLabel(Dialog)
        self.labelEventos.setGeometry(QtCore.QRect(210, 80, 55, 16))
        self.labelEventos.setObjectName("labelEventos")
        self.labelHoja = QtWidgets.QLabel(Dialog)
        self.labelHoja.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.labelHoja.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.labelHoja.setObjectName("labelHoja")
        self.buttonCrear = QtWidgets.QPushButton(Dialog)
        self.buttonCrear.setGeometry(QtCore.QRect(30, 440, 121, 41))
        self.buttonCrear.setObjectName("buttonCrear")
        self.labelCrear = QtWidgets.QLabel(Dialog)
        self.labelCrear.setGeometry(QtCore.QRect(30, 420, 131, 16))
        self.labelCrear.setObjectName("labelCrear")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelAnyo.setText(_translate("Dialog", "Año:"))
        self.comboMes.setItemText(0, _translate("Dialog", "Enero"))
        self.comboMes.setItemText(1, _translate("Dialog", "Febrero"))
        self.comboMes.setItemText(2, _translate("Dialog", "Marzo"))
        self.comboMes.setItemText(3, _translate("Dialog", "Abril"))
        self.comboMes.setItemText(4, _translate("Dialog", "Mayo"))
        self.comboMes.setItemText(5, _translate("Dialog", "Junio"))
        self.comboMes.setItemText(6, _translate("Dialog", "Julio"))
        self.comboMes.setItemText(7, _translate("Dialog", "Agosto"))
        self.comboMes.setItemText(8, _translate("Dialog", "Septiembre"))
        self.comboMes.setItemText(9, _translate("Dialog", "Octubre"))
        self.comboMes.setItemText(10, _translate("Dialog", "Noviembre"))
        self.comboMes.setItemText(11, _translate("Dialog", "Diciembre"))
        self.labelMes.setText(_translate("Dialog", "Mes:"))
        self.tableEventos.setSortingEnabled(True)
        self.labelEventos.setText(_translate("Dialog", "Eventos:"))
        self.labelHoja.setText(_translate("Dialog", "Hoja de ruta"))
        self.buttonCrear.setText(_translate("Dialog", "Crear"))
        self.labelCrear.setText(_translate("Dialog", "Crear hoja de ruta:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = HojaRuta_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

