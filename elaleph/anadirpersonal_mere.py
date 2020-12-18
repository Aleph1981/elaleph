# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:21:22 2020

@author: aleja
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:14:57 2020
@author: Alejandro Pérez Pérez
"""

# mere cambiados imports
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QApplication, QMainWindow, QDialog, QLineEdit
from PyQt5 import QtCore, QtGui 
import os
from anadirpersonal_ui import *
from bdstd import *




#-------------------Clase de la ventana añadir personal-----------------------

class AnadirPersonal(QtWidgets.QMainWindow, AnadirPersonal_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

#-------------------Accion de los botones aceptar y cancelar------------------
        
        self.aceptcancel.accepted.connect(self.aceptar)
        self.aceptcancel.rejected.connect(self.cancelar)
        
        # ---> mere added
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
            label_c.setGeometry(20, 10+(i*25), 80, 20) 
            
            checkBox_c = QtWidgets.QCheckBox(self.widget)
            checkBox_c.setObjectName("checkBox_c"+str(i))
            checkBox_c.setGeometry(120, 10+(i*25), 50, 20)
            if map_cargo['checked'] == "1" :
                checkBox_c.setChecked(True)
            else:
                checkBox_c.setChecked(False)
            
            input_c = QtWidgets.QLineEdit(self.widget)
            input_c.setObjectName("input_c"+str(i))
            input_c.setGeometry(200, 10+(i*25), 80, 20)
            input_c.setStyleSheet("background-color: rgb(255, 255, 255);")
            input_c.setText(str(map_cargo['tarifa']))
        # ---> end mere added
                
#------------------Aceptar y grabar datos--------------------------------------
           
    def aceptar(self):
        

        
        if self.radioSI.isChecked():
            autonomo="Si"
        elif self.radioNO.isChecked():
            autonomo="No"
        
        campos_personal=(self.entryID.text(),self.entryNOMBRE.text(),self.entryAPELL.text(),self.entryDNI.text(),\
                self.entryTFN.text(),self.entryEMAIL.text(),autonomo,self.textNOTAS.toPlainText())
        txtsql = "INSERT INTO personal (id_personal,nombre,apellidos,dni,telefono,email,autonomo,notas) VALUES\
                (?,?,?,?,?,?,?,?);"
            
        bd = BdStd()
        bd.runsql(txtsql, campos_personal)

#-----------------Chequeo de los checkboxes----------------------------------- 
#
# ---> mere added
#
        self.id_personal = self.entryID.text()
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
#
# ---> end mere added

                    
#------Crea una carpeta con su id como nombre para guardar su documentación----

        carpeta = self.entryID.text()
        os.mkdir(f"{carpeta}")        

#---------------------------Tras chequearlos todos graba y cierra-------------                  
#       mere commentado
#        conexion.commit()
#        conexion.close()
        self.setupUi(self)
        self.close()
          
#------------- Funcion cancelar y cerrar ventana-------------------------------
    
    def cancelar(self):
        self.setupUi(self)
        self.close()    
        
#-------------------------------------------------------------------
# mere añadidas funciones
# LAS TRES FUNCIONES QUE CARGAN LOS CARGOS, TARIFAS DE LA BBDD Y 
# LAS GUARDAN
#------------------------------------------------------------------
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
    #print(map_cargos)
    return (map_cargos)


def guardaTarifas(id_personal, map_cargos):
    # guarda los cargos y las tarifas de la persona en la base de datos
    #
    bd = BdStd()
    bd.runsql("DELETE FROM tarifas WHERE id_personal = '"+id_personal+"'")
    
    txtsql = "INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES ('{}','{}','{}');"

    for item in map_cargos :
    
        if item['checked'] == "1":
           
           bd.runsql(txtsql,id_personal, item['id'], str(item['tarifa']))       
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AnadirPersonal()
    window.show()
    app.exec_()