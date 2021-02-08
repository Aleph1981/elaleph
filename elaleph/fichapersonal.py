# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:49:16 2020

@author: aleja
"""

from PyQt5 import QtCore, QtWidgets, QtGui
from fichapersonal_ui import *
import os
from bdstd import BdStd
from configctx import *
import calendar
from datetime import date
        

class FichaPersonal(QtWidgets.QDialog, FichaPersonal_Ui):
    

    def __init__(self, id_personal):

        QtWidgets.QWidget.__init__(self)
        self.id_personal = id_personal          
        
        ctx = ConfigCtx()
        self.carpeta = ctx.readvar("RUTAS", "datos_usr")
        self.carpeta = self.carpeta.format(self.carpeta, id=id_personal)
        
        
        
        self.ui = FichaPersonal_Ui()            
        self.ui.setupUi(self)      
        

        
        #----------Botones------------------------------------------------------------

        self.ui.buttonDocumentos.clicked.connect(self.documentos)
        self.ui.buttonGuardar.clicked.connect(self.guardar)
              
        #-----------Poner foto--------------------------------------------------------
        
        
        foto = QtGui.QPixmap(self.carpeta+"foto_personal.jpg")
        self.ui.foto.setPixmap(foto)
        self.ui.foto.setScaledContents(True)
        print(self.carpeta+"foto_personal.jpg")
        
        #---------Rellenar datos------------------------------------------------------
        self.loadData()
        
        #----------Crear Checks------------------------------------------------------
        
        self.map_cargos = getCargosPersonal(self.id_personal)
        
        for i, map_cargo in enumerate(self.map_cargos):
            title = map_cargo['nombre']
            label_c = QtWidgets.QLabel(title, self.ui.widget)
            label_c.setObjectName("label_c"+str(i))
            label_c.setGeometry(20, 10+(i*25), 80, 20) 
            
            
            checkBox_c = QtWidgets.QCheckBox(self.ui.widget)
            checkBox_c.setObjectName("checkBox_c"+str(i))
            checkBox_c.setGeometry(120, 10+(i*25), 50, 20)
            if map_cargo['checked'] == "1" :
                checkBox_c.setChecked(True)
                
            else:
                checkBox_c.setChecked(False)
            
            
            
            input_c = QtWidgets.QLineEdit(self.ui.widget)
            input_c.setObjectName("input_c"+str(i))
            input_c.setGeometry(180, 10+(i*25), 80, 20)
            if map_cargo['checked'] == "1" :
                input_c.setText(str(map_cargo['tarifa']))
            else:
                input_c.setToolTip(str(map_cargo['tarifa']))
            
            
        #---------Rellena calendario--------------------------------------------------
        
        self.kale = Acalendar(self.ui, self.id_personal)
        self.kale.crea_calendario()
                           
          #--------------Conecto los botones para pasar de mes---------------
        self.ui.buttonPre.clicked.connect(self.pre_month)
        self.ui.buttonNext.clicked.connect(self.next_month)                   
        
        #----------------Conecto los botones ocupar y liberar-----------------
        
        self.ui.buttonOcupar.clicked.connect(self.ocupar)
        self.ui.buttonLiberar.clicked.connect(self.liberar)
        
    
        #---------------Funciones para avanzar y retroceder mes---------------
    
    def pre_month(self):
        if self.kale.mes == 1:
            self.kale.mes=12
            self.kale.anyo-=1
        else:
            self.kale.mes-=1
        self.kale.crea_calendario()
            
    def next_month(self):
        print("antes:", self.kale.mes)
        if self.kale.mes==12:
            self.kale.mes=1
            self.kale.anyo+=1
        else:
            self.kale.mes+=1
        print("despues:", self.kale.mes)
        self.kale.crea_calendario()   
        
        #---------------Funciones para ocupar y liberar fechas----------------
        
    def ocupar(self):
        row = self.ui.tableWidget.currentRow()
        column = self.ui.tableWidget.currentColumn()
        dd = self.ui.tableWidget.item(row, column).text()
        dd = dd.replace(" ","0")
        fecha=f"{self.kale.anyo}-{self.kale.mes:02d}-{dd}"
        print(fecha)
        self.ui.tableWidget.item(row, column).setBackground(QtGui.QColor(255,0,0))
        bd = BdStd()
        bd.runsql(f"INSERT INTO personal_ocupado (id_personal,fecha) VALUES ('{self.id_personal}','{fecha}');")
        
        
    def liberar(self):
        row = self.ui.tableWidget.currentRow()
        column = self.ui.tableWidget.currentColumn()
        dd = self.ui.tableWidget.item(row, column).text()
        dd = dd.replace(" ","0")
        fecha=f"{self.kale.anyo}-{self.kale.mes:02d}-{dd}"
        self.ui.tableWidget.item(row, column).setBackground(QtGui.QColor(255,255,255))
        bd = BdStd()
        bd.runsql(f"DELETE FROM personal_ocupado WHERE id_personal = '{self.id_personal}' AND fecha = '{fecha}';")
        
        
    #---------METODOS ------------------------------------------------------
        
    def loadData(self):                 
        # Creado mere
        if self.id_personal == None :
            data = ["PEPEAL","Alejandro", "Pérez Pérez", "67458932M","654321987", "alejandro@example.es",
                    "carrer example nº3 08012 Barcelona","Sí","ES12 2345 2345 2345 2345", "Ingles" ]
            self.load_one(data)
        else :
            bd = BdStd()
            bd.runsql("SELECT * FROM personal WHERE id_personal = '" + self.id_personal + "'")
            if bd.rows != None :
                for row in bd.rows :
                    self.load_one(row)
                    

    def load_one(self, data):            #<------- en esta funcion he añadido 2 campos que faltaban
        self.ui.inputNombre.setText(data[0])
        self.ui.inputApellidos.setText(data[2])
        self.ui.inputDni.setText(data[3])
        self.ui.inputTelefono.setText(data[4])
        self.ui.inputMail.setText(data[5])
        self.ui.inputAutonomo.setText(data[6])
        self.ui.inputDireccion.setText(data[7])
        self.ui.inputCp.setText(data[8])
        self.ui.inputCiudad.setText(data[9])
        self.ui.inputIban.setText(data[10])
        self.ui.inputNotas.setPlainText(data[11])

#------------Función abrir documentos-----------------------------------------

    def documentos(self):
        # mere añadidoo try catch, porque fallaba
        # se podria añadir un label a la pantalla para mostrar el mensaje
        try :
            path = self.carpeta
            path = os.path.realpath(path)
            os.startfile(path)
        except :
            import sys
            print("Error:", sys.exc_info()[0])
            qm = QtWidgets.QMessageBox
            qm.warning(self, '', "No hay documentos")
            return
        
    
    def guardar(self):
        
        # Puesto el Update de los datos cambiados de personal en ficha personal---------
        nombre = self.ui.inputNombre.text()
        apellidos   = self.ui.inputApellidos.text()
        dni   = self.ui.inputDni.text()
        telefono   = self.ui.inputTelefono.text()
        email   = self.ui.inputMail.text()
        direccion   = self.ui.inputDireccion.text()
        cp   = self.ui.inputCp.text()
        ciudad   = self.ui.inputCiudad.text()
        autonomo   = self.ui.inputAutonomo.text()
        iban   = self.ui.inputIban.text()
        notas   = self.ui.inputNotas.toPlainText()
               
        txtsql = "UPDATE personal SET nombre = '{}', apellidos = '{}', dni = '{}'," \
        "telefono = '{}', email = '{}', direccion = '{}'," \
        "cp = '{}', ciudad = '{}', autonomo = '{}'," \
        "iban = '{}', notas = '{}'  WHERE id_personal = '{}'"
        txtsql = txtsql.format(nombre, apellidos, dni ,telefono  ,email, direccion , cp, ciudad, autonomo, iban , notas, self.id_personal)
        bd = BdStd()
        bd.runsql(txtsql)
        
        i = 0
        for checkobj in self.ui.widget.findChildren(QtWidgets.QCheckBox):
            title = self.map_cargos[i]
            if checkobj.checkState():
                self.map_cargos[i]['checked'] = "1"
            else: 
                self.map_cargos[i]['checked'] = "0"
            i+=1
        
        i = 0
        for caja in self.ui.widget.findChildren(QtWidgets.QLineEdit):
            title = self.map_cargos[i]
    
            if caja.text() != "":
                self.map_cargos[i]['tarifa'] = int(caja.text())
            i+=1   
        
        guardaTarifas(self.id_personal, self.map_cargos)
        
        
        
        
    

#--------Calendario-----------------------------------------------------------
 
class Acalendar() :
 
    def __init__(self, winui, id_personal):
        
        #Instancia de TextCalendar
        self.cl = calendar.TextCalendar()
        self.id_personal=id_personal
        hoy = date.today()
        self.mes = hoy.month
        self.anyo = hoy.year
        self.winui = winui
        
    def crea_calendario(self):
    
  
        #Elegimos el formato del año y mes del calendario
        calendario = self.cl.formatmonth(self.anyo,self.mes)
        
        #Cambio los saltos de línea por espacios
        
        calendario=calendario.replace("\n"," ")
        
        #Separo el calendario por espacios
        
        calendario=calendario.split(" ")
        
        #Elimino el año el mes y los dias de la semana.
        
        for i in range(12):
            calendario.remove(calendario[0])
        
        #Vuelco a unir el calendario
        
        calendario=" ".join(calendario)
        
        #Creo la variable newcalendar añadiendo los dias con los espacios del principio
        #para saberqué día de la semana es el 1.
        
        newcalendar=[]
        for i in range(0,len(calendario)-1,3):
            newcalendar.append(calendario[i]+calendario[i+1])
        for i in range(7):
            # mere añadido el viernes
            if newcalendar[0]=="Fr" or newcalendar[0]=="Sa" or newcalendar[0]=="Su":
                newcalendar.remove(newcalendar[0])
        #-----Monta el calendario de la persona----------------------------
        
        self.dias_event = getEventCale(self.id_personal, "{:04d}-{:02d}".format(self.anyo,self.mes))
        self.dias_ocupado = getOcupadoCale(self.id_personal, "{:04d}-{:02d}".format(self.anyo,self.mes))
        
        #------Rellena el calendario---------------------------------------
        
        k=0
        for i in range(5):
            for j in range(7):
                texto = ""
                dia = int0( newcalendar[k])
                evento=QtWidgets.QTableWidgetItem(newcalendar[k]+texto)
                if self.dias_event[dia-1] != "" :
                    #colorear la celda AQUI
                      texto = "->" + self.dias_event[dia-1]
                      evento=QtWidgets.QTableWidgetItem(newcalendar[k]+texto)
                      evento.setBackground(QtGui.QColor(170,0,255))
                
                elif self.dias_ocupado[dia-1] != "":
                      evento.setBackground(QtGui.QColor(255,0,0))
                
                self.winui.tableWidget.setItem(i,j,evento)
                k+=1
                if k == len(newcalendar):
                    newcalendar.append(" ")
                             
        #----Pongo en las  etiquetas el mes y el año correspondientes---------
        meses = {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",\
        7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
        self.winui.labelMes.setText(meses[self.mes])
        self.winui.labelMes_2.setText(str(self.anyo))  #------labelMes_2 debería ser labelAnyo
    
    
    
        
# LAS TRES FUNCIONES QUE CARGAN LOS CARGOS, TARIFAS DE LA BBDD, y DIAS OCUPADOS Y 
# LAS GUARDAN
#------------------------------------------------------------------
def getArrayCargos():
    # devuelve un array con los cargos de la base de datos
    bd = BdStd()
    map_cargos = []
    bd.runsql("SELECT * FROM cargos ORDER BY id_cargo")  #id_cargo, nombre, tarifa
    
    if bd.rows != None :
        for row in bd.rows :
            dic = {'id' : row[0], 'nombre' : row[1],  'tarifa' : row[2], 'checked' : "0"}
            map_cargos.append(dic)
    #print(map_cargos)
    return (map_cargos)


def getCargosPersonal(id_personal):
    # rellena el array de cargos con los que tiene la persona en la base de datos
    map_cargos = getArrayCargos()
    bd = BdStd()
    bd.runsql("SELECT * FROM tarifas WHERE id_personal = '"+id_personal+"'")
    #id_personal, id_cargo, tarifa

    if bd.rows != None :
        for row in bd.rows :
            for i, cargo in enumerate(map_cargos):
                if cargo['id'] == row[1]:
                    map_cargos[i]['checked'] = "1"    # ON
                    map_cargos[i]['tarifa'] = row[2]
                    break
    #print(map_cargos)
    return (map_cargos) 

def guardaTarifas(id_personal, map_cargos):
    # guarda los cargos y las tarifas de la persona en la base de datos

    bd = BdStd()
    bd.runsql("DELETE FROM tarifas WHERE id_personal = '"+id_personal+"'")
    
    sql = "INSERT INTO tarifas (id_personal,id_cargo,tarifa) VALUES ('{}','{}','{}');"

    for item in map_cargos :
        print (item)
        if item['checked'] == "1":
           print(sql.format(id_personal, item['id'], str(item['tarifa'])))
           bd.runsql(sql.format(id_personal, item['id'], str(item['tarifa'])))

def getEventCale(id_personal, yyyymm):
    
    # devuelve un array con dias y sus eventos 
    bd = BdStd()
    dias_event =  ["" for x in range(31)]
    txtsql = f"""SELECT fecha, id_evento  FROM personal_evento   WHERE id_personal = '{id_personal}'
    AND  fecha BETWEEN '{yyyymm}-01' AND '{yyyymm}-31' ORDER BY id_personal, fecha"""    
    bd.runsql(txtsql) 
    if bd.rows != None :
        for row in bd.rows :
            dia = int0(row[0][8:10])
            dias_event[dia-1] = row[1]
    return (dias_event)

def getOcupadoCale(id_personal, yyyymm):
    
    # devuelve un array con dias y sus eventos 
    bd = BdStd()
    dias_ocupado =  ["" for x in range(31)]
    txtsql = f"""SELECT fecha, id_personal FROM personal_ocupado   WHERE id_personal = '{id_personal}'
    AND  fecha BETWEEN '{yyyymm}-01' AND '{yyyymm}-31' ORDER BY id_personal, fecha"""
    
    print("getOcupadoCale: ", txtsql)
    
    bd.runsql(txtsql)
    print(bd.rows)
    if bd.rows != None :
        for row in bd.rows :
            dia = int0(row[0][8:10])
            dias_ocupado[dia-1] = row[1]
    return (dias_ocupado)
                        

def int0 (texto) :
    try:
        return(int(texto))
    except :
        return(0)
                    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = FichaPersonal("ALPE48")             
    window.show()
    app.exec_()
