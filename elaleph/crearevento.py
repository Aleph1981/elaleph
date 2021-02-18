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
from fichapersonal import *
from personalevento import *            # mere 30-01-21 added
from proveedorevento import *

class CrearEvento(QtWidgets.QWidget, CrearEvento_Ui):
    
    def __init__(self, id_evento_parm = None):
        QtWidgets.QWidget.__init__(self)
        self.ui = CrearEvento_Ui()
        self.ui.setupUi(self)
        self.id_evento = id_evento_parm
        self.fecha = ""       
        self.hora = ""
        self.setWindowTitle("Crear/Editar Evento")
        #Escondo los vertical headers
        self.ui.fechas_table.verticalHeader().hide()
        self.ui.personal_table.verticalHeader().hide()
        self.ui.personal_added.verticalHeader().hide()
        self.ui.prov_table.verticalHeader().hide()
        self.ui.prov_added.verticalHeader().hide()
        
#------------------------------------------------------------------------------
#-------------------------PÁGINA DE DATOS--------------------------------------
#------------------------------------------------------------------------------
        self.ui.buttonAddRecinto.clicked.connect(self.addRecinto)
        self.ui.buttonAddManager.clicked.connect(self.addManager)
        self.ui.comboBox_2.addItem("Ciudad")
        bd = BdStd()
        bd.runsql("SELECT ciudad FROM recintos GROUP BY ciudad ORDER BY ciudad;")  # mere 03-02-2021
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
                 
                 
        if self.id_evento == None :       # es un alta cambia el título del formulario
            print ("cambia el título del formulario: ES UN ALTA")
        else:                            # carga datos evento
            self.load_evento(self.id_evento)
            
            
        self.ui.buttonDatosNext.clicked.connect(self.guardarDatos)  
        self.ui.comboBox_2.currentIndexChanged['QString'].connect(self.updateCombo)
        self.ui.tabWidget.currentChanged.connect(self.cambia_pestanya)
        
#------------------------------------------------------------------------------
#-------------------------PÁGINA DE FECHAS-------------------------------------
#------------------------------------------------------------------------------
        
#-------------------------Esconder y activar botones---------------------------
        
        if self.id_evento == None :       # es un alta cambia el título del formulario       
            pass
            #self.ui.fechas_table.hide()
            #self.ui.frame.hide()
        else: 
            self.load_dias_evento(self.id_evento)
        self.ui.combo_tarea.activated['QString'].connect(self.activaAdd)
        self.ui.buttonAddDate.clicked.connect(self.addDate)
        self.ui.buttonDelDate.clicked.connect(self.delDate)   # merem 30-01-21 added
        self.ui.fechas_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.fechas_table.setSelectionBehavior(self.ui.fechas_table.SelectRows)
        #self.ui.fechas_table.hideColumn(3)
        self.ui.fechas_table.clicked.connect(self.activaDel)
        self.ui.buttonFechaNext.clicked.connect(self.pasa_pagina)
        

#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PERSONAL-----------------------------------
#-----------------------------------------------------------------------------

