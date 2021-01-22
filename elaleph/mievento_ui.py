# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mievento_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MiEvento_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1234, 858)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1211, 821))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.pag_personal = QtWidgets.QWidget()
        self.pag_personal.setObjectName("pag_personal")
        self.layoutWidget = QtWidgets.QWidget(self.pag_personal)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 1111, 691))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.personal = QtWidgets.QLabel(self.layoutWidget)
        self.personal.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.personal.setObjectName("personal")
        self.horizontalLayout_25.addWidget(self.personal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.nombre_personal = QtWidgets.QLabel(self.layoutWidget)
        self.nombre_personal.setObjectName("nombre_personal")
        self.horizontalLayout_24.addWidget(self.nombre_personal)
        self.entry_nombre_personal = QtWidgets.QLineEdit(self.layoutWidget)
        self.entry_nombre_personal.setObjectName("entry_nombre_personal")
        self.horizontalLayout_24.addWidget(self.entry_nombre_personal)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.filtrar_cargos = QtWidgets.QLabel(self.layoutWidget)
        self.filtrar_cargos.setObjectName("filtrar_cargos")
        self.horizontalLayout_19.addWidget(self.filtrar_cargos)
        self.combo_filtrar_cargos = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_filtrar_cargos.setObjectName("combo_filtrar_cargos")
        # mere el combo se carga directo
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
#        self.combo_filtrar_cargos.addItem("")
        self.horizontalLayout_19.addWidget(self.combo_filtrar_cargos)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_19)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.dia_personal = QtWidgets.QLabel(self.layoutWidget)
        self.dia_personal.setObjectName("dia_personal")
        self.horizontalLayout_10.addWidget(self.dia_personal)
        self.combo_dia_personal = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_dia_personal.setObjectName("combo_dia_personal")
        self.horizontalLayout_10.addWidget(self.combo_dia_personal)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_25)
        #------------------------------- 
#        self.personal_table = QtWidgets.QTableView(self.layoutWidget)
#        self.personal_table.setObjectName("personal_table")
#        self.verticalLayout_3.addWidget(self.personal_table)
#        self.personal_added = QtWidgets.QTableView(self.layoutWidget)
#        self.personal_added.setObjectName("personal_added")
#        self.verticalLayout_3.addWidget(self.personal_added)

        self.personal_table = QtWidgets.QTableWidget(self.layoutWidget)
        self.personal_table.setGeometry(QtCore.QRect(10, 10, 541, 281))
        self.personal_table.setRowCount(5)
        self.personal_table.setColumnCount(10)
        self.personal_table.setObjectName("personal_table")
        self.verticalLayout_3.addWidget(self.personal_table)
        self.personal_table.clicked.connect(self.tabla1_clic)
        # seleccionar solo filas, usar seleccion simple, una fila a la vez
        self.personal_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.personal_table.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        # evento producido cuando cambia el elemento seleccionado
        self.personal_table.itemSelectionChanged.connect(self.tabla1_select)

        self.personal_added = QtWidgets.QTableWidget(self.layoutWidget)
        self.personal_added.setGeometry(QtCore.QRect(10, 300, 541, 281))
        self.personal_added.setRowCount(5)
        self.personal_added.setColumnCount(10)
        self.personal_added.setObjectName("personal_table")
        self.verticalLayout_3.addWidget(self.personal_added)
        self.personal_added.clicked.connect(self.tabla2_clic)
        # seleccionar solo filas, usar seleccion simple, una fila a la vez
        self.personal_added.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.personal_added.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        # evento producido cuando cambia el elemento seleccionado
        self.personal_added.itemSelectionChanged.connect(self.tabla2_select)

        #--------------------------------------------------------------------
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_add_personal = QtWidgets.QPushButton(self.layoutWidget)
        self.button_add_personal.setObjectName("button_add_personal")
        self.horizontalLayout_3.addWidget(self.button_add_personal)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.button_remove_personal = QtWidgets.QPushButton(self.layoutWidget)
        self.button_remove_personal.setObjectName("button_remove_personal")
        self.horizontalLayout_3.addWidget(self.button_remove_personal)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_guardar_personal = QtWidgets.QPushButton(self.layoutWidget)
        self.button_guardar_personal.setObjectName("button_guardar_personal")
        self.horizontalLayout_5.addWidget(self.button_guardar_personal)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.button_cancelar_personal = QtWidgets.QPushButton(self.layoutWidget)
        self.button_cancelar_personal.setObjectName("button_cancelar_personal")
        self.horizontalLayout_5.addWidget(self.button_cancelar_personal)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.pag_personal, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidget, self.entry_nombre_personal)
        Dialog.setTabOrder(self.entry_nombre_personal, self.combo_filtrar_cargos)
        Dialog.setTabOrder(self.combo_filtrar_cargos, self.combo_dia_personal)
        Dialog.setTabOrder(self.combo_dia_personal, self.button_add_personal)
        Dialog.setTabOrder(self.button_add_personal, self.button_remove_personal)
        Dialog.setTabOrder(self.button_remove_personal, self.button_guardar_personal)
        Dialog.setTabOrder(self.button_guardar_personal, self.button_cancelar_personal)


    def tabla1_clic(self, item):
         cellContent = item.data()
