# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hojadebolos_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class HojaBolos_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 528)
        self.comboAnyo = QtWidgets.QComboBox(Dialog)
        self.comboAnyo.setGeometry(QtCore.QRect(30, 100, 91, 22))
        self.comboAnyo.setObjectName("comboAnyo")
        self.labelAnyo = QtWidgets.QLabel(Dialog)
        self.labelAnyo.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.labelAnyo.setObjectName("labelAnyo")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 180, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.labelMes = QtWidgets.QLabel(Dialog)
        self.labelMes.setGeometry(QtCore.QRect(30, 160, 55, 16))
        self.labelMes.setObjectName("labelMes")
        self.tablePersonal = QtWidgets.QTableWidget(Dialog)
        self.tablePersonal.setGeometry(QtCore.QRect(210, 100, 301, 381))
        self.tablePersonal.setObjectName("tablePersonal")
        self.tablePersonal.setColumnCount(0)
        self.tablePersonal.setRowCount(0)
        self.labelPersonal = QtWidgets.QLabel(Dialog)
        self.labelPersonal.setGeometry(QtCore.QRect(210, 80, 55, 16))
        self.labelPersonal.setObjectName("labelPersonal")
        self.buttoCrearIndi = QtWidgets.QPushButton(Dialog)
        self.buttoCrearIndi.setGeometry(QtCore.QRect(30, 350, 121, 41))
        self.buttoCrearIndi.setObjectName("buttoCrearIndi")
        self.labelHoja = QtWidgets.QLabel(Dialog)
        self.labelHoja.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.labelHoja.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.labelHoja.setObjectName("labelHoja")
        self.buttoCrearMulti = QtWidgets.QPushButton(Dialog)
        self.buttoCrearMulti.setGeometry(QtCore.QRect(30, 440, 121, 41))
        self.buttoCrearMulti.setObjectName("buttoCrearMulti")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 330, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 420, 131, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelAnyo.setText(_translate("Dialog", "Año"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Enero"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Febrero"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Marzo"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Abril"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Mayo"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "Junio"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "Julio"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "Agosto"))
        self.comboBox_2.setItemText(8, _translate("Dialog", "Septiembre"))
        self.comboBox_2.setItemText(9, _translate("Dialog", "Octubre"))
        self.comboBox_2.setItemText(10, _translate("Dialog", "Noviembre"))
        self.comboBox_2.setItemText(11, _translate("Dialog", "Diciembre"))
        self.labelMes.setText(_translate("Dialog", "Mes"))
        self.tablePersonal.setSortingEnabled(True)
        self.labelPersonal.setText(_translate("Dialog", "Personal"))
        self.buttoCrearIndi.setText(_translate("Dialog", "Crear hoja"))
        self.labelHoja.setText(_translate("Dialog", "Hoja de bolos"))
        self.buttoCrearMulti.setText(_translate("Dialog", "Crear hojas"))
        self.label.setText(_translate("Dialog", "Crear hoja individual"))
        self.label_2.setText(_translate("Dialog", "Crear todas las hojas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = HojaBolos_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

