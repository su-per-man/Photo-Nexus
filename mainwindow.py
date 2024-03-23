# This Python file uses the following encoding: utf-8
import sys
import subprocess
import platform

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
        self.dirListItemSet = set()
        self.resListItemSet = set()

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)

        # Connections and Slots for Tab1
        self.ui.btnBrowseFace.clicked.connect(self.photoSelection)
        self.ui.btnNext1.clicked.connect(self.nextPage)

        # Connections and Slots for Tab2
        self.ui.btnAddDir.clicked.connect(self.addDir)
        self.ui.btnRmDir.clicked.connect(self.removeDir)
        self.ui.lstDir.itemSelectionChanged.connect(self.listSelectionChanged)
        self.ui.btnNext2.clicked.connect(self.nextPage)

        # Connections and Slots for Tab3
        self.ui.lstResults.itemClicked.connect(self.openContainingFolder)

    def openContainingFolder(self, path):
        if platform.system() == "Windows":  # Windows
            subprocess.run(["explorer", "/select,", path.text()])
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "-R", path.text()])

    def addDir(self):
        folderPath = QFileDialog.getExistingDirectory(self)
        self.dirListItemSet.add(folderPath)
        self.ui.lstDir.clear()
        self.ui.lstDir.addItems(self.dirListItemSet)
        self.updateNextButtonState()

    def removeDir(self):
        selectedItems = self.ui.lstDir.selectedItems()
        self.dirListItemSet -= set(item.text() for item in selectedItems)
        self.ui.lstDir.clear()
        self.ui.lstDir.addItems(self.dirListItemSet)
        self.updateNextButtonState()

    def listSelectionChanged(self):
        if self.ui.lstDir.selectedItems():
            self.ui.btnRmDir.setEnabled(True)
        else:
            self.ui.btnRmDir.setEnabled(False)

    def updateNextButtonState(self):
        if len(self.dirListItemSet) > 0:
            self.ui.btnNext2.setEnabled(True)
        else:
            self.ui.btnNext2.setEnabled(False)

    def initiateSearch(self):
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(len(self.dirListItemSet))
        self.ui.progressBar.setValue(0)
        progress = 0
        self.resListItemSet.clear()

        for dir in self.dirListItemSet:
            res = DeepFace.find(
                img_path=self.searchFacePath, db_path=dir, model_name="Facenet512"
            )
            progress += 1
            self.ui.progressBar.setValue(progress)
            for value in res[0]["identity"].values:
                self.resListItemSet.add(value)

        # TODO: Disable ds_facenet512_opencv_v2.pkl generation by adding db_path in the find param

        self.ui.lstResults.clear()
        self.ui.lstResults.addItems(sorted(self.resListItemSet))

    def nextPage(self):
        current = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.setTabEnabled(current + 1, True)
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
