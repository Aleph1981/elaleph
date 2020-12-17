# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:34:12 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from crearevento_ui import *
from diasevento import *


def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setHostName("localhost")
    db.setDatabaseName("elaleph.db")
    db.open()
    print(db.lastError().text())
    return True

class CrearEvento(QtWidgets.QDialog, CrearEvento_Ui):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = CrearEvento_Ui()
        self.ui.setupUi(self)
        
        self.model = QtSql.QSqlQueryModel(self)
        self.sql = 'SELECT personal.id_personal, personal.nombre, apellidos, dni, \
               telefono, email, autonomo, notas FROM personal'
        self.model.setQuery(self.sql)
        self.ui.personal_table.setModel(self.model)
        self.ui.personal_table.setSelectionBehavior(self.ui.personal_table.SelectRows)
        
#-------------Escribe la cabecera de la tabla----------------------------------

        self.model.setHeaderData(0, QtCore.Qt.Horizontal , "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal , "Nombre")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal , "Apellidos")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal , "DNI")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal , "Teléfono")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal , "Email")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal , "Autónomo")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal , "Notas")
        
#-------Si el combobox se activa llama a la funcion de filtrado----------------

        self.ui.combo_filtrar_cargos.activated[str].connect(self.filtro_checks)
        
#--------Conexión del boton añadir fechas-------------------------------------
        
        self.ui.button_fechas.clicked.connect(self.open_dias_evento)
        
#-------abrir añadir fechas---------------------------------------------------

    def open_dias_evento(self,checked):
        self.w = DiasEvento()
        self.w.show()

#------Función de filtrado----------------------------------------------------       
    
    def filtro_checks(self,text):
        self.sql = 'SELECT personal.id_personal, nombre, apellidos, dni,telefono, email, \
        autonomo, notas FROM personal,tarifas \
        WHERE tarifas.id_personal=personal.id_personal'
        
        sigue=''
        if text == "ALL":
            self.sql = 'SELECT * FROM personal'
            
        if text == "Crew Chief":
             sigue += ' AND tarifas.id_cargo = "cc"'
             
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
            
            
        self.sql += sigue
        self.model.setQuery(self.sql)
        print(self.sql)
        #self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.personal_table.setModel(self.model)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = CrearEvento_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())