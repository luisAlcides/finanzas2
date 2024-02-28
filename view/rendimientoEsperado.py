from PyQt6 import uic


class RendimientoEsperado:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/rendimientoEsperado.ui')
        self.ui.show()