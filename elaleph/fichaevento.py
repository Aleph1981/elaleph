# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:56:17 2021

@author: aleja
"""
from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from fichaevento_ui import *
from bdstd import BdStd
from crearevento import *

class FichaEvento(QtWidgets.QDialog, FichaEvento_Ui):
    
    def __init__(self,id_evento):
        QtWidgets.QDialog.__init__(self)
        self.ui = FichaEvento_Ui()
        self.ui.setupUi(self)
        self.id_evento=id_evento
        self.loadDataDatos(id_evento)
        self.loadDataFechas(id_evento)
        self.ui.tableFechas.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableFechas.setSelectionBehavior(self.ui.tableFechas.SelectRows)
        self.ui.buttonEditar.clicked.connect(self.openEvento)
        print(id_evento)
#-----Abre la ventana de crear evento con los datos precargados para esa id----
      
    def openEvento(self):        
        self.w = CrearEvento(self.id_evento)
        self.w.show()
        print("ficha",id_evento)
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
            bd.runsql(f"""SELECT fecha, hora, tarea FROM dias_evento WHERE id_evento = '{id_evento}';""")
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
   
        
        
        
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FichaEvento("JB1243")
    ui.show()
    sys.exit(app.exec_())