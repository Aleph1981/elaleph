# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:14:57 2020

@author: Alejandro Pérez Pérez
"""

from anadirpersonal_ui import *
from error import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os


#-------------------Clase de la ventana añadir personal-----------------------

class AnadirPersonal(QtWidgets.QMainWindow, AnadirPersonal_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

#-------------------Accion de los botones aceptar y cancelar------------------
        
        self.aceptcancel.accepted.connect(self.aceptar)
        self.aceptcancel.rejected.connect(self.cancelar)





#------------------Aceptar y grabar datos--------------------------------------
           
    def aceptar(self):
        
        import sqlite3
        conexion = sqlite3.connect("elaleph.db")
        cursor=conexion.cursor()

#----------generador de id------------------------------------------------------

        id_personal = self.entryNOMBRE.text()[0:2]+self.entryAPELL.text()[0:2]+self.entryDNI.text()[0:2]
        id_personal = id_personal.upper()
        trans_table = id_personal.maketrans("Á,É,Í,Ó,Ú,À,È,Ì,Ò,Ù","A,E,I,O,U,A,E,I,O,U")
        id_personal = id_personal.translate(trans_table)
        

#-----------radio button de autonomo-------------------------------------------

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
        try:
            campos_personal=(id_personal,nom,apell,\
                    self.entryDNI.text().upper(),self.entryTFN.text(),self.entryEMAIL.text().lower(),\
                    autonomo,self.entryDIRECCION.text().capitalize(),self.entryCP.text(),\
                    self.entryCIUDAD.text().capitalize(),self.entryIBAN.text().upper(),self.textNOTAS.toPlainText())
                
            cursor.execute("INSERT INTO personal (id_personal,nombre,apellidos,dni,\
                           telefono,email,autonomo,direccion,cp,ciudad,iban,notas)\
                           VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",campos_personal)
    
    #-----------------Chequeo de los checkboxes-----------------------------------        
    
            #--------------------------CC------------------------------------------
            
            if self.checkCC.isChecked():
                
                cargo_CC = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='cc';").fetchone()
                cargo_CC = cargo_CC[0]
                
                if self.tarifaCC.text() != "":
                    tarifa_CC=self.tarifaCC.text()
                else:
                    tarifa_CC=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'cc';").fetchone()
                    tarifa_CC=tarifa_CC[0]
                    
                    
                tarifas_CC=(id_personal,cargo_CC,tarifa_CC)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_CC)
            
            #---------------------------OPL----------------------------------------
            
            if self.checkOPL.isChecked():
                
                cargo_OPL = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='opl';").fetchone()
                cargo_OPL = cargo_OPL[0]
                
                if self.tarifaOPL.text() != "":
                    tarifa_OPL=self.tarifaOPL.text()
                else:
                    tarifa_OPL=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'opl';").fetchone()
                    tarifa_OPL=tarifa_OPL[0]
                    
                tarifas_OPL=(id_personal,cargo_OPL,tarifa_OPL)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_OPL)
            
            #---------------------------DIM----------------------------------------
            
            if self.checkDIM.isChecked():
                
                cargo_DIM = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='dim';").fetchone()
                cargo_DIM = cargo_DIM[0]
                
                if self.tarifaDIM.text() != "":
                    tarifa_DIM=self.tarifaDIM.text()
                else:
                    tarifa_DIM=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'dim';").fetchone()
                    tarifa_DIM=tarifa_DIM[0]
                    
                tarifas_DIM=(id_personal,cargo_DIM,tarifa_DIM)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_DIM)
            
            #---------------------------TECL----------------------------------------
            
            if self.checkTECL.isChecked():
                
                cargo_TECL = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='tecl';").fetchone()
                cargo_TECL = cargo_TECL[0]
                
                if self.tarifaTECL.text() != "":
                    tarifa_TECL=self.tarifaTECL.text()
                else:
                    tarifa_TECL=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'tecl';").fetchone()
                    tarifa_TECL=tarifa_TECL[0]
                    
                tarifas_TECL=(id_personal,cargo_TECL,tarifa_TECL)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_TECL)
                        
            #---------------------------RIGG---------------------------------------
            
            if self.checkRIG.isChecked():
                
                cargo_RIG = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='rigg';").fetchone()
                cargo_RIG = cargo_RIG[0]
                
                if self.tarifaRIG.text() != "":
                    tarifa_RIG=self.tarifaRIG.text()
                else:
                    tarifa_RIG=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'rigg';").fetchone()
                    tarifa_RIG=tarifa_RIG[0]
                    
                tarifas_RIG=(id_personal,cargo_RIG,tarifa_RIG)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_RIG)
                        
            #---------------------------REGI---------------------------------------
            
            if self.checkREGI.isChecked():
                
                cargo_REGI = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='regi';").fetchone()
                cargo_REGI = cargo_REGI[0]
                
                if self.tarifaREGI.text() != "":
                    tarifa_REGI=self.tarifaREGI.text()
                else:
                    tarifa_REGI=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'regi';").fetchone()
                    tarifa_REGI=tarifa_REGI[0]
                    
                tarifas_REGI=(id_personal,cargo_REGI,tarifa_REGI)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_REGI)
                        
            #---------------------------OPS---------------------------------------
            
            if self.checkOPS.isChecked():
                
                cargo_OPS = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='ops';").fetchone()
                cargo_OPS = cargo_OPS[0]
                
                if self.tarifaOPS.text() != "":
                    tarifa_OPS=self.tarifaOPS.text()
                else:
                    tarifa_OPS=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'ops';").fetchone()
                    tarifa_OPS=tarifa_OPS[0]
                    
                tarifas_OPS=(id_personal,cargo_OPS,tarifa_OPS)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_OPS)
                        
            #---------------------------RF---------------------------------------
            
            if self.checkRF.isChecked():
                
                cargo_RF = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='rf';").fetchone()
                cargo_RF = cargo_RF[0]
                
                if self.tarifaRF.text() != "":
                    tarifa_RF=self.tarifaRF.text()
                else:
                    tarifa_RF=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'rf';").fetchone()
                    tarifa_RF=tarifa_RF[0]
                    
                tarifas_RF=(id_personal,cargo_RF,tarifa_RF)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_RF)
                        
            #---------------------------TECS---------------------------------------
            
            if self.checkTECS.isChecked():
                
                cargo_TECS = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='tecs';").fetchone()
                cargo_TECS = cargo_TECS[0]
                
                if self.tarifaTECS.text() != "":
                    tarifa_TECS=self.tarifaTECS.text()
                else:
                    tarifa_TECS=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'tecs';").fetchone()
                    tarifa_TECS=tarifa_TECS[0]
                    
                tarifas_TECS=(id_personal,cargo_TECS,tarifa_TECS)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_TECS)
                        
            #---------------------------DECO---------------------------------------
            
            if self.checkDECO.isChecked():
                
                cargo_DECO = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='deco';").fetchone()
                cargo_DECO = cargo_DECO[0]
                
                if self.tarifaDECO.text() != "":
                    tarifa_DECO=self.tarifaDECO.text()
                else:
                    tarifa_DECO=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'deco';").fetchone()
                    tarifa_DECO=tarifa_DECO[0]
                    
                tarifas_DECO=(id_personal,cargo_DECO,tarifa_DECO)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_DECO)
                        
            #---------------------------CONT---------------------------------------
            
            if self.checkCONT.isChecked():
                
                cargo_CONT = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='cont';").fetchone()
                cargo_CONT = cargo_CONT[0]
                
                if self.tarifaCONT.text() != "":
                    tarifa_CONT=self.tarifaCONT.text()
                else:
                    tarifa_CONT=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'cont';").fetchone()
                    tarifa_CONT=tarifa_CONT[0]
                    
                tarifas_CONT=(id_personal,cargo_CONT,tarifa_CONT)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_CONT)
                        
            #---------------------------OPV---------------------------------------
            
            if self.checkOPV.isChecked():
                
                cargo_OPV = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='opv';").fetchone()
                cargo_OPV = cargo_OPV[0]
                
                if self.tarifaOPV.text() != "":
                    tarifa_OPV=self.tarifaOPV.text()
                else:
                    tarifa_OPV=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'opv';").fetchone()
                    tarifa_OPV=tarifa_OPV[0]
                    
                tarifas_OPV=(id_personal,cargo_OPV,tarifa_OPV)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_OPV)
                        
            #---------------------------LED---------------------------------------
            
            if self.checkLED.isChecked():
                
                cargo_LED = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='led';").fetchone()
                cargo_LED = cargo_LED[0]
                
                if self.tarifaLED.text() != "":
                    tarifa_LED=self.tarifaLED.text()
                else:
                    tarifa_LED=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'led';").fetchone()
                    tarifa_LED=tarifa_LED[0]
                    
                tarifas_LED=(id_personal,cargo_LED,tarifa_LED)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_LED)
                        
            #---------------------------TECV---------------------------------------
            
            if self.checkTECV.isChecked():
                
                cargo_TECV = cursor.execute("SELECT id_cargo FROM cargos WHERE id_cargo ='tecv';").fetchone()
                cargo_TECV = cargo_TECV[0]
                
                if self.tarifaTECV.text() != "":
                    tarifa_TECV=self.tarifaTECV.text()
                else:
                    tarifa_TECV=cursor.execute("SELECT tarifa FROM cargos WHERE id_cargo = 'tecv';").fetchone()
                    tarifa_TECV=tarifa_TECV[0]
                    
                tarifas_TECV=(id_personal,cargo_TECV,tarifa_TECV)    
                         
                cursor.execute("INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES\
                        (?,?,?);",tarifas_TECV)
                        
#------Crea una carpeta con su id como nombre para guardar su documentación----
        
            os.mkdir(f"{id_personal}")        

#---------------------------Tras chequearlos todos graba y cierra-------------                  

            conexion.commit()
            conexion.close()
            self.setupUi(self)
            self.close()
        
        except Exception as error:
            self.window=Error(str(error))
            self.window.show()
            
            
          
#------------- Funcion cancelar y cerrar ventana-------------------------------
    
    def cancelar(self):
        self.setupUi(self)
        self.close()    
        
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AnadirPersonal()
    window.show()
    app.exec_()