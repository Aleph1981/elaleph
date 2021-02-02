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

class CrearEvento(QtWidgets.QDialog, CrearEvento_Ui):
    
    def __init__(self, id_evento_parm = None):
        QtWidgets.QDialog.__init__(self)
        self.ui = CrearEvento_Ui()
        self.ui.setupUi(self)
        self.id_evento = id_evento_parm
        self.fecha = ""       
        print("esta es")
        
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
                 
        if self.id_evento == None :       # es un alta cambia el título del formulario
            print ("cambia el título del formulario: ES UN ALTA")
        else:                            # carga datos evento
            self.load_evento(self.id_evento)
            self.showFrame()
            
        self.ui.button_guardar.clicked.connect(self.guardarDatos)
        self.ui.comboBox_2.currentIndexChanged['QString'].connect(self.updateCombo)
        self.ui.tabWidget.currentChanged.connect(self.cambia_pestanya)
        
#------------------------------------------------------------------------------
#-------------------------PÁGINA DE FECHAS-------------------------------------
#------------------------------------------------------------------------------
        
#-------------------------Esconder y activar botones---------------------------
        
        if self.id_evento == None :       # es un alta cambia el título del formulario       
            self.ui.fechas_table.hide()
            self.ui.frame.hide()
        else: 
            self.load_dias_evento(self.id_evento)
        self.ui.combo_tarea.activated['QString'].connect(self.activaAdd)
        self.ui.buttonAddDate.clicked.connect(self.addDate)
        self.ui.buttonDelDate.clicked.connect(self.delDate)   # merem 30-01-21 added
        self.ui.calendar.clicked.connect(self.showFrame)
        self.ui.fechas_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.fechas_table.setSelectionBehavior(self.ui.fechas_table.SelectRows)
        self.ui.fechas_table.hideColumn(3)
        self.ui.fechas_table.clicked.connect(self.activaDel)

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
        
        
        
        self.ui.personal_added.setColumnCount(11)
        self.ui.personal_added.setSortingEnabled(True)
        self.ui.personal_added.setSelectionBehavior(self.ui.personal_table.SelectRows)
        self.ui.personal_added.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.personal_added.setHorizontalHeaderLabels([ "Fecha", "Cargo", "ID","Nombre", "Apellidos", "Cargo",  
                                  "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas","Suplemento"])
        #self.ui.personal_added.hideColumn(0)
        
