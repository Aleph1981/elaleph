# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:17:25 2021

@author: aleja
"""
from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from hojadebolos_ui import *
from bdstd import BdStd
from openpyxl import Workbook
from openpyxl import load_workbook
from bdstd import *
from datetime import timedelta, datetime
import datetime

class HojaBolos(QtWidgets.QDialog, HojaBolos_Ui):
    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = HojaBolos_Ui()
        self.ui.setupUi(self)
        self.year = datetime.datetime.today().year
        for i in range (0,5):
            self.ui.comboAnyo.addItem(str(self.year-i))
        self.dic_meses={"Enero":"-01","Febrero":"-02","Marzo":"-03","Abril":"-04",\
                        "mayo":"-05","Junio":"-06","Julio":"-07","Agosto":"-08",\
                        "Septiembre":"-09","Octubre":"-10","Noviembre":"-11","Diciembre":"12"}
        
        self.ui.comboBox_2.activated.connect(self.load_tabla)
        self.ui.tablePersonal.setColumnCount(3)
        self.ui.tablePersonal.setHorizontalHeaderLabels(["ID","Nombre","Apellidos"])
        self.ui.tablePersonal.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tablePersonal.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tablePersonal.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.ui.tablePersonal.verticalHeader.hide()
        self.ui.buttoCrearIndi.clicked.connect(self.crear_indi)
        self.ui.buttoCrearMulti.clicked.connect(self.crear_multi)
        
    def load_tabla(self):
        self.ui.tablePersonal.setRowCount(0)
        self.year=self.ui.comboAnyo.currentText()
        self.mes=self.ui.comboBox_2.currentText()
        self.mes_num=self.dic_meses[self.mes]
        self.fecha=f"{self.year}{self.mes_num}"
        bd=BdStd()
        bd.runsql(f"SELECT pe.id_personal,fecha,nombre,apellidos FROM personal_evento as pe,\
                  personal as per WHERE fecha LIKE '{self.fecha}%' AND  pe.id_personal=per.id_personal GROUP BY pe.id_personal")
        if bd.rows != None:
            for row in bd.rows:
                rowPosition = self.ui.tablePersonal.rowCount()
                self.ui.tablePersonal.insertRow(rowPosition)
                self.ui.tablePersonal.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.tablePersonal.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tablePersonal.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(row[3]))
                
    def crear_indi(self):
        row=self.ui.tablePersonal.currentRow()
        print(row)
        if row >= 0:
            self.id_personal=self.ui.tablePersonal.item(row,0).text()
            print(self.id_personal)
            self.crear_hoja()
            
    def crear_multi(self):              
        rows=self.ui.tablePersonal.rowCount()
        for i in range (0,rows):
            self.id_personal=self.ui.tablePersonal.item(i,0).text()
            self.crear_hoja()
            
    def crear_hoja(self):
        wb = load_workbook(filename = r"C:\Users\aleja\Desktop\Programacion\elaleph\hojadebolos.xlsx")
        ws1 = wb.active
        bd = BdStd()
        
        #self.id_personal="ALPE48"
        #self.fecha="2021-02"
        ws1.title = "Hoja de bolos"
        
        bd.runsql(f"""SELECT pe.id_personal, per.nombre, per.apellidos, pe.fecha, pe.id_evento, ev.nombre, ma.nombre, ma.apellidos, pe.id_cargo, ca.nombre, ta.tarifa, suplemento  
        FROM personal_evento as pe JOIN evento as ev JOIN tarifas as ta JOIN personal as per JOIN managers as ma JOIN cargos as ca
        WHERE pe.id_evento=ev.id_evento AND pe.id_cargo=ta.id_cargo AND pe.id_personal='{self.id_personal}' AND ta.id_personal=pe.id_personal 
        AND ca.id_cargo=ta.id_cargo and ta.id_personal=pe.id_personal AND ma.id_manager=ev.id_manager AND per.id_personal=pe.id_personal
        AND pe.fecha LIKE '{self.fecha}%';""")
        
        nombreapell=bd.rows[0][1]+bd.rows[0][2]
        ws1["C5"]=nombreapell
        ws1["C6"]=self.fecha
        
        if bd.rows != None:
            i=0
            for row in bd.rows:
                
                ws1[f"A{9+i}"]=row[3]
                ws1[f"B{9+i}"]=row[4]
                ws1[f"C{9+i}"]=row[5]
                ws1[f"D{9+i}"]=row[6]+row[7]
                ws1[f"E{9+i}"]=row[9]
                ws1[f"F{9+i}"]=row[10]
                ws1[f"G{9+i}"]=row[11]
                i+=1
                
        
        
        wb.save(f"hojadebolos-{nombreapell}-{self.fecha}.xlsx")
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = HojaBolos()
    ui.show()
    sys.exit(app.exec_())
