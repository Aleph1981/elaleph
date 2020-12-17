# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:24:02 2020

@author: aleja
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anadirpersonal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class AnadirPersonal_Ui(object):
    def setupUi(self, MainWindow):
        
        """Esta función crea la ventana"""
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 526)
        #MainWindow.setStyleSheet("background-color: rgb(125, 125, 125);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
   #---------------------------------Título-----------------------------
        
        self.anadirperso = QtWidgets.QLabel(self.centralwidget)
        self.anadirperso.setGeometry(QtCore.QRect(20, 10, 231, 61))
        self.anadirperso.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.anadirperso.setObjectName("anadirperso")
        
   #------------------------Entry datos personales---------------------
    
        self.entryID = QtWidgets.QLineEdit(self.centralwidget)
        self.entryID.setGeometry(QtCore.QRect(110, 100, 150, 22))
        self.entryID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryID.setObjectName("entryID")
        self.entryNOMBRE = QtWidgets.QLineEdit(self.centralwidget)
        self.entryNOMBRE.setGeometry(QtCore.QRect(110, 140, 150, 22))
        self.entryNOMBRE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryNOMBRE.setObjectName("entryNOMBRE")
        self.entryAPELL = QtWidgets.QLineEdit(self.centralwidget)
        self.entryAPELL.setGeometry(QtCore.QRect(110, 180, 150, 22))
        self.entryAPELL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryAPELL.setObjectName("entryAPELL")
        self.entryDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.entryDNI.setGeometry(QtCore.QRect(110, 220, 150, 22))
        self.entryDNI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryDNI.setObjectName("entryDNI")   
        self.entryTFN = QtWidgets.QLineEdit(self.centralwidget)
        self.entryTFN.setGeometry(QtCore.QRect(110, 260, 150, 22))
        self.entryTFN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryTFN.setObjectName("entryTFN")
        self.entryEMAIL = QtWidgets.QLineEdit(self.centralwidget)
        self.entryEMAIL.setGeometry(QtCore.QRect(110, 300, 150, 22))
        self.entryEMAIL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entryEMAIL.setObjectName("entryEMAIL")
        
    #----------------------------Campo de texto para notas--------------------
        
        self.textNOTAS = QtWidgets.QTextEdit(self.centralwidget)
        self.textNOTAS.setGeometry(QtCore.QRect(110, 380, 221, 111))
        self.textNOTAS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textNOTAS.setObjectName("textNOTAS")
        
    #----------------------------Radio buttons si o no------------------------
    
        self.radioSI = QtWidgets.QRadioButton(self.centralwidget)
        self.radioSI.setGeometry(QtCore.QRect(110, 340, 51, 20))
        self.radioSI.setChecked(True)
        self.radioSI.setObjectName("radioSI")
        
        
        self.radioNO = QtWidgets.QRadioButton(self.centralwidget)
        self.radioNO.setGeometry(QtCore.QRect(160, 340, 51, 20))
        self.radioNO.setObjectName("radioNO")
        
    #---------------------Entry tarifas----------------------------------------
