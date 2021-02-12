# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaproveedor_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ConsultaProveedor_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 753)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(Form)
        self.labelTitle.setStyleSheet("")
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAdd = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAdd.sizePolicy().hasHeightForWidth())
        self.buttonAdd.setSizePolicy(sizePolicy)
        self.buttonAdd.setObjectName("buttonAdd")
        self.horizontalLayout.addWidget(self.buttonAdd)
        self.buttonDel = QtWidgets.QPushButton(Form)
        self.buttonDel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDel.sizePolicy().hasHeightForWidth())
        self.buttonDel.setSizePolicy(sizePolicy)
        self.buttonDel.setObjectName("buttonDel")
        self.horizontalLayout.addWidget(self.buttonDel)
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboFiltro = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFiltro.sizePolicy().hasHeightForWidth())
        self.comboFiltro.setSizePolicy(sizePolicy)
        self.comboFiltro.setMinimumSize(QtCore.QSize(150, 0))
        self.comboFiltro.setObjectName("comboFiltro")
        self.horizontalLayout.addWidget(self.comboFiltro)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableProveedor = QtWidgets.QTableWidget(Form)
        self.tableProveedor.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableProveedor.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableProveedor.setColumnCount(12)
        self.tableProveedor.setObjectName("tableProveedor")
        self.tableProveedor.setRowCount(0)
        self.verticalLayout.addWidget(self.tableProveedor)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitle.setText(_translate("Form", "Consulta Proveedores"))
        self.buttonAdd.setText(_translate("Form", "Añadir"))
        self.buttonDel.setText(_translate("Form", "Borrar"))
        self.tableProveedor.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ConsultaProveedor_Ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

