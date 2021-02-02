# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:33:01 2020

@author: aleja
"""

from error_ui import *

class Error(QtWidgets.QDialog, Error_Ui):
    
    def __init__(self, error):
        QtWidgets.QWidget.__init__(self)
        self.ui = Error_Ui()
        self.ui.setupUi(self)
        self.ui.error.setText(error)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Error("Fallo general")
    window.show()
    app.exec_()
        