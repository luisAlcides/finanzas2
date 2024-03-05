from PyQt6 import uic

class AcercaDe:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/acercade.ui')
        self.ui.show()
