# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:38:55 2021

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from hojaderuta_ui import *
from bdstd import BdStd
from openpyxl import Workbook
from openpyxl import load_workbook
from bdstd import *
from datetime import timedelta, datetime
import datetime

class HojaDeRuta(QtWidgets.QDialog, HojaDeRuta_Ui):
    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = HojaDeRuta_Ui()
        self.ui.setupUi(self)
        self.year = datetime.datetime.today().year
        for i in range (0,5):
            self.ui.comboAnyo.addItem(str(self.year-i))
        self.dic_meses={"Enero":"-01","Febrero":"-02","Marzo":"-03","Abril":"-04",\
                        "mayo":"-05","Junio":"-06","Julio":"-07","Agosto":"-08",\
                        "Septiembre":"-09","Octubre":"-10","Noviembre":"-11","Diciembre":"12"}
        
        self.ui.comboMes.activated.connect(self.load_tabla)
        self.ui.tableEventos.setColumnCount(4)
        self.ui.tableEventos.setHorizontalHeaderLabels(["ID","Nombre","Cliente","Fecha"])
        self.ui.tableEventos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableEventos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableEventos.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.ui.buttonCrear.clicked.connect(self.crear_hoja)
        
    def load_tabla(self):
        self.ui.tableEventos.setRowCount(0)
        self.year=self.ui.comboAnyo.currentText()
        self.mes=self.ui.comboMes.currentText()
        self.mes_num=self.dic_meses[self.mes]
        self.fecha=f"{self.year}{self.mes_num}"
        bd=BdStd()
        bd.runsql(f"""SELECT strftime('%d-%m-%Y', di.fecha),di.id_evento,ev.nombre,di.tarea,ev.cliente
                      FROM dias_evento as di, evento as ev
                      WHERE ev.id_evento=di.id_evento
                      AND di.fecha LIKE '{self.fecha}%' GROUP BY di.id_evento""")
        if bd.rows != None:
            for row in bd.rows:
                rowPosition = self.ui.tableEventos.rowCount()
                self.ui.tableEventos.insertRow(rowPosition)
                self.ui.tableEventos.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableEventos.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tableEventos.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(row[3])) 
                self.ui.tableEventos.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(row[0])) 
                
    def crear_hoja(self):
        row=self.ui.tableEventos.currentRow()
        if row >= 0:
            self.id_evento=self.ui.tableEventos.item(row,0).text()
            print(self.id_evento)
        
        wb = load_workbook(filename = r"C:\Users\aleja\Desktop\Programacion\elaleph\hojaderutabase.xlsx")
        ws1 = wb.active
        bd = BdStd()
        
        #self.id_personal="ALPE48"
        #self.fecha="2021-02"
        ws1.title = "Hoja de ruta"
        
        bd.runsql(f"""SELECT ev.id_evento,ev.nombre,re.nombre,re.direccion||' '|| re.ciudad,cliente,
                  contacto_onsite,telefono_onsite,email_onsite, ev.notas, ma.nombre||''||ma.apellidos
                  FROM evento as ev,recintos as re, managers as ma 
                  WHERE ev.id_evento = '{self.id_evento}' AND re.id_recinto = ev.id_recinto AND
                  ma.id_manager = ev.id_manager;""")
        print(bd.rows)
        if bd.rows!=None:
            row=bd.rows[0]
            for i in range(0,8):
                ws1[f"C{15+i}"]=row[i]
                
            
            ws1["C24"]=row[8]
            ws1["C27"]=row[9]
            
        bd.runsql(f"""SELECT id_evento, strftime('%d-%m /', MIN(fecha))
                  ||''||strftime('%d-%m-%Y', MAX(fecha)) FROM dias_evento
                  WHERE id_evento='{self.id_evento}';""")
                  
        if bd.rows!=None:
            ws1["C23"]=bd.rows[0][1]
        
        
        wb.save(f"hojaderuta-{self.id_evento}.xlsx")
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = HojaDeRuta()
    ui.show()
    sys.exit(app.exec_())