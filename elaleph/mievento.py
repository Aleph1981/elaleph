# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:34:12 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from mievento_ui import *
from diasevento import *
from bdstd import BdStd


class CrearEvento(QtWidgets.QDialog, MiEvento_Ui):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.id_evento = "JB1243"             # OJO MERE
        self.ui = MiEvento_Ui()
        self.ui.setupUi(self)
        self.yymmdd = ""
        
        
#-------------Escribe la cabecera de la tabla----------------------------------

#        self.model.setHeaderData(0, QtCore.Qt.Horizontal , "ID")
#        self.model.setHeaderData(1, QtCore.Qt.Horizontal , "Nombre")
#        self.model.setHeaderData(2, QtCore.Qt.Horizontal , "Apellidos")
#        self.model.setHeaderData(3, QtCore.Qt.Horizontal , "Cargo")
#        self.model.setHeaderData(4, QtCore.Qt.Horizontal , "DNI")
#        self.model.setHeaderData(5, QtCore.Qt.Horizontal , "Teléfono")
#        self.model.setHeaderData(6, QtCore.Qt.Horizontal , "Email")
#        self.model.setHeaderData(7, QtCore.Qt.Horizontal , "Autónomo")
#        self.model.setHeaderData(8, QtCore.Qt.Horizontal , "Notas")
        self.ui.personal_table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellidos", "Cargo",  
                                  "DNI",  "Teléfono",  "Email",  "Autónomo",  "Notas"])
#-------Si el combobox se activa llama a la funcion de filtrado----------------
        self.loadcombo1()
        self.ui.combo_filtrar_cargos.activated[str].connect(self.filtro_checks)
        self.filtro_checks("ALL")
        self.loadcombo2()
        self.ui.combo_dia_personal.activated[str].connect(self.filtro_dia)
        
                
        self.ui.button_add_personal.clicked.connect(self.anade_persona)
       
#------Función de filtrado----------------------------------------------------       
    
    def filtro_checks(self,text):
        #
        # mere 19/01/2021 cambiado sql, añadido nombre del cargo pero no funciona el filtro
        #
        sql_base = 'SELECT p.id_personal, p.nombre, apellidos, cargos.nombre as cargo, dni, \
        telefono, email, autonomo, notas FROM personal as p,tarifas, cargos'
        sql_base += ' WHERE tarifas.id_personal=p.id_personal AND tarifas.id_cargo = cargos.id_cargo'
        
        print ("voy a filtrar ", text, self.dic_cargos[text])
    
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

        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.personal_table.insertRow(i)
                for j, data in enumerate(row_data):
                    self.ui.personal_table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))
                    
    def filtro_dia(self,text):
        print ("filtro dia ", text)
        self.color_ocupado(text[0:10])

    def load_personal_added(self):
                    
        bd=BdStd()
        txtsql = 'SELECT id_evento, id_personal, yymmdd, nombre FROM personal_evento as pev'
        txtsql += ' JOIN cargos ON cargos.id_cargo = pev.id_cargo   WHERE  id_evento = "' 
        txtsql += self.id_evento + '"'
       
        print ("load_personal_added ", txtsql)
        bd.runsql(txtsql)
        self.ui.personal_added.setRowCount(0)

        if bd.rows != None :
            for i, row_data in enumerate(bd.rows):
                self.ui.personal_added.insertRow(i)
                for j, data in enumerate(row_data):
                    self.ui.personal_added.setItem(i, j, QtWidgets.QTableWidgetItem(str(data)))


    def loadcombo1 (self) :
        
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

    def loadcombo2 (self) :

        
        bd=BdStd()
        txtsql = "SELECT fecha, tarea FROM dias_evento WHERE id_evento = '"+self.id_evento+ "'"
        txtsql += " ORDER BY fecha"
        bd.runsql(txtsql)
        self.ui.combo_dia_personal.clear()

        self.map_fechas =  {"ALL": '000'}
        self.ui.combo_dia_personal.addItem("ALL")

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
            id_personal = self.ui.personal_table.item(row,0).text()
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
        self.yymmdd = fecha[8:10] + fecha[3:5] + fecha[0:2]
        bd=BdStd()
        color = 0
        #------------ mira si está en otros eventos
        txtsql = "SELECT id_cargo, orden FROM personal_evento WHERE id_evento != '{}' AND "
        txtsql += " id_personal = '{}'  AND yymmdd = '{}'"
        txtsql = txtsql.format(id_evento, id_personal, self.yymmdd)
        bd.runsql(txtsql)
        print (bd.rows, txtsql)

        if bd.rows != None and len(bd.rows) > 0:
            color = 1
            print("esta ocupado en otro evento")
        #------------ mira si está ocupado
        txtsql = "SELECT * FROM personal_ocupado WHERE "
        txtsql += " id_personal = '{}'  AND yymmdd = '{}'"
        txtsql = txtsql.format(id_personal, self.yymmdd)
        bd.runsql(txtsql)
        print (bd.rows, txtsql)

        if bd.rows != None and len(bd.rows) > 0:
            color = 2
            print("esta ocupado por terceros") 
        return (color)

    def anade_persona (self):
        
        if self.ui.nom_cargo in self.dic_cargos :
            id_cargo = self.dic_cargos[self.ui.nom_cargo]
        else:
            id_cargo = ""
        if (self.yymmdd != ""):
        #-------------------------- inserta persona, evento, fecha en la base de datos
            bd=BdStd()
#            campos=(self.ui.id_personal, self.id_evento,self.yymmdd, self.ui.id_cargo)
#            bd.runsql("INSERT INTO personal_evento (id_personal, id_evento, yymmdd, id_cargo)\
#                           VALUES (?,?,?,?);",campos)  
            txtsql = "INSERT INTO personal_evento (id_personal, id_evento, yymmdd, id_cargo)\
                           VALUES ('{}','{}','{}','{}');"
            txtsql= txtsql.format(self.ui.id_personal, self.id_evento,self.yymmdd, id_cargo)
            print(txtsql)
            bd.runsql(txtsql)
            self.load_personal_added()
        else :
            print("No ha seleccionado fecha, no añado")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = CrearEvento()
    ui.show()
    sys.exit(app.exec_())