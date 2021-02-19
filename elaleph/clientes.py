# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:50:51 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from clientes_ui import *
from bdstd import BdStd
from cambios_ui import *

class Clientes(QtWidgets.QWidget, Clientes_Ui):
    
    def __init__(self,padre=None):
        QtWidgets.QWidget.__init__(self)
        self.ui = Clientes_Ui()
        self.ui.setupUi(self) 
        self.padre=padre
    
    #------------------Ajuste de la tabla-----------------------
    
        self.ui.tableClientes.setSortingEnabled(True)
        self.ui.tableClientes.verticalHeader().hide()
        
        
    #-----------------Conexion de los botones---------------------------------
        self.ui.buttonAnadir.clicked.connect(self.anadir)
        self.ui.buttonGuardar.clicked.connect(self.guardar_cambios)
        self.ui.buttonEliminar.clicked.connect(self.eliminar)
        
    #-----------------Relleno de la parrilla----------------------------------
        self.loadData()
    
    def loadData(self):
        self.ui.tableClientes.setRowCount(0)
        bd = BdStd()
        bd.runsql("SELECT * FROM clientes")
        if bd.rows != None :
            for row in bd.rows :
                self.load_one(row)
                
    def load_one(self, data):
        rowPosition = self.ui.tableClientes.rowCount()
        self.ui.tableClientes.insertRow(rowPosition)
        self.ui.tableClientes.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[0]))
        self.ui.tableClientes.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
        self.ui.tableClientes.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[2]))
        self.ui.tableClientes.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[3]))
        self.ui.tableClientes.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(data[4]))
        self.ui.tableClientes.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(data[5]))
        self.ui.tableClientes.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(data[6]))
        self.ui.tableClientes.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(data[7]))
        self.ui.tableClientes.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(data[8]))
        self.ui.tableClientes.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(data[9]))
        self.ui.tableClientes.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(data[10]))
        self.ui.tableClientes.setItem(rowPosition , 11, QtWidgets.QTableWidgetItem(data[11]))
        self.ui.tableClientes.setItem(rowPosition , 12, QtWidgets.QTableWidgetItem(data[12]))
        self.ui.tableClientes.setItem(rowPosition , 13, QtWidgets.QTableWidgetItem(data[13]))
                
        
        
        
    def anadir(self):
        
        #--------------------------generador de ID
        id_cliente = self.ui.inputNombre.text()[0:4]+self.ui.inputCif.text()[0:4]
        id_cliente = id_cliente.upper()
        trans_table = id_cliente.maketrans("Á,É,Í,Ó,Ú,À,È,Ì,Ò,Ù","A,E,I,O,U,A,E,I,O,U")
        id_cliente = id_cliente.translate(trans_table)
        self.id_cliente = id_cliente
        
        #---------------FORMATO DE NOMBRE Y APELLIDOS----------------------------------

        nombre = self.ui.inputNombre.text()
        nombre = nombre.split(" ")
        
        nom=""
        
        for palabra in nombre:
            palabra=palabra.capitalize()
            nom+=palabra+" "
        
        
        campos_clientes = (id_cliente,nom,self.ui.inputPais.text().capitalize(),\
                    self.ui.inputProvincia.text().capitalize(),self.ui.inputLocalidad.text().capitalize(),\
                    self.ui.inputDireccion.text(),self.ui.inputCif.text(),\
                    self.ui.inputTelefono.text(),self.ui.inputEmail.text().lower(),\
                    self.ui.inputWeb.text().lower(),self.ui.inputContacto.text(),\
                    self.ui.inputTfnCont.text(),self.ui.inputEmailCont.text().lower(),\
                    self.ui.inputNotas.toPlainText())
        bd = BdStd()
        bd.runsql("""INSERT INTO clientes (id_cliente, nombre, pais, provincia, localidad, direccion,
                  cif, telefono, email, web, contacto1, telefono_contacto1, email_contacto1, notas)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",campos_clientes)
        
        #----------------Carga los datos en la tabla---------------------------
            
        self.load_one(campos_clientes)
        
        #---------------Resetea los inputs-------------------------------------
        
        self.ui.inputNombre.setText("")
        self.ui.inputPais.setText("")
        self.ui.inputProvincia.setText("")
        self.ui.inputLocalidad.setText("")
        self.ui.inputDireccion.setText("")
        self.ui.inputCif.setText("")
        self.ui.inputTelefono.setText("")
        self.ui.inputEmail.setText("")
        self.ui.inputWeb.setText("")
        self.ui.inputContacto.setText("")
        self.ui.inputTfnCont.setText("")
        self.ui.inputEmailCont.setText("")
        self.ui.inputNotas.setPlainText("")
        
    #-------- Si se ha abierto desde seleccionar cliente se cierra y refresca la tabla---------------
    
        if self.padre != None:
            
            self.padre.loadData()
            self.close()
            
    def guardar_cambios(self):
        # mere añadido el contenido de la función
    
        # lista de campos tal como figura en el grid
        campos = ["Id Cliente", "Nombre", "Pais", "Provincia", "Localidad", \
                  "Dirección", "CIF","Teléfono","Email","Web","Contacto","Tfn Contacto",\
                  "Email Contacto","Notas"]
        bd = BdStd()
        #
        # se barre todo el grid de pantalla , busca el registro en la bbdd y compara todos
        # los campos para ver si han cambiado, en caso que sí, actualiza el cambio en la bbdd
        #
        for tbrow in range(self.ui.tableClientes.rowCount()) :
            clave = self.ui.tableClientes.item(tbrow,0).text()
            print(clave)            
            #---- busca el registro y compara los campos cambiados 
            bd.runsql("SELECT * FROM clientes WHERE id_cliente = '" + clave + "'")      
            for row in bd.rows :
                sql = ""
                for i in range(1, len(campos)) :
                    if self.ui.tableClientes.item(tbrow,i) != None:
                        if row[i] != self.ui.tableClientes.item(tbrow,i).text() :
                            sql += campos [i] + "= '" + self.ui.tableClientes.item(tbrow,i).text() + "' ,"
                            print ("<> (",row[i], ") (",self.ui.tableClientes.item(tbrow,i).text() , ")")
            if sql != "" :
                sql = "UPDATE clientes SET " + sql[0:len(sql)-2]
                sql += " WHERE id_cliente = '" + clave + "'"
                print("SQL->", sql)
                bd.runsql(sql)
        #w = Cambios_Ui()  mere quitado
        #w.show()
    
    def eliminar(self):
        
        row=self.ui.tableClientes.currentRow()
        clave = self.ui.tableClientes.item(row,0).text()
        print(clave)
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Quiere eliminar a " + self.ui.tableClientes.item(row,1).text()  + "? ", qm.Yes | qm.No)
        
        if ret == qm.Yes:
            #-------------- Borrar el registro
            print("Voy a borrar ", clave)
            bd = BdStd()
            bd.runsql("DELETE FROM clientes  WHERE id_cliente = '" + clave + "'")
            if bd.rows != None :
                print("Ha borrado a ", clave)                
                self.ui.tableClientes.removeRow(row)
        else:
            print("No borro ", clave)
        
                  
        
        
       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Clientes()
    ui.show()
    sys.exit(app.exec_())