# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:41:43 2020

@author: aleja
"""
from PyQt5 import QtSql

def open_bbdd():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setHostName("localhost")
    db.setDatabaseName("elaleph.db")
    db.open()
    print(db.lastError().text())
    