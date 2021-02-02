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

from datetime import timedelta, datetime
import datetime


#-------------------Clase del menu principal-----------------------

class MenuPrincipal(QtWidgets.QMainWindow, MenuPrincipal_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
    
    #------------------Ajuste de las columnas a la tabla-----------------------
    
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    
    
    #-------------------Acciones del menu------------------------------------------
        
        self.action_consultar_personal.triggered.connect(self.open_consultar_personal)
        self.action_alta_personal.triggered.connect(self.open_alta_personal)
        self.actionProject_Managers.triggered.connect(self.open_project_managers)
        self.action_consultar_proveedor.triggered.connect(self.open_consultar_proveedor)
        self.action_alta_proveedor.triggered.connect(self.open_alta_proveedor)
        self.action_alta_recinto.triggered.connect(self.open_alta_recinto)
        self.action_crear_evento.triggered.connect(self.open_crear_evento)
        self.action_consultar_evento.triggered.connect(self.open_consultar_evento)
        
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
    
    #--------------DOBLE CLICK EN CELDA---------------------------------------
        
        self.tableWidget.cellDoubleClicked.connect(self.openEvento)
        
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
        print(self.seven_days)
        self.loadData(self.seven_days)
        
    #-------Cargar los datos---------------------------------------------------
    
    def loadData(self,dias):
        bd=BdStd()
        self.tableWidget.setRowCount(0)       #<------ mere added
        self.tableWidget.insertRow(0)
        maxrow = 0
        columna = 0                             # mere columna del dia
        for fecha in dias: 
            # mere --------------- cambiado todo lo de abajo
            texto = ""
            bd.runsql(f"""SELECT di.id_evento, nombre, tarea, fecha FROM dias_evento as di
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
                fila+=1
            columna +=1
                      
        
                
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
        id_evento = self.tableWidget.item(row,col).text()
        id_evento = id_evento.split()
        id_evento = id_evento[0]
        self.w = FichaEvento(id_evento)
        self.w.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MenuPrincipal()
    window.show()
    app.exec_()