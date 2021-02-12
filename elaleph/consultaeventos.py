# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:05:18 2021

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from consultaeventos_ui import *
from bdstd import BdStd
from fichaevento import *
import datetime
from hojadeestilos import *

class ConsultaEventos(QtWidgets.QWidget, ConsultaEventos_Ui):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = ConsultaEventos_Ui()
        self.ui.setupUi(self)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        year = datetime.date.today().year
        for i in range(0,5):
            self.ui.comboYear.addItem(f"{year-i}")
        self.ui.comboYear.activated.connect(self.loadData)
        self.loadData()
        
        #---------------ordenar por columnas-----------------------------------
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectRows)
        self.ui.tableWidget.cellDoubleClicked.connect(self.openEvento)
        self.ui.tableWidget.verticalHeader().hide()
    def loadData(self):
        self.ui.tableWidget.setRowCount(0)
        filtroYear = self.ui.comboYear.currentText()
        
        if filtroYear == "Año" :
            bd = BdStd()
            bd.runsql(f"""SELECT strftime('%d-%m-%Y', di.fecha),di.id_evento,ev.nombre,di.tarea, ev.cliente,
                      re.nombre,ma.nombre||''||ma.apellidos  FROM 
                      dias_evento as di, evento as ev, recintos as re, 
                      managers as ma WHERE ev.id_evento=di.id_evento AND 
                      re.id_recinto=ev.id_recinto AND ma.id_manager=ev.id_manager""")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadEventos(row)
                    
                    
            
        else :
            bd = BdStd()
            bd.runsql(f"""SELECT strftime('%d-%m-%Y', di.fecha),di.id_evento,ev.nombre,di.tarea,ev.cliente,
                      re.nombre,ma.nombre||''||ma.apellidos  FROM
                      dias_evento as di, evento as ev, recintos as re, 
                      managers as ma WHERE ev.id_evento=di.id_evento AND 
                      re.id_recinto=ev.id_recinto AND ma.id_manager=ev.id_manager
                      AND di.fecha LIKE '{filtroYear}%'""")
            if bd.rows != None :
                for row in bd.rows :
                    self.loadEventos(row)
                    
    def loadEventos(self, data):
         rowPosition = self.ui.tableWidget.rowCount()
         self.ui.tableWidget.insertRow(rowPosition)
         self.ui.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[0]))
         self.ui.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
         self.ui.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[2]))
         self.ui.tableWidget.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[3]))
         self.ui.tableWidget.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(data[4]))
         self.ui.tableWidget.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(data[5]))
         self.ui.tableWidget.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(data[6]))
       
    def openEvento(self,row):
        id_evento= self.ui.tableWidget.item(row,1).text()
        self.w = FichaEvento(id_evento)
        self.w.show()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ConsultaEventos()
    ui.show()
    sys.exit(app.exec_())
