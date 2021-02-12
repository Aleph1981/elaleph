# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:24:10 2021

@author: aleja
"""

QWidget{
font:  10pt "EmojiOne Color";
color: rgb(235, 235, 235);
background-color: qlineargradient(spread:pad, x1:0.497512, y1:0, x2:0.502, y2:1, stop:0 rgba(54, 54, 54, 255), stop:0.507463 rgba(102, 102, 102, 255), stop:0.970149 rgba(54, 54, 54, 255));}
	


QWidget#widgetCal{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 200), stop:1 rgba(180, 0, 0, 200));border-radius:4px}

QMenuBar{background-color: rgba(54,54,54,255)}

QMenu::item:selected,QMenuBar::item::selected{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 200), stop:1 rgba(180, 0, 0, 200));border-radius:4px}

QLineEdit,QPlainTextEdit,QTableWidget {background-color: rgba(255, 255, 255, 200);
color: rgb(0,0,0);border-radius: 4px}

QLabel{ background-color: rgba(255, 255, 255, 0);}

QHeaderView::section,QHeaderview{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));border-radius:4px}

QTableView QTableCornerButton::section{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));;border-top-radius: 4px}


QPushButton,QToolButton{background-color:qlineargradient(spread:pad, x1:0.497512, y1:0, x2:0.502, y2:1, stop:0.0298507 rgba(230, 230, 230, 255), stop:0.532338 rgba(210, 210, 210, 255), stop:1 rgba(230, 230, 230, 255));
color: rgb(50,50,50); border-style: outset;border-radius: 4px;border-width: 2px;border-color: rgba(50,50,50,200)}

QPushButton:pressed{border-style: inset; }
QPushButton:checked{background-color:rgba(0,125,255,80);border-style: inset; }




QLabel#labelVista{font: 12pt;}
QLabel#label,QLabel#label_2,QLabel#label_3,QLabel#label_4{background-color: rgba(0, 0, 0, 0);font: 9pt;border-radius: 5px}


