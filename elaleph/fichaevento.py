# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:56:17 2021

@author: aleja
"""
from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from fichaevento_ui import *
from bdstd import BdStd
from crearevento import *

class FichaEvento(QtWidgets.QWidget, FichaEvento_Ui):
    
    def __init__(self,id_evento):
        QtWidgets.QWidget.__init__(self)
        self.ui = FichaEvento_Ui()
        self.ui.setupUi(self)
        self.id_evento=id_evento
        self.loadDataDatos(id_evento)
        self.loadDataFechas(id_evento)
        self.ui.tableFechas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableFechas.setSelectionBehavior(self.ui.tableFechas.SelectRows)
        self.ui.tableFechas.setSortingEnabled(True)
        self.ui.tableFechas.verticalHeader().hide()
        self.ui.tableFechas.clicked.connect(self.filtro_fechas)
        self.ui.tablePersonal.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tablePersonal.setSelectionBehavior(self.ui.tablePersonal.SelectRows)
        self.ui.tablePersonal.setSortingEnabled(True)
        self.ui.tablePersonal.setColumnCount(11)
        self.ui.tablePersonal.setHorizontalHeaderLabels([ "Fecha", "Cargo", "ID","Nombre", "Apellidos",  
                                  "Suplemento", "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas"])
        self.ui.tablePersonal.verticalHeader().hide()
        self.ui.tableProveedores.setColumnCount(11)
        self.ui.tableProveedores.setHorizontalHeaderLabels([ "Fecha", "Cargo", "ID","Nombre", "Apellidos",  
                                  "Suplemento", "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas"])
        self.ui.tableProveedores.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableProveedores.setSelectionBehavior(self.ui.tableProveedores.SelectRows)
        self.ui.tableProveedores.setSortingEnabled(True)
        self.ui.tableProveedores.verticalHeader().hide()
        self.ui.buttonEditar.clicked.connect(self.openEvento)
        self.load_personal()
        self.load_proveedor()
        
        
        
        
    def filtro_fechas(self):
        row=self.ui.tableFechas.currentRow()
        fecha= self.ui.tableFechas.item(row,0).text()
        hora=self.ui.tableFechas.item(row,1).text()
        self.load_personal(fecha,hora)
        self.load_proveedor(fecha,hora)
        
#-----Abre la ventana de crear evento con los datos precargados para esa id----
      
    def openEvento(self):        
        self.w = CrearEvento(self.id_evento)
        self.w.show()
        self.close()
        #print("ficha",id_evento)
#---------Carga los datos para los inputs--------------------------------------        
    def loadDataDatos(self,id_evento):                 
    
        if self.id_evento == None :
            data = []
            self.load_one(data)
        else :
            bd = BdStd()
            bd.runsql(f"""SELECT * FROM evento WHERE id_evento = '{id_evento}';""")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadInputs(row)
                      
#----------Muestra los datos anteriormente cargados en los inputs--------------

    def loadInputs(self, data):
        self.ui.inputId.setText(data[0])
        self.ui.inputNombre.setText(data[1])
        self.ui.inputCliente.setText(data[2])
        self.ui.inputContacto.setText(data[3])
        self.ui.inputTelefono.setText(data[4])
        self.ui.inputEmail.setText(data[5])
        bd=BdStd()
        bd.runsql(f"SELECT nombre, ciudad FROM recintos WHERE id_recinto = '{data[6]}';")
        print(bd.rows)
        self.ui.inputRecinto.setText(f"{bd.rows[0][0]}- {bd.rows[0][1]}")
        bd.runsql(f"SELECT nombre, apellidos FROM managers WHERE id_manager = '{data[7]}';")
        self.ui.inputManager.setText(f"{bd.rows[0][0]}{bd.rows[0][1]}")
        self.ui.inputNotas.setPlainText(data[8])

#-----------Carga los datos para la tabla de fechas---------------------------
        
    def loadDataFechas(self,id_evento):                 
    
        if self.id_evento == None :
            data = []
            self.loadFechas(data)
        else :
            bd = BdStd()
            bd.runsql(f"""SELECT strftime('%d-%m-%Y', fecha), hora, tarea, id_dias_evento FROM dias_evento 
                      WHERE id_evento = '{id_evento}' ORDER BY fecha;""")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadFechas(row)
#-----------Muestra los datos en la tabla de fechas----------------------------
                    
    def loadFechas(self, data):
     rowPosition = self.ui.tableFechas.rowCount()
     self.ui.tableFechas.insertRow(rowPosition)
     self.ui.tableFechas.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[0]))
     self.ui.tableFechas.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
     self.ui.tableFechas.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[2]))
     self.ui.tableFechas.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[3]))
#---------Muestra los datos del personal---------------------------------------    
   
    def load_personal(self,fecha=None,hora=None):
        print(self.id_evento)
        bd=BdStd()
        txtsql=f"""SELECT strftime('%d-%m-%Y',fecha)||" "||hora, cargos.nombre, pev.id_personal, p.nombre, p.apellidos, 
                  suplemento, dni, telefono, email, autonomo, notas
                  FROM personal_evento as pev
                  JOIN personal as p ON p.id_personal = pev.id_personal
                  JOIN cargos ON cargos.id_cargo = pev.id_cargo 
                  WHERE id_evento = '{self.id_evento}'"""
        if fecha != None:
            txtsql += f" AND strftime('%d-%m-%Y',fecha)='{fecha}' AND hora = '{hora}'"
            
        bd.runsql(txtsql)
        
        self.ui.tablePersonal.setRowCount(0)
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.tablePersonal.insertRow(i)
                for j, data in enumerate(row_data):
                    self.ui.tablePersonal.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
    
#--------Muestra los datos de los proveedores----------------------------------   
    
    def load_proveedor(self,fecha=None,hora=None):        
        self.ui.tableProveedores.setRowCount(0)
        if self.id_evento == None :
            return
                    
        bd=BdStd()
        txtsql = f"""SELECT strftime('%d-%m-%Y',fecha)||" "||hora, pre.servicio, pre.id_proveedor,  \
                  p.provincia, contacto_onsite, telefono_onsite, email_onsite, pre.notas \
                  FROM proveedores_evento as pre \
                  JOIN proveedores as p ON  p.id_proveedor = pre.id_proveedor WHERE id_evento='{self.id_evento}' """
        if fecha != None:
            txtsql += f" AND strftime('%d-%m-%Y',fecha)='{fecha}' AND hora = '{hora}'"
    
        bd.runsql(txtsql)
    
        if bd.rows != None :
            
            for i, row_data in enumerate(bd.rows):
                self.ui.tableProveedores.insertRow(i)
                
                for j, data in enumerate(row_data):
                    if j==0:
                        self.ui.tableProveedores.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        self.ui.tableProveedores.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
    
        
        
        
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FichaEvento("JB-356-2021")
    ui.show()
    sys.exit(app.exec_())