# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:05:18 2021

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from selectcliente_ui import *
from clientes import *

from bdstd import BdStd



class SelectCliente(QtWidgets.QWidget, SelectCliente_Ui):
    
    def __init__(self,self_padre=None):
        QtWidgets.QWidget.__init__(self)
        self.ui = SelectCliente_Ui()
        self.ui.setupUi(self)
        self.loadData()
        self.padre = self_padre
        #---------------ordenar por columnas-----------------------------------
        self.ui.tableClientes.setSortingEnabled(True)
        self.ui.tableClientes.setSelectionBehavior(self.ui.tableClientes.SelectRows)
        self.ui.tableClientes.verticalHeader().hide()
        self.ui.lineEdit.textChanged.connect(self.loadData)
        self.ui.buttonSeleccionar.clicked.connect(self.devuelveCliente)
        self.ui.buttonAdd.clicked.connect(self.addCliente)
    
    def loadData(self):
        self.ui.tableClientes.setRowCount(0)
        filtro = self.ui.lineEdit.text().lower()
        if filtro=="":
            bd = BdStd()
            bd.runsql("SELECT * FROM clientes")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadClientes(row)
        else :
            bd = BdStd()
            bd.runsql(f"""SELECT * FROM clientes WHERE LOWER(nombre) LIKE '%{filtro}%'""")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadClientes(row)
                    
    def loadClientes(self, data):
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
     
    def devuelveCliente(self):
        row = self.ui.tableClientes.currentRow()
        nombre = self.ui.tableClientes.item(row,1).text()
        print(nombre)
        self.padre.id_cliente = nombre
        self.padre.set_cliente(nombre)
        self.close()
       
    def addCliente(self):
        self.w = Clientes(self)
        self.w.show()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = SelectCliente()
    ui.show()
    sys.exit(app.exec_())
