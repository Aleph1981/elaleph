# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:50:51 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
#import easygui
from personalevento_ui import *
from bdstd import BdStd


class PersonalEvento(QtWidgets.QDialog, PersonalEvento_Ui):
    
    def __init__(self, self_padre = None, alta = None):
        QtWidgets.QDialog.__init__(self)
        self.ui = PersonalEvento_Ui()
        self.ui.setupUi(self)        
        self.padre = self_padre
        self.esalta = alta
        self.id_personal = ""
        self.nom_cargo = ""
        self.fecha = ""
        self.clave_registro = ""

        if self.padre == None: 
           qm = QtWidgets.QMessageBox
           qm.warning(self, '', "Error: necesita ser abierto desde un evento")
           self.close()

    #-----------------Conexion de los botones---------------------------------
        self.ui.buttonGuardar.clicked.connect(self.guardar_cambios)
        self.ui.buttonCancelar.clicked.connect(self.eliminar)
        
    #-----------------Relleno de las cajas de texto----------------------------------

        self.ui.inputEvento.setText (self.padre.id_evento)
        if self.esalta == False :  
             # es una modificación de un registro existente carga del grid inferior datos pev (personal_evento)
            self.load_grid_inferior()
        else:   
             # es una alta, coge los datos del grid superior 

            self.id_personal = self.padre.id_personal
            self.nom_cargo = self.padre.nom_cargo
            self.fecha = self.padre.fecha
            self.hora= self.padre.hora
            print("alta"+self.fecha)

        self.ui.inputCodigo.setText(self.id_personal)
        self.ui.inputFecha.setText (self.fecha+" "+self.hora)
        
        self.load_datos_ficha_persona()

        #--------------- crea combo de cargos
        self.cargacombocargos()
      
        # posiciona el combo con el cargo escogido
        index = self.ui.comboBox.findText(self.nom_cargo, QtCore.Qt.MatchFixedString)
        print("index", index)
        if index >= 0:
             self.ui.comboBox.setCurrentIndex(index)

   
    def load_grid_inferior (self):

        # en la parrilla de crear evento el orden es : fecha, cargo, id_personal
        for i, item in enumerate(self.padre.ui.personal_added.selectedItems()) :
            if i== 0: 
                self.fecha_hora = item.text()
                tmp=self.fecha_hora.split(" ")
                self.fecha=tmp[0]
                self.hora=tmp[1]
            if i== 1: 
                self.nom_cargo = item.text()
            if i== 2: 
                self.id_personal = item.text()
            
        bd1=BdStd() 
        txtsql = f"""SELECT suplemento, orden FROM personal_evento 
        WHERE id_evento = '{self.padre.id_evento}' 
        AND strftime('%d-%m-%Y',fecha) = '{self.fecha}' AND id_personal = '{self.id_personal}'"""
        bd1.runsql(txtsql) 
        print("cargo", self.nom_cargo, txtsql)
        if bd1.rows != None :
            for row_data in bd1.rows:
                self.ui.inputSuplem.setText(str(row_data[0]))
                self.clave_registro = row_data[1]
                
    def load_datos_ficha_persona (self):
            
        bd1=BdStd() 
        txtsql = f"""SELECT nombre, apellidos FROM personal WHERE id_personal = '{self.id_personal}'"""
        bd1.runsql(txtsql) 
        if bd1.rows != None :
            for row_data in bd1.rows:
                self.ui.inputNombre.setText(row_data[0])
                self.ui.inputApellidos.setText(row_data[1])

    #--------------- crea combo de cargos       

    def cargacombocargos (self):
        
        self.dic_cargos ={}    #crea un diccionario vacio
        bd1=BdStd()        
        txtsql = f"""SELECT tarifas.id_cargo,  cargos.nombre FROM tarifas
        JOIN cargos ON cargos.id_cargo = tarifas.id_cargo
        WHERE tarifas.id_personal='{self.id_personal}'"""
        bd1.runsql(txtsql) 
        if bd1.rows != None :
            for i, row_data in enumerate(bd1.rows):
                self.ui.comboBox.addItem(row_data[1])
                self.dic_cargos [row_data[1]] = row_data[0]
        
    def guardar_cambios(self):

        #------------------ buscar el código de cargo a partir del nombre        
        nom_cargo = self.ui.comboBox.currentText()
        if  nom_cargo in self.dic_cargos :
            id_cargo = self.dic_cargos[nom_cargo]
        else:
            id_cargo = ""

        if self.padre != None: 
            #-------------------------- inserta persona, evento, fecha en la base de datos
            if self.esalta == True :
                if (self.padre.fecha != ""):
                    if (self.padre.fecha == "ALL"):   # crea un registro por cada dia del evento
                        bd1=BdStd()        
                        txtsql = f"""SELECT strftime('%d-%m-%Y',fecha),hora FROM dias_evento WHERE id_evento = '{self.padre.id_evento}'"""
                        bd1.runsql(txtsql) 
                        if bd1.rows != None :
                            for row_data in bd1.rows :
                                self.crear_fecha(row_data[0],row_data[1], id_cargo)
                                
                    else :
                        # crea solo para el dia escogido
                        self.crear_fecha( self.padre.fecha,self.hora, id_cargo)
                    
            else  :    # no es un alta, es un cambio
                bd=BdStd()                
                txtsql = f"""UPDATE personal_evento SET suplemento = '{self.ui.inputSuplem.text()}'"""
                if nom_cargo != self.nom_cargo :
                    txtsql += f""", id_cargo = '{id_cargo}'"""

                txtsql += f"""  WHERE orden = {self.clave_registro} """
                print(txtsql)
                bd.runsql(txtsql)
                    
                    
        self.padre.load_personal_added()  # Refresca grid padre
        self.close()
  

    def crear_fecha(self, fecha,hora, id_cargo):
        
        bd=BdStd()
        txtsql = "INSERT INTO personal_evento (id_personal, id_evento,fecha, id_cargo\
                       , suplemento,hora) VALUES ('{}','{}','{}','{}','{}','{}');"
        txtsql= txtsql.format(self.id_personal, self.padre.id_evento,
                              bd.gira_fecha(fecha), 
                              id_cargo, self.ui.inputSuplem.text(),hora)
        print(txtsql)
        bd.runsql(txtsql)
              
    def eliminar(self):
        print("No borro ")
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = PersonalEvento()
    ui.show()
    sys.exit(app.exec_())