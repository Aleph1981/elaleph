# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:54:40 2021

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from crearevento_ui import *
from bdstd import *
from projectmanagers import *
from recintos import *
from fichapersonal import *
from personalevento import *            # mere 30-01-21 added
from proveedorevento import *
from selectcliente import *
from clientes import *
from selectrecinto import *
from anadirproveedor import *
import pyperclip

class CrearEvento(QtWidgets.QWidget, CrearEvento_Ui):
    
    def __init__(self, id_evento_parm = None):
        QtWidgets.QWidget.__init__(self)
        self.ui = CrearEvento_Ui()
        self.ui.setupUi(self)
        self.id_evento = id_evento_parm
        self.fecha = ""       
        self.hora = ""
        self.setWindowTitle("Aleph - Crear/Editar Evento")
        #Escondo los vertical headers
        self.ui.fechas_table.verticalHeader().hide()
        self.ui.personal_table.verticalHeader().hide()
        self.ui.personal_added.verticalHeader().hide()
        self.ui.prov_table.verticalHeader().hide()
        self.ui.prov_added.verticalHeader().hide()
        self.id_cliente=""
        self.self_id = "crearevento"
#------------------------------------------------------------------------------
#-------------------------PÁGINA DE DATOS--------------------------------------
#------------------------------------------------------------------------------
        self.ui.buttonAddRecinto.clicked.connect(self.addRecinto)
        self.ui.buttonAddManager.clicked.connect(self.addManager)
        self.ui.buttonAddCliente.clicked.connect(self.addCliente)
        self.ui.buttonSelect.clicked.connect(self.selectCliente)
        self.load_comboRecintos()
        
        bd=BdStd()         
        bd.runsql(f"SELECT nombre, apellidos FROM managers;")
        if bd.rows != None :
              for nombre in bd.rows :
                 self.ui.combo_manager.addItem(f"{nombre[0]} {nombre[1]}")
                 
                 
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
            
        else: 
            self.load_dias_evento(self.id_evento)
        self.ui.combo_tarea.activated['QString'].connect(self.activaAdd)
        self.ui.buttonAddDate.clicked.connect(self.addDate)
        self.ui.buttonDelDate.clicked.connect(self.delDate)   # merem 30-01-21 added
        self.ui.fechas_table.horizontalHeader().setStretchLastSection(True)
        self.ui.fechas_table.setSelectionBehavior(self.ui.fechas_table.SelectRows)
        self.ui.fechas_table.setSortingEnabled(True)
        self.ui.fechas_table.hideColumn(3)
        self.ui.fechas_table.clicked.connect(self.activaDel)
        self.ui.buttonFechaNext.clicked.connect(self.pasa_pagina)
        self.ui.buttonModificar.clicked.connect(self.chgDate)
        
        
        

#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PERSONAL-----------------------------------
#-----------------------------------------------------------------------------

#-------Si el combobox se activa llama a la funcion de filtrado----------------
        self.id_personal = ""     # contendrá la persona seleccionada del grid de personas
        self.nom_cargo = ""       # contendrá su cargo
        self.ui.personal_table.setSortingEnabled(True)       
        self.ui.personal_table.horizontalHeader().setStretchLastSection(True)
        self.ui.personal_table.setColumnCount(10)   # Alejandro cambiado 25-1 lo saco de la función si no no etiqueta el header 
        self.ui.personal_table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellidos", "Cargo",  
                                  "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas","Suplemento"])
        self.ui.personal_table.itemSelectionChanged.connect(self.tabla1_select)
        self.ui.personal_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # mere
        self.ui.personal_table.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.ui.buttonPersonalNext.clicked.connect(self.pasa_pagina)
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
        self.ui.personal_added.horizontalHeader().setStretchLastSection(True)
        self.ui.personal_added.setHorizontalHeaderLabels([ "Fecha", "Cargo", "ID","Nombre", "Apellidos",  
                                  "Suplemento", "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas"])
        #self.ui.personal_added.hideColumn(0)
        self.ui.personal_added.cellDoubleClicked.connect(self.select_pev)       
        
        
        
        
        
        
        
