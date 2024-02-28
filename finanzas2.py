from PyQt6.QtWidgets import QApplication

from view.mainWindow import MainWindow


class Finanzas2():
    def __init__(self):
        self.app = QApplication([])
        self.main = MainWindow()
        self.app.exec()