# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:54:40 2021

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from crearevento_ui import *
from bdstd import BdStd
from projectmanagers import *
from recintos import *

class CrearEvento(QtWidgets.QDialog, CrearEvento_Ui):
    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = CrearEvento_Ui()
        self.ui.setupUi(self)


#------------------------------------------------------------------------------
#-------------------------PÁGINA DE DATOS--------------------------------------
#------------------------------------------------------------------------------
        self.ui.buttonAddRecinto.clicked.connect(self.addRecinto)
        self.ui.buttonAddManager.clicked.connect(self.addManager)
        self.ui.comboBox_2.addItem("Ciudad")
        bd = BdStd()
        bd.runsql("SELECT ciudad FROM recintos;")
        ciudades = []
        if bd.rows != None :
              for ciudad in bd.rows :
                 ciudades.append(ciudad)
        ciudades.sort()
        if len(ciudades) > 0:
            for ciudad in ciudades:
                  self.ui.comboBox_2.addItem(ciudad[0])
        
        bd.runsql(f"SELECT nombre FROM recintos WHERE ciudad = '{self.ui.comboBox_2.currentText()}';")
        if bd.rows != None :
              for recinto in bd.rows :
                 self.ui.comboBox.addItem("Recintos")
        bd.runsql(f"SELECT nombre, apellidos FROM managers;")
        if bd.rows != None :
              for nombre in bd.rows :
                 self.ui.combo_manager.addItem(f"{nombre[0]}{nombre[1]}")
                 print (f"{nombre[0]} {nombre[1]}")
                 
        self.ui.button_guardar.clicked.connect(self.guardarDatos)
        self.ui.comboBox_2.currentIndexChanged['QString'].connect(self.updateCombo)
        
        
#------------------------------------------------------------------------------
#-------------------------PÁGINA DE FECHAS-------------------------------------
#------------------------------------------------------------------------------
        
#-------------------------Esconder y activar botones---------------------------
        
        
        self.ui.fechas_table.hide()
        self.ui.frame.hide()
        self.ui.combo_tarea.activated['QString'].connect(self.activaAdd)
        self.ui.buttonAddDate.clicked.connect(self.addDate)
        self.ui.calendar.clicked.connect(self.showFrame)
        self.ui.fechas_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.fechas_table.setSelectionBehavior(self.ui.fechas_table.SelectRows)
        self.ui.fechas_table.hideColumn(3)
        self.ui.fechas_table.clicked.connect(self.activaDel)
       
        

        

        
#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PERSONAL-----------------------------------
#-----------------------------------------------------------------------------



        
        
#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PROVEEDORES--------------------------------
#----------------------------------------------------------------------------- 



            
#-------------------FUNCIONES PAGINA DATOS-------------------------------------

    def addRecinto(self):
        self.w = Recintos()
        self.w.show()
    def addManager(self):
        self.w = ProjectManagers()
        self.w.show()
    def updateCombo(self):
        self.ui.comboBox.clear()
        bd = BdStd()
        bd.runsql(f"SELECT nombre FROM recintos WHERE ciudad = '{self.ui.comboBox_2.currentText()}';")
        if bd.rows != None :
              for recinto in bd.rows :
                 self.ui.comboBox.addItem(recinto[0])
        
    def guardarDatos(self):
        bd = BdStd()
        bd.runsql(f"""SELECT id_recinto FROM recintos WHERE 
                  nombre = '{self.ui.comboBox.currentText()}' AND 
                  ciudad = '{self.ui.comboBox_2.currentText()}'""")
        id_recinto = bd.rows[0][0]
        manager = self.ui.combo_manager.currentText().split(" ")
        nombre_manager = manager[0]
        apellidos_manager = manager[1]
        bd.runsql(f"""SELECT id_manager FROM managers WHERE nombre='{nombre_manager} '
                  AND apellidos = '{apellidos_manager} '""")
        id_manager = bd.rows[0][0]
        campos_datos = (self.ui.entry_id.text().upper(), self.ui.entry_nombre.text()\
                        ,self.ui.entry_cliente.text().capitalize(), self.ui.entry_onsite.text()\
                        ,self.ui.entry_tfn_onsite.text(),self.ui.entry_email_onsite.text().lower()\
                        , id_recinto, id_manager, self.ui.entry_notas.toPlainText())
        bd.runsql("INSERT INTO evento (id_evento,nombre,cliente,contacto_onsite,\
                  telefono_onsite,email_onsite,id_recinto,id_manager,notas) VALUES\
                  (?,?,?,?,?,?,?,?,?);", campos_datos)
        
        self.ui.tabWidget.setCurrentIndex(1)
        
#-------------------FUNCIONES PAGINA FECHAS------------------------------------

    def activaAdd(self):
        self.ui.buttonAddDate.setEnabled(True)
    def showFrame(self):
        self.ui.frame.show()
        
    def addDate(self):
        
        date = self.ui.calendar.selectedDate()
        date = date.toString("dd-MM-yyyy")
        time = self.ui.time.time()
        time = time.toString("hh:mm")
        tarea = self.ui.combo_tarea.currentText()
        id_evento = self.ui.entry_id.text().upper()
        id_dias_evento = f"{id_evento}{date}{tarea}"
        campos_fecha = (id_dias_evento,id_evento,date,time,tarea)
        #----------Guarda la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        bd.runsql("""INSERT INTO dias_evento (id_dias_evento,id_evento,fecha,
                  hora,tarea) VALUES (?,?,?,?,?);""",campos_fecha)
        
        #----------Muestra las fechas en la tabla------------------------------
        
        self.loadData(id_evento)
        self.ui.fechas_table.show()
    def loadData(self,id_evento):
        bd = BdStd()
        bd.runsql(f"""SELECT fecha, hora, tarea, id_dias_evento FROM dias_evento
                  WHERE id_evento = '{id_evento}'""")
        if bd.rows != None :
            for row in bd.rows :
                self.load_one(row)
                
    def load_one(self, data):
        rowPosition = self.ui.fechas_table.rowCount()
        self.ui.fechas_table.insertRow(rowPosition)
        self.ui.fechas_table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(data[0]))
        self.ui.fechas_table.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
        self.ui.fechas_table.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[2]))
        self.ui.fechas_table.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[3]))
        
        
    def activaDel(self):    
        self.ui.buttonDelDate.setEnabled(True)   
        
#---------------FUNCIONES PÁGINA PERSONAL--------------------------------------
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CrearEvento()
    ui.show()
    sys.exit(app.exec_())