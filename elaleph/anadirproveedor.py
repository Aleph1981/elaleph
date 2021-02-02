# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:50:48 2020

@author: aleja
"""

from anadirproveedor_ui import *
from bdstd import *

class AnadirProveedor(QtWidgets.QMainWindow, AnadirProveedor_Ui):
    
    def __init__(self, id_proveedor = None, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.opcion = "A"  # Alta
        self.id_proveedor = id_proveedor
        
        
        self.aceptcancel.accepted.connect(self.aceptar)
        
        if self.id_proveedor != None :
            self.loadData()
            self.opcion = "M"  # Modificacion

    def loadData (self) :
        bd = BdStd()
        bd.runsql(f"""SELECT * FROM proveedores WHERE id_proveedor = '{self.id_proveedor}'""")
        # 0 id_proveedor, 1 empresa, 2 provincia, 3 localidad, 4 direccion, 5 servicio, 6 cif, 7 telefono, 
        # 8 email, 9 web, 10 contacto1, 11 telefono_contacto1, 12 email_contacto1, 13 notas
        
        if bd.rows != None :
            for row in bd.rows :
                self.entry_empresa.setText(row[1])
                self.entry_provincia.setText(row[2])
                self.entry_localidad.setText(row[3])
                self.entry_direccion.setText(row[4])
                self.entry_cif.setText(row[6])
                self.entryTFN.setText(row[7])
                self.entry_email.setText(row[8])
                self.entry_web.setText(row[9])
                self.entry_contacto.setText(row[10])
                self.entry_tfn_contacto.setText(row[11])
                self.entry_email_contacto.setText(row[12])
                self.textNOTAS.setPlainText(row[13]) 
                
                
                servicios = row[5]
                self.check_trailer.setChecked(True if servicios.find("Trailer") != -1 else False)
                self.check_camion.setChecked(True if servicios.find("Camión") != -1 else False)
                self.check_furgo.setChecked(True if servicios.find("Furgoneta") != -1 else False)
                self.check_runner.setChecked(True if servicios.find("Runner") != -1 else False)

                self.check_c_d.setChecked(True if servicios.find("Carga/Descarga") != -1 else False)
                self.check_rigging.setChecked(True if servicios.find("Rigging") != -1 else False)
                self.check_deco.setChecked(True if servicios.find("Deco") != -1 else False)
                self.check_generadores.setChecked(True if servicios.find("Generadores") != -1 else False)
                
                self.check_tradu.setChecked(True if servicios.find("Cabinas") != -1 else False)
                self.check_catering.setChecked(True if servicios.find("Catering") != -1 else False)
                self.check_iluminacion.setChecked(True if servicios.find("Iluminación") != -1 else False)
                self.check_sonido.setChecked(True if servicios.find("Sonido") != -1 else False)
                self.check_video.setChecked(True if servicios.find("Video") != -1 else False)
                self.check_mobiliario.setChecked(True if servicios.find("Mobiliario") != -1 else False)
                self.check_otros.setChecked(True if servicios.find("Otro") != -1 else False)
                if servicios.find("Otro") != -1:
                    x = servicios.find("(")
                    y = servicios.find(")")
                    otro = servicios[x+1:y]
                    self.entry_otros.setText(f"{otro} ")
                    print(x,y,otro)  
                    print(servicios)    
    #------------------Aceptar y grabar datos---------------------------------
 
          
    def aceptar(self):
        
        #----------------------Checks de servicio-----------------------------
        
        if self.opcion != "A" :   # Estan modificando, hay que anular los registros de servicios
           #self.borra_tabla_servicios() 
           print("merce no entiendo la tabla de servicios")
            
        self.servicio = ""
        
        if self.check_trailer.isChecked():
            self.servicio += "Trailer "
        if self.check_camion.isChecked():
            self.servicio+= "Camión "
        if self.check_furgo.isChecked():
            self.servicio+= "Furgoneta "
        if self.check_runner.isChecked():
            self.servicio+= "Runner "
        if self.check_c_d.isChecked():
            self.servicio+= "Carga/Descarga "
        if self.check_rigging.isChecked():
            self.servicio+= "Rigging "
        if self.check_deco.isChecked():
            self.servicio+= "Deco "    
        if self.check_generadores.isChecked():
            self.servicio+= "Generadores "
        if self.check_tradu.isChecked():
            self.servicio+= "Cabinas "
        if self.check_catering.isChecked():
            self.servicio+= "Catering "
        if self.check_iluminacion.isChecked():
            self.servicio+= "Iluminación "
        if self.check_sonido.isChecked():
            self.servicio+= "Sonido "
        if self.check_video.isChecked():
            self.servicio+= "Video "
        if self.check_mobiliario.isChecked():
            self.servicio+= "Mobiliario "
        if self.check_otros.isChecked():
            self.serv_list = self.entry_otros.text().split()
            txt=""
            for item in self.serv_list:
                item=item.capitalize()
                txt+=item+" "
            self.servicio += f"Otro( {txt})"
                
    #-----------------Crea una tupla con los campos del proveedor--------------    
        id_proveedor = self.entry_empresa.text()[0:3]+self.entry_cif.text()[0:3]
        id_proveedor = id_proveedor.upper()
        trans_table = id_proveedor.maketrans("Á,É,Í,Ó,Ú,À,È,Ì,Ò,Ù","A,E,I,O,U,A,E,I,O,U")
        id_proveedor = id_proveedor.translate(trans_table)
        self.id_proveedor=id_proveedor
        
        
        campos_proveedor=(self.id_proveedor,self.entry_empresa.text().upper(),\
            self.entry_provincia.text().capitalize(),self.entry_localidad.text().capitalize(),\
            self.entry_direccion.text().capitalize(),self.servicio,self.entry_cif.text(),\
            self.entryTFN.text(),self.entry_email.text().lower(),self.entry_web.text().lower(),\
            self.entry_contacto.text(),self.entry_tfn_contacto.text(),\
            self.entry_email_contacto.text().lower(),self.textNOTAS.toPlainText())
    
    #-----------------Introduce la tupla en los campos-------------------------
        bd=BdStd()    
        if self.opcion == "A" :         # Alta  
            try:
                
                bd.runsql("INSERT INTO proveedores (id_proveedor,empresa,provincia,\
                           localidad,direccion,servicio,cif,telefono,email,web,contacto1,\
                           telefono_contacto1,email_contacto1,notas) VALUES\
                           (?,?,?,?,?,?,?,?,?,?,?,?,?,?);",campos_proveedor)
            except Exception as e:
                print(e)
        else :

            txtsql = "UPDATE proveedores SET empresa = '{1}', provincia = '{2}', localidad = '{3}'," \
            "direccion = '{4}', servicio = '{5}', cif = '{6}'," \
            "telefono = '{7}', email = '{8}', web = '{9}'," \
            "contacto1 = '{10}', telefono_contacto1 = '{11}', email_contacto1 = '{12}'," \
            " notas = '{13}' WHERE id_proveedor = '{0}'"
            txtsql = txtsql.format(self.id_proveedor,self.entry_empresa.text().upper(),\
                self.entry_provincia.text().capitalize(),self.entry_localidad.text().capitalize(),\
                self.entry_direccion.text().capitalize(),self.servicio,self.entry_cif.text(),\
                self.entryTFN.text(),self.entry_email.text().lower(),self.entry_web.text().lower(),\
                self.entry_contacto.text(),self.entry_tfn_contacto.text(),\
                self.entry_email_contacto.text().lower(),self.textNOTAS.toPlainText())
            bd.runsql(txtsql)
            
        
        self.close()
        
    # def borra_tabla_servicios(self) :
    #     bd1=BdStd()
    #     try:               
    #         bd1.runsql(f"""DELETE FROM proveedor_servicio WHERE id_proveedor = '{self.id_proveedor}';""")
        
    #     except Exception as e:
    #         print(e)           
        
    # def add_servicio(self,item):
    #     bd1=BdStd()
    #     #------------------Alejandro 28-1
    #     if item != "":
    #         try:               
    #             bd1.runsql(f"INSERT INTO servicios (servicio) VALUES ('{item}');")
            
    #         except Exception as e:
    #             print(e)     
                
                
    
    
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AnadirProveedor("ALBB45")
    window.show()
    app.exec_()