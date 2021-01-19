# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 05:53:12 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from diasevento_ui import *
from crearevento import *


class DiasEvento(QtWidgets.QDialog, Dias_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.button_add.clicked.connect(self.add_date)
        
    def add_date(self):
        date = self.calendar.selectedDate()
        date= date.toString("dd-MM-yyyy")
        print(date)
        time = self.time.time()
        time = time.toString("hh:mm")
        print(time)
        tarea = self.combo_tarea.currentText()
        print(tarea)
        crear_evento=CrearEvento()
        crear_evento.ui.fechas_table.set
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = DiasEvento()
    ui.show()
    sys.exit(app.exec_())