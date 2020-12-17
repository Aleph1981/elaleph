# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dias_evento.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Dias_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 401)
        self.calendar = QtWidgets.QCalendarWidget(Dialog)
        self.calendar.setGeometry(QtCore.QRect(20, 80, 391, 261))
        self.calendar.setObjectName("calendar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 181, 16))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(450, 80, 131, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.combo_tarea = QtWidgets.QComboBox(self.widget)
        self.combo_tarea.setObjectName("combo_tarea")
        self.combo_tarea.addItem("")
        self.combo_tarea.addItem("")
        self.combo_tarea.addItem("")
        self.combo_tarea.addItem("")
        self.combo_tarea.addItem("")
        self.combo_tarea.addItem("")
        self.combo_tarea.addItem("")
        self.combo_tarea.addItem("")
        self.verticalLayout.addWidget(self.combo_tarea)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.time = QtWidgets.QTimeEdit(self.widget)
        self.time.setObjectName("time")
        self.verticalLayout.addWidget(self.time)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.button_add = QtWidgets.QPushButton(self.widget)
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        self.button_cancel = QtWidgets.QPushButton(self.widget)
        self.button_cancel.setObjectName("button_cancel")
        self.verticalLayout.addWidget(self.button_cancel)
        
        self.button_cancel.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Fechas de evento"))
        self.combo_tarea.setItemText(0, _translate("Dialog", "Carga"))
        self.combo_tarea.setItemText(1, _translate("Dialog", "Montaje"))
        self.combo_tarea.setItemText(2, _translate("Dialog", "Pruebas"))
        self.combo_tarea.setItemText(3, _translate("Dialog", "Evento"))
        self.combo_tarea.setItemText(4, _translate("Dialog", "Desmontaje"))
        self.combo_tarea.setItemText(5, _translate("Dialog", "Descarga"))
        self.combo_tarea.setItemText(6, _translate("Dialog", "Produccion"))
        self.combo_tarea.setItemText(7, _translate("Dialog", "Almacén"))
        self.button_add.setText(_translate("Dialog", "Añadir"))
        self.button_cancel.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Dias_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

