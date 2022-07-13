import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice

import pyqtgraph as pg
from pyqtgraph.graphicsItems.PlotDataItem import dataType
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.pyplot as plt
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet
from executor import Ui_MainWindow

import pyqtgraph as pg

#import seabornplot
import formulas

from decimal import *

class MainWindow(QMainWindow):
    siz1= 0
    siz2= 0

    sizx= 0
    sizy= 0
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.boto_menu.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_menu, self.siz1, self.sizx))
        self.ui.boto_tool.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_tool, self.siz2, self.sizy))
        ####----####

        self.ui.boto_men1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.boto_men2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.boto_men3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        #self.ui.boto_men4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        #self.ui.frame_7= pg.PlotWidget()
        #self.centralWidget(self.ui.frame_7)
        self.ui.boto_max.hide()
        
        ####BOTO####
        self.ui.boto_cerrar.clicked.connect(lambda: self.close())
        self.ui.boto_max.clicked.connect(lambda: self.maxi_window())
        self.ui.boto_restaurar.clicked.connect(self.rest_window)
        self.ui.boto_min.clicked.connect(self.showMinimized)

        self.ui.boto_calcular.clicked.connect(lambda: self.calcular())

        self.showMaximized()
        self.show()

    def calcular(self):
        F= 10
        P= 10
        n= 10
        i= 0.1
        d= 10
        R= 0.1

        try:
            F= float((self.ui.line_final.text()))
        except:
            F= 10
        try:
            P= float((self.ui.line_presente.text()))
        except:
            P= 10
        try:
            n= float((self.ui.line_periodo.text()))
        except:
            n= 10
        try:
            i= float((self.ui.line_taza.text()))
        except:
            i= 10
        try:
            d= float((self.ui.line_taza_descuento.text()))
        except:
            d= 10
        try:
            R= float((self.ui.line_renta.text()))
        except:
            R= 10

        self.ui.simple_final.setText(str(formulas.interesSimple_Final(P, n, i)))
        self.ui.simple_presente.setText(str(formulas.interesSimple_Presente(F, n, i)))
        self.ui.simple_taza.setText(str(formulas.interesSimple_i(F, P, n)))
        self.ui.simple_periodo.setText(str(formulas.interesSimple_n(F, P, i)))
        self.ui.simple_ganado.setText(str(formulas.interesSimple_Interes_P_ni(P, n, i)))

        self.ui.compuesto_final.setText(str(formulas.interesCompuesto_Final(P, n, i)))
        self.ui.compuesto_presente.setText(str(formulas.interesCompuesto_Presente(F, n, i)))
        self.ui.compuesto_taza.setText(str(formulas.interesCompuesto_i(F, P, n)))
        try:
            self.ui.compuesto_periodo.setText(str(formulas.interesCompuesto_n(F, P, i)))
        except:
            pass
        self.ui.compuesto_ganado.setText(str(formulas.interesCompuesto_Interes_P_ni(P, n, i)))
        ####
        self.ui.bacn_simple_final.setText(str(formulas.descuentoBancarioSimple_Final(P, n, d)))
        self.ui.bacn_simple_presente.setText(str(formulas.descuentoBancarioSimple_Presente(F, n, d)))
        self.ui.bacn_simple_taza.setText(str(formulas.descuentoBancarioSimple_d(F, P, n)))
        try:
            self.ui.bacn_simple_periodo.setText(str(formulas.descuentoBancarioSimple_n(F, P, d)))
        except:
            pass
        self.ui.bacn_simple_descuento.setText(str(formulas.descuentoBancarioSimple_D(F, n, d)))

        self.ui.bacn_comp_final.setText(str(formulas.descuentoBancarioCompuesto_Final(P, n, d)))
        self.ui.bacn_comp_presente.setText(str(formulas.descuentoBancarioCompuesto_Presente(F, n, d)))
        self.ui.bacn_comp_taza.setText(str(formulas.descuentoBancarioCompuesto_d(F, P, n)))
        try:
            self.ui.bacn_comp_periodo.setText(str(formulas.descuentoBancarioCompuesto_n(F, P, d)))
        except:
            pass
        self.ui.bacn_comp_descuento.setText(str(formulas.descuentoBancarioCompuesto_Descuento(F, n, d)))
        ####
        self.ui.racional_simple_final.setText(str(formulas.descuentoRacionalSimple_Final(P, n, i)))
        self.ui.racional_simple_presente.setText(str(formulas.descuentoRacionalSimple_Presente(F, n, i)))
        try:
            self.ui.venc_i.setText(str(formulas.interpo(P, R, n)))
        except:
            pass
        #self.ui.racional_simple_periodo.setText(str(formulas.descuentoBancarioSimple_n(F, P, d)))
        self.ui.racional_simple_descuento.setText(str(formulas.descuentoRacionalSimple_Descuento(F, n, i)))

        self.ui.racional_comp_final.setText(str(formulas.descuentoRacionalCompuesto_Final(P, n, d)))
        self.ui.racional_comp_presente.setText(str(formulas.descuentoBancarioCompuesto_Presente(F, n, d)))
        self.ui.anti_i.setText(str(formulas.interpo(P, R, n)))
        #self.ui.racional_comp_periodo.setText(str(formulas.descuentoBancarioCompuesto_n(F, P, d)))
        self.ui.racional_comp_descuento.setText(str(formulas.descuentoBancarioCompuesto_Descuento(F, n, d)))

        self.ui.comer_final.setText(str(formulas.decuentoCompercial_unitario_Final(P,d)))
        self.ui.comer_descuento.setText(str(formulas.decuentoCompercial_unitario_Descuento(P, d)))

        self.ui.venc_final.setText(str(formulas.anualidadVencida_Final(R, n, i)))
        self.ui.venc_presente.setText(str(formulas.anualidad_Presente(R, n, i)))
        self.ui.venc_renta_f.setText(str(formulas.anualidadVencida_Renta_F(F, n, i)))
        self.ui.venc_renta_p.setText(str(formulas.anualidadVencida_Renta_F(F, n, i)))
        try:
            self.ui.venc_n_f.setText(str(formulas.anualidadVencida_n_F(F, R, i)))
        except:
            pass
        try:
            self.ui.venc_n_p.setText(str(formulas.anualidadVencida_n_P(P, R, i)))
        except:
            pass
        
        self.ui.anti_final.setText(str(formulas.anualidadAnticipada_Final(R, n, i)))
        self.ui.anti_presente.setText(str(formulas.anualidad_Presente(R, n, i)))
        self.ui.anti_renta_f.setText(str(formulas.anualidadAnticipada_Renta_F(F, n, i)))
        self.ui.anti_p.setText(str(formulas.anualidadAnticipada_Renta_F(F, n, i)))
        try:
            self.ui.anti_n_f.setText(str(formulas.anualidadAnticipada_n_F(F, R, i)))
        except:
            pass
        try:
            self.ui.anti_n_p.setText(str(formulas.anualidadVencida_n_P(P, n, i)))
        except:
            pass

        self.ui.perp_vencida.setText(str(formulas.anualidadPerpetuaVencida_P(R, i)))
        self.ui.perp_vencida.setText(str(formulas.anualidadPerpetuaAnticipada_P(R, i)))

        #print(formulas.interesSimple_Final(P, n, i))
    def move_menu(self, menu, lonx, lony):
        #self.clickPosition = event.globalPos()
        vi= menu.width()
        print('vi: ', vi)
        #cait= self.ui.frame_barra_menu.size()
        #print(menu.size().width())
        #print(menu.size())
        #print(size)
        #print(cait)
        extend=0
        
        #self.ui.frame_barra_menu
        
        if vi==0:
            extend= lonx
            menu.setMinimumSize(extend,lony)
            #menu.setMaximumWidth(extend)
            #self.ui.frame_barra_menu.setMaximumWidth
        else:
            #self.siz1= menu.size().width()
            self.update_data()
            menu.setMaximumSize(extend,lony)
            print('oh me ejecuto')
            #self.ui.frame_barra_menu.resize(extend,844)
            #self.ui.frame_barra_menu.setGeometry()

        self.animacion = QPropertyAnimation(menu, b'minimumWidth')
        self.animacion.setDuration(400)
        self.animacion.setStartValue(vi)
        self.animacion.setEndValue(extend)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

        print( vi, ' <> ',extend)
        print('ra: ',self.siz1, ' & ',self.sizx)
        print('ga: ',self.siz2, ' & ',self.sizy)
        #print(vi)
	

    def rest_window(self): 
        self.showNormal()		
        self.ui.boto_restaurar.hide()
        self.ui.boto_max.show()
        self.update_data()


    def maxi_window(self): 
        self.showMaximized()
        self.ui.boto_max.hide()
        self.ui.boto_restaurar.show()
        self.update_data()

    def desplegar_ventana(self, event):
        pass


if __name__== '__main__':
    print('raaaa')
    app= QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_cyan.xml')
    window= MainWindow()
    sys.exit(app.exec_())

#pucci.obtenerVentas_Fecha()
#pyside6-uic dasdh_bo.ui -o dash_bo.py