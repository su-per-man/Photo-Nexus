# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(130, 40, 471, 431))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 121, 51))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.btnBrowseFace = QPushButton(self.tab)
        self.btnBrowseFace.setObjectName(u"btnBrowseFace")
        self.btnBrowseFace.setGeometry(QRect(180, 280, 100, 32))
        self.btnBrowseFace.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBrowseFace.setCheckable(False)
        self.btnBrowseFace.setFlat(False)
        self.lblImage = QLabel(self.tab)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setGeometry(QRect(140, 100, 191, 151))
        self.btnNext1 = QPushButton(self.tab)
        self.btnNext1.setObjectName(u"btnNext1")
        self.btnNext1.setGeometry(QRect(350, 350, 100, 32))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.btnAddDir = QPushButton(self.tab_2)
        self.btnAddDir.setObjectName(u"btnAddDir")
        self.btnAddDir.setGeometry(QRect(330, 60, 100, 32))
        self.listWidget = QListWidget(self.tab_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 60, 291, 192))
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 100, 100, 32))
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 350, 100, 32))
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 300, 120, 80))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuPhoto_Nexus = QMenu(self.menubar)
        self.menuPhoto_Nexus.setObjectName(u"menuPhoto_Nexus")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPhoto_Nexus.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Get Started!", None))
        self.btnBrowseFace.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lblImage.setText("")
        self.btnNext1.setText(QCoreApplication.translate("MainWindow", u"Next >", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Face Selection", None))
        self.btnAddDir.setText(QCoreApplication.translate("MainWindow", u"Add Directory", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Manage ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Search Config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Results", None))
        self.menuPhoto_Nexus.setTitle(QCoreApplication.translate("MainWindow", u"Photo Nexus", None))
    # retranslateUi

