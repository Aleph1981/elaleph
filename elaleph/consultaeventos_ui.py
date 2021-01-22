# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaeventos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ConsultaEventos_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1279, 759)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.labelConsulta = QtWidgets.QLabel(Dialog)
        self.labelConsulta.setGeometry(QtCore.QRect(13, 16, 361, 40))
        self.labelConsulta.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.labelConsulta.setObjectName("labelConsulta")
        self.comboYear = QtWidgets.QComboBox(Dialog)
        self.comboYear.setGeometry(QtCore.QRect(14, 64, 138, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboYear.sizePolicy().hasHeightForWidth())
        self.comboYear.setSizePolicy(sizePolicy)
        self.comboYear.setObjectName("comboYear")
        self.comboYear.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(13, 94, 1261, 661))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Consulta de Eventos"))
        self.labelConsulta.setText(_translate("Dialog", "CONSULTA DE EVENTOS"))
        self.comboYear.setItemText(0, _translate("Dialog", "Año"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Id Evento"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Tarea"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Cliente"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Recinto"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Project Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ConsultaEventos_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

