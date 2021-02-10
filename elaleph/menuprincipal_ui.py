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
        MainWindow.setStyleSheet("\n"
"QWidget{\n"
"font:  10pt \"EmojiOne Color\";\n"
"color: rgb(235, 235, 235);\n"
"background-color: qlineargradient(spread:pad, x1:0.497512, y1:0, x2:0.502, y2:1, stop:0 rgba(54, 54, 54, 255), stop:0.507463 rgba(102, 102, 102, 255), stop:0.970149 rgba(54, 54, 54, 255));}\n"
"\n"
"\n"
"QWidget#widgetCal{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 200), stop:1 rgba(180, 0, 0, 200));border-radius:4px}\n"
"\n"
"QMenuBar{background-color: rgba(54,54,54,255)}\n"
"\n"
"QMenu::item:selected,QMenuBar::item::selected{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 200), stop:1 rgba(180, 0, 0, 200));border-radius:4px}\n"
"\n"
"QLineEdit,QPlainTextEdit,QTableWidget {background-color: rgba(255, 255, 255, 200);\n"
"color: rgb(0,0,0);border-radius: 4px}\n"
"\n"
"QLabel{ background-color: rgba(255, 255, 255, 0);}\n"
"\n"
"QHeaderView::section,QHeaderview{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));border-radius:4px}\n"
"\n"
"QTableView QTableCornerButton::section{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));;border-top-radius: 4px}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));\n"
"}\n"
"\n"
"\n"
"QPushButton,QToolButton{background-color:qlineargradient(spread:pad, x1:0.497512, y1:0, x2:0.502, y2:1, stop:0.0298507 rgba(230, 230, 230, 255), stop:0.532338 rgba(210, 210, 210, 255), stop:1 rgba(230, 230, 230, 255));\n"
"color: rgb(50,50,50); border-style: outset;border-radius: 4px;border-width: 2px;border-color: rgba(50,50,50,200);margin:5px;padding:2px}\n"
"\n"
"QPushButton:pressed{border-style: inset; }\n"
"QPushButton:checked{background-color:rgba(0,125,255,80);border-style: inset; }\n"
"\n"
"QLabel#labelVista{font: 12pt;}\n"
"QLabel#labelFechas{font: 12pt;}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected {background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));border:1px solid;border-color:rgb(255,255,255);border-radius:2px}\n"
"QTabBar::tab:hover {background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 100), stop:1 rgba(180, 0, 0, 100))}\n"
"QTabBar::tab:!selected {margin-top: 2px;}\n"
"QTabWidget::tab-bar {left: 5px;}\n"
"QTabBar::tab {min-width: 12ex;\n"
"    padding: 10px; padding-top:5px;padding-bottom:5px;}\n"
"QWidget#qt_calendar_calendarview {background-color: rgb(200,200,200);color:rgb(0,0,0);alternate-background-color: rgb(150,0,0);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 40)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonSinConf = QtWidgets.QToolButton(self.centralwidget)
        self.buttonSinConf.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonSinConf.setStyleSheet("background-color: rgba(255, 0, 255,200);")
        self.buttonSinConf.setText("")
        self.buttonSinConf.setObjectName("buttonSinConf")
        self.horizontalLayout_2.addWidget(self.buttonSinConf)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonPersonal = QtWidgets.QToolButton(self.centralwidget)
        self.buttonPersonal.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonPersonal.setStyleSheet("background-color: rgba(255, 0, 0,200);")
        self.buttonPersonal.setText("")
        self.buttonPersonal.setObjectName("buttonPersonal")
        self.horizontalLayout_2.addWidget(self.buttonPersonal)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonProveedor = QtWidgets.QToolButton(self.centralwidget)
        self.buttonProveedor.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonProveedor.setStyleSheet("background-color: rgba(0, 75, 255,200);")
        self.buttonProveedor.setText("")
        self.buttonProveedor.setObjectName("buttonProveedor")
        self.horizontalLayout_2.addWidget(self.buttonProveedor)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.buttonCerrado = QtWidgets.QToolButton(self.centralwidget)
        self.buttonCerrado.setMinimumSize(QtCore.QSize(35, 35))
        self.buttonCerrado.setStyleSheet("background-color: rgba(74, 222, 0,200);")
        self.buttonCerrado.setText("")
        self.buttonCerrado.setObjectName("buttonCerrado")
        self.horizontalLayout_2.addWidget(self.buttonCerrado)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.widgetCal = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetCal.sizePolicy().hasHeightForWidth())
        self.widgetCal.setSizePolicy(sizePolicy)
        self.widgetCal.setMinimumSize(QtCore.QSize(0, 30))
        self.widgetCal.setObjectName("widgetCal")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetCal)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.buttonPrev30 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonPrev30.setMinimumSize(QtCore.QSize(55, 35))
        self.buttonPrev30.setObjectName("buttonPrev30")
        self.horizontalLayout_5.addWidget(self.buttonPrev30)
        self.buttonPrev7 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonPrev7.setMinimumSize(QtCore.QSize(55, 35))
        self.buttonPrev7.setObjectName("buttonPrev7")
        self.horizontalLayout_5.addWidget(self.buttonPrev7)
        self.buttonPrev1 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonPrev1.setMinimumSize(QtCore.QSize(55, 35))
        self.buttonPrev1.setObjectName("buttonPrev1")
        self.horizontalLayout_5.addWidget(self.buttonPrev1)
        self.labelVista = QtWidgets.QLabel(self.widgetCal)
        self.labelVista.setStyleSheet("")
        self.labelVista.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVista.setObjectName("labelVista")
        self.horizontalLayout_5.addWidget(self.labelVista)
        self.buttonNext1 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonNext1.setMinimumSize(QtCore.QSize(55, 35))
        self.buttonNext1.setObjectName("buttonNext1")
        self.horizontalLayout_5.addWidget(self.buttonNext1)
        self.buttonNext7 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonNext7.setMinimumSize(QtCore.QSize(55, 35))
        self.buttonNext7.setObjectName("buttonNext7")
        self.horizontalLayout_5.addWidget(self.buttonNext7)
        self.buttonNext30 = QtWidgets.QToolButton(self.widgetCal)
        self.buttonNext30.setMinimumSize(QtCore.QSize(55, 35))
        self.buttonNext30.setObjectName("buttonNext30")
        self.horizontalLayout_5.addWidget(self.buttonNext30)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widgetCal, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 27))
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
        self.menuPersonal.addAction(self.action_alta_personal)
        self.menuPersonal.addAction(self.action_consultar_personal)
        self.menuPersonal.addAction(self.actionProject_Managers)
        self.menuEventos.addAction(self.action_crear_evento)
        self.menuEventos.addAction(self.action_consultar_evento)
        self.menuCrear_hojas.addAction(self.action_crear_hoja_de_ruta)
        self.menuCrear_hojas.addAction(self.action_crear_hoja_de_bolos)
        self.menuCrear_hojas.addAction(self.action_crear_hoja_de_almac_n)
        self.menuCrear_hojas.addAction(self.action_crear_hoja_de_transportes)
        self.menuProveedores.addAction(self.action_alta_proveedor)
        self.menuProveedores.addAction(self.action_consultar_proveedor)
        self.menuRecintos.addAction(self.action_alta_recinto)
        self.menuRecintos.addAction(self.action_consultar_recintos)
        self.menubar.addAction(self.menuEventos.menuAction())
        self.menubar.addAction(self.menuPersonal.menuAction())
        self.menubar.addAction(self.menuProveedores.menuAction())
        self.menubar.addAction(self.menuRecintos.menuAction())
        self.menubar.addAction(self.menuCrear_hojas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sin\n"
"confirmar"))
        self.label_2.setText(_translate("MainWindow", "Falta\n"
"personal"))
        self.label_3.setText(_translate("MainWindow", "Falta\n"
"proveedor"))
        self.label_4.setText(_translate("MainWindow", "Cerrado"))
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
        self.buttonPrev30.setText(_translate("MainWindow", "-30"))
        self.buttonPrev7.setText(_translate("MainWindow", "-7"))
        self.buttonPrev1.setText(_translate("MainWindow", "-1"))
        self.labelVista.setText(_translate("MainWindow", "Vista Semanal"))
        self.buttonNext1.setText(_translate("MainWindow", "+1"))
        self.buttonNext7.setText(_translate("MainWindow", "+7"))
        self.buttonNext30.setText(_translate("MainWindow", "+30"))
        self.menuPersonal.setTitle(_translate("MainWindow", "Personal"))
        self.menuEventos.setTitle(_translate("MainWindow", "Eventos"))
        self.menuCrear_hojas.setTitle(_translate("MainWindow", "Crear hojas"))
        self.menuProveedores.setTitle(_translate("MainWindow", "Proveedores"))
        self.menuRecintos.setTitle(_translate("MainWindow", "Recintos"))
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
        self.action_alta_recinto.setText(_translate("MainWindow", "Alta BBDD"))
        self.action_consultar_recintos.setText(_translate("MainWindow", "Consultar BBDD"))
        self.actionProject_Managers.setText(_translate("MainWindow", "Project Managers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MenuPrincipal_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

