# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'economia.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1493, 883)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_17)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)


        self.horizontalLayout.addWidget(self.frame_17)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_18 = QFrame(self.frame_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)


        self.horizontalLayout_3.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_10)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_19)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.simple_final = QLabel(self.frame_19)
        self.simple_final.setObjectName(u"simple_final")

        self.verticalLayout_15.addWidget(self.simple_final)


        self.horizontalLayout_3.addWidget(self.frame_19)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_21 = QFrame(self.frame_8)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)


        self.horizontalLayout_5.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.simple_presente = QLabel(self.frame_20)
        self.simple_presente.setObjectName(u"simple_presente")

        self.verticalLayout_16.addWidget(self.simple_presente)


        self.horizontalLayout_5.addWidget(self.frame_20)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_27 = QFrame(self.frame_14)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_27)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.frame_27)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)


        self.horizontalLayout_7.addWidget(self.frame_27)

        self.frame_23 = QFrame(self.frame_14)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.simple_periodo = QLabel(self.frame_23)
        self.simple_periodo.setObjectName(u"simple_periodo")

        self.verticalLayout_17.addWidget(self.simple_periodo)


        self.horizontalLayout_7.addWidget(self.frame_23)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_26 = QFrame(self.frame_15)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_26)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_11 = QLabel(self.frame_26)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)


        self.horizontalLayout_8.addWidget(self.frame_26)

        self.frame_24 = QFrame(self.frame_15)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_24)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.simple_taza = QLabel(self.frame_24)
        self.simple_taza.setObjectName(u"simple_taza")

        self.verticalLayout_18.addWidget(self.simple_taza)


        self.horizontalLayout_8.addWidget(self.frame_24)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_25 = QFrame(self.frame_6)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_25)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_12 = QLabel(self.frame_25)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_13.addWidget(self.label_12)


        self.horizontalLayout_6.addWidget(self.frame_25)

        self.frame_22 = QFrame(self.frame_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_22)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.simple_ganado = QLabel(self.frame_22)
        self.simple_ganado.setObjectName(u"simple_ganado")

        self.verticalLayout_19.addWidget(self.simple_ganado)


        self.horizontalLayout_6.addWidget(self.frame_22)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 2, 1)

        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_32 = QFrame(self.frame_11)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_32)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_18 = QLabel(self.frame_32)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_29.addWidget(self.label_18)


        self.horizontalLayout_9.addWidget(self.frame_32)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_29 = QFrame(self.frame_9)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_34 = QFrame(self.frame_29)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_34)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_2 = QLabel(self.frame_34)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_14.addWidget(self.label_2)


        self.horizontalLayout_10.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.frame_29)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_33)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.compuesto_final = QLabel(self.frame_33)
        self.compuesto_final.setObjectName(u"compuesto_final")

        self.verticalLayout_20.addWidget(self.compuesto_final)


        self.horizontalLayout_10.addWidget(self.frame_33)


        self.verticalLayout_7.addWidget(self.frame_29)

        self.frame_28 = QFrame(self.frame_9)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_35 = QFrame(self.frame_28)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_35)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_4 = QLabel(self.frame_35)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_21.addWidget(self.label_4)


        self.horizontalLayout_11.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_28)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_36)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.compuesto_presente = QLabel(self.frame_36)
        self.compuesto_presente.setObjectName(u"compuesto_presente")

        self.verticalLayout_22.addWidget(self.compuesto_presente)


        self.horizontalLayout_11.addWidget(self.frame_36)


        self.verticalLayout_7.addWidget(self.frame_28)

        self.frame_30 = QFrame(self.frame_9)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_38 = QFrame(self.frame_30)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_38)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_7 = QLabel(self.frame_38)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_23.addWidget(self.label_7)


        self.horizontalLayout_12.addWidget(self.frame_38)

        self.frame_37 = QFrame(self.frame_30)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_37)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.compuesto_periodo = QLabel(self.frame_37)
        self.compuesto_periodo.setObjectName(u"compuesto_periodo")

        self.verticalLayout_24.addWidget(self.compuesto_periodo)


        self.horizontalLayout_12.addWidget(self.frame_37)


        self.verticalLayout_7.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_9)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_40 = QFrame(self.frame_31)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_40)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_14 = QLabel(self.frame_40)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_25.addWidget(self.label_14)


        self.horizontalLayout_13.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.frame_31)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_39)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.compuesto_taza = QLabel(self.frame_39)
        self.compuesto_taza.setObjectName(u"compuesto_taza")

        self.verticalLayout_27.addWidget(self.compuesto_taza)


        self.horizontalLayout_13.addWidget(self.frame_39)


        self.verticalLayout_7.addWidget(self.frame_31)

        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_41 = QFrame(self.frame_16)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_41)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_15 = QLabel(self.frame_41)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_26.addWidget(self.label_15)


        self.horizontalLayout_14.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_16)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_42)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.compuesto_ganado = QLabel(self.frame_42)
        self.compuesto_ganado.setObjectName(u"compuesto_ganado")

        self.verticalLayout_28.addWidget(self.compuesto_ganado)


        self.horizontalLayout_14.addWidget(self.frame_42)


        self.verticalLayout_7.addWidget(self.frame_16)


        self.gridLayout_2.addWidget(self.frame_9, 0, 1, 2, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_45 = QFrame(self.frame_3)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_45)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_70 = QLabel(self.frame_45)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_8.addWidget(self.label_70, 3, 0, 1, 1)

        self.comer_descuento = QLabel(self.frame_45)
        self.comer_descuento.setObjectName(u"comer_descuento")

        self.gridLayout_8.addWidget(self.comer_descuento, 3, 1, 1, 1)

        self.label_86 = QLabel(self.frame_45)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_8.addWidget(self.label_86, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_45)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u"economista/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(120, 120))

        self.gridLayout_8.addWidget(self.pushButton, 4, 1, 1, 1)

        self.label_65 = QLabel(self.frame_45)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_8.addWidget(self.label_65, 0, 0, 1, 1)

        self.label_66 = QLabel(self.frame_45)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_8.addWidget(self.label_66, 2, 0, 1, 1)

        self.comer_final = QLabel(self.frame_45)
        self.comer_final.setObjectName(u"comer_final")

        self.gridLayout_8.addWidget(self.comer_final, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_45, 0, 1, 1, 1)

        self.frame_46 = QFrame(self.frame_3)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_46)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_17 = QLabel(self.frame_46)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_24 = QLabel(self.frame_46)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 3, 2, 1, 1)

        self.label_20 = QLabel(self.frame_46)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 2, 2, 1, 1)

        self.label_19 = QLabel(self.frame_46)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_23 = QLabel(self.frame_46)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_4.addWidget(self.label_23, 5, 0, 1, 1)

        self.label_25 = QLabel(self.frame_46)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 4, 2, 1, 1)

        self.racional_comp_taza = QLabel(self.frame_46)
        self.racional_comp_taza.setObjectName(u"racional_comp_taza")

        self.gridLayout_4.addWidget(self.racional_comp_taza, 5, 3, 1, 1)

        self.label_22 = QLabel(self.frame_46)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 4, 0, 1, 1)

        self.racional_comp_descuento = QLabel(self.frame_46)
        self.racional_comp_descuento.setObjectName(u"racional_comp_descuento")

        self.gridLayout_4.addWidget(self.racional_comp_descuento, 6, 3, 1, 1)

        self.racional_comp_periodo = QLabel(self.frame_46)
        self.racional_comp_periodo.setObjectName(u"racional_comp_periodo")

        self.gridLayout_4.addWidget(self.racional_comp_periodo, 4, 3, 1, 1)

        self.label_26 = QLabel(self.frame_46)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 5, 2, 1, 1)

        self.racional_comp_presente = QLabel(self.frame_46)
        self.racional_comp_presente.setObjectName(u"racional_comp_presente")

        self.gridLayout_4.addWidget(self.racional_comp_presente, 3, 3, 1, 1)

        self.label_21 = QLabel(self.frame_46)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 3, 0, 1, 1)

        self.racional_comp_final = QLabel(self.frame_46)
        self.racional_comp_final.setObjectName(u"racional_comp_final")

        self.gridLayout_4.addWidget(self.racional_comp_final, 2, 3, 1, 1)

        self.racional_simple_final = QLabel(self.frame_46)
        self.racional_simple_final.setObjectName(u"racional_simple_final")

        self.gridLayout_4.addWidget(self.racional_simple_final, 2, 1, 1, 1)

        self.label_29 = QLabel(self.frame_46)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_4.addWidget(self.label_29, 6, 2, 1, 1)

        self.label_28 = QLabel(self.frame_46)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_4.addWidget(self.label_28, 6, 0, 1, 1)

        self.racional_simple_taza = QLabel(self.frame_46)
        self.racional_simple_taza.setObjectName(u"racional_simple_taza")

        self.gridLayout_4.addWidget(self.racional_simple_taza, 5, 1, 1, 1)

        self.racional_simple_descuento = QLabel(self.frame_46)
        self.racional_simple_descuento.setObjectName(u"racional_simple_descuento")

        self.gridLayout_4.addWidget(self.racional_simple_descuento, 6, 1, 1, 1)

        self.racional_simple_periodo = QLabel(self.frame_46)
        self.racional_simple_periodo.setObjectName(u"racional_simple_periodo")

        self.gridLayout_4.addWidget(self.racional_simple_periodo, 4, 1, 1, 1)

        self.label_40 = QLabel(self.frame_46)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_4.addWidget(self.label_40, 1, 0, 1, 1)

        self.label_41 = QLabel(self.frame_46)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_4.addWidget(self.label_41, 1, 2, 1, 1)

        self.racional_simple_presente = QLabel(self.frame_46)
        self.racional_simple_presente.setObjectName(u"racional_simple_presente")

        self.gridLayout_4.addWidget(self.racional_simple_presente, 3, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_46, 0, 0, 1, 1)

        self.frame_47 = QFrame(self.frame_3)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_47)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.bacn_simple_descuento = QLabel(self.frame_47)
        self.bacn_simple_descuento.setObjectName(u"bacn_simple_descuento")

        self.gridLayout_7.addWidget(self.bacn_simple_descuento, 6, 1, 1, 1)

        self.bacn_simple_periodo = QLabel(self.frame_47)
        self.bacn_simple_periodo.setObjectName(u"bacn_simple_periodo")

        self.gridLayout_7.addWidget(self.bacn_simple_periodo, 4, 1, 1, 1)

        self.bacn_simple_taza = QLabel(self.frame_47)
        self.bacn_simple_taza.setObjectName(u"bacn_simple_taza")

        self.gridLayout_7.addWidget(self.bacn_simple_taza, 5, 1, 1, 1)

        self.label_48 = QLabel(self.frame_47)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_7.addWidget(self.label_48, 4, 0, 1, 1)

        self.bacn_simple_presente = QLabel(self.frame_47)
        self.bacn_simple_presente.setObjectName(u"bacn_simple_presente")

        self.gridLayout_7.addWidget(self.bacn_simple_presente, 3, 1, 1, 1)

        self.label_49 = QLabel(self.frame_47)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_7.addWidget(self.label_49, 5, 0, 1, 1)

        self.label_44 = QLabel(self.frame_47)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_7.addWidget(self.label_44, 2, 2, 1, 1)

        self.label_50 = QLabel(self.frame_47)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_7.addWidget(self.label_50, 6, 0, 1, 1)

        self.label_45 = QLabel(self.frame_47)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_7.addWidget(self.label_45, 3, 0, 1, 1)

        self.bacn_comp_final = QLabel(self.frame_47)
        self.bacn_comp_final.setObjectName(u"bacn_comp_final")

        self.gridLayout_7.addWidget(self.bacn_comp_final, 2, 3, 1, 1)

        self.label_51 = QLabel(self.frame_47)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_7.addWidget(self.label_51, 1, 0, 1, 1)

        self.label_52 = QLabel(self.frame_47)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_7.addWidget(self.label_52, 1, 2, 1, 1)

        self.bacn_simple_final = QLabel(self.frame_47)
        self.bacn_simple_final.setObjectName(u"bacn_simple_final")

        self.gridLayout_7.addWidget(self.bacn_simple_final, 2, 1, 1, 1)

        self.label_43 = QLabel(self.frame_47)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_7.addWidget(self.label_43, 2, 0, 1, 1)

        self.label_58 = QLabel(self.frame_47)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_7.addWidget(self.label_58, 4, 2, 1, 1)

        self.label_59 = QLabel(self.frame_47)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_7.addWidget(self.label_59, 5, 2, 1, 1)

        self.label_42 = QLabel(self.frame_47)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_7.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_57 = QLabel(self.frame_47)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_7.addWidget(self.label_57, 3, 2, 1, 1)

        self.label_60 = QLabel(self.frame_47)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_7.addWidget(self.label_60, 6, 2, 1, 1)

        self.bacn_comp_presente = QLabel(self.frame_47)
        self.bacn_comp_presente.setObjectName(u"bacn_comp_presente")

        self.gridLayout_7.addWidget(self.bacn_comp_presente, 3, 3, 1, 1)

        self.bacn_comp_periodo = QLabel(self.frame_47)
        self.bacn_comp_periodo.setObjectName(u"bacn_comp_periodo")

        self.gridLayout_7.addWidget(self.bacn_comp_periodo, 4, 3, 1, 1)

        self.bacn_comp_taza = QLabel(self.frame_47)
        self.bacn_comp_taza.setObjectName(u"bacn_comp_taza")

        self.gridLayout_7.addWidget(self.bacn_comp_taza, 5, 3, 1, 1)

        self.bacn_comp_descuento = QLabel(self.frame_47)
        self.bacn_comp_descuento.setObjectName(u"bacn_comp_descuento")

        self.gridLayout_7.addWidget(self.bacn_comp_descuento, 6, 3, 1, 1)


        self.gridLayout_6.addWidget(self.frame_47, 1, 0, 1, 1)

        self.frame_48 = QFrame(self.frame_3)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_48, 1, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_9 = QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_49 = QFrame(self.page_3)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_49)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.venc_presente = QLabel(self.frame_49)
        self.venc_presente.setObjectName(u"venc_presente")

        self.gridLayout_10.addWidget(self.venc_presente, 1, 1, 1, 1)

        self.label_31 = QLabel(self.frame_49)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_10.addWidget(self.label_31, 1, 0, 1, 1)

        self.label_35 = QLabel(self.frame_49)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_10.addWidget(self.label_35, 4, 0, 1, 1)

        self.venc_renta_p = QLabel(self.frame_49)
        self.venc_renta_p.setObjectName(u"venc_renta_p")

        self.gridLayout_10.addWidget(self.venc_renta_p, 4, 1, 1, 1)

        self.label_36 = QLabel(self.frame_49)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_10.addWidget(self.label_36, 5, 0, 1, 1)

        self.venc_n_f = QLabel(self.frame_49)
        self.venc_n_f.setObjectName(u"venc_n_f")

        self.gridLayout_10.addWidget(self.venc_n_f, 5, 1, 1, 1)

        self.label_30 = QLabel(self.frame_49)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_10.addWidget(self.label_30, 0, 0, 1, 1)

        self.venc_final = QLabel(self.frame_49)
        self.venc_final.setObjectName(u"venc_final")

        self.gridLayout_10.addWidget(self.venc_final, 2, 1, 1, 1)

        self.label_34 = QLabel(self.frame_49)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_10.addWidget(self.label_34, 3, 0, 1, 1)

        self.venc_renta_f = QLabel(self.frame_49)
        self.venc_renta_f.setObjectName(u"venc_renta_f")

        self.gridLayout_10.addWidget(self.venc_renta_f, 3, 1, 1, 1)

        self.venc_i = QLabel(self.frame_49)
        self.venc_i.setObjectName(u"venc_i")

        self.gridLayout_10.addWidget(self.venc_i, 7, 1, 1, 1)

        self.venc_n_p = QLabel(self.frame_49)
        self.venc_n_p.setObjectName(u"venc_n_p")

        self.gridLayout_10.addWidget(self.venc_n_p, 6, 1, 1, 1)

        self.label_38 = QLabel(self.frame_49)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_10.addWidget(self.label_38, 7, 0, 1, 1)

        self.label_37 = QLabel(self.frame_49)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_10.addWidget(self.label_37, 6, 0, 1, 1)

        self.label_33 = QLabel(self.frame_49)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_10.addWidget(self.label_33, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_49, 0, 0, 1, 1)

        self.frame_50 = QFrame(self.page_3)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_50)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_64 = QLabel(self.frame_50)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_11.addWidget(self.label_64, 4, 0, 1, 1)

        self.label_74 = QLabel(self.frame_50)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_11.addWidget(self.label_74, 6, 0, 1, 1)

        self.label_39 = QLabel(self.frame_50)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_11.addWidget(self.label_39, 0, 0, 1, 1)

        self.label_67 = QLabel(self.frame_50)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_11.addWidget(self.label_67, 5, 0, 1, 1)

        self.anti_p = QLabel(self.frame_50)
        self.anti_p.setObjectName(u"anti_p")

        self.gridLayout_11.addWidget(self.anti_p, 4, 1, 1, 1)

        self.label_62 = QLabel(self.frame_50)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_11.addWidget(self.label_62, 2, 0, 1, 1)

        self.anti_n_f = QLabel(self.frame_50)
        self.anti_n_f.setObjectName(u"anti_n_f")

        self.gridLayout_11.addWidget(self.anti_n_f, 5, 1, 1, 1)

        self.anti_final = QLabel(self.frame_50)
        self.anti_final.setObjectName(u"anti_final")

        self.gridLayout_11.addWidget(self.anti_final, 2, 1, 1, 1)

        self.label_61 = QLabel(self.frame_50)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_11.addWidget(self.label_61, 1, 0, 1, 1)

        self.label_63 = QLabel(self.frame_50)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_11.addWidget(self.label_63, 3, 0, 1, 1)

        self.anti_renta_f = QLabel(self.frame_50)
        self.anti_renta_f.setObjectName(u"anti_renta_f")

        self.gridLayout_11.addWidget(self.anti_renta_f, 3, 1, 1, 1)

        self.anti_n_p = QLabel(self.frame_50)
        self.anti_n_p.setObjectName(u"anti_n_p")

        self.gridLayout_11.addWidget(self.anti_n_p, 6, 1, 1, 1)

        self.anti_presente = QLabel(self.frame_50)
        self.anti_presente.setObjectName(u"anti_presente")

        self.gridLayout_11.addWidget(self.anti_presente, 1, 1, 1, 1)

        self.label_76 = QLabel(self.frame_50)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_11.addWidget(self.label_76, 7, 0, 1, 1)

        self.anti_i = QLabel(self.frame_50)
        self.anti_i.setObjectName(u"anti_i")

        self.gridLayout_11.addWidget(self.anti_i, 7, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_50, 1, 0, 1, 1)

        self.frame_51 = QFrame(self.page_3)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_51)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_78 = QLabel(self.frame_51)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_12.addWidget(self.label_78, 0, 0, 1, 1)

        self.label_79 = QLabel(self.frame_51)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_12.addWidget(self.label_79, 1, 0, 1, 1)

        self.perpetia_presente = QLabel(self.frame_51)
        self.perpetia_presente.setObjectName(u"perpetia_presente")

        self.gridLayout_12.addWidget(self.perpetia_presente, 2, 1, 1, 1)

        self.label_80 = QLabel(self.frame_51)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_12.addWidget(self.label_80, 2, 0, 1, 1)

        self.perp_vencida = QLabel(self.frame_51)
        self.perp_vencida.setObjectName(u"perp_vencida")

        self.gridLayout_12.addWidget(self.perp_vencida, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_51)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(160, 160))

        self.gridLayout_12.addWidget(self.pushButton_2, 3, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame_51, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame_2, 1, 2, 1, 1)

        self.frame_barra_tool = QFrame(self.centralwidget)
        self.frame_barra_tool.setObjectName(u"frame_barra_tool")
        self.frame_barra_tool.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_tool.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_barra_tool)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_43 = QFrame(self.frame_barra_tool)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_43)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_44)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_16 = QLabel(self.frame_44)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame_44)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame_44)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_44)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.line_taza_descuento = QLineEdit(self.frame_44)
        self.line_taza_descuento.setObjectName(u"line_taza_descuento")

        self.gridLayout_3.addWidget(self.line_taza_descuento, 4, 1, 1, 1)

        self.label_27 = QLabel(self.frame_44)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 4, 0, 1, 1)

        self.line_final = QLineEdit(self.frame_44)
        self.line_final.setObjectName(u"line_final")

        self.gridLayout_3.addWidget(self.line_final, 0, 1, 1, 1)

        self.line_presente = QLineEdit(self.frame_44)
        self.line_presente.setObjectName(u"line_presente")

        self.gridLayout_3.addWidget(self.line_presente, 1, 1, 1, 1)

        self.line_periodo = QLineEdit(self.frame_44)
        self.line_periodo.setObjectName(u"line_periodo")

        self.gridLayout_3.addWidget(self.line_periodo, 2, 1, 1, 1)

        self.line_taza = QLineEdit(self.frame_44)
        self.line_taza.setObjectName(u"line_taza")

        self.gridLayout_3.addWidget(self.line_taza, 3, 1, 1, 1)

        self.line_renta = QLineEdit(self.frame_44)
        self.line_renta.setObjectName(u"line_renta")

        self.gridLayout_3.addWidget(self.line_renta, 5, 1, 1, 1)

        self.label_32 = QLabel(self.frame_44)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_3.addWidget(self.label_32, 5, 0, 1, 1)


        self.verticalLayout_30.addWidget(self.frame_44)


        self.verticalLayout_5.addWidget(self.frame_43)

        self.frame_12 = QFrame(self.frame_barra_tool)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.boto_calcular = QPushButton(self.frame_12)
        self.boto_calcular.setObjectName(u"boto_calcular")
        self.boto_calcular.setMinimumSize(QSize(80, 80))
        self.boto_calcular.setMaximumSize(QSize(16777215, 16777215))
        self.boto_calcular.setSizeIncrement(QSize(80, 80))
        icon1 = QIcon()
        icon1.addFile(u"economista/vi.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.boto_calcular.setIcon(icon1)
        self.boto_calcular.setIconSize(QSize(120, 120))

        self.gridLayout_5.addWidget(self.boto_calcular, 3, 1, 1, 1)

        self.boto_enriqo_pucci = QPushButton(self.frame_12)
        self.boto_enriqo_pucci.setObjectName(u"boto_enriqo_pucci")
        icon2 = QIcon()
        icon2.addFile(u"economista/cait.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.boto_enriqo_pucci.setIcon(icon2)
        self.boto_enriqo_pucci.setIconSize(QSize(120, 120))

        self.gridLayout_5.addWidget(self.boto_enriqo_pucci, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.gridLayout.addWidget(self.frame_barra_tool, 1, 1, 1, 1)

        self.frame_tool = QFrame(self.centralwidget)
        self.frame_tool.setObjectName(u"frame_tool")
        self.frame_tool.setFrameShape(QFrame.StyledPanel)
        self.frame_tool.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tool)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boto_menu = QToolButton(self.frame_tool)
        self.boto_menu.setObjectName(u"boto_menu")
        self.boto_menu.setMinimumSize(QSize(40, 40))
        self.boto_menu.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_menu)

        self.boto_tool = QToolButton(self.frame_tool)
        self.boto_tool.setObjectName(u"boto_tool")
        self.boto_tool.setMinimumSize(QSize(40, 40))
        self.boto_tool.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_tool)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.boto_min = QToolButton(self.frame_tool)
        self.boto_min.setObjectName(u"boto_min")
        self.boto_min.setMinimumSize(QSize(40, 40))
        self.boto_min.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_min)

        self.boto_restaurar = QToolButton(self.frame_tool)
        self.boto_restaurar.setObjectName(u"boto_restaurar")
        self.boto_restaurar.setMinimumSize(QSize(40, 40))
        self.boto_restaurar.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_restaurar)

        self.boto_max = QToolButton(self.frame_tool)
        self.boto_max.setObjectName(u"boto_max")
        self.boto_max.setMinimumSize(QSize(40, 40))
        self.boto_max.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_max)

        self.boto_cerrar = QToolButton(self.frame_tool)
        self.boto_cerrar.setObjectName(u"boto_cerrar")
        self.boto_cerrar.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.boto_cerrar)


        self.gridLayout.addWidget(self.frame_tool, 0, 1, 1, 2)

        self.frame_barra_menu = QFrame(self.centralwidget)
        self.frame_barra_menu.setObjectName(u"frame_barra_menu")
        self.frame_barra_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_barra_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_barra_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_13 = QFrame(self.frame_barra_menu)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_13)

        self.frame_5 = QFrame(self.frame_barra_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.boto_men1 = QPushButton(self.frame_5)
        self.boto_men1.setObjectName(u"boto_men1")

        self.verticalLayout_2.addWidget(self.boto_men1)

        self.boto_men2 = QPushButton(self.frame_5)
        self.boto_men2.setObjectName(u"boto_men2")

        self.verticalLayout_2.addWidget(self.boto_men2)

        self.boto_men3 = QPushButton(self.frame_5)
        self.boto_men3.setObjectName(u"boto_men3")

        self.verticalLayout_2.addWidget(self.boto_men3)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_barra_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame_barra_menu, 0, 0, 2, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 19)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 8)
        self.gridLayout.setColumnStretch(2, 21)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Interes Simple", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Final: ", None))
        self.simple_final.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Presente: ", None))
        self.simple_presente.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"periodo: ", None))
        self.simple_periodo.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"taza interes: ", None))
        self.simple_taza.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Interes ganado", None))
        self.simple_ganado.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Interes Compuesto", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Final: ", None))
        self.compuesto_final.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Presente: ", None))
        self.compuesto_presente.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"periodo: ", None))
        self.compuesto_periodo.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"taza interes: ", None))
        self.compuesto_taza.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Interes ganado", None))
        self.compuesto_ganado.setText(QCoreApplication.translate("MainWindow", u"null", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Descuento", None))
        self.comer_descuento.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Simple", None))
        self.pushButton.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Descuento comercial", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Precio Final", None))
        self.comer_final.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Desuento racional", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"taza", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"periodo", None))
        self.racional_comp_taza.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"periodo", None))
        self.racional_comp_descuento.setText("")
        self.racional_comp_periodo.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"taza", None))
        self.racional_comp_presente.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.racional_comp_final.setText("")
        self.racional_simple_final.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"DESCUENTO", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"DESCUENTO", None))
        self.racional_simple_taza.setText("")
        self.racional_simple_descuento.setText("")
        self.racional_simple_periodo.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Simple", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Compuesto", None))
        self.racional_simple_presente.setText("")
        self.bacn_simple_descuento.setText("")
        self.bacn_simple_periodo.setText("")
        self.bacn_simple_taza.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"periodo", None))
        self.bacn_simple_presente.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"taza", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"DESCUENTO", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.bacn_comp_final.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Simple", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Compuesto", None))
        self.bacn_simple_final.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"periodo", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"taza", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Descuento bancario", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"DESCUENTO", None))
        self.bacn_comp_presente.setText("")
        self.bacn_comp_periodo.setText("")
        self.bacn_comp_taza.setText("")
        self.bacn_comp_descuento.setText("")
        self.venc_presente.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Renta en base a presente", None))
        self.venc_renta_p.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Periodo base a final", None))
        self.venc_n_f.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Anualidad vencida", None))
        self.venc_final.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Renta en base a final", None))
        self.venc_renta_f.setText("")
        self.venc_i.setText("")
        self.venc_n_p.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"interes", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Periodo base a presente", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Renta en base a presente", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Periodo base a presente", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Anualidad anticipada", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Periodo base a final", None))
        self.anti_p.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.anti_n_f.setText("")
        self.anti_final.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Renta en base a final", None))
        self.anti_renta_f.setText("")
        self.anti_n_p.setText("")
        self.anti_presente.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"interes", None))
        self.anti_i.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Anulalidad perpetua", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Vencida", None))
        self.perpetia_presente.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.perp_vencida.setText("")
        self.pushButton_2.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"taza interes: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Final: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Presente: ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"periodo: ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"taza descuento:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"renta", None))
        self.boto_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.boto_enriqo_pucci.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.boto_menu.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_tool.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_min.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_restaurar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_max.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_cerrar.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.boto_men1.setText(QCoreApplication.translate("MainWindow", u"Intereses", None))
        self.boto_men2.setText(QCoreApplication.translate("MainWindow", u"Descuentos", None))
        self.boto_men3.setText(QCoreApplication.translate("MainWindow", u"Anualidades", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PIN", None))
    # retranslateUi

