# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:05:18 2021

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from selectrecinto_ui import *
from recintos import *
from bdstd import BdStd



class SelectRecinto(QtWidgets.QWidget, SelectRecinto_Ui):
    
    def __init__(self,self_padre=None):
        QtWidgets.QWidget.__init__(self)
        self.ui = SelectRecinto_Ui()
        self.ui.setupUi(self)
        self.loadData()
        self.padre = self_padre
        self.setWindowTitle("Aleph - Selección de recinto")
        #---------------ordenar por columnas-----------------------------------
        self.ui.tableRecintos.setSortingEnabled(True)
        self.ui.tableRecintos.setSelectionBehavior(self.ui.tableRecintos.SelectRows)
        self.ui.tableRecintos.verticalHeader().hide()
        self.ui.lineEdit.textChanged.connect(self.loadData)
        self.ui.buttonSelect.clicked.connect(self.devuelveRecinto)
        self.ui.buttonAdd.clicked.connect(self.addRecinto)
        self.self_id = "selectrecinto"
    
    def loadData(self):
        self.ui.tableRecintos.setRowCount(0)
        filtro = self.ui.lineEdit.text().lower()
        if filtro=="":
            bd = BdStd()
            bd.runsql("SELECT * FROM recintos")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadRecintos(row)
        else :
            bd = BdStd()
            bd.runsql(f"""SELECT * FROM recintos WHERE LOWER(nombre) LIKE '%{filtro}%'""")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadRecintos(row)
                    
    def loadRecintos(self, data):
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
         self.ui.tableRecintos.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(data[9]))
         self.ui.tableRecintos.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(data[10]))
         self.ui.tableRecintos.setItem(rowPosition , 11, QtWidgets.QTableWidgetItem(data[11]))
         self.ui.tableRecintos.setItem(rowPosition , 12, QtWidgets.QTableWidgetItem(data[12]))
         
     
    def devuelveRecinto(self):
        row = self.ui.tableRecintos.currentRow()
        id_recinto = self.ui.tableRecintos.item(row,0).text()
        
        if self.padre.r_e == "r":
            self.padre.load_recintoR(id_recinto)
            
        elif self.padre.r_e == "e":
            self.padre.load_recintoE(id_recinto)
        
        self.close()
       
    def addRecinto(self):
        self.w = Recintos(self)
        self.w.show()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = SelectRecinto()
    ui.show()
    sys.exit(app.exec_())
