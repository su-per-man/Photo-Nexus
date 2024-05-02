# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(100, 50, 600, 450))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"color: rgba(0, 0, 0, 103);")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(False)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 201, 131))
        font = QFont()
        font.setFamilies([u"Quicksand"])
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(0, 0, 255, 69), stop:0.375 rgba(0, 0, 255, 69), stop:0.423533 rgba(0, 4, 255, 145), stop:0.45 rgba(0, 8, 255, 208), stop:0.477581 rgba(11, 0, 184, 130), stop:0.518717 rgba(37, 0, 184, 130), stop:0.55 rgba(0, 0, 255, 255), stop:0.57754 rgba(52, 0, 130, 130), stop:0.625 rgba(0, 0, 255, 69), stop:1 rgba(0, 0, 255, 69));")
        self.label.setAlignment(Qt.AlignCenter)
        self.btnBrowseFace = QPushButton(self.tab)
        self.btnBrowseFace.setObjectName(u"btnBrowseFace")
        self.btnBrowseFace.setGeometry(QRect(240, 320, 100, 32))
        self.btnBrowseFace.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnBrowseFace.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnBrowseFace.setCheckable(False)
        self.btnBrowseFace.setFlat(False)
        self.lblImage = QLabel(self.tab)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setGeometry(QRect(180, 100, 221, 181))
        self.lblImage.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.lblImage.setFrameShape(QFrame.NoFrame)
        self.lblImage.setFrameShadow(QFrame.Raised)
        self.lblImage.setScaledContents(False)
        self.lblImage.setAlignment(Qt.AlignCenter)
        self.btnNext1 = QPushButton(self.tab)
        self.btnNext1.setObjectName(u"btnNext1")
        self.btnNext1.setGeometry(QRect(470, 370, 100, 32))
        self.btnNext1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(4, 51, 255, 75);")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 290, 221, 20))
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setAutoFillBackground(False)
        self.btnAddDir = QPushButton(self.tab_2)
        self.btnAddDir.setObjectName(u"btnAddDir")
        self.btnAddDir.setGeometry(QRect(90, 310, 100, 32))
        self.btnAddDir.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lstDir = QListWidget(self.tab_2)
        self.lstDir.setObjectName(u"lstDir")
        self.lstDir.setGeometry(QRect(90, 90, 411, 192))
        self.lstDir.setAutoFillBackground(False)
        self.lstDir.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.lstDir.setFrameShape(QFrame.NoFrame)
        self.lstDir.setFrameShadow(QFrame.Sunken)
        self.btnRmDir = QPushButton(self.tab_2)
        self.btnRmDir.setObjectName(u"btnRmDir")
        self.btnRmDir.setEnabled(False)
        self.btnRmDir.setGeometry(QRect(200, 310, 121, 32))
        self.btnRmDir.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btnNext2 = QPushButton(self.tab_2)
        self.btnNext2.setObjectName(u"btnNext2")
        self.btnNext2.setEnabled(False)
        self.btnNext2.setGeometry(QRect(470, 370, 100, 32))
        self.btnNext2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(4, 51, 255, 75);")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 50, 261, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setAutoFillBackground(False)
        self.progressBar = QProgressBar(self.tab_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(100, 40, 371, 23))
        self.progressBar.setValue(24)
        self.lstResults = QListWidget(self.tab_3)
        self.lstResults.setObjectName(u"lstResults")
        self.lstResults.setGeometry(QRect(90, 80, 391, 250))
        self.lstResults.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"color: rgb(255, 255, 255);")
        self.lstResults.setFrameShape(QFrame.NoFrame)
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 800, 600))
        self.label_2.setMinimumSize(QSize(800, 600))
        self.label_2.setMaximumSize(QSize(800, 600))
        self.label_2.setPixmap(QPixmap(u":/resources/background.jpg"))
        self.label_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.tabWidget.raise_()
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Photo Nexus", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Get Started!", None))
        self.btnBrowseFace.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.lblImage.setText("")
        self.btnNext1.setText(QCoreApplication.translate("MainWindow", u"Next >", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select a photo of an individual", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Face Selection", None))
        self.btnAddDir.setText(QCoreApplication.translate("MainWindow", u"Add Directory", None))
        self.btnRmDir.setText(QCoreApplication.translate("MainWindow", u"Exclude Directory", None))
        self.btnNext2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Where do you want to search the person?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Search Config", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.statusbar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.statusbar.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

