from PyQt6 import uic

from view.capitalMarketLine import CapitalMarketLine
from view.correlacion import Correlacion
from view.costoAccionesPreferentes import CostoAccionesPreferentes
from view.CAMP import CAMP
from view.covarianza import Covarianza
from view.desviacionEstandar import DesviacionEstandar
from view.financiamientoConDeuda import FinanciamientoConDeuda
from view.modeloCrecimientoConstanteDividendo import ModeloCrecimientoConstanteDividendo
from view.precioAccionHoy import PrecioAccionHoy
from view.rendimientoEsperado import RendimientoEsperado
from view.rendimientoEsperadoMultiple import RendimientoEsperadoMultiple
from view.rendimientoRequerido import RendimientoRequerido
from view.securityMarketLine import SecurityMarketLine
from view.varianza import Varianza


class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi('view/ui/mainWindow.ui')
        self.ui.showMaximized()

        self.ui.qa_financiamiento_con_deuda.triggered.connect(self.openFinanciamientoConDeuda)
        self.ui.qa_CAMP.triggered.connect(self.openCAMP)
        self.ui.qa_costo_acciones_preferentes.triggered.connect(self.openCostoAccionesPreferentes)
        self.ui.qa_modelo_crecimiento_constante_dividendo.triggered.connect(
            self.openModeloCrecimientoConstanteDividendo)
        self.ui.qa_precio_accion_hoy.triggered.connect(self.openPrecioAccionHoy)
        self.ui.qa_rendimiento_esperado.triggered.connect(self.openRendimientoEsperado)
        self.ui.qa_rendimiento_requerido.triggered.connect(self.openRendimientoRequerido)
        self.ui.qa_rendimiento_esperado_multiple.triggered.connect(self.openRendimientoEsperadoMultiple)
        self.ui.qa_desviacion_estandar.triggered.connect(self.openDesviacionEstandar)
        self.ui.qa_correlacion.triggered.connect(self.openCorrelacion)
        self.ui.qa_capital_market_line.triggered.connect(self.openCapitalMarketLine)
        self.ui.qa_security_market_line.triggered.connect(self.openSecurityMarketLine)
        self.ui.qa_varianza.triggered.connect(self.openVarianza)
        self.ui.qa_covarianza.triggered.connect(self.openCovarianza)

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

    def openDesviacionEstandar(self):
        self.desviacion_estandar = DesviacionEstandar()
        return self.desviacion_estandar

    def openCorrelacion(self):
        self.correlacion = Correlacion()
        return self.correlacion

    def openCapitalMarketLine(self):
        self.capital_market_line = CapitalMarketLine()
        return self.capital_market_line

    def openSecurityMarketLine(self):
        self.security_market_line = SecurityMarketLine()
        return self.security_market_line

    def openVarianza(self):
        self.varianza = Varianza()
        return self.varianza

    def openCovarianza(self):
        self.covarianza = Covarianza()
        return self.covarianza