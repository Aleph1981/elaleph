# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultapersonal_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ConsultaPersonal_Ui(object):
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
        self.button_Add = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_Add.sizePolicy().hasHeightForWidth())
        self.button_Add.setSizePolicy(sizePolicy)
        self.button_Add.setObjectName("button_Add")
        self.horizontalLayout.addWidget(self.button_Add)
        self.button_Borrar = QtWidgets.QPushButton(Form)
        self.button_Borrar.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_Borrar.sizePolicy().hasHeightForWidth())
        self.button_Borrar.setSizePolicy(sizePolicy)
        self.button_Borrar.setObjectName("button_Borrar")
        self.horizontalLayout.addWidget(self.button_Borrar)
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(180, 0))
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
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitle.setText(_translate("Form", "Consulta de Personal"))
        self.button_Add.setText(_translate("Form", "Añadir"))
        self.button_Borrar.setText(_translate("Form", "Borrar"))
        self.comboBox.setItemText(0, _translate("Form", "ALL"))
        self.comboBox.setItemText(1, _translate("Form", "Crew Chief"))
        self.comboBox.setItemText(2, _translate("Form", "Operador de Luces"))
        self.comboBox.setItemText(3, _translate("Form", "Dimmers"))
        self.comboBox.setItemText(4, _translate("Form", "Técnico Luces"))
        self.comboBox.setItemText(5, _translate("Form", "Operador Sonido"))
        self.comboBox.setItemText(6, _translate("Form", "RF"))
        self.comboBox.setItemText(7, _translate("Form", "Técnico de Sonido"))
        self.comboBox.setItemText(8, _translate("Form", "Operador de Video"))
        self.comboBox.setItemText(9, _translate("Form", "LED"))
        self.comboBox.setItemText(10, _translate("Form", "Técnico de Video"))
        self.comboBox.setItemText(11, _translate("Form", "Contenidos"))
        self.comboBox.setItemText(12, _translate("Form", "Rigger"))
        self.comboBox.setItemText(13, _translate("Form", "Regidor"))
        self.comboBox.setItemText(14, _translate("Form", "Deco"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ConsultaPersonal_Ui()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

