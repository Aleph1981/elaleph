# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuprincipal_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MenuPrincipal_Ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(200, 100))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        spacerItem = QtWidgets.QSpacerItem(84, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.widgetCal = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetCal.sizePolicy().hasHeightForWidth())
        self.widgetCal.setSizePolicy(sizePolicy)
        self.widgetCal.setMinimumSize(QtCore.QSize(526, 56))
        self.widgetCal.setObjectName("widgetCal")
        self.buttonNext1 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonNext1.setGeometry(QtCore.QRect(330, 10, 55, 34))
        self.buttonNext1.setMinimumSize(QtCore.QSize(55, 25))
        self.buttonNext1.setObjectName("buttonNext1")
        self.buttonNext30 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonNext30.setGeometry(QtCore.QRect(450, 10, 63, 34))
        self.buttonNext30.setMinimumSize(QtCore.QSize(55, 25))
        self.buttonNext30.setObjectName("buttonNext30")
        self.buttonPrev7 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonPrev7.setGeometry(QtCore.QRect(70, 10, 55, 34))
        self.buttonPrev7.setMinimumSize(QtCore.QSize(55, 25))
        self.buttonPrev7.setObjectName("buttonPrev7")
        self.buttonPrev1 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonPrev1.setGeometry(QtCore.QRect(130, 10, 55, 34))
        self.buttonPrev1.setMinimumSize(QtCore.QSize(55, 25))
        self.buttonPrev1.setObjectName("buttonPrev1")
        self.labelVista = QtWidgets.QLabel(self.widgetCal)
        self.labelVista.setGeometry(QtCore.QRect(190, 10, 141, 41))
        self.labelVista.setStyleSheet("font: 12pt;")
        self.labelVista.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVista.setObjectName("labelVista")
        self.buttonPrev30 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonPrev30.setGeometry(QtCore.QRect(10, 10, 57, 34))
        self.buttonPrev30.setMinimumSize(QtCore.QSize(55, 25))
        self.buttonPrev30.setObjectName("buttonPrev30")
        self.buttonNext7 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonNext7.setGeometry(QtCore.QRect(390, 10, 55, 34))
        self.buttonNext7.setMinimumSize(QtCore.QSize(55, 25))
        self.buttonNext7.setObjectName("buttonNext7")
        self.horizontalLayout_3.addWidget(self.widgetCal)
        spacerItem1 = QtWidgets.QSpacerItem(84, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.logo_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_2.sizePolicy().hasHeightForWidth())
        self.logo_2.setSizePolicy(sizePolicy)
        self.logo_2.setMinimumSize(QtCore.QSize(200, 100))
        self.logo_2.setText("")
        self.logo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_2.setObjectName("logo_2")
        self.horizontalLayout_3.addWidget(self.logo_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonSinConf = QtWidgets.QToolButton(self.centralwidget)
        self.buttonSinConf.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonSinConf.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.562, y1:0, x2:0.522, y2:1, stop:0 rgba(255, 0, 255, 255), stop:1 rgba(180, 0, 180, 255));")
        self.buttonSinConf.setText("")
        self.buttonSinConf.setObjectName("buttonSinConf")
        self.horizontalLayout_2.addWidget(self.buttonSinConf)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.buttonPersonal = QtWidgets.QToolButton(self.centralwidget)
        self.buttonPersonal.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonPersonal.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.562, y1:0, x2:0.522, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));")
        self.buttonPersonal.setText("")
        self.buttonPersonal.setObjectName("buttonPersonal")
        self.horizontalLayout_2.addWidget(self.buttonPersonal)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.buttonProveedor = QtWidgets.QToolButton(self.centralwidget)
        self.buttonProveedor.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonProveedor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.562, y1:0, x2:0.522, y2:1, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 180, 255));")
        self.buttonProveedor.setText("")
        self.buttonProveedor.setObjectName("buttonProveedor")
        self.horizontalLayout_2.addWidget(self.buttonProveedor)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.buttonCerrado = QtWidgets.QToolButton(self.centralwidget)
        self.buttonCerrado.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonCerrado.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.562, y1:0, x2:0.522, y2:1, stop:0 rgba(0, 255, 0, 255), stop:1 rgba(0, 180, 0, 255));")
        self.buttonCerrado.setText("")
        self.buttonCerrado.setObjectName("buttonCerrado")
        self.horizontalLayout_2.addWidget(self.buttonCerrado)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuPersonal = QtWidgets.QMenu(self.menubar)
        self.menuPersonal.setObjectName("menuPersonal")
        self.menuEventos = QtWidgets.QMenu(self.menubar)
        self.menuEventos.setObjectName("menuEventos")
        self.menuCrear_hojas = QtWidgets.QMenu(self.menubar)
        self.menuCrear_hojas.setObjectName("menuCrear_hojas")
        self.menuProveedores = QtWidgets.QMenu(self.menubar)
        self.menuProveedores.setObjectName("menuProveedores")
        self.menuRecintos = QtWidgets.QMenu(self.menubar)
        self.menuRecintos.setObjectName("menuRecintos")
        self.menuClientes = QtWidgets.QMenu(self.menubar)
        self.menuClientes.setObjectName("menuClientes")
        MainWindow.setMenuBar(self.menubar)
        self.action_crear_hoja_de_ruta = QtWidgets.QAction(MainWindow)
        self.action_crear_hoja_de_ruta.setObjectName("action_crear_hoja_de_ruta")
        self.action_crear_hoja_de_bolos = QtWidgets.QAction(MainWindow)
        self.action_crear_hoja_de_bolos.setObjectName("action_crear_hoja_de_bolos")
        self.action_crear_hoja_de_almac_n = QtWidgets.QAction(MainWindow)
        self.action_crear_hoja_de_almac_n.setObjectName("action_crear_hoja_de_almac_n")
        self.action_guardar = QtWidgets.QAction(MainWindow)
        self.action_guardar.setObjectName("action_guardar")
        self.action_imprimir = QtWidgets.QAction(MainWindow)
        self.action_imprimir.setObjectName("action_imprimir")
        self.action_crear_hoja_de_transportes = QtWidgets.QAction(MainWindow)
        self.action_crear_hoja_de_transportes.setObjectName("action_crear_hoja_de_transportes")
        self.action_crear_evento = QtWidgets.QAction(MainWindow)
        self.action_crear_evento.setObjectName("action_crear_evento")
        self.action_consultar_evento = QtWidgets.QAction(MainWindow)
        self.action_consultar_evento.setObjectName("action_consultar_evento")
        self.action_alta_personal = QtWidgets.QAction(MainWindow)
        self.action_alta_personal.setObjectName("action_alta_personal")
        self.action_consultar_personal = QtWidgets.QAction(MainWindow)
        self.action_consultar_personal.setObjectName("action_consultar_personal")
        self.action_alta_proveedor = QtWidgets.QAction(MainWindow)
        self.action_alta_proveedor.setObjectName("action_alta_proveedor")
        self.action_consultar_proveedor = QtWidgets.QAction(MainWindow)
        self.action_consultar_proveedor.setObjectName("action_consultar_proveedor")
        self.action_alta_recinto = QtWidgets.QAction(MainWindow)
        self.action_alta_recinto.setObjectName("action_alta_recinto")
        self.action_consultar_recintos = QtWidgets.QAction(MainWindow)
        self.action_consultar_recintos.setObjectName("action_consultar_recintos")
        self.actionProject_Managers = QtWidgets.QAction(MainWindow)
        self.actionProject_Managers.setObjectName("actionProject_Managers")
        self.actionClientes = QtWidgets.QAction(MainWindow)
        self.actionClientes.setObjectName("actionClientes")
        self.actionPlantilla = QtWidgets.QAction(MainWindow)
        self.actionPlantilla.setObjectName("actionPlantilla")
        self.menuPersonal.addAction(self.action_alta_personal)
        self.menuPersonal.addAction(self.action_consultar_personal)
        self.menuPersonal.addSeparator()
        self.menuPersonal.addAction(self.actionProject_Managers)
        self.menuPersonal.addAction(self.actionPlantilla)
        self.menuEventos.addAction(self.action_crear_evento)
        self.menuEventos.addAction(self.action_consultar_evento)
        self.menuCrear_hojas.addAction(self.action_crear_hoja_de_ruta)
        self.menuCrear_hojas.addAction(self.action_crear_hoja_de_bolos)
        self.menuCrear_hojas.addAction(self.action_crear_hoja_de_transportes)
        self.menuProveedores.addAction(self.action_alta_proveedor)
        self.menuProveedores.addAction(self.action_consultar_proveedor)
        self.menuRecintos.addAction(self.action_alta_recinto)
        self.menuClientes.addAction(self.actionClientes)
        self.menubar.addAction(self.menuEventos.menuAction())
        self.menubar.addAction(self.menuPersonal.menuAction())
        self.menubar.addAction(self.menuProveedores.menuAction())
        self.menubar.addAction(self.menuClientes.menuAction())
        self.menubar.addAction(self.menuRecintos.menuAction())
        self.menubar.addAction(self.menuCrear_hojas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "El Aleph"))
        self.logo.setText(_translate("MainWindow", "Logo"))
        self.buttonNext1.setText(_translate("MainWindow", "+1"))
        self.buttonNext30.setText(_translate("MainWindow", "+30"))
        self.buttonPrev7.setText(_translate("MainWindow", "-7"))
        self.buttonPrev1.setText(_translate("MainWindow", "-1"))
        self.labelVista.setText(_translate("MainWindow", "Vista Semanal"))
        self.buttonPrev30.setText(_translate("MainWindow", "-30"))
        self.buttonNext7.setText(_translate("MainWindow", "+7"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nueva fila"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lunes"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Martes"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Miércoles"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Jueves"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Viernes"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sábado"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Domingo"))
        self.label.setText(_translate("MainWindow", "Sin\n"
"confirmar"))
        self.label_2.setText(_translate("MainWindow", "Falta\n"
"personal"))
        self.label_3.setText(_translate("MainWindow", "Falta\n"
"proveedor"))
        self.label_4.setText(_translate("MainWindow", "Cerrado"))
        self.menuPersonal.setTitle(_translate("MainWindow", "Personal"))
        self.menuEventos.setTitle(_translate("MainWindow", "Eventos"))
        self.menuCrear_hojas.setTitle(_translate("MainWindow", "Crear hojas"))
        self.menuProveedores.setTitle(_translate("MainWindow", "Proveedores"))
        self.menuRecintos.setTitle(_translate("MainWindow", "Recintos"))
        self.menuClientes.setTitle(_translate("MainWindow", "Clientes"))
        self.action_crear_hoja_de_ruta.setText(_translate("MainWindow", "Crear hoja de ruta"))
        self.action_crear_hoja_de_bolos.setText(_translate("MainWindow", "Crear hoja de bolos"))
        self.action_crear_hoja_de_almac_n.setText(_translate("MainWindow", "Crear hoja de almacén"))
        self.action_guardar.setText(_translate("MainWindow", "Guardar"))
        self.action_imprimir.setText(_translate("MainWindow", "Imprimir"))
        self.action_crear_hoja_de_transportes.setText(_translate("MainWindow", "Crear hoja de transportes"))
        self.action_crear_evento.setText(_translate("MainWindow", "Crear Evento"))
        self.action_consultar_evento.setText(_translate("MainWindow", "Consultar Evento"))
        self.action_alta_personal.setText(_translate("MainWindow", "Alta BBDD"))
        self.action_consultar_personal.setText(_translate("MainWindow", "Consultar BBDD"))
        self.action_alta_proveedor.setText(_translate("MainWindow", "Alta BBDD"))
        self.action_consultar_proveedor.setText(_translate("MainWindow", "Consultar BBDD"))
        self.action_alta_recinto.setText(_translate("MainWindow", "Base de Datos"))
        self.action_consultar_recintos.setText(_translate("MainWindow", "Consultar BBDD"))
        self.actionProject_Managers.setText(_translate("MainWindow", "Project Managers"))
        self.actionClientes.setText(_translate("MainWindow", "Base de Datos"))
        self.actionPlantilla.setText(_translate("MainWindow", "Personal de plantilla"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MenuPrincipal_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

