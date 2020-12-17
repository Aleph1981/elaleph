# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:43:56 2020

@author: aleja
"""

from consultaproveedor_ui import *
from anadirproveedor import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql



class ConsultaProveedor(QtWidgets.QDialog, ConsultaProveedor_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.ui = ConsultaProveedor_Ui()
        self.setupUi(self)
        self.model = QtSql.QSqlQueryModel(self)
        self.sql = 'SELECT personal.id_personal, personal.nombre, apellidos, dni, \
               telefono, email, autonomo, notas FROM personal'
        self.model.setQuery(self.sql)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(self.ui.tableView.SelectRows)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal , "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal , "Empresa")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal , "Ubicación")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal , "Servicio")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal , "CIF")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal , "Teléfono")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal , "Email")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal , "Web")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal , "Contacto")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal , "Tfn Contacto")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal , "Email Contacto")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal , "Notas")
        
#-------------Conexion a la bbdd-----------------------------------------
        
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setHostName("localhost")
        db.setDatabaseName("elaleph.db")
        db.open()
        print(db.lastError().text())
        

        
#---------Acciones de los botones----------------------------------------------
        

        self.button_Add.clicked.connect(self.open_alta_proveedor)
        
        
        
        
#---------------------------- Filtros -----------------------------------------
       
    def filtro_checks(self,text):
            self.sql = 'SELECT personal.id_personal, nombre, apellidos, dni,telefono, email, \
            autonomo, notas FROM personal,tarifas \
            WHERE tarifas.id_personal=personal.id_personal'
            
            sigue=''
            if text == "ALL":
                self.sql = 'SELECT * FROM personal'
                
            if text == "Crew Chief":
                 sigue += ' AND tarifas.id_cargo = "cc"'
                 self.model.setHeaderData(8, QtCore.Qt.Horizontal , "Cargo")
            if text == "Operador de Luces":
                 sigue += ' AND tarifas.id_cargo = "opl"'
                 
            if text == "Dimmers":
                 sigue += ' AND tarifas.id_cargo = "dim"'
                 
            if text == "Técnico Luces":
                 sigue += ' AND tarifas.id_cargo = "tecl"'
                 
            if text == "Operador Sonido":
                 sigue += ' AND tarifas.id_cargo = "ops"'
                 
            if text == "RF":
                 sigue += ' AND tarifas.id_cargo = "rf"'
                 
            if text == "Técnico de Sonido":
                sigue += ' AND tarifas.id_cargo = "tecs"'
            
            if text == "Operador de Video":
                sigue += ' AND tarifas.id_cargo = "opv"'
                
            if text == "LED":
                sigue += ' AND tarifas.id_cargo = "led"'
                
            if text == "Técnico de Video":
                sigue += ' AND tarifas.id_cargo = "tecv"'
                
            if text == "Contenidos":
                sigue += ' AND tarifas.id_cargo = "cont"'
                
            if text == "Regidor":
                sigue += ' AND tarifas.id_cargo = "regi"'
            
            if text == "Rigger":
                sigue += ' AND tarifas.id_cargo = "rigg"'
                
            if text == "Deco":
                sigue += ' AND tarifas.id_cargo = "deco"'


            
            
    
    def open_alta_proveedor(self,checked):
        self.w = AnadirProveedor()
        self.w.show()
    
   
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    consulta_proveedor= ConsultaProveedor()
    consulta_proveedor.show()
    sys.exit(app.exec_())
        
       
        
    
        
        
        
        
        
