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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

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
        self.btnAddDir.setGeometry(QRect(50, 270, 100, 32))
        self.lstDir = QListWidget(self.tab_2)
        self.lstDir.setObjectName(u"lstDir")
        self.lstDir.setGeometry(QRect(30, 60, 411, 192))
        self.btnRmDir = QPushButton(self.tab_2)
        self.btnRmDir.setObjectName(u"btnRmDir")
        self.btnRmDir.setEnabled(False)
        self.btnRmDir.setGeometry(QRect(160, 270, 100, 32))
        self.btnNext2 = QPushButton(self.tab_2)
        self.btnNext2.setObjectName(u"btnNext2")
        self.btnNext2.setEnabled(False)
        self.btnNext2.setGeometry(QRect(340, 350, 100, 32))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.progressBar = QProgressBar(self.tab_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 30, 371, 23))
        self.progressBar.setValue(24)
        self.lstResults = QListWidget(self.tab_3)
        self.lstResults.setObjectName(u"lstResults")
        self.lstResults.setGeometry(QRect(30, 80, 391, 251))
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.btnRmDir.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.btnNext2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Search Config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Results", None))
    # retranslateUi

