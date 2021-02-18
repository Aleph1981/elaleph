# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:50:51 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
#import easygui
from proveedorevento_ui import *
from bdstd import BdStd


class ProveedorEvento(QtWidgets.QDialog, ProveedorEvento_Ui):
    
    def __init__(self, self_padre = None, alta = None):
        QtWidgets.QDialog.__init__(self)
        self.ui = ProveedorEvento_Ui()
        self.ui.setupUi(self)        
        self.padre = self_padre
        self.esalta = alta
        self.id_proveedor = ""
        self.nom_servicio = ""
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
             # es una modificación de un registro existente carga del grid inferior datos pev (proveedor_evento)
            self.load_grid_inferior()
        else:   
             # es una alta, coge los datos del grid superior 

            self.id_proveedor = self.padre.id_proveedor
            self.nom_servicio = self.padre.nom_servicio
            self.fecha = self.padre.fecha_prov
        
        self.ui.inputCodigo.setText(self.id_proveedor)
        self.ui.inputFecha.setText (self.fecha)
        
        self.load_datos_ficha_proveedor()

        #--------------- crea combo de cargos
        self.carga_combo_servicios()

   
    def load_grid_inferior (self):

        # en la parrilla de crear evento el orden es : fecha, cargo, id_proveedor
        for i, item in enumerate(self.padre.ui.prov_added.selectedItems()) :
            if i== 0: 
                self.fecha = item.text()
            if i== 1: 
                self.nom_servicio = item.text()
            if i== 2: 
                self.id_proveedor = item.text()
            
        bd1=BdStd() 
        txtsql = f"""SELECT orden, contacto_onsite, telefono_onsite,email_onsite, notas 
        FROM proveedores_evento 
        WHERE id_evento = '{self.padre.id_evento}' 
        AND strftime('%d-%m-%Y',fecha) = '{self.fecha}' AND id_proveedor = '{self.id_proveedor}'"""
        bd1.runsql(txtsql) 
        print("servicio", self.nom_servicio, txtsql)
        if bd1.rows != None :
            for row_data in bd1.rows:
                self.clave_registro = row_data[0]
                self.ui.inputContacto.setText(row_data[1])
                self.ui.inputTelefono.setText(row_data[2])
                self.ui.inputEmail.setText(row_data[3])
                self.ui.inputNotas.setPlainText(row_data[4])


                
    def load_datos_ficha_proveedor (self):
            
        bd1=BdStd() 
        txtsql = f"""SELECT empresa FROM proveedores WHERE id_proveedor = '{self.id_proveedor}'"""
        bd1.runsql(txtsql) 
        if bd1.rows != None :
            for row_data in bd1.rows:
                self.ui.inputEmpresa.setText(row_data[0])
                

    #--------------- crea combo de cargos       

    def carga_combo_servicios (self):
        
        self.list_servicios = []   
        bd1=BdStd()        
        bd1.runsql(f"SELECT servicio FROM proveedores WHERE id_proveedor='{self.id_proveedor}'") 
        if bd1.rows != None :
            print(bd1.rows)
            servicios = bd1.rows[0][0].split()
            #print("servicios ",servicios)
            for item in servicios:
                self.list_servicios.append(item)
                self.ui.comboServicio.addItem(item)
        
                
        
    def guardar_cambios(self):

        #------------------ buscar el código de cargo a partir del nombre        
        nom_servicio = self.ui.comboServicio.currentText()
        
        if self.padre != None: 
            print("pasa el if de padre")#-------------------------- inserta proveedor, evento, fecha en la base de datos
            if self.esalta == True :
                print("pasa el if de alta") 
                if (self.padre.fecha_prov != ""):
                    print("pasa el if de padre.fecha")
                    if (self.padre.fecha_prov == "ALL"):   # crea un registro por cada dia del evento
                        bd1=BdStd()        
                        txtsql = f"""SELECT strftime('%d-%m-%Y',fecha) FROM dias_evento WHERE id_evento = '{self.padre.id_evento}'"""
                        bd1.runsql(txtsql) 
                        if bd1.rows != None :
                            print(bd1.rows)
                            for row_data in bd1.rows :
                                self.crear_fecha(row_data[0], nom_servicio)
                                
                                
                    else :
                        # crea solo para el dia escogido
                        self.crear_fecha( self.padre.fecha_prov, nom_servicio)
            else  :    # no es un alta, es un cambio
                bd=BdStd()                
                txtsql = f"""UPDATE proveedores_evento SET contacto_onsite = '{self.ui.inputContacto.text()}', \
                telefono_onsite = '{self.ui.inputTelefono.text()}', \
                email_onsite = '{self.ui.inputEmail.text().lower()}', \
                notas = '{self.ui.inputNotas.toPlainText()}' """
                
                if nom_servicio != self.nom_servicio :
                    txtsql += f""", servicio = '{nom_servicio}'"""

                txtsql += f"""  WHERE orden = {self.clave_registro} """
                print(txtsql)
                bd.runsql(txtsql)                        
                    
                 
        self.padre.load_prov_added()  # Refresca grid padre
        self.close()
  

    def crear_fecha(self, fecha, nom_servicio):
        print("pasa por crearfecha")
        bd=BdStd()
        txtsql = "INSERT INTO proveedores_evento (id_proveedor, id_evento, servicio, fecha\
                       ,hora, contacto_onsite, telefono_onsite,email_onsite, notas) \
                    VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');"
        txtsql= txtsql.format(self.id_proveedor, self.padre.id_evento, nom_servicio,
                              bd.gira_fecha(fecha),self.hora.time(), self.ui.inputContacto.text(),
                              self.ui.inputTelefono.text(),self.ui.inputEmail.text().lower(),
                              self.ui.inputNotas.toPlainText())
        print(txtsql)
        bd.runsql(txtsql)
              
    def eliminar(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ProveedorEvento()
    ui.show()
    sys.exit(app.exec_())