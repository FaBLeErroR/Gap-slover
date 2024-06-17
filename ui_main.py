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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(752, 393)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 500, 350))
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

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 50, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"test", None))
    # retranslateUi

