from PyQt6 import uic

from view.financiamientoConAccionesComunes import FinanciamientoConAccionesComunes
from view.financiamientoConDeuda import FinanciamientoConDeuda
from view.rendimientoEsperado import RendimientoEsperado


class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/ui/mainWindow.ui')
        self.ui.showMaximized()

        self.ui.qa_financiamiento_con_deuda.triggered.connect(self.openFinanciamientoConDeuda)
        self.ui.qa_financiamiento_con_acciones_comunes.triggered.connect(self.openFinanciamientoConAccionesComunes)
        self.ui.qa_rendimiento_esperado.triggered.connect(self.openRendimientoEsperado)

    def openFinanciamientoConDeuda(self):
        self.financiamiento_con_deuda = FinanciamientoConDeuda()
        return self.financiamiento_con_deuda

    def openFinanciamientoConAccionesComunes(self):
        self.financiamiento_con_acciones_comunes = FinanciamientoConAccionesComunes()
        return self.financiamiento_con_acciones_comunes

    def openRendimientoEsperado(self):
        self.rendimiento_esperado = RendimientoEsperado()
        return self.rendimiento_esperado
