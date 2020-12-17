# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:41:43 2020

@author: aleja
"""

import sqlite3
from sqlite3 import Error
import sys

class BdStd():

	def __init__(self):
		#self.nombrebd = r"C:\sqlite\db\pythonsqlite.db"
		self.nombrebd = r"elaleph.db"
		self.conecta()

	def cierra(self):
		self.conex.close()
		
	def conecta(self):
		self.conex = None
		try:
			self.conex = sqlite3.connect(self.nombrebd)
		except Error as e:
			print(e)
			sys.exit(1)
			
	def runsql(self, txtsql):

		if self.conex == None :
			self.conecta()
		
		cur = self.conex.cursor()
		cur.execute(txtsql)

		self.rows = cur.fetchall()
		# coleccion de tuplas
		for row in self.rows:
			print(row)

		self.conex.commit()

if __name__ == "__main__":
	bd = BdStd()
	bd.runsql("SELECT * FROM PERSONAL")




