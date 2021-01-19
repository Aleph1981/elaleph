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
        app.focusChanged.connect(self.checkFocus)
        


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
        self.ui.buttonAddDate.clicked.connect(self.addDate)
        self.ui.fechas_table.hide()
        self.ui.frame.hide()
        self.ui.fechas_table.setSelectionBehavior(self.ui.fechas_table.SelectRows)
        self.ui.fechas_table.clicked.connect(self.activaDel)
        self.ui.combo_tarea.activated['QString'].connect(self.activaAdd)


        
#-----------Escribe la cabecera de la tabla de fechas--------------------------
        
        self.ui.fechas_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal , "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal , "Fecha")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal , "Hora prevista")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal , "Tarea")
        self.ui.fechas_table.hideColumn(0)
#-----------Carga el modelo en el table view-----------------------------------
        
        
        self.sql = 'SELECT id_dias_evento, fecha, hora, tarea  FROM dias_evento;'
        self.model.setQuery(self.sql)
        self.ui.fechas_table.setModel(self.model)
        
#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PERSONAL-----------------------------------
#-----------------------------------------------------------------------------        
        self.model = QtSql.QSqlQueryModel(self)
        self.sql = 'SELECT personal.id_personal, personal.nombre, apellidos, dni, \
               telefono, email, autonomo, notas FROM personal'
        self.model.setQuery(self.sql)
        self.ui.personal_table.setModel(self.model)
        self.ui.personal_table.setSelectionBehavior(self.ui.personal_table.SelectRows)
        
#-------------Escribe la cabecera de la tabla----------------------------------

        self.model.setHeaderData(0, QtCore.Qt.Horizontal , "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal , "Nombre")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal , "Apellidos")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal , "DNI")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal , "Teléfono")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal , "Email")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal , "Autónomo")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal , "Notas")
        
#-------Si el combobox se activa llama a la funcion de filtrado----------------

        self.ui.combo_filtrar_cargos.activated[str].connect(self.filtro_checks)

#------Función de filtrado----------------------------------------------------       
    
    def filtro_checks(self,text):
        self.sql = 'SELECT personal.id_personal, nombre, apellidos, dni,telefono, email, \
        autonomo, notas FROM personal,tarifas \
        WHERE tarifas.id_personal=personal.id_personal'
        
        sigue=''
        if text == "ALL":
            self.sql = 'SELECT * FROM personal'
            
        if text == "Crew Chief":
             sigue += ' AND tarifas.id_cargo = "001"'
             
        if text == "Operador de Luces":
             sigue += ' AND tarifas.id_cargo = "002"'
             
        if text == "Dimmers":
             sigue += ' AND tarifas.id_cargo = "003"'
             
        if text == "Técnico Luces":
             sigue += ' AND tarifas.id_cargo = "004"'
             
        if text == "Operador Sonido":
             sigue += ' AND tarifas.id_cargo = "006"'
             
        if text == "RF":
             sigue += ' AND tarifas.id_cargo = "007"'
             
        if text == "Técnico de Sonido":
            sigue += ' AND tarifas.id_cargo = "008"'
        
        if text == "Operador de Video":
            sigue += ' AND tarifas.id_cargo = "010"'
            
        if text == "LED":
            sigue += ' AND tarifas.id_cargo = "011"'
            
        if text == "Técnico de Video":
            sigue += ' AND tarifas.id_cargo = "012"'
            
        if text == "Contenidos":
            sigue += ' AND tarifas.id_cargo = "013"'
            
        if text == "Regidor":
            sigue += ' AND tarifas.id_cargo = "009"'
        
        if text == "Rigger":
            sigue += ' AND tarifas.id_cargo = "005"'
            
        if text == "Deco":
            sigue += ' AND tarifas.id_cargo = "014"'
            
            
        self.sql += sigue
        self.model.setQuery(self.sql)
        print(self.sql)
        #self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.ui.personal_table.setModel(self.model)
#-------------------FUNCIONES GENERALES----------------------------------------

    def checkFocus(self):
        if self.isActiveWindow():
            self.refresca_grid()
            
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

#-------------------FUNCIONES PAGINA FECHAS------------------------------------



        
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
        
        #----------Genera el modelo para la tabla de fechas--------------------
        
        self.model = QtSql.QSqlQueryModel(self)
        self.sql = 'SELECT fecha, hora, tarea  FROM dias_evento;'
        self.model.setQuery(self.sql)
        self.ui.fechas_table.setModel(self.model)
            
    def activaAdd(self):
        self.ui.buttonAddDate.setEnabled(True)
        
    def activaDel(self):    
        self.ui.buttonDelDate.setEnabled(True)   
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CrearEvento()
    ui.show()
    sys.exit(app.exec_())