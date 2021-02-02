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
    
    def __init__(self, self_padre = None):
        QtWidgets.QDialog.__init__(self)
        self.ui = PersonalEvento_Ui()
        self.ui.setupUi(self)        
        self.padre = self_padre
    #-----------------Conexion de los botones---------------------------------
        self.ui.buttonGuardar.clicked.connect(self.guardar_cambios)
        self.ui.buttonCancelar.clicked.connect(self.eliminar)
        
    #-----------------Relleno de las cajas de texto----------------------------------
        if self.padre != None: 
            self.ui.inputCodigo.setText(self.padre.id_personal)
            self.ui.inputNombre.setText (self.padre.ui.entry_nombre.text())
            self.ui.inputApellidos.setText (self.padre.id_evento)
            self.ui.inputFecha.setText (self.padre.fecha)
            #--------------- crea combo de cargos
            for cargo in self.padre.dic_cargos :
                self.ui.comboBox.addItem(cargo)
                
            # posiciona el combo con el cargo escogido
            index = self.ui.comboBox.findText(self.padre.nom_cargo, QtCore.Qt.MatchFixedString)
            print("index", index)
            if index >= 0:
                 self.ui.comboBox.setCurrentIndex(index)
        
      
    def guardar_cambios(self):

        if self.padre != None: 
            if self.padre.nom_cargo in self.padre.dic_cargos :
                id_cargo = self.padre.dic_cargos[self.padre.nom_cargo]
            else:
                id_cargo = ""
            if (self.padre.fecha != ""):
            #-------------------------- inserta persona, evento, fecha en la base de datos
                bd=BdStd()
                txtsql = "INSERT INTO personal_evento (id_personal, id_evento, fecha, id_cargo\
                               , suplemento) VALUES ('{}','{}','{}','{}','{}');"
                txtsql= txtsql.format(self.padre.id_personal, self.padre.id_evento,self.padre.fecha, 
                                      id_cargo, self.ui.inputSuplem.text())
                print(txtsql)
                bd.runsql(txtsql)
        self.close()
                
    def eliminar(self):
        print("No borro ")
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = PersonalEvento()
    ui.show()
    sys.exit(app.exec_())