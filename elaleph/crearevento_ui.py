# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crear_evento.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class CrearEvento_Ui(object):
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
        self.pag_datos = QtWidgets.QWidget()
        self.pag_datos.setObjectName("pag_datos")
        self.layoutWidget = QtWidgets.QWidget(self.pag_datos)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 150, 360, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.id = QtWidgets.QLabel(self.layoutWidget)
        self.id.setObjectName("id")
        self.horizontalLayout.addWidget(self.id)
        self.entry_id = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_id.sizePolicy().hasHeightForWidth())
        self.entry_id.setSizePolicy(sizePolicy)
        self.entry_id.setObjectName("entry_id")
        self.horizontalLayout.addWidget(self.entry_id)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nombre = QtWidgets.QLabel(self.layoutWidget)
        self.nombre.setObjectName("nombre")
        self.horizontalLayout_2.addWidget(self.nombre)
        self.entry_nombre = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_nombre.sizePolicy().hasHeightForWidth())
        self.entry_nombre.setSizePolicy(sizePolicy)
        self.entry_nombre.setText("")
        self.entry_nombre.setObjectName("entry_nombre")
        self.horizontalLayout_2.addWidget(self.entry_nombre)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.cliente = QtWidgets.QLabel(self.layoutWidget)
        self.cliente.setObjectName("cliente")
        self.horizontalLayout_11.addWidget(self.cliente)
        self.entry_cliente = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_cliente.sizePolicy().hasHeightForWidth())
        self.entry_cliente.setSizePolicy(sizePolicy)
        self.entry_cliente.setObjectName("entry_cliente")
        self.horizontalLayout_11.addWidget(self.entry_cliente)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.recinto = QtWidgets.QLabel(self.layoutWidget)
        self.recinto.setObjectName("recinto")
        self.horizontalLayout_17.addWidget(self.recinto)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_17.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_17.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.presupuesto = QtWidgets.QLabel(self.layoutWidget)
        self.presupuesto.setObjectName("presupuesto")
        self.horizontalLayout_15.addWidget(self.presupuesto)
        self.entry_presu = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_presu.sizePolicy().hasHeightForWidth())
        self.entry_presu.setSizePolicy(sizePolicy)
        self.entry_presu.setObjectName("entry_presu")
        self.horizontalLayout_15.addWidget(self.entry_presu)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.manager = QtWidgets.QLabel(self.layoutWidget)
        self.manager.setObjectName("manager")
        self.horizontalLayout_13.addWidget(self.manager)
        self.combo_manager = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_manager.sizePolicy().hasHeightForWidth())
        self.combo_manager.setSizePolicy(sizePolicy)
        self.combo_manager.setObjectName("combo_manager")
        self.horizontalLayout_13.addWidget(self.combo_manager)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.onsite = QtWidgets.QLabel(self.layoutWidget)
        self.onsite.setObjectName("onsite")
        self.horizontalLayout_12.addWidget(self.onsite)
        self.entry_onsite = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_onsite.sizePolicy().hasHeightForWidth())
        self.entry_onsite.setSizePolicy(sizePolicy)
        self.entry_onsite.setText("")
        self.entry_onsite.setObjectName("entry_onsite")
        self.horizontalLayout_12.addWidget(self.entry_onsite)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.tfn_onsite = QtWidgets.QLabel(self.layoutWidget)
        self.tfn_onsite.setObjectName("tfn_onsite")
        self.horizontalLayout_14.addWidget(self.tfn_onsite)
        self.entry_tfn_onsite = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_tfn_onsite.sizePolicy().hasHeightForWidth())
        self.entry_tfn_onsite.setSizePolicy(sizePolicy)
        self.entry_tfn_onsite.setObjectName("entry_tfn_onsite")
        self.horizontalLayout_14.addWidget(self.entry_tfn_onsite)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.email_onsite = QtWidgets.QLabel(self.layoutWidget)
        self.email_onsite.setObjectName("email_onsite")
        self.horizontalLayout_16.addWidget(self.email_onsite)
        self.entry_email_onsite = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_email_onsite.sizePolicy().hasHeightForWidth())
        self.entry_email_onsite.setSizePolicy(sizePolicy)
        self.entry_email_onsite.setText("")
        self.entry_email_onsite.setObjectName("entry_email_onsite")
        self.horizontalLayout_16.addWidget(self.entry_email_onsite)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.layoutWidget1 = QtWidgets.QWidget(self.pag_datos)
        self.layoutWidget1.setGeometry(QtCore.QRect(670, 120, 271, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.fechas = QtWidgets.QLabel(self.layoutWidget1)
        self.fechas.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.fechas.setObjectName("fechas")
        self.horizontalLayout_20.addWidget(self.fechas)
        self.button_fechas = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_fechas.setObjectName("button_fechas")
        self.horizontalLayout_20.addWidget(self.button_fechas)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.fechas_table = QtWidgets.QTableView(self.layoutWidget1)
        self.fechas_table.setObjectName("fechas_table")
        self.verticalLayout_4.addWidget(self.fechas_table)
        self.datos = QtWidgets.QLabel(self.pag_datos)
        self.datos.setGeometry(QtCore.QRect(290, 120, 71, 16))
        self.datos.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.datos.setObjectName("datos")
        self.crear_evento = QtWidgets.QLabel(self.pag_datos)
        self.crear_evento.setGeometry(QtCore.QRect(530, 30, 161, 51))
        self.crear_evento.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.crear_evento.setObjectName("crear_evento")
        self.widget = QtWidgets.QWidget(self.pag_datos)
        self.widget.setGeometry(QtCore.QRect(670, 590, 271, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_guardar = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_guardar.sizePolicy().hasHeightForWidth())
        self.button_guardar.setSizePolicy(sizePolicy)
        self.button_guardar.setObjectName("button_guardar")
        self.horizontalLayout_4.addWidget(self.button_guardar)
        self.button_cancelar = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancelar.sizePolicy().hasHeightForWidth())
        self.button_cancelar.setSizePolicy(sizePolicy)
        self.button_cancelar.setObjectName("button_cancelar")
        self.horizontalLayout_4.addWidget(self.button_cancelar)
        self.tabWidget.addTab(self.pag_datos, "")
        self.pag_personal = QtWidgets.QWidget()
        self.pag_personal.setObjectName("pag_personal")
        self.widget1 = QtWidgets.QWidget(self.pag_personal)
        self.widget1.setGeometry(QtCore.QRect(40, 30, 1111, 691))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.personal = QtWidgets.QLabel(self.widget1)
        self.personal.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.personal.setObjectName("personal")
        self.horizontalLayout_25.addWidget(self.personal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.nombre_personal = QtWidgets.QLabel(self.widget1)
        self.nombre_personal.setObjectName("nombre_personal")
        self.horizontalLayout_24.addWidget(self.nombre_personal)
        self.entry_nombre_personal = QtWidgets.QLineEdit(self.widget1)
        self.entry_nombre_personal.setObjectName("entry_nombre_personal")
        self.horizontalLayout_24.addWidget(self.entry_nombre_personal)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.filtrar_cargos = QtWidgets.QLabel(self.widget1)
        self.filtrar_cargos.setObjectName("filtrar_cargos")
        self.horizontalLayout_19.addWidget(self.filtrar_cargos)
        self.combo_filtrar_cargos = QtWidgets.QComboBox(self.widget1)
        self.combo_filtrar_cargos.setObjectName("combo_filtrar_cargos")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.combo_filtrar_cargos.addItem("")
        self.horizontalLayout_19.addWidget(self.combo_filtrar_cargos)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_19)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.dia_personal = QtWidgets.QLabel(self.widget1)
        self.dia_personal.setObjectName("dia_personal")
        self.horizontalLayout_10.addWidget(self.dia_personal)
        self.combo_dia_personal = QtWidgets.QComboBox(self.widget1)
        self.combo_dia_personal.setObjectName("combo_dia_personal")
        self.horizontalLayout_10.addWidget(self.combo_dia_personal)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_25)
        self.personal_table = QtWidgets.QTableView(self.widget1)
        self.personal_table.setObjectName("personal_table")
        self.verticalLayout_3.addWidget(self.personal_table)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_add_personal = QtWidgets.QPushButton(self.widget1)
        self.button_add_personal.setObjectName("button_add_personal")
        self.horizontalLayout_3.addWidget(self.button_add_personal)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.button_remove_personal = QtWidgets.QPushButton(self.widget1)
        self.button_remove_personal.setObjectName("button_remove_personal")
        self.horizontalLayout_3.addWidget(self.button_remove_personal)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.personal_added = QtWidgets.QTableView(self.widget1)
        self.personal_added.setObjectName("personal_added")
        self.verticalLayout_5.addWidget(self.personal_added)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_guardar_personal = QtWidgets.QPushButton(self.widget1)
        self.button_guardar_personal.setObjectName("button_guardar_personal")
        self.horizontalLayout_5.addWidget(self.button_guardar_personal)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.button_cancelar_personal = QtWidgets.QPushButton(self.widget1)
        self.button_cancelar_personal.setObjectName("button_cancelar_personal")
        self.horizontalLayout_5.addWidget(self.button_cancelar_personal)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.pag_personal, "")
        self.pag_proveedores = QtWidgets.QWidget()
        self.pag_proveedores.setObjectName("pag_proveedores")
        self.layoutWidget_4 = QtWidgets.QWidget(self.pag_proveedores)
        self.layoutWidget_4.setGeometry(QtCore.QRect(40, 30, 1111, 691))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.proveedores = QtWidgets.QLabel(self.layoutWidget_4)
        self.proveedores.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.proveedores.setObjectName("proveedores")
        self.horizontalLayout_26.addWidget(self.proveedores)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem5)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.nombre_prov = QtWidgets.QLabel(self.layoutWidget_4)
        self.nombre_prov.setObjectName("nombre_prov")
        self.horizontalLayout_27.addWidget(self.nombre_prov)
        self.entry_nombre_prov = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.entry_nombre_prov.setObjectName("entry_nombre_prov")
        self.horizontalLayout_27.addWidget(self.entry_nombre_prov)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem6)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.filtrar_serv = QtWidgets.QLabel(self.layoutWidget_4)
        self.filtrar_serv.setObjectName("filtrar_serv")
        self.horizontalLayout_21.addWidget(self.filtrar_serv)
        self.combo_filtrar_serv = QtWidgets.QComboBox(self.layoutWidget_4)
        self.combo_filtrar_serv.setObjectName("combo_filtrar_serv")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.combo_filtrar_serv.addItem("")
        self.horizontalLayout_21.addWidget(self.combo_filtrar_serv)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_21)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem7)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.dia_prov = QtWidgets.QLabel(self.layoutWidget_4)
        self.dia_prov.setObjectName("dia_prov")
        self.horizontalLayout_18.addWidget(self.dia_prov)
        self.combo_dia_prov = QtWidgets.QComboBox(self.layoutWidget_4)
        self.combo_dia_prov.setObjectName("combo_dia_prov")
        self.horizontalLayout_18.addWidget(self.combo_dia_prov)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_18)
        self.verticalLayout_7.addLayout(self.horizontalLayout_26)
        self.prov_table_2 = QtWidgets.QTableView(self.layoutWidget_4)
        self.prov_table_2.setObjectName("prov_table_2")
        self.verticalLayout_7.addWidget(self.prov_table_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_add_prov = QtWidgets.QPushButton(self.layoutWidget_4)
        self.button_add_prov.setObjectName("button_add_prov")
        self.horizontalLayout_6.addWidget(self.button_add_prov)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.button_remove_prov = QtWidgets.QPushButton(self.layoutWidget_4)
        self.button_remove_prov.setObjectName("button_remove_prov")
        self.horizontalLayout_6.addWidget(self.button_remove_prov)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.personal_added_2 = QtWidgets.QTableView(self.layoutWidget_4)
        self.personal_added_2.setObjectName("personal_added_2")
        self.verticalLayout_6.addWidget(self.personal_added_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.button_guardar_prov = QtWidgets.QPushButton(self.layoutWidget_4)
        self.button_guardar_prov.setObjectName("button_guardar_prov")
        self.horizontalLayout_7.addWidget(self.button_guardar_prov)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.button_cancel_prov = QtWidgets.QPushButton(self.layoutWidget_4)
        self.button_cancel_prov.setObjectName("button_cancel_prov")
        self.horizontalLayout_7.addWidget(self.button_cancel_prov)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.pag_proveedores, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.button_cancelar.clicked.connect(Dialog.close)
        self.button_cancel_prov.clicked.connect(self.personal_added_2.clearSelection)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.entry_id, self.entry_nombre)
        Dialog.setTabOrder(self.entry_nombre, self.entry_cliente)
        Dialog.setTabOrder(self.entry_cliente, self.entry_presu)
        Dialog.setTabOrder(self.entry_presu, self.combo_manager)
        Dialog.setTabOrder(self.combo_manager, self.entry_onsite)
        Dialog.setTabOrder(self.entry_onsite, self.entry_tfn_onsite)
        Dialog.setTabOrder(self.entry_tfn_onsite, self.entry_email_onsite)
        Dialog.setTabOrder(self.entry_email_onsite, self.button_fechas)
        Dialog.setTabOrder(self.button_fechas, self.button_guardar)
        Dialog.setTabOrder(self.button_guardar, self.button_cancelar)
        Dialog.setTabOrder(self.button_cancelar, self.fechas_table)
        Dialog.setTabOrder(self.fechas_table, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.entry_nombre_personal)
        Dialog.setTabOrder(self.entry_nombre_personal, self.combo_filtrar_cargos)
        Dialog.setTabOrder(self.combo_filtrar_cargos, self.combo_dia_personal)
        Dialog.setTabOrder(self.combo_dia_personal, self.button_add_personal)
        Dialog.setTabOrder(self.button_add_personal, self.button_remove_personal)
        Dialog.setTabOrder(self.button_remove_personal, self.button_guardar_personal)
        Dialog.setTabOrder(self.button_guardar_personal, self.button_cancelar_personal)
        Dialog.setTabOrder(self.button_cancelar_personal, self.personal_table)
        Dialog.setTabOrder(self.personal_table, self.personal_added)
        Dialog.setTabOrder(self.personal_added, self.entry_nombre_prov)
        Dialog.setTabOrder(self.entry_nombre_prov, self.combo_filtrar_serv)
        Dialog.setTabOrder(self.combo_filtrar_serv, self.combo_dia_prov)
        Dialog.setTabOrder(self.combo_dia_prov, self.prov_table_2)
        Dialog.setTabOrder(self.prov_table_2, self.button_add_prov)
        Dialog.setTabOrder(self.button_add_prov, self.button_remove_prov)
        Dialog.setTabOrder(self.button_remove_prov, self.personal_added_2)
        Dialog.setTabOrder(self.personal_added_2, self.button_guardar_prov)
        Dialog.setTabOrder(self.button_guardar_prov, self.button_cancel_prov)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.id.setText(_translate("Dialog", "ID EVENTO"))
        self.nombre.setText(_translate("Dialog", "NOMBRE"))
        self.cliente.setText(_translate("Dialog", "CLIENTE"))
        self.recinto.setText(_translate("Dialog", "RECINTO"))
        self.presupuesto.setText(_translate("Dialog", "PRESUPUESTO"))
        self.manager.setText(_translate("Dialog", "PROJECT MANAGER"))
        self.onsite.setText(_translate("Dialog", "CONTACTO ON-SITE"))
        self.tfn_onsite.setText(_translate("Dialog", "TELEFONO ON-SITE"))
        self.email_onsite.setText(_translate("Dialog", "EMAIL ON-SITE"))
        self.fechas.setText(_translate("Dialog", "FECHAS"))
        self.button_fechas.setText(_translate("Dialog", "AÑADIR FECHA"))
        self.datos.setText(_translate("Dialog", "DATOS"))
        self.crear_evento.setText(_translate("Dialog", "Crear Evento"))
        self.button_guardar.setText(_translate("Dialog", "Guardar"))
        self.button_cancelar.setText(_translate("Dialog", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pag_datos), _translate("Dialog", "Datos"))
        self.personal.setText(_translate("Dialog", "PERSONAL"))
        self.nombre_personal.setText(_translate("Dialog", "Nombre"))
        self.filtrar_cargos.setText(_translate("Dialog", "Filtrar Cargos"))
        self.combo_filtrar_cargos.setItemText(0, _translate("Dialog", "All"))
        self.combo_filtrar_cargos.setItemText(1, _translate("Dialog", "Crew Chief"))
        self.combo_filtrar_cargos.setItemText(2, _translate("Dialog", "Operador de Luces"))
        self.combo_filtrar_cargos.setItemText(3, _translate("Dialog", "Dimmers"))
        self.combo_filtrar_cargos.setItemText(4, _translate("Dialog", "Técnico de Luces"))
        self.combo_filtrar_cargos.setItemText(5, _translate("Dialog", "Operador de Sonido"))
        self.combo_filtrar_cargos.setItemText(6, _translate("Dialog", "RF"))
        self.combo_filtrar_cargos.setItemText(7, _translate("Dialog", "Técnico de Sonido"))
        self.combo_filtrar_cargos.setItemText(8, _translate("Dialog", "Operador de Video"))
        self.combo_filtrar_cargos.setItemText(9, _translate("Dialog", "Led"))
        self.combo_filtrar_cargos.setItemText(10, _translate("Dialog", "Técnico de Video"))
        self.combo_filtrar_cargos.setItemText(11, _translate("Dialog", "Rigger"))
        self.combo_filtrar_cargos.setItemText(12, _translate("Dialog", "Regidor"))
        self.combo_filtrar_cargos.setItemText(13, _translate("Dialog", "Contenidos"))
        self.combo_filtrar_cargos.setItemText(14, _translate("Dialog", "Deco"))
        self.dia_personal.setText(_translate("Dialog", "Día"))
        self.button_add_personal.setText(_translate("Dialog", "Añadir"))
        self.button_remove_personal.setText(_translate("Dialog", "Quitar"))
        self.button_guardar_personal.setText(_translate("Dialog", "Guardar"))
        self.button_cancelar_personal.setText(_translate("Dialog", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pag_personal), _translate("Dialog", "Personal"))
        self.proveedores.setText(_translate("Dialog", "PROVEEDORES"))
        self.nombre_prov.setText(_translate("Dialog", "Nombre"))
        self.filtrar_serv.setText(_translate("Dialog", "Filtrar Servicio"))
        self.combo_filtrar_serv.setItemText(0, _translate("Dialog", "All"))
        self.combo_filtrar_serv.setItemText(1, _translate("Dialog", "Trailer"))
        self.combo_filtrar_serv.setItemText(2, _translate("Dialog", "Camión"))
        self.combo_filtrar_serv.setItemText(3, _translate("Dialog", "Furgoneta"))
        self.combo_filtrar_serv.setItemText(4, _translate("Dialog", "Runner"))
        self.combo_filtrar_serv.setItemText(5, _translate("Dialog", "Carga/Descarga"))
        self.combo_filtrar_serv.setItemText(6, _translate("Dialog", "Rigging"))
        self.combo_filtrar_serv.setItemText(7, _translate("Dialog", "Deco"))
        self.combo_filtrar_serv.setItemText(8, _translate("Dialog", "Generadores"))
        self.combo_filtrar_serv.setItemText(9, _translate("Dialog", "Traducción"))
        self.combo_filtrar_serv.setItemText(10, _translate("Dialog", "Catering"))
        self.combo_filtrar_serv.setItemText(11, _translate("Dialog", "Iluminación"))
        self.combo_filtrar_serv.setItemText(12, _translate("Dialog", "Sonido"))
        self.combo_filtrar_serv.setItemText(13, _translate("Dialog", "Video"))
        self.combo_filtrar_serv.setItemText(14, _translate("Dialog", "Mobiliario"))
        self.combo_filtrar_serv.setItemText(15, _translate("Dialog", "Otros"))
        self.dia_prov.setText(_translate("Dialog", "Día"))
        self.button_add_prov.setText(_translate("Dialog", "Añadir"))
        self.button_remove_prov.setText(_translate("Dialog", "Quitar"))
        self.button_guardar_prov.setText(_translate("Dialog", "Guardar"))
        self.button_cancel_prov.setText(_translate("Dialog", "Cancelar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pag_proveedores), _translate("Dialog", "Proveedores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CrearEvento_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

