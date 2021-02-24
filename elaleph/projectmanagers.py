# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:50:51 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from projectmanagers_ui import *
from bdstd import BdStd
from cambios_ui import *

class ProjectManagers(QtWidgets.QWidget, ProjectManagers_Ui):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ProjectManagers_Ui()
        self.ui.setupUi(self)        
    
    #------------------Ajuste de las columnas a la tabla-----------------------
    
        self.ui.tableManagers.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableManagers.verticalHeader().hide()
    #-----------------Conexion de los botones---------------------------------
        self.ui.buttonAnadir.clicked.connect(self.anadir)
        self.ui.buttonGuardar.clicked.connect(self.guardar_cambios)
        self.ui.buttonEliminar.clicked.connect(self.eliminar)
        
    #-----------------Relleno de la parrilla----------------------------------
        self.loadData()
    
    def loadData(self):
        self.ui.tableManagers.setRowCount(0)
        bd = BdStd()
        bd.runsql("SELECT * FROM managers")
        if bd.rows != None :
            for row in bd.rows :
                self.load_one(row)
                
    def load_one(self, data):
        rowPosition = self.ui.tableManagers.rowCount()
        self.ui.tableManagers.insertRow(rowPosition)
        self.ui.tableManagers.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[1]))
        self.ui.tableManagers.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[2]))
        self.ui.tableManagers.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[4]))
        self.ui.tableManagers.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[5]))
        self.ui.tableManagers.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(data[3]))
        self.ui.tableManagers.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(data[6]))
        self.ui.tableManagers.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(data[0]))        
        
        
    def anadir(self):
        
        #--------------------------generador de ID
        id_manager = self.ui.inputNombre.text()[0:2]+self.ui.inputApellidos.text()[0:2]+self.ui.inputDni.text()[0:2]
        id_manager = id_manager.upper()
        trans_table = id_manager.maketrans("Á,É,Í,Ó,Ú,À,È,Ì,Ò,Ù","A,E,I,O,U,A,E,I,O,U")
        id_manager = id_manager.translate(trans_table)
        self.id_manager = id_manager
        
        #---------------FORMATO DE NOMBRE Y APELLIDOS----------------------------------

        nombre = self.ui.inputNombre.text()
        apellidos = self.ui.inputApellidos.text()
        nombre = nombre.split(" ")
        apellidos = apellidos.split(" ")
        nom=""
        apell=""
        for palabra in nombre:
            palabra=palabra.capitalize()
            nom+=palabra+" "
        for palabra in apellidos:
            palabra=palabra.capitalize()
            apell+=palabra+" "
        
        campos_managers = (id_manager,nom,apell, self.ui.inputDni.text().upper(),\
                    self.ui.inputTelefono.text(),self.ui.inputEmail.text().lower(),\
                    self.ui.inputNotas.toPlainText())
        bd = BdStd()
        bd.runsql("INSERT INTO managers (id_manager, nombre, apellidos, dni, \
                  telefono, email, notas) VALUES (?,?,?,?,?,?,?);",campos_managers)
        
        #----------------Carga los datos en la tabla---------------------------
            
        self.load_one(campos_managers)
        
        #---------------Resetea los inputs-------------------------------------
        
        self.ui.inputNombre.setText("")
        self.ui.inputApellidos.setText("")
        self.ui.inputDni.setText("")
        self.ui.inputTelefono.setText("")
        self.ui.inputEmail.setText("")
        self.ui.inputNotas.setPlainText("")

    def guardar_cambios(self):
        # mere añadido el contenido de la función
    
        # lista de campos tal como figura en el grid
        campos = ["id_manager", "nombre", "apellidos", "telefono", "email", "dni", "notas"]
        bd = BdStd()
        #
        # se barre todo el grid de pantalla , busca el registro en la bbdd y compara todos
        # los campos para ver si han cambiado, en caso que sí, actualiza el cambio en la bbdd
        #
        for tbrow in range(self.ui.tableManagers.rowCount()) :
            clave = self.ui.tableManagers.item(tbrow,0).text()
            print(clave)            
            #---- busca el registro y compara los campos cambiados 
            bd.runsql("SELECT * FROM managers WHERE id_manager = '" + clave + "'")      
            for row in bd.rows :
                sql = ""
                for i in range(1, len(campos)) :
                    if self.ui.tableManagers.item(tbrow,i) != None:
                        if row[i] != self.ui.tableManagers.item(tbrow,i).text() :
                            sql += campos [i] + "= '" + self.ui.tableManagers.item(tbrow,i).text() + "' ,"
                            print ("<> (",row[i], ") (",self.ui.tableManagers.item(tbrow,i).text() , ")")
            if sql != "" :
                sql = "UPDATE managers SET " + sql[0:len(sql)-2]
                sql += " WHERE id_manager = '" + clave + "'"
                print("SQL->", sql)
                bd.runsql(sql)
                
        msgBox = QtWidgets.QMessageBox()
        msgBox.information(self, "Aleph", "Cambios guardados correctamente")
    
    def eliminar(self):
        
        row=self.ui.tableManagers.currentRow()
        clave = self.ui.tableManagers.item(row,0).text()
        print(clave)
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Quiere eliminar a " + self.ui.tableManagers.item(row,1).text()  + "? ", qm.Yes | qm.No)
        
        if ret == qm.Yes:
            #-------------- Borrar el registro
            print("Voy a borrar ", clave)
            bd = BdStd()
            bd.runsql("DELETE FROM managers  WHERE id_manager = '" + clave + "'")
            if bd.rows != None :
                print("Ha borrado a ", clave)                
                self.ui.tableManagers.removeRow(row)
        else:
            print("No borro ", clave)
        
                  
        
        
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ProjectManagers()
    ui.show()
    sys.exit(app.exec_())