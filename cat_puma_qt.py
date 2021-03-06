#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:23:15 2017

author: Jiajia Liu @ University of Sheffield
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pickle
from datetime import datetime, timedelta
from cat_puma import get_mean, read_omni, get_svm_input

class svm_engine:
    pass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sp2rc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(0.95)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(150, 230, 87, 30))
        self.closeButton.setObjectName("closeButton")
        self.resultlabel = QtWidgets.QLabel(Dialog)
        self.resultlabel.setGeometry(QtCore.QRect(30, 30, 351, 201))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.resultlabel.setFont(font)
        self.resultlabel.setText("")
        self.resultlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultlabel.setObjectName("resultlabel")

        self.retranslateUi(Dialog)
        self.closeButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prediction Result"))
        self.closeButton.setText(_translate("Dialog", "Close"))


class cat_ui(object):
    def __init__(self, uid, Dialog, path):
        self.uid = uid
        self.Dialog = Dialog
        self.path = path

    def setupUi(self, CatPuma):
        CatPuma.setObjectName("CatPuma")
        CatPuma.resize(650, 650)
        CatPuma.setMinimumSize(QtCore.QSize(0, 0))
        CatPuma.setMaximumSize(QtCore.QSize(650, 669))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setItalic(True)
        CatPuma.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path + "sp2rc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CatPuma.setWindowIcon(icon)
        CatPuma.setWindowOpacity(0.95)
        CatPuma.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralWidget = QtWidgets.QWidget(CatPuma)
        self.centralWidget.setObjectName("centralWidget")
        self.cmelabel = QtWidgets.QLabel(self.centralWidget)
        self.cmelabel.setGeometry(QtCore.QRect(90, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cmelabel.setFont(font)
        self.cmelabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cmelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cmelabel.setObjectName("cmelabel")
        self.windlabel = QtWidgets.QLabel(self.centralWidget)
        self.windlabel.setGeometry(QtCore.QRect(390, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.windlabel.setFont(font)
        self.windlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.windlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.windlabel.setObjectName("windlabel")
        self.timevar = QtWidgets.QDateTimeEdit(self.centralWidget)
        self.timevar.setGeometry(QtCore.QRect(120, 60, 181, 21))
        self.timevar.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.timevar.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 4, 10), QtCore.QTime(11, 12, 5)))
        self.timevar.setDate(QtCore.QDate(2016, 4, 10))
        self.timevar.setTime(QtCore.QTime(11, 12, 5))
        self.timevar.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.timevar.setCalendarPopup(True)
        self.timevar.setTimeSpec(QtCore.Qt.LocalTime)
        self.timevar.setObjectName("timevar")
        self.tinmelabel = QtWidgets.QLabel(self.centralWidget)
        self.tinmelabel.setGeometry(QtCore.QRect(0, 60, 111, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.tinmelabel.setFont(font)
        self.tinmelabel.setAutoFillBackground(False)
        self.tinmelabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tinmelabel.setObjectName("tinmelabel")
        self.speedlabel = QtWidgets.QLabel(self.centralWidget)
        self.speedlabel.setGeometry(QtCore.QRect(0, 100, 111, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.speedlabel.setFont(font)
        self.speedlabel.setAutoFillBackground(False)
        self.speedlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speedlabel.setObjectName("speedlabel")
        self.speedvar = QtWidgets.QLineEdit(self.centralWidget)
        self.speedvar.setGeometry(QtCore.QRect(120, 100, 113, 21))
        self.speedvar.setObjectName("speedvar")
        self.speedunit = QtWidgets.QLabel(self.centralWidget)
        self.speedunit.setGeometry(QtCore.QRect(250, 100, 51, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.speedunit.setFont(font)
        self.speedunit.setAutoFillBackground(False)
        self.speedunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speedunit.setObjectName("speedunit")
        self.fspeedvar = QtWidgets.QLineEdit(self.centralWidget)
        self.fspeedvar.setGeometry(QtCore.QRect(120, 140, 113, 21))
        self.fspeedvar.setObjectName("fspeedvar")
        self.fspeedlabel = QtWidgets.QLabel(self.centralWidget)
        self.fspeedlabel.setGeometry(QtCore.QRect(0, 140, 111, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.fspeedlabel.setFont(font)
        self.fspeedlabel.setAutoFillBackground(False)
        self.fspeedlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fspeedlabel.setObjectName("fspeedlabel")
        self.fspeedunit = QtWidgets.QLabel(self.centralWidget)
        self.fspeedunit.setGeometry(QtCore.QRect(250, 140, 51, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.fspeedunit.setFont(font)
        self.fspeedunit.setAutoFillBackground(False)
        self.fspeedunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fspeedunit.setObjectName("fspeedunit")
        self.widthvar = QtWidgets.QLineEdit(self.centralWidget)
        self.widthvar.setGeometry(QtCore.QRect(120, 180, 113, 21))
        self.widthvar.setObjectName("widthvar")
        self.widthlabel = QtWidgets.QLabel(self.centralWidget)
        self.widthlabel.setGeometry(QtCore.QRect(0, 180, 111, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.widthlabel.setFont(font)
        self.widthlabel.setAutoFillBackground(False)
        self.widthlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthlabel.setObjectName("widthlabel")
        self.widthunit = QtWidgets.QLabel(self.centralWidget)
        self.widthunit.setGeometry(QtCore.QRect(250, 180, 51, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.widthunit.setFont(font)
        self.widthunit.setAutoFillBackground(False)
        self.widthunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthunit.setObjectName("widthunit")
        self.massvar = QtWidgets.QLineEdit(self.centralWidget)
        self.massvar.setGeometry(QtCore.QRect(120, 220, 113, 21))
        self.massvar.setObjectName("massvar")
        self.masslabel = QtWidgets.QLabel(self.centralWidget)
        self.masslabel.setGeometry(QtCore.QRect(0, 220, 111, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.masslabel.setFont(font)
        self.masslabel.setAutoFillBackground(False)
        self.masslabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.masslabel.setObjectName("masslabel")
        self.massunit = QtWidgets.QLabel(self.centralWidget)
        self.massunit.setGeometry(QtCore.QRect(250, 220, 51, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.massunit.setFont(font)
        self.massunit.setAutoFillBackground(False)
        self.massunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.massunit.setObjectName("massunit")
        self.mpavar = QtWidgets.QLineEdit(self.centralWidget)
        self.mpavar.setGeometry(QtCore.QRect(120, 260, 113, 21))
        self.mpavar.setObjectName("mpavar")
        self.mpalabel = QtWidgets.QLabel(self.centralWidget)
        self.mpalabel.setGeometry(QtCore.QRect(0, 260, 111, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.mpalabel.setFont(font)
        self.mpalabel.setAutoFillBackground(False)
        self.mpalabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mpalabel.setObjectName("mpalabel")
        self.mpaunit = QtWidgets.QLabel(self.centralWidget)
        self.mpaunit.setGeometry(QtCore.QRect(250, 260, 51, 18))
        font = QtGui.QFont()
        font.setItalic(False)
        self.mpaunit.setFont(font)
        self.mpaunit.setAutoFillBackground(False)
        self.mpaunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mpaunit.setObjectName("mpaunit")
        self.arrivevar = QtWidgets.QDateTimeEdit(self.centralWidget)
        self.arrivevar.setGeometry(QtCore.QRect(80, 340, 181, 21))
        self.arrivevar.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.arrivevar.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 4, 14), QtCore.QTime(06, 50, 0)))
        self.arrivevar.setDate(QtCore.QDate(2016, 4, 14))
        self.arrivevar.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.arrivevar.setCalendarPopup(True)
        self.arrivevar.setTimeSpec(QtCore.Qt.LocalTime)
        self.arrivevar.setObjectName("arrivevar")
        self.arrivecheck = QtWidgets.QCheckBox(self.centralWidget)
        self.arrivecheck.setGeometry(QtCore.QRect(90, 310, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.arrivecheck.setFont(font)
        self.arrivecheck.setObjectName("arrivecheck")
        self.bzvar = QtWidgets.QLineEdit(self.centralWidget)
        self.bzvar.setGeometry(QtCore.QRect(470, 60, 113, 21))
        self.bzvar.setObjectName("bzvar")
        self.bzlabel = QtWidgets.QLabel(self.centralWidget)
        self.bzlabel.setGeometry(QtCore.QRect(340, 60, 121, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.bzlabel.setFont(font)
        self.bzlabel.setAutoFillBackground(False)
        self.bzlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bzlabel.setObjectName("bzlabel")
        self.bzunit = QtWidgets.QLabel(self.centralWidget)
        self.bzunit.setGeometry(QtCore.QRect(590, 60, 41, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.bzunit.setFont(font)
        self.bzunit.setAutoFillBackground(False)
        self.bzunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bzunit.setObjectName("bzunit")
        self.bxlabel = QtWidgets.QLabel(self.centralWidget)
        self.bxlabel.setGeometry(QtCore.QRect(340, 100, 121, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.bxlabel.setFont(font)
        self.bxlabel.setAutoFillBackground(False)
        self.bxlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bxlabel.setObjectName("bxlabel")
        self.bxunit = QtWidgets.QLabel(self.centralWidget)
        self.bxunit.setGeometry(QtCore.QRect(590, 100, 41, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.bxunit.setFont(font)
        self.bxunit.setAutoFillBackground(False)
        self.bxunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bxunit.setObjectName("bxunit")
        self.bxvar = QtWidgets.QLineEdit(self.centralWidget)
        self.bxvar.setGeometry(QtCore.QRect(470, 100, 113, 21))
        self.bxvar.setObjectName("bxvar")
        self.vlabel = QtWidgets.QLabel(self.centralWidget)
        self.vlabel.setGeometry(QtCore.QRect(340, 140, 121, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.vlabel.setFont(font)
        self.vlabel.setAutoFillBackground(False)
        self.vlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vlabel.setObjectName("vlabel")
        self.vunit = QtWidgets.QLabel(self.centralWidget)
        self.vunit.setGeometry(QtCore.QRect(590, 140, 41, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.vunit.setFont(font)
        self.vunit.setAutoFillBackground(False)
        self.vunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.vunit.setObjectName("vunit")
        self.vvar = QtWidgets.QLineEdit(self.centralWidget)
        self.vvar.setGeometry(QtCore.QRect(470, 140, 113, 21))
        self.vvar.setObjectName("vvar")
        self.plabel = QtWidgets.QLabel(self.centralWidget)
        self.plabel.setGeometry(QtCore.QRect(340, 180, 121, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.plabel.setFont(font)
        self.plabel.setAutoFillBackground(False)
        self.plabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.plabel.setObjectName("plabel")
        self.punit = QtWidgets.QLabel(self.centralWidget)
        self.punit.setGeometry(QtCore.QRect(590, 180, 41, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.punit.setFont(font)
        self.punit.setAutoFillBackground(False)
        self.punit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.punit.setObjectName("punit")
        self.pvar = QtWidgets.QLineEdit(self.centralWidget)
        self.pvar.setGeometry(QtCore.QRect(470, 180, 113, 21))
        self.pvar.setObjectName("pvar")
        self.latlabel = QtWidgets.QLabel(self.centralWidget)
        self.latlabel.setGeometry(QtCore.QRect(340, 220, 121, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.latlabel.setFont(font)
        self.latlabel.setAutoFillBackground(False)
        self.latlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.latlabel.setObjectName("latlabel")
        self.latunit = QtWidgets.QLabel(self.centralWidget)
        self.latunit.setGeometry(QtCore.QRect(590, 220, 41, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.latunit.setFont(font)
        self.latunit.setAutoFillBackground(False)
        self.latunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.latunit.setObjectName("latunit")
        self.latvar = QtWidgets.QLineEdit(self.centralWidget)
        self.latvar.setGeometry(QtCore.QRect(470, 220, 113, 21))
        self.latvar.setObjectName("latvar")
        self.lonlabel = QtWidgets.QLabel(self.centralWidget)
        self.lonlabel.setGeometry(QtCore.QRect(340, 260, 121, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.lonlabel.setFont(font)
        self.lonlabel.setAutoFillBackground(False)
        self.lonlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lonlabel.setObjectName("lonlabel")
        self.lonunit = QtWidgets.QLabel(self.centralWidget)
        self.lonunit.setGeometry(QtCore.QRect(590, 260, 41, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.lonunit.setFont(font)
        self.lonunit.setAutoFillBackground(False)
        self.lonunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lonunit.setObjectName("lonunit")
        self.lonvar = QtWidgets.QLineEdit(self.centralWidget)
        self.lonvar.setGeometry(QtCore.QRect(470, 260, 113, 21))
        self.lonvar.setObjectName("lonvar")
        self.tlabel = QtWidgets.QLabel(self.centralWidget)
        self.tlabel.setGeometry(QtCore.QRect(330, 300, 131, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.tlabel.setFont(font)
        self.tlabel.setAutoFillBackground(False)
        self.tlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tlabel.setObjectName("tlabel")
        self.tunit = QtWidgets.QLabel(self.centralWidget)
        self.tunit.setGeometry(QtCore.QRect(590, 300, 41, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.tunit.setFont(font)
        self.tunit.setAutoFillBackground(False)
        self.tunit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tunit.setObjectName("tunit")
        self.tvar = QtWidgets.QLineEdit(self.centralWidget)
        self.tvar.setGeometry(QtCore.QRect(470, 300, 113, 21))
        self.tvar.setObjectName("tvar")
        self.ratiovar = QtWidgets.QLineEdit(self.centralWidget)
        self.ratiovar.setGeometry(QtCore.QRect(470, 340, 113, 21))
        self.ratiovar.setObjectName("ratiovar")
        self.ratiolabel = QtWidgets.QLabel(self.centralWidget)
        self.ratiolabel.setGeometry(QtCore.QRect(330, 340, 131, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        self.ratiolabel.setFont(font)
        self.ratiolabel.setAutoFillBackground(False)
        self.ratiolabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ratiolabel.setObjectName("ratiolabel")
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(180, 440, 311, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 500, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.logolabel = QtWidgets.QLabel(self.centralWidget)
        self.logolabel.setGeometry(QtCore.QRect(0, 600, 51, 51))
        self.logolabel.setText("")
        self.logolabel.setPixmap(QtGui.QPixmap(self.path + "sp2rc.png"))
        self.logolabel.setScaledContents(True)
        self.logolabel.setWordWrap(False)
        self.logolabel.setObjectName("logolabel")
        self.afflabel = QtWidgets.QLabel(self.centralWidget)
        self.afflabel.setGeometry(QtCore.QRect(60, 620, 451, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.afflabel.setFont(font)
        self.afflabel.setTextFormat(QtCore.Qt.RichText)
        self.afflabel.setOpenExternalLinks(True)
        self.afflabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.afflabel.setObjectName("afflabel")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 3, 371))
        self.label.setStyleSheet("background-color: rgb(225, 222, 219);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.cmelabel.raise_()
        self.windlabel.raise_()
        self.timevar.raise_()
        self.tinmelabel.raise_()
        self.speedlabel.raise_()
        self.speedvar.raise_()
        self.speedunit.raise_()
        self.fspeedvar.raise_()
        self.fspeedlabel.raise_()
        self.fspeedunit.raise_()
        self.widthvar.raise_()
        self.widthlabel.raise_()
        self.widthunit.raise_()
        self.massvar.raise_()
        self.masslabel.raise_()
        self.massunit.raise_()
        self.mpavar.raise_()
        self.mpalabel.raise_()
        self.mpaunit.raise_()
        self.arrivevar.raise_()
        self.arrivecheck.raise_()
        self.bzvar.raise_()
        self.bzlabel.raise_()
        self.bzunit.raise_()
        self.bxlabel.raise_()
        self.bxunit.raise_()
        self.bxvar.raise_()
        self.vlabel.raise_()
        self.vunit.raise_()
        self.vvar.raise_()
        self.plabel.raise_()
        self.punit.raise_()
        self.pvar.raise_()
        self.latlabel.raise_()
        self.latunit.raise_()
        self.latvar.raise_()
        self.lonlabel.raise_()
        self.lonunit.raise_()
        self.lonvar.raise_()
        self.tlabel.raise_()
        self.tunit.raise_()
        self.tvar.raise_()
        self.ratiovar.raise_()
        self.ratiolabel.raise_()
        self.checkBox.raise_()
        self.pushButton.raise_()
        self.afflabel.raise_()
        self.label.raise_()
        self.logolabel.raise_()
        CatPuma.setCentralWidget(self.centralWidget)

        self.retranslateUi(CatPuma)
        self.pushButton.clicked.connect(self.submit)
        QtCore.QMetaObject.connectSlotsByName(CatPuma)

    def retranslateUi(self, CatPuma):
        _translate = QtCore.QCoreApplication.translate
        CatPuma.setWindowTitle(_translate("CatPuma", "CAT-PUMA"))
        self.cmelabel.setText(_translate("CatPuma", "CME Parameters"))
        self.windlabel.setText(_translate("CatPuma", "Solar Wind Parameters"))
        self.timevar.setDisplayFormat(_translate("CatPuma", "yyyy-MM-ddThh:mm:ss"))
        self.tinmelabel.setText(_translate("CatPuma", "Onset Time:"))
        self.speedlabel.setText(_translate("CatPuma", "Average Speed:"))
        self.speedvar.setText(_translate("CatPuma", "543.0"))
        self.speedunit.setText(_translate("CatPuma", "km/s"))
        self.fspeedvar.setText(_translate("CatPuma", "547.0"))
        self.fspeedlabel.setText(_translate("CatPuma", "Final Speed:"))
        self.fspeedunit.setText(_translate("CatPuma", "km/s"))
        self.widthvar.setText(_translate("CatPuma", "136.0"))
        self.widthlabel.setText(_translate("CatPuma", "Angular Width:"))
        self.widthunit.setText(_translate("CatPuma", "degree"))
        self.massvar.setText(_translate("CatPuma", "4.6e15"))
        self.masslabel.setText(_translate("CatPuma", "Total Mass:"))
        self.massunit.setText(_translate("CatPuma", "g"))
        self.mpavar.setText(_translate("CatPuma", "25.0"))
        self.mpalabel.setText(_translate("CatPuma", "MPA:"))
        self.mpaunit.setText(_translate("CatPuma", "degree"))
        self.arrivevar.setDisplayFormat(_translate("CatPuma", "yyyy-MM-ddThh:mm:ss"))
        self.arrivecheck.setText(_translate("CatPuma", "Known Arrival Time"))
        self.bzvar.setText(_translate("CatPuma", "0.0"))
        self.bzlabel.setText(_translate("CatPuma", "Magnetic Field Bz:"))
        self.bzunit.setText(_translate("CatPuma", "nT"))
        self.bxlabel.setText(_translate("CatPuma", "Magnetic Field Bx:"))
        self.bxunit.setText(_translate("CatPuma", "nT"))
        self.bxvar.setText(_translate("CatPuma", "0.0"))
        self.vlabel.setText(_translate("CatPuma", "Flow Speed:"))
        self.vunit.setText(_translate("CatPuma", "km/s"))
        self.vvar.setText(_translate("CatPuma", "0.0"))
        self.plabel.setText(_translate("CatPuma", "Flow Pressure:"))
        self.punit.setText(_translate("CatPuma", "nPa"))
        self.pvar.setText(_translate("CatPuma", "0.0"))
        self.latlabel.setText(_translate("CatPuma", "Flow Latitude:"))
        self.latunit.setText(_translate("CatPuma", "degree"))
        self.latvar.setText(_translate("CatPuma", "0.0"))
        self.lonlabel.setText(_translate("CatPuma", "Flow Longitude:"))
        self.lonunit.setText(_translate("CatPuma", "degree"))
        self.lonvar.setText(_translate("CatPuma", "0.0"))
        self.tlabel.setText(_translate("CatPuma", "Plasma Temperature:"))
        self.tunit.setText(_translate("CatPuma", "K"))
        self.tvar.setText(_translate("CatPuma", "0.0"))
        self.ratiovar.setText(_translate("CatPuma", "0.0"))
        self.ratiolabel.setText(_translate("CatPuma", "Alpha/Proton Ratio:"))
        self.checkBox.setText(_translate("CatPuma", "Automatically Obtain Solar Wind Parameters"))
        self.pushButton.setText(_translate("CatPuma", "Submit"))
        self.afflabel.setText(_translate("CatPuma", "<html><head/><body><p><a href=\"http://example.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">S</span></a><a href=\"http://sp2rc.group.shef.ac.uk/\"><span style=\" text-decoration: underline; color:#0000ff;\">olar Physics and Space Plasma Research Centre, The University of Sheffield</span></a></p></body></html>"))

    def submit(self):
        # Do not edit the following parameters
        # --------------------------------------------------------------------
        features = ['CME Average Speed',
                    'CME Final Speed',
                    'CME Angular Width',
                    'CME Mass',
                    'Solar Wind Bz',
                    'Solar Wind Speed',
                    'Solar Wind Temperature',
                    'Solar Wind Pressure',
                    'Solar Wind Longitude',
                    'Solar Wind He Proton Ratio',
                    'Solar Wind Bx',
                    'CME Position Angle'
                    ]
        duration = 6  # will average 6-hour solar wind parameters after the CME
        engine_file = self.path + 'engine.obj'
        # CME Parameters
        self.time = self.timevar.dateTime().toString('yyyy-MM-ddTHH:mm:ss')
        # CME Onset time in LASCO C2

        width = float(self.widthvar.text())  # angular width, degree
        speed = float(self.speedvar.text())  # linear speed in LASCO FOV, km/s
        final_speed = float(self.fspeedvar.text())  # second order final speed
                                                   # leaving LASCO FOV
        mass = float(self.massvar.text())  # estimated mass using 'cme_mass.pro'
                                          # in SSWIDL or from the SOHO LASCO
                                          # CME Catalog
        mpa = float(self.mpavar.text())  # degree, position angle corresponding
                                        # to the fasted front
        self.actual = self.arrivevar.dateTime().toString('yyyy-MM-ddTHH:mm:ss')
        # Actual arrival time
        if not self.arrivecheck.checkState():
            self.actual = None

        auto = self.checkBox.checkState()
        if auto:
            wind = read_omni(self.time, duration)
            self.bzvar.setText("%.5f" % float(wind['Bz']))
            self.ratiovar.setText(str(wind['Ratio']))
            self.vvar.setText(str(wind['V']))
            self.latvar.setText(str(wind['Lat']))
            self.pvar.setText(str(wind['P']))
            self.lonvar.setText(str(wind['Lon']))
            self.bxvar.setText(str(wind['Bx']))
            self.tvar.setText(str(wind['T']))
        else:
            wind = {'Bz': float(self.bzvar.text()),
                    'Ratio': float(self.ratiovar.text()),
                    'V': float(self.vvar.text()),
                    'Lat': float(self.latvar.text()),
                    'P': float(self.pvar.text()),
                    'Lon': float(self.lonvar.text()),
                    'Bx': float(self.bxvar.text()),
                    'T': float(self.tvar.text())}
        info = {'CME': self.time,
                'Speed': speed,
                'Speed_final': final_speed,
                'Width': width,
                'Mass': mass,
                'PA': mpa}

        info.setdefault('Wind', wind)
        # Get input for the engine
        xinput = get_svm_input(info, features)
        # Load the engine
        f = open(engine_file, 'r')
        engine = pickle.load(f)
        f.close()
        # Normalize x
        xinput = engine.scaler.transform(xinput)
        # Do Prediction
        self.travel = engine.clf.predict(xinput)[0]
        arrive = datetime.strptime(self.time, '%Y-%m-%dT%H:%M:%S') + \
                                   timedelta(hours=self.travel)
        self.arrive = datetime.strftime(arrive, '%Y-%m-%dT%H:%M:%S')
        if self.actual is not None:
            self.diff = datetime.strptime(self.arrive, '%Y-%m-%dT%H:%M:%S') - \
                        datetime.strptime(self.actual, '%Y-%m-%dT%H:%M:%S')
            self.diff = self.diff.total_seconds() / 3600.
        else:
            self.diff = None
        reinfo = ('%s%s%s' % ('CME with onset time ', self.time, ' UT\n\n')) + \
                 ('%s%s%s' % ('Will hit the Earth at ', self.arrive,
                              ' UT\n\n')) + \
                 ('%s%6.1f%s' % ('With a transit time of', self.travel,
                                 ' hours\n\n'))
        if self.diff is not None:
            reinfo = reinfo + \
                     ('%s%s%s' % ('The actual arrival time is ',
                                  self.actual, ' UT\n\n')) + \
                     ('%s%6.1f%s' % ('The prediction error is',
                                     self.diff, ' hours\n'))
        show_dialog(reinfo, self.uid, self.Dialog)


def show_dialog(text=' ', uid=None, Dialog=None):
    uid.resultlabel.setText(text)
    Dialog.close()
    Dialog.show()


def main():
    path = './'
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    uid = Ui_Dialog()
    uid.setupUi(Dialog)
    CatPuma = QtWidgets.QMainWindow()
    ui = cat_ui(uid, Dialog, path)
    ui.setupUi(CatPuma)
    CatPuma.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

