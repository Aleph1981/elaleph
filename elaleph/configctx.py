# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:10:56 2020

@author: aleja
"""


import configparser
import sys

class ConfigCtx ():
    
    def __init__(self):
        try :
            self.ctx = configparser.ConfigParser()
            if len(self.ctx.read('config.ini')) == 0 :
                self.createfile()
        except:
            self.createfile()
            
    def readvar(self, seccion, variable):
        if seccion in self.ctx.sections() :
            if variable in self.ctx[seccion]:
                return (self.ctx[seccion][variable])
        return("")
            
        
    def createfile(self):
        try :
            config = configparser.ConfigParser()
            config['BBDD'] = {'tipo': 'QSQLITE', 'host': 'localhost', 'nombre': 'elaleph'}
            config['ROLES'] = {}
            config['ROLES']['Admin'] = 'PEPEAL'
            config['RUTAS'] = {}
            config['RUTAS']['datos_usr'] = r"C:\\Users\\aleja\\Desktop\\Programacion\\elaleph\\{id}\\"
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            self.ctx.read('config.ini')
        except:
            e = sys.exc_info()[0]
            print("No puedo crear config.ini",e)
            sys.exit(1)
            
            
if __name__ == "__main__":
    cfg = ConfigCtx()
    print("1", cfg.readvar("RUTAS", "datos_usr"))
    print("2", cfg.readvar("BBDD", "host"))
