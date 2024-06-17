# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 390)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 471, 351))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formula_label = QLabel(self.widget)
        self.formula_label.setObjectName(u"formula_label")

        self.verticalLayout.addWidget(self.formula_label)

        self.formula_input = QTextEdit(self.widget)
        self.formula_input.setObjectName(u"formula_input")

        self.verticalLayout.addWidget(self.formula_input)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.atoms_label = QLabel(self.widget)
        self.atoms_label.setObjectName(u"atoms_label")

        self.verticalLayout_2.addWidget(self.atoms_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.atoms_input = QLineEdit(self.widget)
        self.atoms_input.setObjectName(u"atoms_input")

        self.horizontalLayout_2.addWidget(self.atoms_input)

        self.split_input = QSpinBox(self.widget)
        self.split_input.setObjectName(u"split_input")
        self.split_input.setMaximum(2)

        self.horizontalLayout_2.addWidget(self.split_input)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.slave_button = QPushButton(self.widget)
        self.slave_button.setObjectName(u"slave_button")

        self.verticalLayout.addWidget(self.slave_button)

        self.solution_label = QLabel(self.widget)
        self.solution_label.setObjectName(u"solution_label")

        self.verticalLayout.addWidget(self.solution_label)

        self.solution_input = QTextEdit(self.widget)
        self.solution_input.setObjectName(u"solution_input")

        self.verticalLayout.addWidget(self.solution_input)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.load_button = QPushButton(self.widget)
        self.load_button.setObjectName(u"load_button")

        self.horizontalLayout.addWidget(self.load_button)

        self.save_button = QPushButton(self.widget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.Greeck_widget = QTabWidget(self.centralwidget)
        self.Greeck_widget.setObjectName(u"Greeck_widget")
        self.Greeck_widget.setGeometry(QRect(500, 20, 180, 230))
        self.Function = QWidget()
        self.Function.setObjectName(u"Function")
        self.f_greeck = QWidget(self.Function)
        self.f_greeck.setObjectName(u"f_greeck")
        self.f_greeck.setGeometry(QRect(10, 10, 160, 180))
        self.gridLayout = QGridLayout(self.f_greeck)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.f_button1 = QPushButton(self.f_greeck)
        self.f_button1.setObjectName(u"f_button1")

        self.gridLayout.addWidget(self.f_button1, 0, 0, 1, 1)

        self.f_button2 = QPushButton(self.f_greeck)
        self.f_button2.setObjectName(u"f_button2")

        self.gridLayout.addWidget(self.f_button2, 0, 1, 1, 1)

        self.f_button3 = QPushButton(self.f_greeck)
        self.f_button3.setObjectName(u"f_button3")

        self.gridLayout.addWidget(self.f_button3, 0, 2, 1, 1)

        self.f_button4 = QPushButton(self.f_greeck)
        self.f_button4.setObjectName(u"f_button4")

        self.gridLayout.addWidget(self.f_button4, 0, 3, 1, 1)

        self.f_button5 = QPushButton(self.f_greeck)
        self.f_button5.setObjectName(u"f_button5")

        self.gridLayout.addWidget(self.f_button5, 0, 4, 1, 1)

        self.f_button6 = QPushButton(self.f_greeck)
        self.f_button6.setObjectName(u"f_button6")

        self.gridLayout.addWidget(self.f_button6, 0, 5, 1, 1)

        self.f_button7 = QPushButton(self.f_greeck)
        self.f_button7.setObjectName(u"f_button7")

        self.gridLayout.addWidget(self.f_button7, 1, 0, 1, 1)

        self.f_button8 = QPushButton(self.f_greeck)
        self.f_button8.setObjectName(u"f_button8")

        self.gridLayout.addWidget(self.f_button8, 1, 1, 1, 1)

        self.f_button9 = QPushButton(self.f_greeck)
        self.f_button9.setObjectName(u"f_button9")

        self.gridLayout.addWidget(self.f_button9, 1, 2, 1, 1)

        self.f_button10 = QPushButton(self.f_greeck)
        self.f_button10.setObjectName(u"f_button10")

        self.gridLayout.addWidget(self.f_button10, 1, 3, 1, 1)

        self.f_button11 = QPushButton(self.f_greeck)
        self.f_button11.setObjectName(u"f_button11")

        self.gridLayout.addWidget(self.f_button11, 1, 4, 1, 1)

        self.f_button12 = QPushButton(self.f_greeck)
        self.f_button12.setObjectName(u"f_button12")

        self.gridLayout.addWidget(self.f_button12, 1, 5, 1, 1)

        self.f_button13 = QPushButton(self.f_greeck)
        self.f_button13.setObjectName(u"f_button13")

        self.gridLayout.addWidget(self.f_button13, 2, 0, 1, 1)

        self.f_button14 = QPushButton(self.f_greeck)
        self.f_button14.setObjectName(u"f_button14")

        self.gridLayout.addWidget(self.f_button14, 2, 1, 1, 1)

        self.f_button15 = QPushButton(self.f_greeck)
        self.f_button15.setObjectName(u"f_button15")

        self.gridLayout.addWidget(self.f_button15, 2, 2, 1, 1)

        self.f_button16 = QPushButton(self.f_greeck)
        self.f_button16.setObjectName(u"f_button16")

        self.gridLayout.addWidget(self.f_button16, 2, 3, 1, 1)

        self.f_button17 = QPushButton(self.f_greeck)
        self.f_button17.setObjectName(u"f_button17")

        self.gridLayout.addWidget(self.f_button17, 2, 4, 1, 1)

        self.f_button18 = QPushButton(self.f_greeck)
        self.f_button18.setObjectName(u"f_button18")

        self.gridLayout.addWidget(self.f_button18, 2, 5, 1, 1)

        self.f_button19 = QPushButton(self.f_greeck)
        self.f_button19.setObjectName(u"f_button19")

        self.gridLayout.addWidget(self.f_button19, 3, 0, 1, 1)

        self.f_button20 = QPushButton(self.f_greeck)
        self.f_button20.setObjectName(u"f_button20")

        self.gridLayout.addWidget(self.f_button20, 3, 1, 1, 1)

        self.f_button21 = QPushButton(self.f_greeck)
        self.f_button21.setObjectName(u"f_button21")

        self.gridLayout.addWidget(self.f_button21, 3, 2, 1, 1)

        self.f_button22 = QPushButton(self.f_greeck)
        self.f_button22.setObjectName(u"f_button22")

        self.gridLayout.addWidget(self.f_button22, 3, 3, 1, 1)

        self.f_button23 = QPushButton(self.f_greeck)
        self.f_button23.setObjectName(u"f_button23")

        self.gridLayout.addWidget(self.f_button23, 4, 0, 1, 1)

        self.f_button24 = QPushButton(self.f_greeck)
        self.f_button24.setObjectName(u"f_button24")

        self.gridLayout.addWidget(self.f_button24, 4, 1, 1, 1)

        self.f_button25 = QPushButton(self.f_greeck)
        self.f_button25.setObjectName(u"f_button25")

        self.gridLayout.addWidget(self.f_button25, 4, 2, 1, 1)

        self.f_button26 = QPushButton(self.f_greeck)
        self.f_button26.setObjectName(u"f_button26")

        self.gridLayout.addWidget(self.f_button26, 4, 3, 1, 1)

        self.f_button27 = QPushButton(self.f_greeck)
        self.f_button27.setObjectName(u"f_button27")

        self.gridLayout.addWidget(self.f_button27, 4, 4, 1, 1)

        self.f_button28 = QPushButton(self.f_greeck)
        self.f_button28.setObjectName(u"f_button28")

        self.gridLayout.addWidget(self.f_button28, 4, 5, 1, 1)

        self.f_button29 = QPushButton(self.f_greeck)
        self.f_button29.setObjectName(u"f_button29")

        self.gridLayout.addWidget(self.f_button29, 5, 0, 1, 1)

        self.f_button30 = QPushButton(self.f_greeck)
        self.f_button30.setObjectName(u"f_button30")

        self.gridLayout.addWidget(self.f_button30, 5, 1, 1, 1)

        self.f_button31 = QPushButton(self.f_greeck)
        self.f_button31.setObjectName(u"f_button31")

        self.gridLayout.addWidget(self.f_button31, 5, 2, 1, 1)

        self.f_button32 = QPushButton(self.f_greeck)
        self.f_button32.setObjectName(u"f_button32")

        self.gridLayout.addWidget(self.f_button32, 5, 3, 1, 1)

        self.Greeck_widget.addTab(self.Function, "")
        self.Atoms = QWidget()
        self.Atoms.setObjectName(u"Atoms")
        self.a_greeck = QWidget(self.Atoms)
        self.a_greeck.setObjectName(u"a_greeck")
        self.a_greeck.setGeometry(QRect(10, 10, 160, 180))
        self.gridLayout_2 = QGridLayout(self.a_greeck)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.f_button1_2 = QPushButton(self.a_greeck)
        self.f_button1_2.setObjectName(u"f_button1_2")

        self.gridLayout_2.addWidget(self.f_button1_2, 0, 0, 1, 1)

        self.f_button2_2 = QPushButton(self.a_greeck)
        self.f_button2_2.setObjectName(u"f_button2_2")

        self.gridLayout_2.addWidget(self.f_button2_2, 0, 1, 1, 1)

        self.f_button3_2 = QPushButton(self.a_greeck)
        self.f_button3_2.setObjectName(u"f_button3_2")

        self.gridLayout_2.addWidget(self.f_button3_2, 0, 2, 1, 1)

        self.f_button4_2 = QPushButton(self.a_greeck)
        self.f_button4_2.setObjectName(u"f_button4_2")

        self.gridLayout_2.addWidget(self.f_button4_2, 0, 3, 1, 1)

        self.f_button5_2 = QPushButton(self.a_greeck)
        self.f_button5_2.setObjectName(u"f_button5_2")

        self.gridLayout_2.addWidget(self.f_button5_2, 0, 4, 1, 1)

        self.f_button6_2 = QPushButton(self.a_greeck)
        self.f_button6_2.setObjectName(u"f_button6_2")

        self.gridLayout_2.addWidget(self.f_button6_2, 0, 5, 1, 1)

        self.f_button7_2 = QPushButton(self.a_greeck)
        self.f_button7_2.setObjectName(u"f_button7_2")

        self.gridLayout_2.addWidget(self.f_button7_2, 1, 0, 1, 1)

        self.f_button8_2 = QPushButton(self.a_greeck)
        self.f_button8_2.setObjectName(u"f_button8_2")

        self.gridLayout_2.addWidget(self.f_button8_2, 1, 1, 1, 1)

        self.f_button9_2 = QPushButton(self.a_greeck)
        self.f_button9_2.setObjectName(u"f_button9_2")

        self.gridLayout_2.addWidget(self.f_button9_2, 1, 2, 1, 1)

        self.f_button10_2 = QPushButton(self.a_greeck)
        self.f_button10_2.setObjectName(u"f_button10_2")

        self.gridLayout_2.addWidget(self.f_button10_2, 1, 3, 1, 1)

        self.f_button11_2 = QPushButton(self.a_greeck)
        self.f_button11_2.setObjectName(u"f_button11_2")

        self.gridLayout_2.addWidget(self.f_button11_2, 1, 4, 1, 1)

        self.f_button12_2 = QPushButton(self.a_greeck)
        self.f_button12_2.setObjectName(u"f_button12_2")

        self.gridLayout_2.addWidget(self.f_button12_2, 1, 5, 1, 1)

        self.f_button13_2 = QPushButton(self.a_greeck)
        self.f_button13_2.setObjectName(u"f_button13_2")

        self.gridLayout_2.addWidget(self.f_button13_2, 2, 0, 1, 1)

        self.f_button14_2 = QPushButton(self.a_greeck)
        self.f_button14_2.setObjectName(u"f_button14_2")

        self.gridLayout_2.addWidget(self.f_button14_2, 2, 1, 1, 1)

        self.f_button15_2 = QPushButton(self.a_greeck)
        self.f_button15_2.setObjectName(u"f_button15_2")

        self.gridLayout_2.addWidget(self.f_button15_2, 2, 2, 1, 1)

        self.f_button16_2 = QPushButton(self.a_greeck)
        self.f_button16_2.setObjectName(u"f_button16_2")

        self.gridLayout_2.addWidget(self.f_button16_2, 2, 3, 1, 1)

        self.f_button17_2 = QPushButton(self.a_greeck)
        self.f_button17_2.setObjectName(u"f_button17_2")

        self.gridLayout_2.addWidget(self.f_button17_2, 2, 4, 1, 1)

        self.f_button18_2 = QPushButton(self.a_greeck)
        self.f_button18_2.setObjectName(u"f_button18_2")

        self.gridLayout_2.addWidget(self.f_button18_2, 2, 5, 1, 1)

        self.f_button19_2 = QPushButton(self.a_greeck)
        self.f_button19_2.setObjectName(u"f_button19_2")

        self.gridLayout_2.addWidget(self.f_button19_2, 3, 0, 1, 1)

        self.f_button20_2 = QPushButton(self.a_greeck)
        self.f_button20_2.setObjectName(u"f_button20_2")

        self.gridLayout_2.addWidget(self.f_button20_2, 3, 1, 1, 1)

        self.f_button21_2 = QPushButton(self.a_greeck)
        self.f_button21_2.setObjectName(u"f_button21_2")

        self.gridLayout_2.addWidget(self.f_button21_2, 3, 2, 1, 1)

        self.f_button22_2 = QPushButton(self.a_greeck)
        self.f_button22_2.setObjectName(u"f_button22_2")

        self.gridLayout_2.addWidget(self.f_button22_2, 3, 3, 1, 1)

        self.f_button23_2 = QPushButton(self.a_greeck)
        self.f_button23_2.setObjectName(u"f_button23_2")

        self.gridLayout_2.addWidget(self.f_button23_2, 4, 0, 1, 1)

        self.f_button24_2 = QPushButton(self.a_greeck)
        self.f_button24_2.setObjectName(u"f_button24_2")

        self.gridLayout_2.addWidget(self.f_button24_2, 4, 1, 1, 1)

        self.f_button25_2 = QPushButton(self.a_greeck)
        self.f_button25_2.setObjectName(u"f_button25_2")

        self.gridLayout_2.addWidget(self.f_button25_2, 4, 2, 1, 1)

        self.f_button26_2 = QPushButton(self.a_greeck)
        self.f_button26_2.setObjectName(u"f_button26_2")

        self.gridLayout_2.addWidget(self.f_button26_2, 4, 3, 1, 1)

        self.f_button27_2 = QPushButton(self.a_greeck)
        self.f_button27_2.setObjectName(u"f_button27_2")

        self.gridLayout_2.addWidget(self.f_button27_2, 4, 4, 1, 1)

        self.f_button28_2 = QPushButton(self.a_greeck)
        self.f_button28_2.setObjectName(u"f_button28_2")

        self.gridLayout_2.addWidget(self.f_button28_2, 4, 5, 1, 1)

        self.f_button29_2 = QPushButton(self.a_greeck)
        self.f_button29_2.setObjectName(u"f_button29_2")

        self.gridLayout_2.addWidget(self.f_button29_2, 5, 0, 1, 1)

        self.f_button30_2 = QPushButton(self.a_greeck)
        self.f_button30_2.setObjectName(u"f_button30_2")

        self.gridLayout_2.addWidget(self.f_button30_2, 5, 1, 1, 1)

        self.f_button31_2 = QPushButton(self.a_greeck)
        self.f_button31_2.setObjectName(u"f_button31_2")

        self.gridLayout_2.addWidget(self.f_button31_2, 5, 2, 1, 1)

        self.f_button32_2 = QPushButton(self.a_greeck)
        self.f_button32_2.setObjectName(u"f_button32_2")

        self.gridLayout_2.addWidget(self.f_button32_2, 5, 3, 1, 1)

        self.Greeck_widget.addTab(self.Atoms, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Greeck_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.formula_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0443\u043b\u0430", None))
        self.atoms_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0442\u043e\u043c\u044b/\u0421\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u044f", None))
        self.slave_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0438\u0442\u044c", None))
        self.solution_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0438\u043b", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0438\u043b", None))
        self.f_button1.setText(QCoreApplication.translate("MainWindow", u"\u03b1", None))
        self.f_button2.setText(QCoreApplication.translate("MainWindow", u"\u03b2", None))
        self.f_button3.setText(QCoreApplication.translate("MainWindow", u"\u03b3", None))
        self.f_button4.setText(QCoreApplication.translate("MainWindow", u"\u03b4", None))
        self.f_button5.setText(QCoreApplication.translate("MainWindow", u"\u03b5", None))
        self.f_button6.setText(QCoreApplication.translate("MainWindow", u"\u03b6", None))
        self.f_button7.setText(QCoreApplication.translate("MainWindow", u"\u03b7", None))
        self.f_button8.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None))
        self.f_button9.setText(QCoreApplication.translate("MainWindow", u"\u03b9", None))
        self.f_button10.setText(QCoreApplication.translate("MainWindow", u"\u03ba", None))
        self.f_button11.setText(QCoreApplication.translate("MainWindow", u"\u03bb", None))
        self.f_button12.setText(QCoreApplication.translate("MainWindow", u"\u03bd", None))
        self.f_button13.setText(QCoreApplication.translate("MainWindow", u"\u03be", None))
        self.f_button14.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.f_button15.setText(QCoreApplication.translate("MainWindow", u"\u03c1", None))
        self.f_button16.setText(QCoreApplication.translate("MainWindow", u"\u03c3", None))
        self.f_button17.setText(QCoreApplication.translate("MainWindow", u"\u03c4", None))
        self.f_button18.setText(QCoreApplication.translate("MainWindow", u"\u03c5", None))
        self.f_button19.setText(QCoreApplication.translate("MainWindow", u"\u03c6", None))
        self.f_button20.setText(QCoreApplication.translate("MainWindow", u"\u03c7", None))
        self.f_button21.setText(QCoreApplication.translate("MainWindow", u"\u03c8", None))
        self.f_button22.setText(QCoreApplication.translate("MainWindow", u"\u03c9", None))
        self.f_button23.setText(QCoreApplication.translate("MainWindow", u"\u0393", None))
        self.f_button24.setText(QCoreApplication.translate("MainWindow", u"\u0394", None))
        self.f_button25.setText(QCoreApplication.translate("MainWindow", u"\u0398", None))
        self.f_button26.setText(QCoreApplication.translate("MainWindow", u"\u039b", None))
        self.f_button27.setText(QCoreApplication.translate("MainWindow", u"\u039e", None))
        self.f_button28.setText(QCoreApplication.translate("MainWindow", u"\u03a0", None))
        self.f_button29.setText(QCoreApplication.translate("MainWindow", u"\u03a3", None))
        self.f_button30.setText(QCoreApplication.translate("MainWindow", u"\u03a6", None))
        self.f_button31.setText(QCoreApplication.translate("MainWindow", u"\u03a8", None))
        self.f_button32.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.Greeck_widget.setTabText(self.Greeck_widget.indexOf(self.Function), QCoreApplication.translate("MainWindow", u"\u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.f_button1_2.setText(QCoreApplication.translate("MainWindow", u"\u03b1", None))
        self.f_button2_2.setText(QCoreApplication.translate("MainWindow", u"\u03b2", None))
        self.f_button3_2.setText(QCoreApplication.translate("MainWindow", u"\u03b3", None))
        self.f_button4_2.setText(QCoreApplication.translate("MainWindow", u"\u03b4", None))
        self.f_button5_2.setText(QCoreApplication.translate("MainWindow", u"\u03b5", None))
        self.f_button6_2.setText(QCoreApplication.translate("MainWindow", u"\u03b6", None))
        self.f_button7_2.setText(QCoreApplication.translate("MainWindow", u"\u03b7", None))
        self.f_button8_2.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None))
        self.f_button9_2.setText(QCoreApplication.translate("MainWindow", u"\u03b9", None))
        self.f_button10_2.setText(QCoreApplication.translate("MainWindow", u"\u03ba", None))
        self.f_button11_2.setText(QCoreApplication.translate("MainWindow", u"\u03bb", None))
        self.f_button12_2.setText(QCoreApplication.translate("MainWindow", u"\u03bd", None))
        self.f_button13_2.setText(QCoreApplication.translate("MainWindow", u"\u03be", None))
        self.f_button14_2.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.f_button15_2.setText(QCoreApplication.translate("MainWindow", u"\u03c1", None))
        self.f_button16_2.setText(QCoreApplication.translate("MainWindow", u"\u03c3", None))
        self.f_button17_2.setText(QCoreApplication.translate("MainWindow", u"\u03c4", None))
        self.f_button18_2.setText(QCoreApplication.translate("MainWindow", u"\u03c5", None))
        self.f_button19_2.setText(QCoreApplication.translate("MainWindow", u"\u03c6", None))
        self.f_button20_2.setText(QCoreApplication.translate("MainWindow", u"\u03c7", None))
        self.f_button21_2.setText(QCoreApplication.translate("MainWindow", u"\u03c8", None))
        self.f_button22_2.setText(QCoreApplication.translate("MainWindow", u"\u03c9", None))
        self.f_button23_2.setText(QCoreApplication.translate("MainWindow", u"\u0393", None))
        self.f_button24_2.setText(QCoreApplication.translate("MainWindow", u"\u0394", None))
        self.f_button25_2.setText(QCoreApplication.translate("MainWindow", u"\u0398", None))
        self.f_button26_2.setText(QCoreApplication.translate("MainWindow", u"\u039b", None))
        self.f_button27_2.setText(QCoreApplication.translate("MainWindow", u"\u039e", None))
        self.f_button28_2.setText(QCoreApplication.translate("MainWindow", u"\u03a0", None))
        self.f_button29_2.setText(QCoreApplication.translate("MainWindow", u"\u03a3", None))
        self.f_button30_2.setText(QCoreApplication.translate("MainWindow", u"\u03a6", None))
        self.f_button31_2.setText(QCoreApplication.translate("MainWindow", u"\u03a8", None))
        self.f_button32_2.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.Greeck_widget.setTabText(self.Greeck_widget.indexOf(self.Atoms), QCoreApplication.translate("MainWindow", u"\u0410\u0442\u043e\u043c\u044b", None))
    # retranslateUi