#-------Si el combobox se activa llama a la funcion de filtrado----------------
        self.id_personal = ""     # contendrá la persona seleccionada del grid de personas
        self.nom_cargo = ""       # contendrá su cargo
        self.ui.personal_table.setSortingEnabled(True)       
        self.ui.personal_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.personal_table.setColumnCount(10)   # Alejandro cambiado 25-1 lo saco de la función si no no etiqueta el header 
        self.ui.personal_table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellidos", "Cargo",  
                                  "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas","Suplemento"])
        self.ui.personal_table.itemSelectionChanged.connect(self.tabla1_select)
        self.ui.personal_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # mere
        self.ui.personal_table.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        #self.ui.buttonPersonalNext.clicked.connect(self.pasa_pagina)
        # mere 30-01-21  comentado lo de abajo
        #self.ui.personal_table.hideColumn(0)
        
        self.loadcombo_cargos()
        self.ui.combo_filtrar_cargos.activated[str].connect(self.filtro_checks)
        self.filtro_checks("ALL")
        self.loadcombo_dias()
        self.ui.combo_dia_personal.activated[str].connect(self.filtro_dia)
        self.ui.button_add_personal.clicked.connect(self.anade_persona)
        self.ui.button_remove_personal.clicked.connect(self.quita_persona)
        self.ui.buttonBuscarPers.clicked.connect(self.filtro_checks)
        self.ui.personal_table.cellDoubleClicked.connect(self.open_ficha_personal)
        
        
        
        self.ui.personal_added.setColumnCount(10)
        self.ui.personal_added.setSortingEnabled(True)
        self.ui.personal_added.setSelectionBehavior(self.ui.personal_table.SelectRows)
        self.ui.personal_added.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.personal_added.setHorizontalHeaderLabels([ "Fecha", "Cargo", "ID","Nombre", "Apellidos",  
                                  "Suplemento", "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas"])
        #self.ui.personal_added.hideColumn(0)
        self.ui.personal_added.cellDoubleClicked.connect(self.select_pev)       
#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PROVEEDORES--------------------------------
#----------------------------------------------------------------------------- 
        
        self.id_proveedor = ""     # contendrá la persona seleccionada del grid de personas
        self.nom_servicio = ""       # contendrá su cargo
        self.ui.prov_table.setSortingEnabled(True)       
        self.ui.prov_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.prov_table.setColumnCount(14)   # Alejandro cambiado 25-1 lo saco de la función si no no etiqueta el header 
        self.ui.prov_table.setHorizontalHeaderLabels(["ID","Empresa","Provincia",\
            "Localidad","Dirección","Servicio/s","CIF","Teléfono","Email","Web",\
            "Contacto","Teléfono Contacto","Email Contacto","Notas"])
        self.ui.prov_table.itemSelectionChanged.connect(self.tabla_prov_select)
        self.ui.prov_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # mere
        self.ui.prov_table.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        # mere 30-01-21  comentado lo de abajo
        #self.ui.prov_table.hideColumn(0)
        
        self.loadcombo_cargos()
        self.ui.combo_filtrar_serv.activated[str].connect(self.filtro_prov_checks)
        self.filtro_prov_checks("ALL")
        self.loadcombo_dias()
        self.ui.combo_dia_prov.activated[str].connect(self.filtro_prov_dia)
        self.ui.button_add_prov.clicked.connect(self.anade_prov)
        self.ui.button_remove_prov.clicked.connect(self.quita_prov)
        self.ui.buttonBuscarProv.clicked.connect(self.filtro_prov_checks)
       
        
        
        
        self.ui.prov_added.setColumnCount(11)
        self.ui.prov_added.setSortingEnabled(True)
        self.ui.prov_added.setSelectionBehavior(self.ui.prov_table.SelectRows)
        self.ui.prov_added.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.prov_added.setHorizontalHeaderLabels(["fecha","Servicio", "Empresa","Provincia",\
            "Contacto","Teléfono Contacto","Email Contacto","Notas"])
        #self.ui.prov_added.hideColumn(0)

        self.ui.prov_added.cellDoubleClicked.connect(self.select_prov)       
        self.hora=""
#------------------------------------------------------------------------------
#-------------------FUNCIONES GENERALES---------------------------------------- 
#------------------------------------------------------------------------------
    def pasa_pagina(self):
        i=self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.setCurrentIndex(i+1)
        self.filtro_prov_checks("ALL")
        self.loadcombo_dias()
