from PyQt6 import uic

from view.financiamientoConDeuda import FinanciamientoConDeuda
from view.rendimientoEsperado import RendimientoEsperado


class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/ui/mainWindow.ui')
        self.ui.showMaximized()

        self.ui.qa_financiamiento_con_deuda.triggered.connect(self.openFinanciamientoConDeuda)
        self.ui.qa_rendimiento_esperado.triggered.connect(self.openRendimientoEsperado)

    def openFinanciamientoConDeuda(self):
        self.financiamiento_con_deuda = FinanciamientoConDeuda()
        return self.financiamiento_con_deuda

    def openRendimientoEsperado(self):
        self.rendimiento_esperado = RendimientoEsperado()
        return self.rendimiento_esperado
