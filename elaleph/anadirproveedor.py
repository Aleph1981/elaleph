# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:50:48 2020

@author: aleja
"""

from anadirproveedor_ui import *


class AnadirProveedor(QtWidgets.QMainWindow, AnadirProveedor_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.aceptcancel.accepted.connect(self.aceptar)
        
    #------------------Aceptar y grabar datos---------------------------------
           
    def aceptar(self):
        
        import sqlite3
        conexion = sqlite3.connect("elaleph.db")
        cursor=conexion.cursor()
        
        #----------------------Checks de servicio-----------------------------
        
        servicio = ""
        
        if self.check_trailer.isChecked():
            servicio += "Trailer "
        if self.check_camion.isChecked():
            servicio+= "Camión "
        if self.check_furgo.isChecked():
            servicio+= "Furgoneta "
        if self.check_runner.isChecked():
            servicio+= "Runner "
        if self.check_c_d.isChecked():
            servicio+= "Carga/Descarga "
        if self.check_rigging.isChecked():
            servicio+= "Rigging "
        if self.check_deco.isChecked():
            servicio+= "Deco "    
        if self.check_generadores.isChecked():
            servicio+= "Generadores "
        if self.check_tradu.isChecked():
            servicio+= "Cabinas de traducción "
        if self.check_catering.isChecked():
            servicio+= "Catering "
        if self.check_iluminacion.isChecked():
            servicio+= "Iluminación "
        if self.check_sonido.isChecked():
            servicio+= "Sonido "
        if self.check_video.isChecked():
            servicio+= "Video "
        if self.check_mobiliario.isChecked():
            servicio+= "Mobiliario "
        if self.check_otros.isChecked():
            servicio+= self.entry_otros.text()
        
    #-----------------Crea una tupla con los campos del proveedor--------------    
        
        campos_proveedor=(self.entry_id.text(),self.entry_empresa.text(),\
                          self.entry_ubicacion.text(),servicio,self.entry_cif.text(),\
            self.entryTFN.text(),self.entry_email.text(),self.entry_contacto.text(),\
            self.entry_tfn_contacto.text(),self.entry_email_contacto.text(),\
            self.textNOTAS.toPlainText())
    
    #-----------------Introduce la tupla en los campos-------------------------
    
        cursor.execute("INSERT INTO proveedores (id_proveedor,empresa,ubicacion,\
                       servicio,cif,telefono,email,contacto1,telefono_contacto1,\
                       email_contacto1,notas) VALUES\
                       (?,?,?,?,?,?,?,?,?,?,?);",campos_proveedor)
                       
    #-----------------Graba y cierra la ventana-------------------------------
    
        conexion.commit()
        conexion.close()
        
        
        self.setupUi(self)
        self.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AnadirProveedor()
    window.show()
    app.exec_()