#------------------------------------------------------------------------------           
#-------------------FUNCIONES PAGINA DATOS-------------------------------------
#------------------------------------------------------------------------------

    def cambia_pestanya (self):
        index = self.ui.tabWidget.currentIndex()
        if index == 1 :
            # refresca grids de fechas
            self.load_dias_evento(self.id_evento)
        if index == 2 :
            # refresca grids personal
            self.loadcombo_cargos()
            self.filtro_checks("ALL")
            self.loadcombo_dias()
        if index == 3 :
            # refresca grids personal
            self.loadcombo_servicios()
            self.filtro_prov_checks("ALL")
            self.loadcombo_dias_prov()
        

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
        my_evento = self.ui.entry_id.text().upper()
        
        id_recinto = self.extraer_recinto()
        id_manager = self.extraer_manager()        


        #-------------------------------------------------------
        if self.id_evento == None :
            campos_datos = (my_evento, self.ui.entry_nombre.text()\
                        ,self.ui.entry_cliente.text().capitalize(), self.ui.entry_onsite.text()\
                        ,self.ui.entry_tfn_onsite.text(),self.ui.entry_email_onsite.text().lower()\
                        , id_recinto, id_manager, self.ui.entry_notas.toPlainText())
            bd.runsql("INSERT INTO evento (id_evento,nombre,cliente,contacto_onsite,\
                      telefono_onsite,email_onsite,id_recinto,id_manager,notas) VALUES\
                      (?,?,?,?,?,?,?,?,?);", campos_datos)
            self.id_evento = my_evento    # <---- a partir de ahora actua como modificacion
        else:
            txtsql = "UPDATE evento SET nombre = '{1}', cliente = '{2}', contacto_onsite = '{3}'," \
            "telefono_onsite = '{4}', email_onsite = '{5}', id_recinto = '{6}'," \
            "id_manager = '{7}', notas = '{8}' WHERE id_evento = '{0}'"
            txtsql = txtsql.format(my_evento, self.ui.entry_nombre.text()\
                        ,self.ui.entry_cliente.text().capitalize(), self.ui.entry_onsite.text()\
                        ,self.ui.entry_tfn_onsite.text(),self.ui.entry_email_onsite.text().lower()\
                        , id_recinto, id_manager, self.ui.entry_notas.toPlainText())
            bd.runsql(txtsql)

        
        self.ui.tabWidget.setCurrentIndex(1)
        
    def extraer_recinto(self):
        #-------------------------------------------------- extrae recinto del combo
        bdaux = BdStd()
        id_recinto = ""
        try :
            bdaux.runsql(f"""SELECT id_recinto FROM recintos WHERE 
                      nombre = '{self.ui.comboBox.currentText()}' AND 
                      ciudad = '{self.ui.comboBox_2.currentText()}'""")
            if bdaux.rows != None and len(bdaux.rows) > 0 :
                id_recinto = bdaux.rows[0][0]
        except:
            print("error extraer_recinto:", sys.exc_info())
        return (id_recinto)
    
    def posiciona_recinto(self, id_recinto):
        #-------------------------------------------------- coloca combo en ciudad y  recinto
        bd1 = BdStd()
        try :
            bd1.runsql(f"""SELECT nombre, ciudad FROM recintos WHERE id_recinto = '{id_recinto}'""") 
            if bd1.rows != None and len(bd1.rows) > 0 :
                #--- primero coloca la ciudad  y luego re-carga el combo de recintos de la ciudad
                index = self.ui.comboBox_2.findText(bd1.rows[0][1], QtCore.Qt.MatchFixedString)
                if index >= 0:
                     self.ui.comboBox_2.setCurrentIndex(index)
                     self.updateCombo()

                #--- ahora coloca el recinto 
                index = self.ui.comboBox.findText(bd1.rows[0][0], QtCore.Qt.MatchFixedString)
                if index >= 0:
                     self.ui.comboBox.setCurrentIndex(index)

        except:
            print("error posiciona_recinto:", sys.exc_info())

    
    def extraer_manager(self):
        #--------------------------------------------------- extrae manager del combo
        bdaux = BdStd()
        id_manager = ""
        try :
            manager = self.ui.combo_manager.currentText().split(" ")
            nombre_manager = manager[0]
            apellidos_manager = manager[1]
            bdaux.runsql(f"""SELECT id_manager FROM managers WHERE nombre='{nombre_manager} '
                      AND apellidos = '{apellidos_manager} '""")
            if bdaux.rows != None and len(bdaux.rows) > 0 :
                id_manager = bdaux.rows[0][0]
        except:
            print("error extraer_manager:", sys.exc_info())
        return (id_manager)
    
    def posiciona_manager(self, id_manager):
        #-------------------------------------------------- coloca combo en ciudad y  recinto
        bd1 = BdStd()
        try :
            bd1.runsql(f"""SELECT nombre, apellidos FROM managers WHERE id_manager = '{id_manager}'""") 

            if bd1.rows != None and len(bd1.rows) > 0 :
                completo  = bd1.rows[0][0] +  bd1.rows[0][1]

                index = self.ui.combo_manager.findText(completo, QtCore.Qt.MatchFixedString)
                if index >= 0:
                     self.ui.combo_manager.setCurrentIndex(index)
        except:
            print("error posiciona_manager:", sys.exc_info())
            
