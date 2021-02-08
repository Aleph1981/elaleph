# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:27:24 2020

@author: aleja
"""
from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from menuprincipal_ui import *
from consultapersonal import *
from anadirpersonal import *
from consultaproveedor import *
from anadirproveedor import *
from crearevento import *
from projectmanagers import *
from recintos import *
from consultaeventos import *
from bdstd import *
from fichaevento import *
from hojadebolos import *
from datetime import timedelta, datetime
import datetime


#-------------------Clase del menu principal-----------------------

class MenuPrincipal(QtWidgets.QMainWindow, MenuPrincipal_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
    
    #------------------Ajuste de las columnas a la tabla-----------------------
    
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    
    #-------------------Botones colorear---------------------------------------
    
        self.buttonSinConf.clicked.connect(self.set_reserva)
        self.buttonPersonal.clicked.connect(self.set_personal)
        self.buttonProveedor.clicked.connect(self.set_proveedor)
        self.buttonCerrado.clicked.connect(self.set_cerrado)
    
    #-------------------Acciones del menu------------------------------------------
        
        self.action_consultar_personal.triggered.connect(self.open_consultar_personal)
        self.action_alta_personal.triggered.connect(self.open_alta_personal)
        self.actionProject_Managers.triggered.connect(self.open_project_managers)
        self.action_consultar_proveedor.triggered.connect(self.open_consultar_proveedor)
        self.action_alta_proveedor.triggered.connect(self.open_alta_proveedor)
        self.action_alta_recinto.triggered.connect(self.open_alta_recinto)
        self.action_crear_evento.triggered.connect(self.open_crear_evento)
        self.action_consultar_evento.triggered.connect(self.open_consultar_evento)
        self.action_crear_hoja_de_bolos.triggered.connect(self.open_crear_hoja_bolos)
        
        self.buttonNext1.clicked.connect(self.nextDay1)
        self.buttonPrev1.clicked.connect(self.prevDay1)
        self.buttonNext7.clicked.connect(self.nextDay7)
        self.buttonPrev7.clicked.connect(self.prevDay7)
        self.buttonNext30.clicked.connect(self.nextDay30)
        self.buttonPrev30.clicked.connect(self.prevDay30)
        
    #---------------Calendario Semanal-----------------------------------------
        
        self.hoy = datetime.date.today()
        self.j=0
        
        for i in range(0,7):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(f"{date.strftime(self.hoy+timedelta(days=i), '%A %d-%m-%Y')}")
        
        self.tableWidget.insertRow(0)
        self.getSevenDays()
    
    #--------------CLICKS EN CELDA---------------------------------------
        
        self.tableWidget.cellDoubleClicked.connect(self.openEvento)
        self.tableWidget.cellClicked.connect(self.find_item)
    #--------------Suma y resta de días------------------------------ mere cambiado hoy por self.hoy       
    def nextDay1(self):
        self.j += 1
        for i in range(0,7):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(f"{date.strftime(self.hoy+timedelta(days=i + self.j), '%A %d-%m-%Y')}")
        self.getSevenDays()    
    
    def prevDay1(self):
        self.j -= 1
        for i in range(0,7):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(f"{date.strftime(self.hoy+timedelta(days=i + self.j), '%A %d-%m-%Y')}")
        self.getSevenDays() 
        
    def nextDay7(self):
        self.j += 7
        for i in range(0,7):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(f"{date.strftime(self.hoy+timedelta(days=i + self.j), '%A %d-%m-%Y')}")
        self.getSevenDays()
        
    def prevDay7(self):
        self.j -= 7
        for i in range(0,7):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(f"{date.strftime(self.hoy+timedelta(days=i + self.j), '%A %d-%m-%Y')}")
        self.getSevenDays()
        
    def nextDay30(self):
        self.j += 30
        for i in range(0,7):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(f"{date.strftime(self.hoy+timedelta(days=i + self.j), '%A %d-%m-%Y')}")
        self.getSevenDays()
        
    def prevDay30(self):
        self.j -= 30
        for i in range(0,7):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(f"{date.strftime(self.hoy+timedelta(days=i + self.j), '%A %d-%m-%Y')}")
        self.getSevenDays()
 
    #------Obtener los días mostrados en el calendario y cargar los datos------
        
    def getSevenDays(self):
        self.seven_days=[]
        for i in range(0,7):    
            day = self.tableWidget.horizontalHeaderItem(i).text()
            day=day.split()
            day = day[1]
            self.seven_days.append(day)
        self.loadData(self.seven_days)
        
    #-------Cargar los datos---------------------------------------------------
    
    def loadData(self,dias):
        bd=BdStd()
        self.tableWidget.setRowCount(0)       #<------ mere added
        self.tableWidget.insertRow(0)
        maxrow = 0
        columna = 0                             # mere columna del dia
        for dia in dias: 
            # mere --------------- cambiado todo lo de abajo
            fecha= bd.gira_fecha(dia)
            texto = ""
            bd.runsql(f"""SELECT di.id_evento, nombre, tarea, fecha, estado FROM dias_evento as di
                      JOIN evento as ev ON di.id_evento = ev.id_evento WHERE di.fecha='{fecha}';""")
            fila = 0
            #----------Mostrar los datos en la tabla-----------------------------------
            for row in bd.rows:
                if fila > maxrow :
                    #------ crea una file nueva
                    self.tableWidget.insertRow(fila)       # mere crea linea para detalle
                    maxrow = fila
                texto =  row[0] + " " +  row[1] +" " + row[2] + "\n"
                self.tableWidget.setItem(fila, columna, QtWidgets.QTableWidgetItem(texto))
                if row[4] == "reserva":
                    self.tableWidget.item(fila,columna).setBackground(QtGui.QColor(255, 0, 255,180))
                elif row[4] == "personal":
                    self.tableWidget.item(fila,columna).setBackground(QtGui.QColor(255, 0, 0,180))
                elif row[4] == "proveedor":
                    self.tableWidget.item(fila,columna).setBackground(QtGui.QColor(0, 75, 255,180))
                elif row[4] == "cerrado":
                    self.tableWidget.item(fila,columna).setBackground(QtGui.QColor(74,222, 0,180))
                fila+=1
            columna +=1
            
        
    def find_item(self):
        
        bd=BdStd()
        bd.runsql("SELECT tarea FROM dias_evento GROUP BY tarea")
        tareas=[]
        if bd.rows!= None:
            for fila in bd.rows:
                tareas.append(fila[0])
        row=self.tableWidget.currentRow()
        col=self.tableWidget.currentColumn()
        if self.tableWidget.item(row,col):
            evento=self.tableWidget.item(row,col).text()
            dia = self.tableWidget.horizontalHeaderItem(col).text()
            dia = dia.split()
            dia=bd.gira_fecha(dia[1])
            evento=evento.split()
            tarea=""
            for item in evento:
                if item in tareas:
                    tarea=item
            print(evento)
            self.id_dias_evento=evento[0]+dia+tarea
            print("id_dias_evento = ",self.id_dias_evento )
            return self.id_dias_evento  
        
    
    def set_reserva(self):
        bd1=BdStd()
        bd1.runsql(f"UPDATE dias_evento SET estado = 'reserva' WHERE id_dias_evento = '{self.id_dias_evento}';")
        self.getSevenDays()
        print(f"reserva para id {self.id_dias_evento}")
    def set_personal(self):
        bd1=BdStd()
        bd1.runsql(f"UPDATE dias_evento SET estado = 'personal' WHERE id_dias_evento = '{self.id_dias_evento}';")
        self.getSevenDays()
        print(f"reserva para id {self.id_dias_evento}")
        
    def set_proveedor(self):
        bd1=BdStd()
        bd1.runsql(f"UPDATE dias_evento SET estado = 'proveedor' WHERE id_dias_evento = '{self.id_dias_evento}';")
        self.getSevenDays()
        print(f"reserva para id {self.id_dias_evento}")
        
    def set_cerrado(self):
        bd1=BdStd()
        bd1.runsql(f"UPDATE dias_evento SET estado = 'cerrado' WHERE id_dias_evento = '{self.id_dias_evento}';")
        self.getSevenDays()
        print(f"reserva para id {self.id_dias_evento}")
    
#-------------------Funciones para abrir nuevas ventanas-----------------------
       
    def open_alta_personal(self, checked):
        self.w = AnadirPersonal()
        self.w.show()
    def open_consultar_personal(self,checked):
        self.w = ConsultaPersonal(app)
        self.w.show()
    def open_project_managers(self,checked):
        self.w = ProjectManagers()
        self.w.show()
    def open_alta_proveedor(self,checked):
        self.w = AnadirProveedor()
        self.w.show()
    def open_consultar_proveedor(self,checked):
        self.w = ConsultaProveedor()
        self.w.show()
    def open_alta_recinto(self,checked):
        self.w = Recintos()
        self.w.show()
    
    def open_crear_evento(self,checked):
        self.w = CrearEvento()
        self.w.show()
        
    def open_consultar_evento(self,checked):
        self.w = ConsultaEventos()
        self.w.show()
    
    def openEvento(self,row,col):
        if self.tableWidget.item(row,col):
            id_evento = self.tableWidget.item(row,col).text()
            id_evento = id_evento.split()
            id_evento = id_evento[0]
            self.w = FichaEvento(id_evento)
            self.w.show()
    def open_crear_hoja_bolos(self):
        self.w = HojaBolos()
        self.w.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MenuPrincipal()
    window.show()
    app.exec_()