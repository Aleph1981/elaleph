# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:09:25 2021

@author: aleja
"""

class HojaEstilos():
        
            red_gray='''/*----------------------------------------------------Generales----------------------------------------------------------------------------*/
QWidget{
font:  10pt "EmojiOne Color";
color: rgb(235, 235, 235);
background-color: qlineargradient(spread:pad, x1:0.497512, y1:0, x2:0.502, y2:1, stop:0 rgba(54, 54, 54, 255), stop:0.507463 rgba(102, 102, 102, 255), stop:0.970149 rgba(54, 54, 54, 255));}


QWidget#widgetCal{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 200), stop:1 rgba(180, 0, 0, 200));border-radius:10px}

/*------------------------------------------------------Menu-------------------------------------------------------------------------------*/
QMenuBar{background-color: rgba(54,54,54,255)}

QMenu::item:selected,QMenuBar::item::selected{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 200), stop:1 rgba(180, 0, 0, 200));border-radius:4px}
/*----------------------------------------------------LineEdit y Labels------------------------------------------------------------*/

QLineEdit,QPlainTextEdit,QTableWidget {background-color: rgba(255, 255, 255, 200);
color: rgb(0,0,0);border-radius: 4px}

QLabel{ background-color: rgba(255, 255, 255, 0);}

/*----------------------------------------------------title labels----------------------------------------------------------------------------*/

QLabel#labelTitle,QLabel#labelTitle2,QLabel#labelTitle3,QLabel#labelTitle4,QLabel#labelTitle5,QLabel#labelTitle6 {font: 14pt;background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 180), stop:1 rgba(180, 0, 0, 180));border-radius:4px;padding: 4px;}

QLabel#labelSubtitle1,QLabel#labelSubtitle2,QLabel#labelSubtitle3,QLabel#labelSubtitle4,QLabel#labelSubtitle5,QLabel#labelSubtitle6 {font: 12pt;background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 180), stop:1 rgba(180, 0, 0, 180));border-radius:4px;padding: 4px;}

QLabel#labelMes,QLabel#labelMes_2{font:12pt;}

QLineEdit:read-only{background-color: rgb(150,150,150)}

/*---------------------------------------------------Tablas---------------------------------------------------------------------------------*/

QHeaderView::section,QHeaderview{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));border-radius:4px;padding:2px}

QTableView QTableCornerButton::section{background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));;border-top-radius: 4px}
QTableView {background-color:rgba(255,255,255,200);color:rgb(0,0,0)}


/*---------------------------------------------------ComboBox--------------------------------------------------------------------------*/

QComboBox QAbstractItemView,QComboBox:editable {
    border: 2px solid darkgray;
    selection-background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));
}

/*-------------------------------------------------------Botones-----------------------------------------------*/

QPushButton,QToolButton{background-color: qlineargradient(spread:pad, x1:0.497512, y1:0, x2:0.502, y2:1, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(180, 180, 180, 255));
color: rgb(50,50,50); border-style: outset;border-radius: 6px;border-width: 2px;border-color: qlineargradient(spread:pad, x1:0.517412, y1:1, x2:0.502, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(180, 180, 180, 255));
 ;padding:3px; padding-left:8px; padding-right:8px;}

QPushButton:pressed,QToolButton:pressed{border-style: inset; }
QPushButton:selected,QToolButton:selected{background-color:rgba(0,125,255,80);border-style: inset; }
QPushButton#buttonCopyR,QPushButton#buttonCopyE {padding:0px;}

/*-------------------------------------------------------Botones-----------------------------------------------*/

QCheckBox{background-color:rgba(0,0,0,0)}

/*----------------------------------------------------TabWidget---------------------------------------------------------------------------*/


QTabBar::tab:selected {background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 255), stop:1 rgba(180, 0, 0, 255));border:1px solid;border-color:rgb(255,255,255);border-radius:2px}
QTabBar::tab:hover {background-color: qlineargradient(spread:pad, x1:0.522, y1:0.932, x2:0.518, y2:0, stop:0.318408 rgba(120, 0, 0, 100), stop:1 rgba(180, 0, 0, 100))}
QTabBar::tab:!selected {margin-top: 2px;}
QTabWidget::tab-bar {left: 5px;}
QTabBar::tab {min-width: 12ex;
    padding: 10px; padding-top:5px;padding-bottom:5px;}
QWidget#qt_calendar_calendarview {background-color: rgb(200,200,200);color:rgb(0,0,0);alternate-background-color: rgb(150,0,0);}'''
    