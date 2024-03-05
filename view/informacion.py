from PyQt6 import uic

class Informacion:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/informacion.ui')
        self.ui.show()