#------------------------------------------------------------------------------           
#-------------------FUNCIONES PAGINA FECHAS------------------------------------
#------------------------------------------------------------------------------

    def activaAdd(self):
        self.ui.buttonAddDate.setEnabled(True)
        
    def addDate(self):
        
        date = self.ui.calendar.selectedDate()
        date = date.toString("yyyy-MM-dd")
        time = self.ui.time.time()
        time = time.toString("hh:mm")
        tarea = self.ui.combo_tarea.currentText()
        id_evento = self.ui.entry_id.text().upper()
        id_dias_evento = f"{id_evento}{date}{time}{tarea}"
        campos_fecha = (id_dias_evento,id_evento,date,time,tarea)
        #----------Guarda la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        bd.runsql("""INSERT INTO dias_evento (id_dias_evento,id_evento,fecha,
                  hora,tarea) VALUES (?,?,?,?,?);""",campos_fecha)
        
        #----------Muestra las fechas en la tabla------------------------------
        
        self.load_dias_evento(id_evento)
        self.ui.fechas_table.show()
        
  
    def delDate(self):
        
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Quiere eliminar la fecha seleccionada ? ", qm.Yes | qm.No)
        
        if ret == qm.No:
            return
        
        #-------------- Borrar la fecha del evento
        # for i, item in enumerate(self.ui.fechas_table.selectedItems()):
        #     if i == 0 : 
        #        date = item.text()
        #     elif i == 1  : 
        #         time = item.text()
        #     elif i == 2  : 
        #         tarea = item.text()
        evento = self.ui.entry_id.text().upper()
            
        row=self.ui.fechas_table.currentRow()
        id_dias_evento = self.ui.fechas_table.item(row,3).text()
        #----------Borra la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        bd.runsql(f"""DELETE FROM dias_evento WHERE id_dias_evento = '{id_dias_evento}'""")
        
        #----------Muestra las fechas en la tabla------------------------------
        
        self.load_dias_evento(evento)       
     
    def load_dias_evento(self,id_evento):

        self.ui.fechas_table.setRowCount(0)
        self.ui.fechas_table.setColumnCount(4)  

        bd = BdStd()
        bd.runsql(f"""SELECT fecha, hora, tarea, id_dias_evento FROM dias_evento
                  WHERE id_evento = '{id_evento}' ORDER BY FECHA""")
        if bd.rows != None :
            for fila, data in enumerate(bd.rows) :
                self.ui.fechas_table.insertRow(fila)
                self.ui.fechas_table.setItem(fila , 0, QtWidgets.QTableWidgetItem(bd.gira_fecha(data[0])))
                self.ui.fechas_table.setItem(fila , 1, QtWidgets.QTableWidgetItem(data[1]))
                self.ui.fechas_table.setItem(fila , 2, QtWidgets.QTableWidgetItem(data[2]))
                self.ui.fechas_table.setItem(fila , 3, QtWidgets.QTableWidgetItem(data[3]))
        
    def load_evento (self, id_evento) :
        bd = BdStd()
        bd.runsql(f"""SELECT * FROM evento WHERE id_evento = '{id_evento}'""")
        if bd.rows != None :
            for row in bd.rows :
                self.ui.entry_id.setText(row[0])
                self.ui.entry_nombre.setText(row[1])
                self.ui.entry_cliente.setText(row[2])
                self.ui.entry_onsite.setText(row[3])
                self.ui.entry_tfn_onsite.setText(row[4])
                self.ui.entry_email_onsite.setText(row[5])
                self.ui.entry_notas.setPlainText(row[8])
                #----- se posiciona en combo  recinto / manager
                self.posiciona_recinto (row[6])
                self.posiciona_manager (row[7])
    
    def activaDel(self):    
        self.ui.buttonDelDate.setEnabled(True)

#------------------------------------------------------------------------------
#---------------FUNCIONES PÁGINA PERSONAL--------------------------------------
#------------------------------------------------------------------------------
        
        
        
    def tabla1_select(self):
        campos = self.ui.personal_table.selectedItems()
        if len(campos) > 0 :
            self.id_personal = campos[0].text()
            self.nom_cargo = campos[3].text()
 
    
    def filtro_checks(self,text):

        self.nombre=self.ui.entry_nombre_personal.text().capitalize()
        sigue=''
        if text == "ALL":
            sql_base = f"""SELECT id_personal, nombre, apellidos,  '', dni, \
            telefono, email, autonomo, notas FROM personal
            WHERE nombre LIKE '{self.nombre}%'"""
        else :
            sql_base = 'SELECT p.id_personal, p.nombre, apellidos, cargos.nombre as cargo, dni, \
            telefono, email, autonomo, notas FROM personal as p,tarifas, cargos'
            sql_base += f' WHERE tarifas.id_personal=p.id_personal AND tarifas.id_cargo = cargos.id_cargo AND p.nombre LIKE "{self.nombre}%"'

            if text in self.dic_cargos :
                sigue += ' AND tarifas.id_cargo = "' + self.dic_cargos[text] + '"'


        self.load_personal(sql_base + sigue)
        self.color_ocupado("")
        self.load_personal_added()

    def load_personal(self, sql):
                    
        bd=BdStd()
        bd.runsql(sql)
        self.ui.personal_table.setRowCount(0)
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.personal_table.insertRow(i)
                for j, data in enumerate(row_data):
                    self.ui.personal_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
                    
    def filtro_dia(self,text):
        self.color_ocupado(text[0:10])
        self.hora=(text[11:16])
        self.load_personal_added()

    def load_personal_added(self):
        self.ui.personal_added.setRowCount(0)
        if self.id_evento == None :
            return
                    
        bd=BdStd()
        txtsql = f"""SELECT strftime('%d-%m-%Y',fecha)||" "||hora, cargos.nombre, pev.id_personal, p.nombre, p.apellidos, 
                  suplemento, dni, telefono, email, autonomo, notas
                  FROM personal_evento as pev
                  JOIN personal as p ON p.id_personal = pev.id_personal
                  JOIN cargos ON cargos.id_cargo = pev.id_cargo 
                  WHERE id_evento = '{self.id_evento}' """
        if self.fecha != "ALL" :
             txtsql += f"""AND strftime('%d-%m-%Y',fecha) = '{self.fecha}' AND hora = '{self.hora}'"""
        txtsql += f"""ORDER BY fecha"""

        bd.runsql(txtsql)
        print(txtsql)
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.personal_added.insertRow(i)
                
                for j, data in enumerate(row_data):
                    if j==0:
                        self.ui.personal_added.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        self.ui.personal_added.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))

    def loadcombo_cargos (self) :
        
        bd=BdStd()
        bd.runsql("SELECT id_cargo, nombre FROM cargos ORDER BY id_cargo")
        self.ui.combo_filtrar_cargos.clear()

        self.dic_cargos = { "ALL": '000'}

        self.ui.combo_filtrar_cargos.addItem("ALL")
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.dic_cargos[row_data[1]] = row_data[0]
                self.ui.combo_filtrar_cargos.addItem(row_data[1])
        
    def loadcombo_dias(self) :

        if self.id_evento == None :
            return

        self.ui.combo_dia_personal.clear()
        self.map_fechas =  {"": '-',"ALL": '000'}
        self.ui.combo_dia_personal.addItem("")        
        self.ui.combo_dia_personal.addItem("ALL")

        bd=BdStd()
        txtsql = f"""SELECT fecha,hora,tarea FROM dias_evento WHERE id_evento = '{self.id_evento}'  
                     ORDER BY fecha"""
        bd.runsql(txtsql)
        if bd.rows != None :
            for row_data in bd.rows:
                self.map_fechas[row_data[0]] : row_data[1]
                self.ui.combo_dia_personal.addItem(bd.gira_fecha(row_data[0]) + " " +row_data[1] + " " + row_data[2])
                

        
    def color_ocupado(self, fecha):
        
        if fecha == "" : 
            return
        print ("fecha", fecha)            
        #----------------------- Para la fecha indicada mira si tiene otro evento 
        
        rows = self.ui.personal_table.rowCount()
        
        for row in range(rows) :
            if self.ui.personal_table.item(row,0) != None :
                id_personal = self.ui.personal_table.item(row,0).text()
            else : 
                id_personal = ""
            id_color = self.calcular_color (self.id_evento, id_personal, fecha)
            
            for i in range(9):
                if id_color == 1:
                   self.ui.personal_table.item(row,i).setBackground(QtGui.QColor(226, 39, 232))
                elif id_color == 2:
                    self.ui.personal_table.item(row,i).setBackground(QtGui.QColor(255, 0, 0))
                else:
                    self.ui.personal_table.item(row,i).setBackground(QtGui.QColor(200, 200, 200))
                
    def calcular_color (self, id_evento, id_personal, fecha):
        #-------------------------- convierte fecha dd-mm-aaaa  01-34-6789
        #self.yymmdd = fecha[8:10] + fecha[3:5] + fecha[0:2]
        self.fecha=fecha
        bd=BdStd()
        color = 0
        #------------ mira si está en otros eventos
        txtsql = "SELECT id_cargo, orden FROM personal_evento WHERE id_evento != '{}' AND "
        txtsql += " id_personal = '{}'  AND strftime('%d-%m-%Y',fecha) = '{}'"
        txtsql = txtsql.format(id_evento, id_personal, self.fecha)
        bd.runsql(txtsql)
        print("calcular color"+txtsql)
        if bd.rows != None and len(bd.rows) > 0:
            color = 1
        #------------ mira si está ocupado
        txtsql = "SELECT * FROM personal_ocupado WHERE "
        txtsql += " id_personal = '{}'  AND strftime('%d-%m-%Y',fecha) = '{}'"
        txtsql = txtsql.format(id_personal, self.fecha)
        bd.runsql(txtsql)
        print("calcular color"+txtsql)
        if bd.rows != None and len(bd.rows) > 0:
            color = 2
        print(color)
        return (color)

    def select_pev(self):
        # Doble clic en el grid de personal seleccionado para el evento
        #print ("itenms selected: ", self.ui.personal_added.selectedItems())
        self.open_detalle_pev() 
        
    def anade_persona (self):
        qm = QtWidgets.QMessageBox
        
        if len(self.ui.personal_table.selectedItems()) == 0:
            qm.warning(self, '', "Seleccione una persona de la rejilla superior")
            return
        
        if  self.ui.combo_dia_personal.currentText() == "" :
            qm.warning(self, '', "Seleccione una fecha en la lista")
            return           
        self.open_detalle_pev(alta = True)

    def open_detalle_pev(self, alta = False) :     
        self.pev = PersonalEvento(self, alta)
        self.pev.show()
        
    def quita_persona (self):     # mere 30-01-21 added 

        qm = QtWidgets.QMessageBox
        
        if len(self.ui.personal_added.selectedItems()) == 0:
            qm.warning(self, '', "Seleccione una persona agregada al evento")
            return

        ret = qm.question(self,'', "Quiere eliminar a la persona seleccionada ? ", qm.Yes | qm.No)
        
        if ret == qm.No:
            return
        
        #-------------- Borrar la persona del evento  
        for i, item in enumerate(self.ui.personal_added.selectedItems()):
            if i == 0 : 
               date = item.text()
               tmp=date.split(" ")
               date=tmp[0]
               hora=tmp[1]
               print(f"dia {date} hora {hora}")
            elif i == 1  : 
                nom_cargo = item.text()
            elif i == 2  : 
                id_personal = item.text()
        if nom_cargo in self.dic_cargos :
            id_cargo = self.dic_cargos[nom_cargo]
        else:
            id_cargo = "xx"
        
        #id_dias_evento = f"{id_evento}{date}{tarea}"
        #----------Guarda la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        bd.runsql(f"""DELETE FROM personal_evento WHERE id_evento = '{self.id_evento}' 
                  AND strftime('%d-%m-%Y',fecha) = '{date}' AND hora = '{hora}'
                  AND id_personal = '{id_personal}' AND id_cargo = '{id_cargo}' """)
                  
        print(f"""DELETE FROM personal_evento WHERE id_evento = '{self.id_evento}' 
        AND strftime('%d-%m-%Y',fecha) = '{date}' 
        AND id_personal = '{id_personal}' AND id_cargo = '{id_cargo}' """)

        
        #----------Refresca Grid------------------------------
        
        self.load_personal_added()      
             
    
    def open_ficha_personal(self,row):
        id_personal= self.ui.personal_table.item(row,0).text()
        self.w = FichaPersonal(id_personal)
        self.w.show()

#-----------------------------------------------------------------------------
#-----------------FUNCIONES PÁGINA PROVEEDORES--------------------------------
#-----------------------------------------------------------------------------
        
    def tabla_prov_select(self):
        campos = self.ui.prov_table.selectedItems()
        if len(campos) > 0 :
            self.id_proveedor = campos[0].text()
            self.nom_servicio = campos[3].text()

    def filtro_prov_checks(self,text):
    
        self.empresa=self.ui.entry_nombre_prov.text().upper()
        self.serv_filtro = self.ui.combo_filtrar_serv.currentText()
        sigue=''
        if text == "ALL":
            sql_base = f"""SELECT * FROM proveedores
            WHERE empresa LIKE '{self.empresa}%'"""
        else :
            sql_base = 'SELECT * FROM proveedores'
            sql_base += f' WHERE empresa LIKE "{self.empresa}%"'
        
        if self.serv_filtro == "ALL":
            self.serv_filtro = ""
        sigue+=f"AND servicio LIKE '%{self.serv_filtro}%'"
        print(sql_base + sigue)
    
    
        self.load_proveedores(sql_base + sigue)
        self.load_prov_added()
    
    def load_proveedores(self, sql):
                    
        bd=BdStd()
        bd.runsql(sql)
        self.ui.prov_table.setRowCount(0)
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.prov_table.insertRow(i)
                for j, data in enumerate(row_data):
                    self.ui.prov_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
                    
    def filtro_prov_dia(self,text):
        self.load_prov_added()
    
   
    def load_prov_added(self):
        
        self.fecha_prov =  self.ui.combo_dia_prov.currentText()[0:10]
        
        self.ui.prov_added.setRowCount(0)
        if self.id_evento == None :
            return
                    
        bd=BdStd()
        txtsql = f"""SELECT strftime('%d-%m-%Y',fecha), pre.servicio, pre.id_proveedor,  \
                  p.provincia, contacto_onsite, telefono_onsite, email_onsite, pre.notas \
                  FROM proveedores_evento as pre \
                  JOIN proveedores as p ON  p.id_proveedor = pre.id_proveedor AND pre.id_evento = '{self.id_evento}' """
                  
        if self.fecha_prov != "ALL" :
              txtsql += f"""AND strftime('%d-%m-%Y',fecha) = '{self.fecha_prov}'"""
        txtsql += f"""ORDER BY fecha"""
    
        bd.runsql(txtsql)

        print("load_prov_added: ", self.fecha_prov, len (bd.rows), txtsql )        
        if bd.rows != None :
            
            for i, row_data in enumerate(bd.rows):
                self.ui.prov_added.insertRow(i)
                
                for j, data in enumerate(row_data):
                    if j==0:
                        self.ui.prov_added.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        self.ui.prov_added.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
    
    def loadcombo_servicios (self) :
        
        bd=BdStd()
        bd.runsql("SELECT * FROM servicios")
        self.ui.combo_filtrar_serv.clear()
    
        self.ui.combo_filtrar_serv.addItem("ALL")
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.combo_filtrar_serv.addItem(row_data[0])
        
        
    def loadcombo_dias_prov(self) :
    
        if self.id_evento == None :
            return
    
        self.ui.combo_dia_prov.clear()
        self.map_fechas =  {"": '-',"ALL": '000'}
        self.ui.combo_dia_prov.addItem("")        
        self.ui.combo_dia_prov.addItem("ALL")
    
        bd=BdStd()
        txtsql = f"""SELECT fecha, tarea FROM dias_evento WHERE id_evento = '{self.id_evento}'  
                     ORDER BY fecha"""
        bd.runsql(txtsql)
        if bd.rows != None :
            for row_data in bd.rows:
                self.map_fechas[row_data[0]] : row_data[1]
                self.ui.combo_dia_prov.addItem(bd.gira_fecha(row_data[0]) + " " +row_data[1])
    
    def select_prov(self):
        # Doble clic en el grid de proveedores seleccionado para el evento
        self.open_detalle_prov()        
    
    
    def anade_prov (self):
        qm = QtWidgets.QMessageBox
        
        if len(self.ui.prov_table.selectedItems()) == 0:
            qm.warning(self, '', "Seleccione un proveedor de la rejilla superior")
            return
        
        if  self.ui.combo_dia_prov.currentText() == "" :
            qm.warning(self, '', "Seleccione una fecha en la lista")
            return           
        self.open_detalle_prov(alta = True)

    def open_detalle_prov(self, alta = False) :     
        self.prov = ProveedorEvento(self, alta)
        self.prov.show()        
        
    def quita_prov (self):     # mere 30-01-21 added 
    
        qm = QtWidgets.QMessageBox
        
        if len(self.ui.prov_added.selectedItems()) == 0:
            qm.warning(self, '', "Seleccione un prov agregada al evento")
            return
    
        ret = qm.question(self,'', "Quiere eliminar al proveedor seleccionado ? ", qm.Yes | qm.No)
        
        if ret == qm.No:
            return
        
        #-------------- Borrar el proveedor del evento  
        for i, item in enumerate(self.ui.prov_added.selectedItems()):
            if i == 0 : 
               date = item.text()
            elif i == 1  : 
                nom_servicio = item.text()
            elif i == 2  : 
                id_proveedor = item.text()
        
        
        #id_dias_evento = f"{id_evento}{date}{tarea}"
        #----------Guarda la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        bd.runsql(f"""DELETE FROM proveedores_evento WHERE id_evento = '{self.id_evento}' 
                  AND strftime('%d-%m-%Y',fecha) = '{date}' 
                  AND id_proveedor = '{id_proveedor}' AND servicio = '{nom_servicio}'""")
    
        
        #----------Refresca Grid------------------------------
        
        self.load_prov_added()      
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CrearEvento('JB-1239-2021')
    ui.show()
    sys.exit(app.exec_())