#-----------------------------------------------------------------------------
#------------------------PÁGINA DE PROVEEDORES--------------------------------
#----------------------------------------------------------------------------- 



            
#-------------------FUNCIONES PAGINA DATOS-------------------------------------
    def cambia_pestanya (self):
        print ("pestaña: ", self.ui.tabWidget.currentIndex())
        index = self.ui.tabWidget.currentIndex()
        if index == 1 :
            # refresca grids de fechas
            self.load_dias_evento(self.id_evento)
        if index == 2 :
            # refresca grids personal
            self.loadcombo_cargos()
            self.filtro_checks("ALL")
            self.loadcombo_dias()
        

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
        print("self.id_evento : ",self.id_evento)
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
                print ("len(bd.rows)", len(bdaux.rows))
                id_recinto = bdaux.rows[0][0]
        except:
            print("error extraer_recinto:", sys.exc_info())
        return (id_recinto)
    
    def posiciona_recinto(self, id_recinto):
        #-------------------------------------------------- coloca combo en ciudad y  recinto
        bd1 = BdStd()
        try :
            bd1.runsql(f"""SELECT nombre, ciudad FROM recintos WHERE id_recinto = '{id_recinto}'""") 
            print ("posiciona_recinto:", id_recinto, "rows", len(bd1.rows) )
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
                print ("len(bd.rows)", len(bdaux.rows))
                id_manager = bdaux.rows[0][0]
        except:
            print("error extraer_manager:", sys.exc_info())
        return (id_manager)
    
    def posiciona_manager(self, id_manager):
        #-------------------------------------------------- coloca combo en ciudad y  recinto
        bd1 = BdStd()
        try :
            bd1.runsql(f"""SELECT nombre, apellidos FROM managers WHERE id_manager = '{id_manager}'""") 
            print ("posiciona_manager:", id_manager, "rows", len(bd1.rows) )

            if bd1.rows != None and len(bd1.rows) > 0 :
                completo  = bd1.rows[0][0] +  bd1.rows[0][1]
                print("busco: " +completo)

                index = self.ui.combo_manager.findText(completo, QtCore.Qt.MatchFixedString)
                print("index", index)
                if index >= 0:
                     self.ui.combo_manager.setCurrentIndex(index)
        except:
            print("error posiciona_manager:", sys.exc_info())
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
        
        self.load_dias_evento(id_evento)
        self.ui.fechas_table.show()
        
  
    def delDate(self):
        
        qm = QtWidgets.QMessageBox
        ret = qm.question(self,'', "Quiere eliminar la fecha seleccionada ? ", qm.Yes | qm.No)
        
        if ret == qm.No:
            return
        
        #-------------- Borrar la fecha del evento
        for i, item in enumerate(self.ui.fechas_table.selectedItems()):
            if i == 0 : 
               date = item.text()
            elif i == 1  : 
                time = item.text()
            elif i == 2  : 
                tarea = item.text()
        evento = self.ui.entry_id.text().upper()
 
        #id_dias_evento = f"{id_evento}{date}{tarea}"
        #----------Guarda la fecha en la bbdd----------------------------------
        
        bd = BdStd()
        bd.runsql(f"""DELETE FROM dias_evento WHERE id_evento = '{evento}' AND fecha = '{date}' 
                  AND tarea = '{tarea}' AND hora = '{time}' """)
        print (f"""DELETE FROM dias_evento WHERE id_evento = '{evento}' AND fecha = '{date}' 
                  AND tarea = '{tarea}' AND hora = '{time}' """)
        
        #----------Muestra las fechas en la tabla------------------------------
        
        self.load_dias_evento(evento)       
     
    def load_dias_evento(self,id_evento):

        self.ui.fechas_table.setRowCount(0)
        self.ui.fechas_table.setColumnCount(4)  

        bd = BdStd()
        bd.runsql(f"""SELECT fecha, hora, tarea, id_dias_evento FROM dias_evento
                  WHERE id_evento = '{id_evento}'""")
        if bd.rows != None :
            for fila, data in enumerate(bd.rows) :
                self.ui.fechas_table.insertRow(fila)
                self.ui.fechas_table.setItem(fila , 0, QtWidgets.QTableWidgetItem(data[0]))
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

        
#---------------FUNCIONES PÁGINA PERSONAL--------------------------------------
#------Función de filtrado----------------------------------------------------       
    
    # def complet_nombre(self): #Nueva función 25-1 Alejandro
    #     self.nombres=[]
    #     self.nombre = self.ui.entry_nombre_personal.text()
            
    #     bdnom = BdStd()
    #     bdnom.runsql(f"SELECT nombre FROM personal WHERE nombre LIKE '{self.nombre}%'" )
    #     if bdnom.rows != None:
    #         for row in bdnom.rows:
    #             self.nombres.append(row[0])
    #     self.completer = QtWidgets.QCompleter(self.nombres)
    #     self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
    #     self.ui.entry_nombre_personal.setCompleter(self.completer)
        
        
        
    def tabla1_select(self):
        campos = self.ui.personal_table.selectedItems()
        if len(campos) > 0 :
            print("Data:", len(campos), campos[0].text())
            self.id_personal = campos[0].text()
            self.nom_cargo = campos[3].text()
 
    
    def filtro_checks(self,text):
        #
        # mere 19/01/2021 cambiado sql, añadido nombre del cargo
        #
        self.nombre=self.ui.entry_nombre_personal.text().capitalize()
        
        sql_base = 'SELECT p.id_personal, p.nombre, apellidos, cargos.nombre as cargo, dni, \
        telefono, email, autonomo, notas FROM personal as p,tarifas, cargos'
        sql_base += f' WHERE tarifas.id_personal=p.id_personal AND tarifas.id_cargo = cargos.id_cargo AND p.nombre LIKE "{self.nombre}%"'
        
        #print ("voy a filtrar ", text, self.dic_cargos[text])
    
        sigue=''
        if text != "ALL":
            if text in self.dic_cargos :
                sigue += ' AND tarifas.id_cargo = "' + self.dic_cargos[text] + '"'
