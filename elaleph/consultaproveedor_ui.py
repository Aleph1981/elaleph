# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaproveedor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ConsultaProveedor_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1279, 759)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelConsulta = QtWidgets.QLabel(Dialog)
        self.labelConsulta.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.labelConsulta.setObjectName("labelConsulta")
        self.verticalLayout.addWidget(self.labelConsulta)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAdd = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAdd.sizePolicy().hasHeightForWidth())
        self.buttonAdd.setSizePolicy(sizePolicy)
        self.buttonAdd.setObjectName("buttonAdd")
        self.horizontalLayout.addWidget(self.buttonAdd)
        self.buttonDel = QtWidgets.QPushButton(Dialog)
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
        self.comboFiltro = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFiltro.sizePolicy().hasHeightForWidth())
        self.comboFiltro.setSizePolicy(sizePolicy)
        self.comboFiltro.setMinimumSize(QtCore.QSize(145, 0))
        self.comboFiltro.setObjectName("comboFiltro")
        self.horizontalLayout.addWidget(self.comboFiltro)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableProveedor = QtWidgets.QTableWidget(Dialog)
        self.tableProveedor.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableProveedor.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableProveedor.setColumnCount(12)
        self.tableProveedor.setObjectName("tableProveedor")
        self.tableProveedor.setRowCount(0)
        self.verticalLayout.addWidget(self.tableProveedor)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Consulta de Proveedores"))
        self.labelConsulta.setText(_translate("Dialog", "CONSULTA DE PROVEEDOR"))
        self.buttonAdd.setText(_translate("Dialog", "Añadir"))
        self.buttonDel.setText(_translate("Dialog", "Borrar"))
        self.tableProveedor.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ConsultaProveedor_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