#--------------------- mere comentados los checks      
#        self.tarifaCC = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaCC.setGeometry(QtCore.QRect(350, 130, 61, 22))
#        self.tarifaCC.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaCC.setObjectName("tarifaCC")
#        self.tarifaOPL = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaOPL.setGeometry(QtCore.QRect(430, 130, 61, 22))
#        self.tarifaOPL.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaOPL.setObjectName("tarifaOPL")
#        self.tarifaDIM = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaDIM.setGeometry(QtCore.QRect(510, 130, 61, 22))
#        self.tarifaDIM.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaDIM.setObjectName("tarifaDIM")
#        self.tarifaTECL = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaTECL.setGeometry(QtCore.QRect(590, 130, 61, 22))
#        self.tarifaTECL.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaTECL.setObjectName("tarifaTECL")
#        self.tarifaRIG = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaRIG.setGeometry(QtCore.QRect(670, 130, 61, 22))
#        self.tarifaRIG.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaRIG.setObjectName("tarifaRIG")
#        self.tarifaREGI = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaREGI.setGeometry(QtCore.QRect(350, 210, 61, 22))
#        self.tarifaREGI.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaREGI.setObjectName("tarifaREGI")
#        self.tarifaOPS = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaOPS.setGeometry(QtCore.QRect(430, 210, 61, 22))
#        self.tarifaOPS.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaOPS.setObjectName("tarifaOPS") 
#        self.tarifaRF = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaRF.setGeometry(QtCore.QRect(510, 210, 61, 22))
#        self.tarifaRF.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaRF.setObjectName("tarifaRF")
#        self.tarifaTECS = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaTECS.setGeometry(QtCore.QRect(590, 210, 61, 22))
#        self.tarifaTECS.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaTECS.setObjectName("tarifaTECS")
#        self.tarifaDECO = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaDECO.setGeometry(QtCore.QRect(670, 210, 61, 22))
#        self.tarifaDECO.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaDECO.setObjectName("tarifaDECO")
#        self.tarifaCONT = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaCONT.setGeometry(QtCore.QRect(350, 290, 61, 22))
#        self.tarifaCONT.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaCONT.setObjectName("tarifaCONT")
#        self.tarifaOPV = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaOPV.setGeometry(QtCore.QRect(430, 290, 61, 22))
#        self.tarifaOPV.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaOPV.setObjectName("tarifaOPV")
#        self.tarifaLED = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaLED.setGeometry(QtCore.QRect(510, 290, 61, 22))
#        self.tarifaLED.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaLED.setObjectName("tarifaLED")
#        self.tarifaTECV = QtWidgets.QLineEdit(self.centralwidget)
#        self.tarifaTECV.setGeometry(QtCore.QRect(590, 290, 61, 22))
#        self.tarifaTECV.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.tarifaTECV.setObjectName("tarifaTECV")
 
        #--------------------------------------------------------- mere añadido       
        self.widget_tar = QtWidgets.QWidget(self.centralwidget)
        self.widget_tar.setGeometry(QtCore.QRect(350, 40, 301, 400))
        self.widget_tar.setObjectName("widget_tar")     
        self.widget_tar.setStyleSheet("background-color: rgb(220, 220, 220);")
    #------------------------------Etiquetas----------------------------------- end mere
        
        self.id = QtWidgets.QLabel(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(30, 100, 55, 16))
        self.id.setObjectName("id")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(30, 140, 55, 16))
        self.nombre.setObjectName("nombre")
        self.apellidos = QtWidgets.QLabel(self.centralwidget)
        self.apellidos.setGeometry(QtCore.QRect(30, 180, 55, 16))
        self.apellidos.setObjectName("apellidos")
        self.dni = QtWidgets.QLabel(self.centralwidget)
        self.dni.setGeometry(QtCore.QRect(30, 220, 55, 16))
        self.dni.setObjectName("dni")
        self.telefono = QtWidgets.QLabel(self.centralwidget)
        self.telefono.setGeometry(QtCore.QRect(30, 260, 55, 16))
        self.telefono.setObjectName("telefono")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(30, 300, 55, 16))
        self.email.setObjectName("email")
        self.autonomo = QtWidgets.QLabel(self.centralwidget)
        self.autonomo.setGeometry(QtCore.QRect(30, 340, 71, 16))
        self.autonomo.setStyleSheet("")
        self.autonomo.setObjectName("autonomo")
        self.notas_2 = QtWidgets.QLabel(self.centralwidget)
        self.notas_2.setGeometry(QtCore.QRect(30, 380, 55, 16))
        self.notas_2.setObjectName("notas_2")
        
    #-----------------------Checkbox de cargos--------------------------------
