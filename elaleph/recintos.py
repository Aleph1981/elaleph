# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:50:51 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from recintos_ui import *
from bdstd import BdStd
from cambios_ui import *

class Recintos(QtWidgets.QDialog, Recintos_Ui):
    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Recintos_Ui()
        self.ui.setupUi(self)        
    
    #------------------Ajuste de las columnas a la tabla-----------------------
    
        self.ui.tableRecintos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
    #-----------------Conexion de los botones---------------------------------
        self.ui.buttonAnadir.clicked.connect(self.anadir)
        self.ui.buttonGuardar.clicked.connect(self.guardar_cambios)
        self.ui.buttonEliminar.clicked.connect(self.eliminar)
        
    #-----------------Relleno de la parrilla----------------------------------
        self.loadData()
    
    def loadData(self):
        bd = BdStd()
        bd.runsql("SELECT * FROM recintos")
        if bd.rows != None :
            for row in bd.rows :
                self.load_one(row)
                
    def load_one(self, data):
        rowPosition = self.ui.tableRecintos.rowCount()
        self.ui.tableRecintos.insertRow(rowPosition)
        self.ui.tableRecintos.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[0]))
        self.ui.tableRecintos.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
        self.ui.tableRecintos.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[2]))
        self.ui.tableRecintos.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[3]))
        self.ui.tableRecintos.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(data[4]))
        self.ui.tableRecintos.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(data[5]))
        self.ui.tableRecintos.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(data[6]))        
        self.ui.tableRecintos.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(data[7]))
        self.ui.tableRecintos.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(data[8]))
        
    def anadir(self):
        
        #--------------------------generador de ID
        id_recinto = self.ui.inputCiudad.text()[0:3]+self.ui.inputNombre.text()[0:3]
        id_recinto = id_recinto.upper()
        trans_table = id_recinto.maketrans("Á,É,Í,Ó,Ú,À,È,Ì,Ò,Ù","A,E,I,O,U,A,E,I,O,U")
        id_recinto = id_recinto.translate(trans_table)
        self.id_recinto = id_recinto
        
        #---------------FORMATO DE LOS INPUTS----------------------------------

        nombre = self.ui.inputNombre.text()
        nombre = nombre.split(" ")
        nom=""
        for palabra in nombre:
            palabra=palabra.capitalize()
            nom+=palabra+" "
        contacto = self.ui.inputContacto.text()
        contacto = contacto.split(" ")
        cont=""
        for palabra in contacto:
            palabra=palabra.capitalize()
            cont+=palabra+" "
        
        campos_recintos = (id_recinto,nom,self.ui.inputDireccion.text(),\
                    self.ui.inputCiudad.text().capitalize(), cont, self.ui.inputTelefono.text(),\
                    self.ui.inputEmail.text().lower(), self.ui.inputWeb.text().lower(),\
                    self.ui.inputNotas.toPlainText())
        bd = BdStd()
        bd.runsql("INSERT INTO recintos (id_recinto, nombre, direccion, ciudad, \
                  contacto, telefono, email, web, notas) VALUES (?,?,?,?,?,?,?,?,?);",\
                  campos_recintos)
        
        #----------------Carga los datos en la tabla---------------------------
            
        self.load_one(campos_recintos)
        
        #---------------Resetea los inputs-------------------------------------
        
        self.ui.inputNombre.setText("")
        self.ui.inputDireccion.setText("")
        self.ui.inputCiudad.setText("")
        self.ui.inputContacto.setText("")
        self.ui.inputTelefono.setText("")
        self.ui.inputEmail.setText("")
        self.ui.inputWeb.setText("")
        self.ui.inputNotas.setPlainText("")

    def guardar_cambios(self):
        # mere añadido el contenido de la función
    
        # lista de campos tal como figura en el grid
        campos = ["id_recintos", "nombre", "direccion", "ciudad", "contacto",\
                  "telefono","email","web", "notas"]
        bd = BdStd()
        #
        # se barre todo el grid de pantalla , busca el registro en la bbdd y compara todos
        # los campos para ver si han cambiado, en caso que sí, actualiza el cambio en la bbdd
        #
        for tbrow in range(self.ui.tableRecintos.rowCount()) :
            clave = self.ui.tableRecintos.item(tbrow,0).text()
            print(clave)            
            #---- busca el registro y compara los campos cambiados 
            bd.runsql("SELECT * FROM recintos WHERE id_recinto = '" + clave + "'")      
            for row in bd.rows :
                sql = ""
                for i in range(1, len(campos)) :
                    if self.ui.tableRecintos.item(tbrow,i) != None:
                        if row[i] != self.ui.tableRecintos.item(tbrow,i).text() :
                            sql += campos [i] + "= '" + self.ui.tableRecintos.item(tbrow,i).text() + "' ,"
                            print ("<> (",row[i], ") (",self.ui.tableRecintos.item(tbrow,i).text() , ")")
            if sql != "" :
                sql = "UPDATE recintos SET " + sql[0:len(sql)-2]
                sql += " WHERE id_recinto = '" + clave + "'"
                print("SQL->", sql)
                bd.runsql(sql)
        
#        ui = Cambios_Ui()
#        ui.setupUi(Dialog)
#        Dialog.show()
                
    def eliminar(self):
        
        row=self.ui.tableRecintos.currentRow()
        clave = self.ui.tableRecintos.item(row,0).text()
        print(clave)
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Quiere eliminar " + self.ui.tableRecintos.item(row,1).text()  + "? ", qm.Yes | qm.No)
        
        if ret == qm.Yes:
            #-------------- Borrar el registro
            print("Voy a borrar ", clave)
            bd = BdStd()
            bd.runsql("DELETE FROM recintos  WHERE id_recinto = '" + clave + "'")
            if bd.rows != None :
                print("Ha borrado a ", clave)                
                self.ui.tableRecintos.removeRow(row)
        else:
            print("No borro ", clave)
        
                  
        
        
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Recintos()
    ui.show()
    sys.exit(app.exec_())