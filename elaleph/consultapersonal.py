# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:47:15 2020

@author: Alejandro Pérez Pérez
"""


from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from consultapersonal_ui import *
from anadirpersonal import *
from fichapersonal import *
import sys
from bdstd import BdStd


class ConsultaPersonal(QtWidgets.QDialog, ConsultaPersonal_Ui):
    
    def __init__(self, app):
        QtWidgets.QWidget.__init__(self)
        self.ui = ConsultaPersonal_Ui()
        self.ui.setupUi(self)        
        self.model = QtSql.QSqlQueryModel(self)
        self.sql = 'SELECT personal.id_personal, personal.nombre, apellidos, dni, \
               telefono, email, autonomo, ciudad, notas FROM personal'
        self.model.setQuery(self.sql)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setSelectionBehavior(self.ui.tableView.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableView.clicked.connect(self.clic_celda)
        self.ui.tableView.doubleClicked.connect(self.dobleclic_celda)   # <----- mere added
        self.ui.button_Borrar.setEnabled(False)
        
#-----------Escribe la cabecera de la tabla------------------------------------

        
        self.model.setHeaderData(0, QtCore.Qt.Horizontal , "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal , "Nombre")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal , "Apellidos")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal , "DNI")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal , "Teléfono")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal , "Email")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal , "Autónomo")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal , "Ciudad")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal , "Notas")
        
        
#---------Control del focus de la ventana--------------------------------------

        app.focusChanged.connect(self.checkFocus)
        
#---------Acciones de los botones----------------------------------------------    
        
        self.ui.button_Add.clicked.connect(self.open_alta_personal)
        self.ui.button_Borrar.clicked.connect(self.borrar_registro)   # Esto mejor a un boton refrescar
        self.ui.comboBox.activated[str].connect(self.filtro_checks)
        
#------------Conexión a la bbdd------------------------------------------------
    
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setHostName("localhost")
        db.setDatabaseName("elaleph.db")
        db.open()
        print(db.lastError().text())
        
    def clic_celda(self, item):
        index= self.ui.tableView.selectedIndexes()[0]
        self.choosen =self.ui.tableView.model().data(index)     # <----- mere changed
        self.ui.button_Borrar.setEnabled(True)                  # <----- mere changed
 
    def dobleclic_celda(self, item):                            # <----- mere added function
        index= self.ui.tableView.selectedIndexes()[0]          
        clave=self.ui.tableView.model().data(index)         
        self.w = FichaPersonal(clave)
        self.w.show()
    
    def checkFocus(self):
        if self.isActiveWindow():
            self.refresca_grid()
          
    def open_alta_personal(self,checked):
        self.w = AnadirPersonal()
        self.w.show()

    def borrar_registro(self):                               # <----- mere changed function

        clave=self.choosen
        
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Quiere eliminar a " + clave  + "? ", qm.Yes | qm.No)
        
        if ret == qm.Yes:
            #-------------- Borrar las tarifas y luego borrar el registro
            print("Voy a borrar ", clave)
            bd = BdStd()
            bd.runsql("DELETE FROM tarifas  WHERE id_personal = '" + clave + "'")
            bd.runsql("DELETE FROM personal WHERE id_personal = '" + clave + "'")
            if bd.rows != None :
                print("Ha borrado a ", clave)                
 
        else:
            print("No borro ", clave)
        self.refresca_grid()
        self.ui.button_Borrar.setEnabled(False)  
        
    def refresca_grid(self) :  
        self.model.setQuery(self.sql)
        print ("sql->", self.sql)
        self.ui.tableView.setModel(self.model)

    def filtro_checks(self,text):
        self.sql = 'SELECT personal.id_personal, nombre, apellidos, dni,telefono, email, \
        autonomo, notas FROM personal,tarifas \
        WHERE tarifas.id_personal=personal.id_personal'
        
        sigue=''
        if text == "ALL":
            self.sql = 'SELECT * FROM personal'
            
        if text == "Crew Chief":
             sigue += ' AND tarifas.id_cargo = "001"'
             self.model.setHeaderData(8, QtCore.Qt.Horizontal , "Cargo")
        if text == "Operador de Luces":
             sigue += ' AND tarifas.id_cargo = "002"'
             
        if text == "Dimmers":
             sigue += ' AND tarifas.id_cargo = "003"'
             
        if text == "Técnico Luces":
             sigue += ' AND tarifas.id_cargo = "004"'
             
        if text == "Operador Sonido":
             sigue += ' AND tarifas.id_cargo = "006"'
             
        if text == "RF":
             sigue += ' AND tarifas.id_cargo = "007"'
             
        if text == "Técnico de Sonido":
            sigue += ' AND tarifas.id_cargo = "008"'
        
        if text == "Operador de Video":
            sigue += ' AND tarifas.id_cargo = "010"'
            
        if text == "LED":
            sigue += ' AND tarifas.id_cargo = "011"'
            
        if text == "Técnico de Video":
            sigue += ' AND tarifas.id_cargo = "012"'
            
        if text == "Contenidos":
            sigue += ' AND tarifas.id_cargo = "013"'
            
        if text == "Regidor":
            sigue += ' AND tarifas.id_cargo = "009"'
        
        if text == "Rigger":
            sigue += ' AND tarifas.id_cargo = "005"'
            
        if text == "Deco":
            sigue += ' AND tarifas.id_cargo = "014"'
            
            
        self.sql += sigue
        self.model.setQuery(self.sql)
        print(self.sql)
        #self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.ui.tableView.setModel(self.model)
         
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    consulta_personal= ConsultaPersonal(app)
    consulta_personal.showMaximized()
    sys.exit(app.exec_())