#        print(cellContent)  # test
#        sf = "You clicked on {}".format(cellContent)
#        print(sf)
#        #self.label.setText("¡Acabas de hacer clic en el botón!")
 
    def tabla1_select(self):
        campos = self.personal_table.selectedItems()
        if len(campos) > 0 :
            print("Data:", len(campos), campos[0].text())
            self.id_personal = campos[0].text()
            self.nom_cargo = campos[3].text()

    def tabla2_clic(self, item):
        cellContent = item.data()
#        print(cellContent)  # test
#        sf = "You clicked on {}".format(cellContent)
#        print(sf)
#        #self.label.setText("¡Acabas de hacer clic en el botón!")
 
    def tabla2_select(self):
        campos = self.personal_added.selectedItems()
        print("Data:", len(campos), campos) 


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.personal.setText(_translate("Dialog", "PERSONAL"))
        self.nombre_personal.setText(_translate("Dialog", "Nombre"))
        self.filtrar_cargos.setText(_translate("Dialog", "Filtrar Cargos"))
        # mere el combo se carga directo
#        self.combo_filtrar_cargos.setItemText(0, _translate("Dialog", "All"))
#        self.combo_filtrar_cargos.setItemText(1, _translate("Dialog", "Crew Chief"))
#        self.combo_filtrar_cargos.setItemText(2, _translate("Dialog", "Operador de Luces"))
#        self.combo_filtrar_cargos.setItemText(3, _translate("Dialog", "Dimmers"))
#        self.combo_filtrar_cargos.setItemText(4, _translate("Dialog", "Técnico de Luces"))
#        self.combo_filtrar_cargos.setItemText(5, _translate("Dialog", "Operador de Sonido"))
#        self.combo_filtrar_cargos.setItemText(6, _translate("Dialog", "RF"))
#        self.combo_filtrar_cargos.setItemText(7, _translate("Dialog", "Técnico de Sonido"))
#        self.combo_filtrar_cargos.setItemText(8, _translate("Dialog", "Operador de Video"))
#        self.combo_filtrar_cargos.setItemText(9, _translate("Dialog", "Led"))
#        self.combo_filtrar_cargos.setItemText(10, _translate("Dialog", "Técnico de Video"))
#        self.combo_filtrar_cargos.setItemText(11, _translate("Dialog", "Rigger"))
#        self.combo_filtrar_cargos.setItemText(12, _translate("Dialog", "Regidor"))
#        self.combo_filtrar_cargos.setItemText(13, _translate("Dialog", "Contenidos"))
#        self.combo_filtrar_cargos.setItemText(14, _translate("Dialog", "Deco"))
        self.dia_personal.setText(_translate("Dialog", "Día"))
        self.button_add_personal.setText(_translate("Dialog", "Añadir"))
        self.button_remove_personal.setText(_translate("Dialog", "Quitar"))
        self.button_guardar_personal.setText(_translate("Dialog", "Guardar"))
        self.button_cancelar_personal.setText(_translate("Dialog", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pag_personal), _translate("Dialog", "Personal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

