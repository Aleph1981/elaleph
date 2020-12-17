# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 05:53:12 2020

@author: aleja
"""

from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from diasevento_ui import *


class DiasEvento(QtWidgets.QDialog, Dias_Ui):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Dias_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())