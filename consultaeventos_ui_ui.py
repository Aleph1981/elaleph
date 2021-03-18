# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaeventos_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 753)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelConsulta = QtWidgets.QLabel(Form)
        self.labelConsulta.setStyleSheet("\n"
"")
        self.labelConsulta.setObjectName("labelConsulta")
        self.verticalLayout.addWidget(self.labelConsulta)
        self.comboYear = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboYear.sizePolicy().hasHeightForWidth())
        self.comboYear.setSizePolicy(sizePolicy)
        self.comboYear.setMinimumSize(QtCore.QSize(120, 22))
        self.comboYear.setObjectName("comboYear")
        self.comboYear.addItem("")
        self.verticalLayout.addWidget(self.comboYear)
        self.tableWidget = QtWidgets.QTableWidget(Form)
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
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelConsulta.setText(_translate("Form", "Consulta de Eventos"))
        self.comboYear.setItemText(0, _translate("Form", "Año"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Id Evento"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tarea"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Cliente"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Recinto"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Project Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

