# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 228)
        self.start_butt = QPushButton(Form)
        self.start_butt.setObjectName(u"start_butt")
        self.start_butt.setGeometry(QRect(10, 150, 101, 61))
        self.stop_butt = QPushButton(Form)
        self.stop_butt.setObjectName(u"stop_butt")
        self.stop_butt.setGeometry(QRect(130, 150, 101, 61))
        self.played_games = QLCDNumber(Form)
        self.played_games.setObjectName(u"played_games")
        self.played_games.setGeometry(QRect(130, 10, 101, 51))
        self.played_games.setProperty("intValue", 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 111, 41))
        font = QFont()
        font.setFamily(u"Adobe Fan Heiti Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 51, 41))
        self.label_2.setFont(font)
        self.mode1 = QRadioButton(Form)
        self.mode1.setObjectName(u"mode1")
        self.mode1.setGeometry(QRect(70, 80, 91, 21))
        self.mode1.setChecked(True)
        self.mode2 = QRadioButton(Form)
        self.mode2.setObjectName(u"mode2")
        self.mode2.setGeometry(QRect(70, 110, 91, 21))
        self.mode2.setChecked(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TFT Helper", None))
        self.start_butt.setText(QCoreApplication.translate("Form", u"Start", None))
        self.stop_butt.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.label.setText(QCoreApplication.translate("Form", u"Played Games:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Mode:", None))
        self.mode1.setText(QCoreApplication.translate("Form", u"Run and Surr", None))
        self.mode2.setText(QCoreApplication.translate("Form", u"Auto play", None))
    # retranslateUi

