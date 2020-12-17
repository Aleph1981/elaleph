# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultapersonal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ConsultaPersonal_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1279, 759)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(12, 15, 1251, 721))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_consulta = QtWidgets.QLabel(self.widget)
        self.label_consulta.setStyleSheet("\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_consulta.setObjectName("label_consulta")
        self.verticalLayout.addWidget(self.label_consulta)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_Add = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_Add.sizePolicy().hasHeightForWidth())
        self.button_Add.setSizePolicy(sizePolicy)
        self.button_Add.setObjectName("button_Add")
        self.horizontalLayout.addWidget(self.button_Add)
        self.button_Borrar = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_Borrar.sizePolicy().hasHeightForWidth())
        self.button_Borrar.setSizePolicy(sizePolicy)
        self.button_Borrar.setObjectName("button_Borrar")
        self.horizontalLayout.addWidget(self.button_Borrar)
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Consulta de Personal"))
        self.label_consulta.setText(_translate("Dialog", "CONSULTA DE PERSONAL"))
        self.button_Add.setText(_translate("Dialog", "Añadir"))
        self.button_Borrar.setText(_translate("Dialog", "Borrar"))
        self.comboBox.setItemText(0, _translate("Dialog", "ALL"))
        self.comboBox.setItemText(1, _translate("Dialog", "Crew Chief"))
        self.comboBox.setItemText(2, _translate("Dialog", "Operador de Luces"))
        self.comboBox.setItemText(3, _translate("Dialog", "Dimmers"))
        self.comboBox.setItemText(4, _translate("Dialog", "Técnico Luces"))
        self.comboBox.setItemText(5, _translate("Dialog", "Operador Sonido"))
        self.comboBox.setItemText(6, _translate("Dialog", "RF"))
        self.comboBox.setItemText(7, _translate("Dialog", "Técnico de Sonido"))
        self.comboBox.setItemText(8, _translate("Dialog", "Operador de Video"))
        self.comboBox.setItemText(9, _translate("Dialog", "LED"))
        self.comboBox.setItemText(10, _translate("Dialog", "Técnico de Video"))
        self.comboBox.setItemText(11, _translate("Dialog", "Contenidos"))
        self.comboBox.setItemText(12, _translate("Dialog", "Rigger"))
        self.comboBox.setItemText(13, _translate("Dialog", "Regidor"))
        self.comboBox.setItemText(14, _translate("Dialog", "Deco"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ConsultaPersonal_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

