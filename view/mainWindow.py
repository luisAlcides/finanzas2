from PyQt6 import uic

from view.costoAccionesPreferentes import CostoAccionesPreferentes
from view.CAMP import CAMP
from view.financiamientoConDeuda import FinanciamientoConDeuda
from view.modeloCrecimientoConstanteDividendo import ModeloCrecimientoConstanteDividendo
from view.precioAccionHoy import PrecioAccionHoy
from view.rendimientoEsperado import RendimientoEsperado
from view.rendimientoEsperadoMultiple import RendimientoEsperadoMultiple
from view.rendimientoRequerido import RendimientoRequerido


class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/ui/mainWindow.ui')
        self.ui.showMaximized()

        self.ui.qa_financiamiento_con_deuda.triggered.connect(self.openFinanciamientoConDeuda)
        self.ui.qa_CAMP.triggered.connect(self.openCAMP)
        self.ui.qa_costo_acciones_preferentes.triggered.connect(self.openCostoAccionesPreferentes)
        self.ui.qa_modelo_crecimiento_constante_dividendo.triggered.connect(self.openModeloCrecimientoConstanteDividendo)
        self.ui.qa_precio_accion_hoy.triggered.connect(self.openPrecioAccionHoy)
        self.ui.qa_rendimiento_esperado.triggered.connect(self.openRendimientoEsperado)
        self.ui.qa_rendimiento_requerido.triggered.connect(self.openRendimientoRequerido)
        self.ui.qa_rendimiento_esperado_multiple.triggered.connect(self.openRendimientoEsperadoMultiple)

    def openFinanciamientoConDeuda(self):
        self.financiamiento_con_deuda = FinanciamientoConDeuda()
        return self.financiamiento_con_deuda

    def openCAMP(self):
        self.camp = CAMP()
        return self.camp

    def openCostoAccionesPreferentes(self):
        self.costo_acciones_preferentes = CostoAccionesPreferentes()
        return self.costo_acciones_preferentes

    def openModeloCrecimientoConstanteDividendo(self):
        self.modelo_crecimiento_constante_dividendo = ModeloCrecimientoConstanteDividendo()
        return self.modelo_crecimiento_constante_dividendo

    def openPrecioAccionHoy(self):
        self.precio_accion_hoy = PrecioAccionHoy()
        return self.precio_accion_hoy

    def openRendimientoEsperado(self):
        self.rendimiento_esperado = RendimientoEsperado()
        return self.rendimiento_esperado

    def openRendimientoRequerido(self):
        self.rendimiento_requerido = RendimientoRequerido()
        return self.rendimiento_requerido

    def openRendimientoEsperadoMultiple(self):
        self.rendimiento_esperado_multiple = RendimientoEsperadoMultiple()
        return self.rendimiento_esperado_multiple