#-----------------------------------------------------------------------------
#------------------------PÁGINA DE TRANSPORTES--------------------------------
#-----------------------------------------------------------------------------

        self.load_comboEmpresa()
        self.load_comboPaises()
        self.paisR = ""
        self.paisE = ""
        self.provinciaR = ""
        self.provinciaE = ""
        self.ui.comboPaisR.activated.connect(self.check_paisR)
        self.ui.comboPaisE.activated.connect(self.check_paisE)
        self.ui.buttonEventoR.clicked.connect(self.load_recintoR)
        self.ui.buttonEventoE.clicked.connect(self.load_recintoE)
        self.ui.buttonAlmacenR.clicked.connect(self.load_almacenR)
        self.ui.buttonAlmacenE.clicked.connect(self.load_almacenE)
        self.ui.buttonOtroR.clicked.connect(self.load_otroR)
        self.ui.buttonOtroE.clicked.connect(self.load_otroE)
        self.ui.buttonCopyR.clicked.connect(self.copyR)
        self.ui.buttonCopyE.clicked.connect(self.copyE)
        self.ui.buttonOtroR.clicked.connect(self.load_otroR)
        self.ui.buttonOtroE.clicked.connect(self.load_otroE)
        self.ui.buttonAddTrans.clicked.connect(self.addTrans)
        self.ui.buttonDelTrans.clicked.connect(self.delTrans)
        self.ui.buttonNextTrans.clicked.connect(self.nextTrans)
        self.ui.tableTransportes.setColumnCount(15)
        self.ui.tableTransportes.setHorizontalHeaderLabels(["Orden","Evento","Empresa","Conductor","Teléfono",\
                    "Email","Vehículo","Matrícula","Notas","Recogida","Fecha","Hora","Entrega","Fecha","Hora"])
        self.ui.tableTransportes.horizontalHeader().setStretchLastSection(True)
        self.ui.tableTransportes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.ui.tableTransportes.verticalHeader().hide()
        self.ui.tableTransportes.hideColumn(0)
        self.ui.buttonAddEmpresa.clicked.connect(self.open_addEmpresa)
        if self.id_evento != None:
            self.loadTrans()

        
        
        
        
