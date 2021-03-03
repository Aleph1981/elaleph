# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:14:57 2020

@author: Alejandro Pérez Pérez
"""

from anadirpersonal_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from bdstd import *
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QApplication, QLineEdit
#-------------------Clase de la ventana añadir personal-----------------------

class AnadirPersonal(QtWidgets.QWidget, AnadirPersonal_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)

#-------------------Accion de los botones aceptar y cancelar------------------
        
        self.buttonAceptar.clicked.connect(self.aceptar)
        self.buttonCancelar.clicked.connect(self.cancelar)
        self.radioSI.setChecked(True)
        #---------------- Crea un array con todos los datos de cargos y marca los que tiene 
        #                 activos la persona indicada. Se llama map_cargos porque no son los
        #                 controles checkbox sinó una estructura de datos que sirve de mapa
        #                 para crealos después
        #'id', 'nombre',  'tarifa', 'checked' : "0" / "1"
        
        
        self.map_cargos = getArrayCargos()
        
        for i, map_cargo in enumerate(self.map_cargos):
            title = map_cargo['nombre']
            label_c = QtWidgets.QLabel(title,self.widget)
            label_c.setObjectName("label_c"+str(i))
            label_c.setGeometry(20, 100+(i*25), 140, 20) 
            
            checkBox_c = QtWidgets.QCheckBox(self.widget)
            checkBox_c.setObjectName("checkBox_c"+str(i))
            checkBox_c.setGeometry(130, 100+(i*25), 140, 20)
            if map_cargo['checked'] == "1" :
                checkBox_c.setChecked(True)
            else:
                checkBox_c.setChecked(False)
            
            input_c = QtWidgets.QLineEdit(self.widget)
            input_c.setObjectName("input_c"+str(i))
            input_c.setGeometry(200, 100+(i*25), 80, 20)
            input_c.setStyleSheet("background-color: rgb(255, 255, 255);")
            input_c.setText(str(map_cargo['tarifa']))




#------------------Aceptar y grabar datos--------------------------------------
           
    def aceptar(self):
        
        

#----------generador de id------------------------------------------------------

        id_personal = self.entryNOMBRE.text()[0:2]+self.entryAPELL.text()[0:2]+self.entryDNI.text()[0:2]
        id_personal = id_personal.upper()
        trans_table = id_personal.maketrans("Á,É,Í,Ó,Ú,À,È,Ì,Ò,Ù","A,E,I,O,U,A,E,I,O,U")
        id_personal = id_personal.translate(trans_table)
        self.id_personal=id_personal

#-----------radio button de autonomo-------------------------------------------
        autonomo=""
        if self.radioSI.isChecked():
            autonomo="Si"
        elif self.radioNO.isChecked():
            autonomo="No"
        
            
#---------------FORMATO DE NOMBRE Y APELLIDOS----------------------------------

        nombre = self.entryNOMBRE.text()
        apellidos = self.entryAPELL.text()
        nombre=nombre.split(" ")
        apellidos= apellidos.split(" ")
        nom=""
        apell=""
        for palabra in nombre:
            palabra=palabra.capitalize()
            nom+=palabra+" "
        for palabra in apellidos:
            palabra=palabra.capitalize()
            apell+=palabra+" "



#------------crea la tupla de campos y la inserta en la bbdd-------------------
        if len(id_personal)>4:

            try:
                campos_personal=(id_personal,nom,apell,\
                        self.entryDNI.text().upper(),self.entryTFN.text(),self.entryEMAIL.text().lower(),\
                        autonomo,self.entryDIRECCION.text().capitalize(),self.entryCP.text(),\
                        self.entryCIUDAD.text().capitalize(),self.entryIBAN.text().upper(),self.textNOTAS.toPlainText())
                
                bd=BdStd()
                
                    
                bd.runsql("INSERT INTO personal (id_personal,nombre,apellidos,dni,\
                               telefono,email,autonomo,direccion,cp,ciudad,iban,notas)\
                               VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",campos_personal)
        
        #-----------------Chequeo de los checkboxes-----------------------------------        
        
                
                i = 0
                for checkobj in self.widget.findChildren(QCheckBox):
                    
                    if checkobj.checkState():
                        self.map_cargos[i]['checked'] = "1"
                        
                    else: 
                        self.map_cargos[i]['checked'] = "0"
                        
                    i+=1
                
                i = 0
                for caja in self.widget.findChildren(QLineEdit):
                    
                    if caja.text() != "":
                        self.map_cargos[i]['tarifa'] = int(caja.text())
                    i+=1   
                
                guardaTarifas(self.id_personal, self.map_cargos)
                            
    #------Crea una carpeta con su id como nombre para guardar su documentación----
            
                os.mkdir(f"{id_personal}")        
    
    #---------------------------Tras chequearlos todos graba y cierra-------------                  
    
                
                self.setupUi(self)
                self.close()
            
            except Exception as e:
                msgBox = QtWidgets.QMessageBox()
                msgBox.warning(self, "Aleph", f"{e}")
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.warning(self, "Aleph", "Introduzca Nombre, apellidos y dni")
            
            
            
          
#------------- Funcion cancelar y cerrar ventana-------------------------------
    
    def cancelar(self):
        self.setupUi(self)
        self.close()    

def getArrayCargos():
    # devuelve un array con los cargos de la base de datos
    #
    bd = BdStd()
    map_cargos = []
    bd.runsql("SELECT * FROM cargos ORDER BY id_cargo")  #id_cargo, nombre, tarifa
    
    if bd.rows != None :
        for row in bd.rows :
            dic = {'id' : row[0], 'nombre' : row[1],  'tarifa' : row[2], 'checked' : "0"}
            map_cargos.append(dic)
    return (map_cargos)


def guardaTarifas(id_personal, map_cargos):
    # guarda los cargos y las tarifas de la persona en la base de datos
    #
    bd = BdStd()
    bd.runsql("DELETE FROM tarifas WHERE id_personal = '"+id_personal+"'")
    
    txtsql = "INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES ('{}','{}','{}');"

    for item in map_cargos :
    
        if item['checked'] == "1":
           
           bd.runsql(txtsql.format(id_personal, item['id'], str(item['tarifa'])))     
           print(txtsql.format(id_personal, item['id'], str(item['tarifa'])))
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AnadirPersonal()
    window.show()
    app.exec_()