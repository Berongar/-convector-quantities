# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 511, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.provod = QtWidgets.QWidget()
        self.provod.setObjectName("provod")
        self.Diametr_input = QtWidgets.QLineEdit(self.provod)
        self.Diametr_input.setGeometry(QtCore.QRect(100, 50, 81, 31))
        self.Diametr_input.setMaximumSize(QtCore.QSize(81, 31))
        self.Diametr_input.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.Diametr_input.setText("")
        self.Diametr_input.setObjectName("Diametr_input")
        self.Button_Diametr = QtWidgets.QPushButton(self.provod)
        self.Button_Diametr.setGeometry(QtCore.QRect(200, 10, 121, 31))
        self.Button_Diametr.setObjectName("Button_Diametr")
        self.Sechenie_Out = QtWidgets.QTextBrowser(self.provod)
        self.Sechenie_Out.setGeometry(QtCore.QRect(330, 50, 81, 31))
        self.Sechenie_Out.setMaximumSize(QtCore.QSize(81, 31))
        self.Sechenie_Out.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhPreferNumbers)
        self.Sechenie_Out.setObjectName("Sechenie_Out")
        self.Sechenie_input = QtWidgets.QLineEdit(self.provod)
        self.Sechenie_input.setGeometry(QtCore.QRect(100, 11, 81, 31))
        self.Sechenie_input.setMaximumSize(QtCore.QSize(81, 31))
        self.Sechenie_input.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.Sechenie_input.setText("")
        self.Sechenie_input.setObjectName("Sechenie_input")
        self.label_2 = QtWidgets.QLabel(self.provod)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.provod)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.label_3.setObjectName("label_3")
        self.Diametr_out = QtWidgets.QTextBrowser(self.provod)
        self.Diametr_out.setGeometry(QtCore.QRect(330, 10, 81, 31))
        self.Diametr_out.setMaximumSize(QtCore.QSize(81, 31))
        self.Diametr_out.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhPreferNumbers)
        self.Diametr_out.setObjectName("Diametr_out")
        self.Button_Sechenie = QtWidgets.QPushButton(self.provod)
        self.Button_Sechenie.setGeometry(QtCore.QRect(200, 50, 121, 31))
        self.Button_Sechenie.setObjectName("Button_Sechenie")
        self.label_4 = QtWidgets.QLabel(self.provod)
        self.label_4.setGeometry(QtCore.QRect(420, 10, 21, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.provod)
        self.label_5.setGeometry(QtCore.QRect(420, 50, 31, 31))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.provod, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_6.setObjectName("label_6")
        self.Rashod_input_m3 = QtWidgets.QLineEdit(self.tab_2)
        self.Rashod_input_m3.setGeometry(QtCore.QRect(90, 10, 91, 31))
        self.Rashod_input_m3.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.Rashod_input_m3.setText("")
        self.Rashod_input_m3.setObjectName("Rashod_input_m3")
        self.Button_Rashod = QtWidgets.QPushButton(self.tab_2)
        self.Button_Rashod.setGeometry(QtCore.QRect(190, 10, 101, 31))
        self.Button_Rashod.setObjectName("Button_Rashod")
        self.Rashod_out_LinH = QtWidgets.QTextBrowser(self.tab_2)
        self.Rashod_out_LinH.setGeometry(QtCore.QRect(300, 10, 81, 31))
        self.Rashod_out_LinH.setMaximumSize(QtCore.QSize(81, 31))
        self.Rashod_out_LinH.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.Rashod_out_LinH.setObjectName("Rashod_out_LinH")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_Diametr.setText(_translate("MainWindow", "Диаметр"))
        self.label_2.setText(_translate("MainWindow", "Сечение"))
        self.label_3.setText(_translate("MainWindow", "Диаметр"))
        self.Button_Sechenie.setText(_translate("MainWindow", "Сечение"))
        self.label_4.setText(_translate("MainWindow", "мм"))
        self.label_5.setText(_translate("MainWindow", "мм2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.provod), _translate("MainWindow", "Расчет провода"))
        self.label_6.setText(_translate("MainWindow", "Расход М3/ч"))
        self.Button_Rashod.setText(_translate("MainWindow", "Пересчет в л/ч"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Расчет насоса"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Страница"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Страница"))
