# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:27:24 2020

@author: aleja
"""
from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from menuprincipal_ui import *
from consultapersonal import *
from anadirpersonal import *
from consultaproveedor import *
from anadirproveedor import *
from crearevento import *
from projectmanagers import *
from recintos import *
#-------------------Clase del menu principal-----------------------

class MenuPrincipal(QtWidgets.QMainWindow, MenuPrincipal_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
    
    #------------------Ajuste de las columnas a la tabla-----------------------
    
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    
    
    #-------------------Acciones del menu------------------------------------------
        
        self.action_consultar_personal.triggered.connect(self.open_consultar_personal)
        self.action_alta_personal.triggered.connect(self.open_alta_personal)
        self.actionProject_Managers.triggered.connect(self.open_project_managers)
        self.action_consultar_proveedor.triggered.connect(self.open_consultar_proveedor)
        self.action_alta_proveedor.triggered.connect(self.open_alta_proveedor)
        self.action_alta_recinto.triggered.connect(self.open_alta_recinto)
        self.action_crear_evento.triggered.connect(self.open_crear_evento)
        
#-------------------Funciones para abrir nuevas ventanas-----------------------
       
    def open_alta_personal(self, checked):
        self.w = AnadirPersonal()
        self.w.show()
    def open_consultar_personal(self,checked):
        if not createConnection():
            sys.exit(1)
        self.w = ConsultaPersonal(app)
        self.w.show()
    def open_project_managers(self,checked):
        self.w = ProjectManagers()
        self.w.show()
    def open_alta_proveedor(self,checked):
        self.w = AnadirProveedor()
        self.w.show()
    def open_consultar_proveedor(self,checked):
        self.w = ConsultaProveedor()
        self.w.show()
    def open_alta_recinto(self,checked):
        self.w = Recintos()
        self.w.show()
    
    def open_crear_evento(self,checked):
        self.w = CrearEvento()
        self.w.show()





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MenuPrincipal()
    window.show()
    app.exec_()