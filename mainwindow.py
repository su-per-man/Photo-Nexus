# This Python file uses the following encoding: utf-8
import os
import sys
import subprocess
import platform
import threading
import queue

# import time

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QThread, Signal
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

        # Variables: Thread safe operation
        self.threads = []  # List to keep track of threads
        self.lock = threading.Lock()
        self.resQ = queue.Queue()

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.btnNext1.setEnabled(False)
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
        self.threads.clear()

        for dir in self.dirListItemSet:
            self.clearHistory(dir)
            worker = SearchFaceThread(self.searchFacePath, dir)
            worker.progress.connect(self.updateProgress)
            worker.result.connect(self.on_threads_finished)
            worker.finished.connect(worker.deleteLater)  # Ensure thread is cleaned up
            worker.start()
            self.threads.append(worker)  # Keep a reference to the thread


    def clearHistory(self, dir):
        files = os.listdir(dir)
        files_to_delete = [f for f in files if "ds_facenet512_opencv" in f and f.endswith(".pkl") and os.path.isfile(os.path.join(dir, f))]
        for f in files_to_delete:
            file_path = os.path.join(dir, f)
            os.remove(file_path)
            print("removed " + file_path)

    def updateProgress(self, increment):
        current_value = self.ui.progressBar.value()
        self.ui.progressBar.setValue(current_value + increment)

    def on_threads_finished(self, result):
        for value in result[0]["identity"]:
            self.resListItemSet.add(value)
        if (self.ui.progressBar.value() == len(self.dirListItemSet) - 1):  # Done with all threads
            for dir in self.dirListItemSet:
                self.clearHistory(dir)

            self.ui.lstResults.clear()
            self.ui.lstResults.addItems(sorted(self.resListItemSet, reverse=True))

    def nextPage(self):
        current = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.setTabEnabled(current + 1, True)
        self.ui.tabWidget.setCurrentIndex(current + 1)
        if current == 1:
            self.ui.lstResults.clear()
            self.initiateSearch()

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
            self.ui.btnNext1.setEnabled(True)


class SearchFaceThread(QThread):
    progress = Signal(int)
    result = Signal(object)

    def __init__(self, facePath, directory):
        super().__init__()
        self.facePath = facePath
        self.directory = directory

    def run(self):
        # simulate delay for demonstration time.sleep(10)
        try:
            res = DeepFace.find(
                img_path=self.facePath, db_path=self.directory, model_name="Facenet512", enforce_detection=False
            )
        except Exception as e:
            res = {"error": str(e)}
        self.result.emit(res)
        self.progress.emit(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