#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PROVEEDORES--------------------------------
#----------------------------------------------------------------------------- 
        
        self.id_proveedor = ""     # contendrá la persona seleccionada del grid de personas
        self.nom_servicio = ""       # contendrá su cargo
        self.ui.prov_table.setSortingEnabled(True)       
        self.ui.prov_table.horizontalHeader().setStretchLastSection(True)
        self.ui.prov_table.setColumnCount(14)   # Alejandro cambiado 25-1 lo saco de la función si no no etiqueta el header 
        self.ui.prov_table.setHorizontalHeaderLabels(["ID","Empresa","Provincia",\
            "Localidad","Dirección","Servicio/s","CIF","Teléfono","Email","Web",\
            "Contacto","Teléfono Contacto","Email Contacto","Notas"])
        self.ui.prov_table.itemSelectionChanged.connect(self.tabla_prov_select)
        self.ui.prov_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  # mere
        self.ui.prov_table.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        # mere 30-01-21  comentado lo de abajo
        #self.ui.prov_table.hideColumn(0)
        self.ui.buttonProvOk.clicked.connect(self.evento_creado)
        self.loadcombo_cargos()
        self.ui.combo_filtrar_serv.activated[str].connect(self.filtro_prov_checks)
        self.filtro_prov_checks("ALL")
        self.loadcombo_dias()
        self.ui.combo_dia_prov.activated[str].connect(self.filtro_prov_dia)
        self.ui.button_add_prov.clicked.connect(self.anade_prov)
        self.ui.button_remove_prov.clicked.connect(self.quita_prov)
        self.ui.buttonBuscarProv.clicked.connect(self.filtro_prov_checks)
       
        
        
        
        self.ui.prov_added.setColumnCount(8)
        self.ui.prov_added.setSortingEnabled(True)
        self.ui.prov_added.setSelectionBehavior(self.ui.prov_table.SelectRows)
        self.ui.prov_added.horizontalHeader().setStretchLastSection(True)
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
            self.load_fechasTrans()
        if index == 4 :
            # refresca grids proveedores
            self.loadcombo_servicios()
            self.filtro_prov_checks("ALL")
            self.loadcombo_dias_prov()
    def addCliente(self):
        self.w = Clientes()
        self.w.show()
        
    def selectCliente(self):
        self.w = SelectCliente(self)
        self.w.show()
        
    def set_cliente(self,nombre):
        self.ui.entry_cliente.setText(nombre)
        print(nombre)
    def addRecinto(self):
        self.w = Recintos(self)
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
                 
    def load_comboRecintos(self):
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
        self.updateCombo()
        bd.runsql(f"SELECT nombre FROM recintos WHERE ciudad = '{self.ui.comboBox_2.currentText()}';")
        if bd.rows != None :
              for recinto in bd.rows :
                 self.ui.comboBox.addItem("Recintos")
                 
    def guardarDatos(self):
        bd = BdStd()
        my_evento = self.ui.entry_id.text().upper()
        
        id_recinto = self.extraer_recinto()
        id_manager = self.extraer_manager()        


        #-------------------------------------------------------
        if self.id_evento == None :
            campos_datos = (my_evento, self.ui.entry_nombre.text()\
                        ,self.ui.entry_cliente.text(), self.ui.entry_onsite.text()\
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
            print("error extraer_manager:", sys.exc_info())
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
            apellidos_manager = ""
            for i in range(1,len(manager)):
                apellidos_manager += f"{manager[i]} "
            apellidos_manager = apellidos_manager[:-1] 
            print(nombre_manager+" "+apellidos_manager)
            bdaux.runsql(f"""SELECT id_manager FROM managers WHERE nombre = '{nombre_manager}'
                      AND apellidos LIKE '{apellidos_manager}'""")
            if bdaux.rows != None and len(bdaux.rows) > 0 :
                id_manager = bdaux.rows[0][0]
        except:
            print("error extraer_manager:", sys.exc_info())
        print(f"El manager de este evento es {id_manager}")
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
        
        evento = self.ui.entry_id.text().upper()
            
        row=self.ui.fechas_table.currentRow()
        id_dias_evento = self.ui.fechas_table.item(row,3).text()
        #----------Borra la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        bd.runsql(f"""DELETE FROM dias_evento WHERE id_dias_evento = '{id_dias_evento}'""")
        
        #----------Muestra las fechas en la tabla------------------------------
        
        self.load_dias_evento(evento)  
        
    def chgDate(self):
        # mere 17-02-21
        bd = BdStd()


        qm = QtWidgets.QMessageBox

        # 1.- Obtener nueva fecha del calendario y hora y cargo de los combos
        #-----------------------------------------------------
        
        newdate = self.ui.calendar.selectedDate()
        newdate = newdate.toString("yyyy-MM-dd")
        newtime = self.ui.time.time()
        newtime = newtime.toString("hh:mm")
        newtarea = self.ui.combo_tarea.currentText()
        newdatebonita = bd.gira_fecha(newdate)
        
        # 2.- Obtener del grid, el registro seleccionado para cambiar : fecha, hora, tarea, id_fecha
        #-----------------------------------------------------
        row=self.ui.fechas_table.currentRow()
        if row < 0 :
            texto = f"""Seleccione una fecha de la cuadrícula derecha"""
            qm.warning(self, '',texto)
            return

        fechabonita = self.ui.fechas_table.item(row,0).text()
        fecha = bd.gira_fecha(fechabonita)
        hora = self.ui.fechas_table.item(row,1).text()
        tarea = self.ui.fechas_table.item(row,2).text()        
        id_dias_evento = self.ui.fechas_table.item(row,3).text()
        id_evento = self.ui.entry_id.text().upper()

        texto = f"""Quiere cambiar {fechabonita} {hora} {tarea} por {newdatebonita} {newtime} {newtarea} ?"""
        ret = qm.question(self,'', texto, qm.Yes | qm.No)
        
        if ret == qm.No :
            return
        
        # 3.- Detecta si hay hijos con los datos nuevos
        #-----------------------------------------------------
        if self.fecha_existe(id_evento, newdate, newtime) == True:
            texto = f""" Ya existe en ese evento la fecha / hora. Desea continuar ?"""
            ret = qm.question(self,'', texto, qm.Yes | qm.No)
        
            if ret == qm.No:
                return
            
        # 4.- Si no hay hijos nuevos -> cambia los hijos
            # 4.1. cambia el personal asociado al dia
            # 4.2. cambia los proveedores asociado al dia
            
        self.cambia_hijos(id_evento, fecha, hora, newdate, newtime)            
            
        # 5.- Si no hijos nuevos -> cambia el padre

        bd.runsql(f"""DELETE FROM dias_evento WHERE id_dias_evento = '{id_dias_evento}'""")
        id_dias_evento = f"{id_evento}{newdate}{newtime}{newtarea}"
        campos_fecha = (id_dias_evento,id_evento,newdate,newtime,newtarea)
        bd.runsql("""INSERT INTO dias_evento (id_dias_evento,id_evento,fecha,
                  hora,tarea) VALUES (?,?,?,?,?);""",campos_fecha)

 

        #----------Muestra las fechas en la tabla------------------------------
        
        self.load_dias_evento(id_evento)
        self.ui.fechas_table.show()    
        
    def fecha_existe(self, id_evento, newdate, newtime) :
        bd = BdStd()
        bd.runsql(f"""SELECT * FROM dias_evento  WHERE id_evento = '{id_evento}'
                  AND fecha = '{newdate}' AND hora = '{newtime}'""")
        if bd.rows != None  and len(bd.rows) > 0 :
            return (True)
        return(False)

    def cambia_hijos(self, id_evento, fecha, hora, newdate, newtime) :
        bd = BdStd()
        txtsql = f"""UPDATE personal_evento SET fecha = '{newdate}', hora = '{newtime}'
            WHERE id_evento = '{id_evento}' AND fecha = '{fecha}' AND hora = '{hora}'"""

        bd.runsql(txtsql)
        print("uuuuupdate : ", txtsql)
     
    def load_dias_evento(self,id_evento):

        self.ui.fechas_table.setRowCount(0)
        self.ui.fechas_table.setColumnCount(4)  

        bd = BdStd()
        bd.runsql(f"""SELECT fecha, hora, tarea, id_dias_evento FROM dias_evento
                  WHERE id_evento = '{id_evento}' ORDER BY FECHA""")
        if bd.rows != None :
            for fila, data in enumerate(bd.rows) :
                self.ui.fechas_table.insertRow(fila)
                self.ui.fechas_table.setItem(fila , 0, SortDate(bd.gira_fecha(data[0]),data[0]))
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
#------------------------FUNCIONES DE TRANSPORTES-----------------------------
#-----------------------------------------------------------------------------
    def open_addEmpresa(self):
        self.w= AnadirProveedor(padre=self)
        self.w.show()
    def load_comboEmpresa(self):
        self.ui.comboEmpresa.clear()
        bdemp=BdStd()
        bdemp.runsql("""SELECT empresa FROM proveedores WHERE servicio LIKE '%Trailer%'
                  or servicio LIKE '%Camión%' or servicio LIKE '%Furgoneta%'""")
        if bdemp.rows != None:
            for empresa in bdemp.rows:
                self.ui.comboEmpresa.addItem(empresa[0])
    
    def load_comboPaises(self):
        
        self.ui.comboPaisR.addItem("")
        self.ui.comboPaisE.addItem("")
        
        bdpais=BdStd()
        bdpais.runsql("SELECT nombre FROM paises")
        
        if bdpais.rows != None:
            for pais in bdpais.rows:
                self.ui.comboPaisR.addItem(pais[0])
                self.ui.comboPaisE.addItem(pais[0])
                
        
    def check_paisR(self):
        
        self.paisR = self.ui.comboPaisR.currentText()
        
        if self.paisR == "España":
            self.ui.comboProvinciaR.setEnabled(True)
            self.load_comboProvinciasR()
            
        else:
            self.ui.comboProvinciaR.clear()
            self.ui.comboProvinciaR.setEnabled(False)
            
    def check_paisE(self):
        
        self.paisE = self.ui.comboPaisE.currentText()
        
        if self.paisE == "España":
            self.ui.comboProvinciaE.setEnabled(True)
            self.load_comboProvinciasE()
        else:
            self.ui.comboProvinciaE.clear()
            self.ui.comboProvinciaE.setEnabled(False)
            
    def load_comboProvinciasR(self):
        
        bdprovi = BdStd()
        bdprovi.runsql("SELECT nombre FROM provincias_es")
        
        if bdprovi.rows != None:
            for provincia in bdprovi.rows:
                self.ui.comboProvinciaR.addItem(provincia[0])
        
        
    def load_comboProvinciasE(self):
        bdprovi = BdStd()
        bdprovi.runsql("SELECT nombre FROM provincias_es")
        
        if bdprovi.rows != None:
            for provincia in bdprovi.rows:
                self.ui.comboProvinciaE.addItem(provincia[0])

    
    def load_fechasTrans(self):
        bd=BdStd()
        bd.runsql(f"SELECT fecha FROM dias_evento WHERE id_evento='{self.id_evento}' GROUP BY fecha")
        self.ui.comboFechaR.clear()
        self.ui.comboFechaE.clear()
        if bd.rows != None:
            for fecha in bd.rows:
                self.ui.comboFechaR.addItem(bd.gira_fecha(fecha[0]))
                self.ui.comboFechaE.addItem(bd.gira_fecha(fecha[0]))
        

    def load_recintoR(self, recinto=0):
        if recinto == 0:                     #Chequea si viene del hijo o no
            print("entra por None")
            id_recinto = self.extraer_recinto()
            
        else:
            print("entra por el else")
            id_recinto = recinto            
    
        bd = BdStd()
        bd.runsql(f"""SELECT nombre,pais,provincia,ciudad,direccion,indicaciones,coordenadas FROM recintos WHERE id_recinto = '{id_recinto}'""")
       
        if len(bd.rows) == 0:
           qm = QtWidgets.QMessageBox
           qm.warning(self,"Aleph","No existe un recinto asignado al evento") 
        elif len(bd.rows) > 0:
            camposrecinto=bd.rows[0]
        
        #----------busca el indice del pais-----------------------------------
        
            bd.runsql(f"SELECT orden FROM paises WHERE nombre = '{camposrecinto[1]}'")
            if bd.rows!=None:
                ordenpais=bd.rows[0][0]
            
            #----------
            if camposrecinto[1] == "España":
                self.load_comboProvinciasR()            
                bd.runsql(f"SELECT orden FROM provincias_es WHERE nombre = '{camposrecinto[2]}'")
                if bd.rows != None:
                    ordenprovincia=bd.rows[0][0]
                    self.ui.comboProvinciaR.setCurrentIndex(int(ordenprovincia)-1)
                    
            
            if bd.rows != None:
                self.ui.inputRecintoR.setText(camposrecinto[0])
                self.ui.comboPaisR.setCurrentIndex(int(ordenpais))
                self.ui.inputLocalidadR.setText(camposrecinto[3])
                self.ui.inputDireccionR.setText(camposrecinto[4])
                self.ui.inputIndicacionesR.setText(camposrecinto[5])
                self.ui.inputCoordenadasR.setText(camposrecinto[6])
            
    def addTrans(self):
        bd=BdStd()
        bd.runsql(f"""SELECT id_proveedor FROM proveedores WHERE empresa = '{self.ui.comboEmpresa.currentText()}'""")
        id_proveedor=bd.rows[0][0]
        fechaR = self.ui.comboFechaR.currentText()
        fechaR=fechaR.split()
        fechaR = bd.gira_fecha(fechaR[0])
        horaR = self.ui.horaR.time()
        horaR = horaR.toString("hh:mm")
        fechaE = self.ui.comboFechaE.currentText()
        fechaE = fechaE.split()
        fechaE = bd.gira_fecha(fechaE[0])
        horaE = self.ui.horaE.time()
        horaE = horaE.toString("hh:mm")
       
        campos_transporte=(self.id_evento, id_proveedor, self.ui.inputConductor.text(),self.ui.inputTfnConductor.text(),\
        self.ui.inputEmailConductor.text(),self.ui.inputTipo.text(),self.ui.inputMatricula.text(),self.ui.inputNotas.toPlainText(),\
        self.ui.inputRecintoR.text(),self.ui.comboPaisR.currentText(),self.ui.comboProvinciaR.currentText(),self.ui.inputLocalidadR.text(),\
        self.ui.inputDireccionR.text(),self.ui.inputIndicacionesR.text(),self.ui.inputCoordenadasR.text(),fechaR,horaR,\
        self.ui.inputRecintoE.text(),self.ui.comboPaisE.currentText(),\
        self.ui.comboProvinciaE.currentText(),self.ui.inputLocalidadE.text(),self.ui.inputDireccionE.text(),\
        self.ui.inputIndicacionesE.text(),self.ui.inputCoordenadasE.text(),fechaE,horaE)
        
        
        
        bd.runsql("""INSERT INTO transporte_evento (id_evento, id_proveedor, conductor, conductor_telefono, conductor_email,
                  tipo_vehiculo ,matricula, notas, recogida_lugar, recogida_pais, recogida_provincia,recogida_localidad, recogida_direc,
                  recogida_indicaciones, recogida_coordenadas, recogida_fecha, recogida_hora,entrega_lugar,entrega_pais,
                  entrega_provincia,entrega_localidad,entrega_direc,entrega_indicaciones,entrega_coordenadas,entrega_fecha,
                  entrega_hora)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",campos_transporte)
        
        self.loadTrans()
        
    def loadTrans(self):
       
        self.ui.tableTransportes.setRowCount(0)
        bd = BdStd()
        bd.runsql(f"""SELECT orden, id_evento, prov.empresa, conductor, conductor_telefono, conductor_email, tipo_vehiculo,matricula,
                  te.notas,recogida_lugar,strftime('%d-%m-%Y',recogida_fecha),recogida_hora,entrega_lugar,strftime('%d-%m-%Y',entrega_fecha),entrega_hora FROM 
                  transporte_evento as te, proveedores as prov WHERE te.id_proveedor = prov.id_proveedor AND id_evento='{self.id_evento}'""")
                  
        if bd.rows != None :
            for row in bd.rows :
                self.load_one(row)
                
    def load_one(self, data):
        rowPosition = self.ui.tableTransportes.rowCount()
        self.ui.tableTransportes.insertRow(rowPosition)
        self.ui.tableTransportes.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(data[0])))
        self.ui.tableTransportes.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(data[1]))
        self.ui.tableTransportes.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(data[2]))
        self.ui.tableTransportes.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data[3]))
        self.ui.tableTransportes.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(data[4]))
        self.ui.tableTransportes.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(data[5]))
        self.ui.tableTransportes.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(data[6]))
        self.ui.tableTransportes.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(data[7]))
        self.ui.tableTransportes.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(data[8]))
        self.ui.tableTransportes.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(data[9]))
        self.ui.tableTransportes.setItem(rowPosition , 10, QtWidgets.QTableWidgetItem(data[10]))
        self.ui.tableTransportes.setItem(rowPosition , 11, QtWidgets.QTableWidgetItem(data[11]))
        self.ui.tableTransportes.setItem(rowPosition , 12, QtWidgets.QTableWidgetItem(data[12]))
        self.ui.tableTransportes.setItem(rowPosition , 13, QtWidgets.QTableWidgetItem(data[13]))
        self.ui.tableTransportes.setItem(rowPosition , 14, QtWidgets.QTableWidgetItem(data[14]))
        
        
        
        
    def delTrans(self):
        row = self.ui.tableTransportes.currentRow()
        orden=self.ui.tableTransportes.item(row,0).text()
        bd=BdStd()
        bd.runsql(f"""DELETE FROM transporte_evento WHERE orden = '{orden}'""")
        self.loadTrans()
        
    def nextTrans(self):
        i = self.ui.tabWidget.currentIndex() 
        self.ui.tabWidget.setCurrentIndex(i+1)
        
        
        
    def load_recintoE(self, recinto=0):
        
        if recinto == 0:                     #Chequea si viene del hijo o no
            id_recinto = self.extraer_recinto()
        else:
            id_recinto = recinto
        
        
        bd = BdStd()
        bd.runsql(f"""SELECT nombre,pais,provincia,ciudad,direccion,indicaciones,coordenadas FROM recintos WHERE id_recinto = '{id_recinto}'""")
        
        if len(bd.rows) == 0:
           qm = QtWidgets.QMessageBox
           qm.warning(self,"Aleph","No existe un recinto asignado al evento") 
        elif len(bd.rows) > 0:
            camposrecinto=bd.rows[0]
            
            #----------busca el indice del pais-----------------------------------
            
            bd.runsql(f"SELECT orden FROM paises WHERE nombre = '{camposrecinto[1]}'")
            if bd.rows!=None:
                ordenpais=bd.rows[0][0]
            
            #----------
            if camposrecinto[1] == "España":
                self.load_comboProvinciasE()            
                bd.runsql(f"SELECT orden FROM provincias_es WHERE nombre = '{camposrecinto[2]}'")
                if bd.rows != None:
                    ordenprovincia=bd.rows[0][0]
                    self.ui.comboProvinciaE.setCurrentIndex(int(ordenprovincia)-1)
                    
            
            if bd.rows != None:
                self.ui.inputRecintoE.setText(camposrecinto[0])
                self.ui.comboPaisE.setCurrentIndex(int(ordenpais))
                self.ui.inputLocalidadE.setText(camposrecinto[3])
                self.ui.inputDireccionE.setText(camposrecinto[4])
                self.ui.inputIndicacionesE.setText(camposrecinto[5])
                self.ui.inputCoordenadasE.setText(camposrecinto[6])
    
    def load_almacenR(self):
        bd = BdStd()
        bd.runsql("""SELECT nombre,pais,provincia,ciudad,direccion,indicaciones,coordenadas FROM recintos WHERE nombre='Almacén '""")
        camposrecinto=bd.rows[0]
        
        #----------busca el indice del pais-----------------------------------
        
        bd.runsql(f"SELECT orden FROM paises WHERE nombre = '{camposrecinto[1]}'")
        if bd.rows!=None:
            ordenpais=bd.rows[0][0]
        
        #----------
        if camposrecinto[1] == "España":
            self.load_comboProvinciasR()            
            bd.runsql(f"SELECT orden FROM provincias_es WHERE nombre = '{camposrecinto[2]}'")
            if bd.rows != None:
                ordenprovincia=bd.rows[0][0]
                self.ui.comboProvinciaE.setCurrentIndex(int(ordenprovincia)-1)
                
        
        if bd.rows != None:
            self.ui.inputRecintoR.setText(camposrecinto[0])
            self.ui.comboPaisR.setCurrentIndex(int(ordenpais))
            self.ui.inputLocalidadR.setText(camposrecinto[3])
            self.ui.inputDireccionR.setText(camposrecinto[4])
            self.ui.inputIndicacionesR.setText(camposrecinto[5])
            self.ui.inputCoordenadasR.setText(camposrecinto[6])
    
    def load_almacenE(self):
        bd = BdStd()
        bd.runsql(f"""SELECT nombre,pais,provincia,ciudad,direccion,indicaciones,coordenadas FROM recintos WHERE nombre='Almacén '""")
        camposrecinto=bd.rows[0]
        
        #----------busca el indice del pais-----------------------------------
        
        bd.runsql(f"SELECT orden FROM paises WHERE nombre = '{camposrecinto[1]}'")
        if bd.rows!=None:
            ordenpais=bd.rows[0][0]
        
        #----------
        if camposrecinto[1] == "España":
            self.load_comboProvinciasE()            
            bd.runsql(f"SELECT orden FROM provincias_es WHERE nombre = '{camposrecinto[2]}'")
            if bd.rows != None:
                ordenprovincia=bd.rows[0][0]
                self.ui.comboProvinciaE.setCurrentIndex(int(ordenprovincia)-1)
                
        
        if bd.rows != None:
            self.ui.inputRecintoE.setText(camposrecinto[0])
            self.ui.comboPaisE.setCurrentIndex(int(ordenpais))
            self.ui.inputLocalidadE.setText(camposrecinto[3])
            self.ui.inputDireccionE.setText(camposrecinto[4])
            self.ui.inputIndicacionesE.setText(camposrecinto[5])
            self.ui.inputCoordenadasE.setText(camposrecinto[6])
    
    def load_otroR(self):
        self.sel_rec_r = SelectRecinto(self)
        self.sel_rec_r.show()
        self.r_e="r"  #-----------chequea si el padre viene de recogida o entrega
        
    def load_otroE(self):
        self.sel_rec_e = SelectRecinto(self)
        self.sel_rec_e.show()
        self.r_e="e"  #-----------chequea si el padre viene de recogida o entrega

    def copyR(self):
        pyperclip.copy(self.ui.inputCoordenadasR.text())
    def copyE(self):
        pyperclip.copy(self.ui.inputCoordenadasE.text())


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
        txtsql = f"""SELECT strftime('%d-%m-%Y',fecha)||" "||hora, pre.servicio, p.empresa,  \
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
        bd.runsql("SELECT servicio FROM servicios WHERE servicio != 'Trailer' AND  servicio != 'Camión' AND servicio != 'Furgoneta' ORDER BY orden")
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
               fecha_hora = item.text()
               tmp=fecha_hora.split(" ")
               date = tmp[0]
               hora = tmp[1]
               print(f"la hora es {hora}")
            elif i == 1  : 
                nom_servicio = item.text()
            elif i == 2  : 
                self.empresa = item.text()
                
        bdid=BdStd()
        bdid.runsql(f"""SELECT id_proveedor FROM proveedores WHERE empresa='{self.empresa}'""")
        self.id_proveedor = bdid.rows[0][0]
        
        
        #id_dias_evento = f"{id_evento}{date}{tarea}"
        #----------Guarda la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        txtsqldel=f"""DELETE FROM proveedores_evento WHERE id_evento = '{self.id_evento}' 
                  AND strftime('%d-%m-%Y',fecha) = '{date}' AND hora = '{hora}'
                  AND id_proveedor = '{self.id_proveedor}' AND servicio = '{nom_servicio}'"""
        bd.runsql(txtsqldel)
        print(txtsqldel)
    
        
        #----------Refresca Grid------------------------------
        
        self.load_prov_added()      
    def evento_creado(self):
        qm=QtWidgets.QMessageBox
        qm.information(self,"Aleph","Evento creado correctamente")
        if qm.clickedButton:
            self.close()
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CrearEvento('JB0001')
    ui.show()
    sys.exit(app.exec_())