#--------------------- mere comentados los checks        
#        self.checkCC = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkCC.setGeometry(QtCore.QRect(350, 100, 81, 20))
#        self.checkCC.setObjectName("checkCC")
#        self.checkOPL = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkOPL.setGeometry(QtCore.QRect(430, 100, 81, 20))
#        self.checkOPL.setObjectName("checkOPL")
#        self.checkDIM = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkDIM.setGeometry(QtCore.QRect(510, 100, 81, 20))
#        self.checkDIM.setObjectName("checkDIM")
#        self.checkTECL = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkTECL.setGeometry(QtCore.QRect(590, 100, 81, 20))
#        self.checkTECL.setObjectName("checkTECL")
#        self.checkOPS = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkOPS.setGeometry(QtCore.QRect(430, 180, 81, 20))
#        self.checkOPS.setObjectName("checkOPS")
#        self.checkRF = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkRF.setGeometry(QtCore.QRect(510, 180, 81, 20))
#        self.checkRF.setObjectName("checkRF")
#        self.checkTECS = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkTECS.setGeometry(QtCore.QRect(590, 180, 81, 20))
#        self.checkTECS.setObjectName("checkTECS")
#        self.checkCONT = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkCONT.setGeometry(QtCore.QRect(350, 260, 81, 20))
#        self.checkCONT.setObjectName("checkCONT")
#        self.checkLED = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkLED.setGeometry(QtCore.QRect(510, 260, 81, 20))
#        self.checkLED.setObjectName("checkLED")
#        self.checkOPV = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkOPV.setGeometry(QtCore.QRect(430, 260, 81, 20))
#        self.checkOPV.setObjectName("checkOPV")
#        self.checkREGI = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkREGI.setGeometry(QtCore.QRect(350, 180, 81, 20))
#        self.checkREGI.setObjectName("checkREGI")
#        self.checkTECV = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkTECV.setGeometry(QtCore.QRect(590, 260, 81, 20))
#        self.checkTECV.setObjectName("checkTECV")
#        self.checkDECO = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkDECO.setGeometry(QtCore.QRect(670, 180, 81, 20))
#        self.checkDECO.setObjectName("checkDECO")
#        self.checkRIG = QtWidgets.QCheckBox(self.centralwidget)
#        self.checkRIG.setGeometry(QtCore.QRect(670, 100, 81, 20))
#        self.checkRIG.setObjectName("checkRIG")
    
    #--------------------aceptar cancelar-------------------------------------
        
        self.aceptcancel = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.aceptcancel.setGeometry(QtCore.QRect(500, 470, 193, 28))
        self.aceptcancel.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.aceptcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.aceptcancel.setObjectName("aceptcancel")
    
        
        
   #--------------------------------------------------------------------------
   
        MainWindow.setCentralWidget(self.centralwidget)
        
    #------------Crea la barra de status al pie de la ventana-----------------
    
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
    #------------------Llama a la función que escribe los textos--------------
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
        
    #-------------------Translate---------------------------------------------

    def retranslateUi(self, MainWindow):
        """Esta función escribe los textos"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "El Aleph"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.notas_2.setText(_translate("MainWindow", "Notas"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.telefono.setText(_translate("MainWindow", "Teléfono"))
        self.dni.setText(_translate("MainWindow", "DNI"))
        self.apellidos.setText(_translate("MainWindow", "Apellidos"))
        self.nombre.setText(_translate("MainWindow", "Nombre"))
#--------------------- mere comentados los checks
#        self.checkCC.setText(_translate("MainWindow", "CC"))
#        self.checkOPL.setText(_translate("MainWindow", "OPL"))
#        self.checkDIM.setText(_translate("MainWindow", "DIM"))
#        self.checkTECL.setText(_translate("MainWindow", "TECL"))
#        self.checkOPS.setText(_translate("MainWindow", "OPS"))
#        self.checkRF.setText(_translate("MainWindow", "RF"))
#        self.checkTECS.setText(_translate("MainWindow", "TECS"))
#        self.checkCONT.setText(_translate("MainWindow", "CONT"))
#        self.checkLED.setText(_translate("MainWindow", "LED"))
#        self.checkOPV.setText(_translate("MainWindow", "OPV"))
#        self.checkREGI.setText(_translate("MainWindow", "REGI"))
#        self.checkTECV.setText(_translate("MainWindow", "TECV"))
#        self.checkDECO.setText(_translate("MainWindow", "DECO"))
#        self.checkRIG.setText(_translate("MainWindow", "RIGGING"))
        self.radioSI.setText(_translate("MainWindow", "Sí"))
        self.radioNO.setText(_translate("MainWindow", "No"))
        self.autonomo.setText(_translate("MainWindow", "Autónomo"))
        self.anadirperso.setText(_translate("MainWindow", "AÑADIR PERSONAL"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AnadirPersonal_Ui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())