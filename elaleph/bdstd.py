# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:41:43 2020
@author: aleja
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, Qt
import sqlite3
from sqlite3 import Error
import sys


        
class BdStd(object):

    def __init__(self):
    		
    		self.nombrebd = r"elaleph.db"
    		self.conecta()
    
    def cierra(self):
    		self.conex.close()
    		self.conex = None            
    		
    def conecta(self):
    		self.conex = None
    		try:
    			self.conex = sqlite3.connect(self.nombrebd)
    		except Error as e:
    			print(e)
    			sys.exit(1)
    			
    def runsql(self, txtsql, campos = None):
        #------> mere changed added campos
        try:
            if self.conex == None :
                self.conecta()
            		
            cur = self.conex.cursor()
            if campos == None :
                cur.execute(txtsql)
            else :
                cur.execute(txtsql, campos)
            
            self.rows = cur.fetchall()
            self.one = cur.fetchone()
            self.conex.commit()
            self.cierra()
        except Exception as e:
            qm = QtWidgets.QMessageBox()
            qm.information(qm,'Aleph', f"{e}")
            
                
        
    def gira_fecha(self,fecha):
        fecha=fecha.split("-")
        fecha.reverse()
        fecha = "-".join(fecha)
        return fecha
    
class SortDate(QtWidgets.QTableWidgetItem):
    def __init__(self, text, sortKey):
        #call custom constructor with UserType item type
        QtWidgets.QTableWidgetItem.__init__(self, text, QtWidgets.QTableWidgetItem.UserType)
        self.sortKey = sortKey

    #Qt uses a simple < check for sorting items, override this to use the sortKey
    def __lt__(self, other):
        return self.sortKey < other.sortKey
        
if __name__ == "__main__":
	bd = BdStd()
	bd.runsql("SELECT * FROM PERSONAL")