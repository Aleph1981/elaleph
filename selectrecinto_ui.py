# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recintos_select.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SelectRecinto_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 753)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableRecintos = QtWidgets.QTableWidget(Form)
        self.tableRecintos.setObjectName("tableRecintos")
        self.tableRecintos.setColumnCount(13)
        self.tableRecintos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecintos.setHorizontalHeaderItem(12, item)
        self.verticalLayout.addWidget(self.tableRecintos)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSelect = QtWidgets.QPushButton(Form)
        self.buttonSelect.setObjectName("buttonSelect")
        self.horizontalLayout.addWidget(self.buttonSelect)
        self.buttonAdd = QtWidgets.QPushButton(Form)
        self.buttonAdd.setObjectName("buttonAdd")
        self.horizontalLayout.addWidget(self.buttonAdd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.buttonSelect, self.buttonAdd)
        Form.setTabOrder(self.buttonAdd, self.tableRecintos)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Aleph"))
        self.labelTitle.setText(_translate("Form", "Seleccionar recinto"))
        self.label.setText(_translate("Form", "Buscar:"))
        self.tableRecintos.setSortingEnabled(True)
        item = self.tableRecintos.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Recinto"))
        item = self.tableRecintos.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableRecintos.horizontalHeaderItem(2)
        item.setText(_translate("Form", "País"))
        item = self.tableRecintos.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Provincia"))
        item = self.tableRecintos.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Ciudad"))
        item = self.tableRecintos.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Dirección"))
        item = self.tableRecintos.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Indicaciones"))
        item = self.tableRecintos.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Coordenadas"))
        item = self.tableRecintos.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Contacto"))
        item = self.tableRecintos.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Teléfono"))
        item = self.tableRecintos.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Email"))
        item = self.tableRecintos.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Web"))
        item = self.tableRecintos.horizontalHeaderItem(12)
        item.setText(_translate("Form", "Notas"))
        self.buttonSelect.setText(_translate("Form", "Seleccionar"))
        self.buttonAdd.setText(_translate("Form", "Añadir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SelectRecinto_Ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

