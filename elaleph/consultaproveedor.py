# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:43:56 2020

@author: aleja
"""

from consultaproveedor_ui import *
from anadirproveedor import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from bdstd import *


class ConsultaProveedor(QtWidgets.QDialog, ConsultaProveedor_Ui):
    
    def __init__(self, app):
        QtWidgets.QDialog.__init__(self)
        self.ui = ConsultaProveedor_Ui()
        self.ui.setupUi(self)     
        #self.ui.tableProveedor.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableProveedor.verticalHeader().setDefaultSectionSize(100)
        self.ui.tableProveedor.setHorizontalHeaderLabels(["ID","Empresa","Provincia",\
            "Localidad","Dirección","Servicio/s","CIF","Teléfono","Email","Web",\
            "Contacto","Teléfono Contacto","Email Contacto","Notas"])
        self.ui.tableProveedor.setSortingEnabled(True)
        self.ui.tableProveedor.clicked.connect(self.current_row)
        self.ui.buttonAdd.clicked.connect(self.open_alta_proveedor)
        self.ui.buttonDel.clicked.connect(self.eliminar)
        self.ui.comboFiltro.activated[str].connect(self.filtro_checks)
        self.id_proveedor = None
        
        self.combo_servicios()
        
        app.focusChanged.connect(self.checkFocus)
        
        
    def current_row(self):
        self.ui.buttonDel.setEnabled(True)
        self.row = self.ui.tableProveedor.currentRow()
        print(self.row)
        for i, item in enumerate(self.ui.tableProveedor.selectedItems()):
            if i == 0 :
                self.id_proveedor = item.text()
                break
        if self.id_proveedor != None :
            self.w = AnadirProveedor(self.id_proveedor)
            self.w.show()            

        
    def combo_servicios(self):   
        bd=BdStd()
        bd.runsql("SELECT servicio FROM servicios")
        self.ui.comboFiltro.clear()
        self.ui.comboFiltro.addItem("All")

        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.comboFiltro.addItem(row_data[0].capitalize())


                
    def load_one(self, data):
        
        rowPosition = self.ui.tableProveedor.rowCount()
        self.ui.tableProveedor.insertRow(rowPosition)
        self.serv=data[5].split()
        self.serv = [x.capitalize() for x in self.serv]
        self.serv = "\n".join(self.serv)
        
        self.ui.tableProveedor.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[0]))
        self.ui.tableProveedor.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
        self.ui.tableProveedor.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[2]))
        self.ui.tableProveedor.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[3]))
        self.ui.tableProveedor.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(data[4]))
        self.ui.tableProveedor.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(self.serv))
        self.ui.tableProveedor.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(data[6]))        
        self.ui.tableProveedor.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(data[7]))
        self.ui.tableProveedor.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(data[8]))    
        self.ui.tableProveedor.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(data[9]))    
        self.ui.tableProveedor.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(data[10]))    
        self.ui.tableProveedor.setItem(rowPosition , 11, QtWidgets.QTableWidgetItem(data[11]))    
        
            
            
    
    def open_alta_proveedor(self,checked):
        self.w = AnadirProveedor()
        self.w.show()
    
   
    def filtro_checks(self):
        self.ui.tableProveedor.setRowCount(0)
        self.serv_filtro = self.ui.comboFiltro.currentText()
        if self.serv_filtro == "All":
            self.serv_filtro = ""
        bdserv=BdStd()
        bdserv.runsql(f"SELECT * FROM proveedores WHERE servicio LIKE '%{self.serv_filtro}%'")
        if bdserv.rows != None :
            for fila in bdserv.rows :
                self.load_one(fila)
     
    def checkFocus(self):
        if self.isActiveWindow():
            self.filtro_checks()
          
                     
        
    def eliminar(self):
        
        clave = self.ui.tableProveedor.item(self.row,0).text()
        print(clave)
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Quiere eliminar a " + self.ui.tableProveedor.item(self.row,1).text()  + "? ", qm.Yes | qm.No)
        
        if ret == qm.Yes:
            #-------------- Borrar el registro
            print("Voy a borrar ", clave)
            bd = BdStd()
            bd.runsql("DELETE FROM proveedores WHERE id_proveedor = '" + clave + "'")
            if bd.rows != None :
                print("Ha borrado a ", clave)                
                self.ui.tableProveedor.removeRow(self.row)
        else:
            print("No borro ", clave)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    consulta_proveedor= ConsultaProveedor(app)
    consulta_proveedor.show()
    sys.exit(app.exec_())
        
       
        
    
        
        
        
        
        