#        if text == "Crew Chief":
#             sigue += ' AND tarifas.id_cargo = "001"'
#             
#        if text == "Operador de Luces":
#             sigue += ' AND tarifas.id_cargo = "002"'
#             
#        if text == "Dimmers":
#             sigue += ' AND tarifas.id_cargo = "003"'
#             
#        if text == "Técnico Luces":
#             sigue += ' AND tarifas.id_cargo = "004"'
#             
#        if text == "Operador Sonido":
#             sigue += ' AND tarifas.id_cargo = "006"'
#             
#        if text == "RF":
#             sigue += ' AND tarifas.id_cargo = "007"'
#             
#        if text == "Técnico de Sonido":
#            sigue += ' AND tarifas.id_cargo = "008"'
#        
#        if text == "Operador de Video":
#            sigue += ' AND tarifas.id_cargo = "010"'
#            
#        if text == "LED":
#            sigue += ' AND tarifas.id_cargo = "011"'
#            
#        if text == "Técnico de Video":
#            sigue += ' AND tarifas.id_cargo = "012"'
#            
#        if text == "Contenidos":
#            sigue += ' AND tarifas.id_cargo = "013"'
#            
#        if text == "Regidor":
#            sigue += ' AND tarifas.id_cargo = "009"'
#        
#        if text == "Rigger":
#            sigue += ' AND tarifas.id_cargo = "005"'
#            
#        if text == "Deco":
#            sigue += ' AND tarifas.id_cargo = "014"'

        self.load_personal(sql_base + sigue)
        self.color_ocupado("")
        self.load_personal_added()

    def load_personal(self, sql):
                    
        bd=BdStd()
        bd.runsql(sql)
        self.ui.personal_table.setRowCount(0)
        print ("load_personal rows ", len(bd.rows), sql)
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.personal_table.insertRow(i)
                for j, data in enumerate(row_data):
                    self.ui.personal_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
                    
    def filtro_dia(self,text):
        print ("filtro dia ", text)
        self.color_ocupado(text[0:10])

    def load_personal_added(self):
        self.ui.personal_added.setRowCount(0)
        if self.id_evento == None :
            return
                    
        bd=BdStd()
        txtsql = f"""SELECT   fecha, cargos.nombre, id_personal FROM personal_evento as pev
                  JOIN cargos ON cargos.id_cargo = pev.id_cargo WHERE id_evento = '{self.id_evento}'"""
        
        print ("load_personal_added ", txtsql)
        bd.runsql(txtsql)
        
        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.personal_added.insertRow(i)
                for j, data in enumerate(row_data):
                    self.ui.personal_added.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))


    def loadcombo_cargos (self) :
        
        bd=BdStd()
        bd.runsql("SELECT id_cargo, nombre FROM cargos")
        self.ui.combo_filtrar_cargos.clear()

        self.dic_cargos = {"ALL": '000'}
        self.ui.combo_filtrar_cargos.addItem("ALL")

        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.dic_cargos[row_data[1]] = row_data[0]
                self.ui.combo_filtrar_cargos.addItem(row_data[1])
            print (self.dic_cargos)

    def loadcombo_dias(self) :

        if self.id_evento == None :
            return

        self.ui.combo_dia_personal.clear()
        self.map_fechas =  {"ALL": '000'}
        self.ui.combo_dia_personal.addItem("ALL")
        
        bd=BdStd()
        txtsql = f"""SELECT fecha, tarea FROM dias_evento WHERE id_evento = '{self.id_evento}'  ORDER BY fecha"""
        bd.runsql(txtsql)
        print("loadcombo_dias", self.id_evento, "rows:", bd.rows, txtsql)
        if bd.rows != None :
            for row_data in bd.rows:
                self.map_fechas[row_data[0]] : row_data[1]
                self.ui.combo_dia_personal.addItem(row_data[0] + " " +row_data[1])

        
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
            
            print(self.ui.personal_table.item(row,0).text(), id_color)
            
            if id_color == 1:
               self.ui.personal_table.item(row,0).setBackground(QtGui.QColor(120, 66, 245))
            elif id_color == 2:
                self.ui.personal_table.item(row,0).setBackground(QtGui.QColor(226, 39, 232))
            else:
                self.ui.personal_table.item(row,0).setBackground(QtGui.QColor(250, 250, 250))
    def calcular_color (self, id_evento, id_personal, fecha):
        #-------------------------- convierte fecha dd-mm-aaaa  01-34-6789
        #self.yymmdd = fecha[8:10] + fecha[3:5] + fecha[0:2]
        self.fecha=fecha
        bd=BdStd()
        color = 0
        #------------ mira si está en otros eventos
        txtsql = "SELECT id_cargo, orden FROM personal_evento WHERE id_evento != '{}' AND "
        txtsql += " id_personal = '{}'  AND fecha = '{}'"
        txtsql = txtsql.format(id_evento, id_personal, self.fecha)
        bd.runsql(txtsql)
        print (bd.rows, txtsql)

        if bd.rows != None and len(bd.rows) > 0:
            color = 1
            print("esta ocupado en otro evento")
        #------------ mira si está ocupado
        txtsql = "SELECT * FROM personal_ocupado WHERE "
        txtsql += " id_personal = '{}'  AND fecha = '{}'"
        txtsql = txtsql.format(id_personal, self.fecha)
        bd.runsql(txtsql)
        print (bd.rows, txtsql)

        if bd.rows != None and len(bd.rows) > 0:
            color = 2
            print("esta ocupado por terceros") 
        return (color)

    def anade_persona (self):
            
        self.pev = PersonalEvento(self)
        self.pev.show()
        
    def quita_persona (self):     # mere 30-01-21 added 

        qm = QtWidgets.QMessageBox
        
        if len(self.ui.personal_added.selectedItems()) == 0:
            qm.warning(self, '', "Seleccione una persona agregada al evento")
            return

        ret = qm.question(self,'', "Quiere eliminar a la persona seleccionada ? ", qm.Yes | qm.No)
        
        if ret == qm.No:
            return
        
        #-------------- Borrar la personal evento  !!! VOT 
        for i, item in enumerate(self.ui.personal_added.selectedItems()):
            if i == 0 : 
               date = item.text()
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
        bd.runsql(f"""DELETE FROM personal_evento WHERE id_evento = '{self.id_evento}' AND fecha = '{date}' 
                  AND id_personal = '{id_personal}' AND id_cargo = '{id_cargo}' """)
        print (f"""DELETE FROM personal_evento WHERE id_evento = '{self.id_evento}' AND fecha = '{date}' 
                  AND id_personal = '{id_personal}' AND id_cargo = '{id_cargo}' """)
        
        #----------Refresca Grid------------------------------
        
        self.load_personal_added()      
             
    
    def open_ficha_personal(self,row):
        id_personal= self.ui.personal_table.item(row,0).text()
        self.w = FichaPersonal(id_personal)
        self.w.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CrearEvento('JB-1239-2021')
    ui.show()
    sys.exit(app.exec_())