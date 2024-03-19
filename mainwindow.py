# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from deepface import DeepFace

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Variables
        self.searchFacePath = "/"
        self.listItemSet = set()

        # Connections and Slots for Tab1
        self.ui.btnBrowseFace.clicked.connect(self.photoSelection)
        self.ui.btnNext1.clicked.connect(self.nextPage)

        # Connections and Slots for Tab2
        self.ui.btnAddDir.clicked.connect(self.addDir)
        self.ui.btnRmDir.clicked.connect(self.removeDir)
        self.ui.listWidget.itemSelectionChanged.connect(self.listSelectionChanged)
        self.ui.btnNext2.clicked.connect(self.nextPage)

    def addDir(self):
        folderPath = QFileDialog.getExistingDirectory(self)
        self.listItemSet.add(folderPath)
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.listItemSet)
        self.updateNextButtonState()

    def removeDir(self):
        selectedItems = self.ui.listWidget.selectedItems()
        self.listItemSet -= set(item.text() for item in selectedItems)
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.listItemSet)
        self.updateNextButtonState()

    def listSelectionChanged(self):
        if self.ui.listWidget.selectedItems():
            self.ui.btnRmDir.setEnabled(True)
        else:
            self.ui.btnRmDir.setEnabled(False)

    def updateNextButtonState(self):
        if len(self.listItemSet) > 0:
            self.ui.btnNext2.setEnabled(True)
        else:
            self.ui.btnNext2.setEnabled(False)

    def initiateSearch(self):
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(len(self.listItemSet))
        self.ui.progressBar.setValue(0)
        progress = 0

        for dir in self.listItemSet:
            self.res = DeepFace.find(
                img_path=self.searchFacePath, db_path=dir, model_name="Facenet512"
            )
            progress += 1
            self.ui.progressBar.setValue(progress)
            print(self.res)

    def nextPage(self):
        current = self.ui.tabWidget.currentIndex()
        if current == 1:
            self.initiateSearch()
        self.ui.tabWidget.setCurrentIndex(current + 1)

    def photoSelection(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image File",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp)",
        )

        if file_name:
            self.searchFacePath = file_name
            pixmap = QPixmap(file_name)
            self.ui.lblImage.setPixmap(
                pixmap.scaled(
                    self.ui.lblImage.size(),
                    aspectMode=Qt.AspectRatioMode.KeepAspectRatio,
                )
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
