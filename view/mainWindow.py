import os

from PyQt6 import uic

from view.TIR import TIR
from view.TMAR import TMAR
from view.VF import VF
from view.VP import VP
from view.VPF import VPF
from view.VPN import VPN
from view.acercaDe import AcercaDe
from view.capitalMarketLine import CapitalMarketLine
from view.correlacion import Correlacion
from view.financiamientoAccionesPreferentes import FinanciamientoAccionesPreferentes
from view.CAMP import CAMP
from view.covarianza import Covarianza
from view.desviacionEstandar import DesviacionEstandar
from view.financiamientoConDeuda import FinanciamientoConDeuda
from view.informacion import Informacion
from view.modeloCrecimientoConstanteDividendo import ModeloCrecimientoConstanteDividendo
from view.precioAccionHoy import PrecioAccionHoy
from view.rendimientoEsperado import RendimientoEsperado
from view.rendimientoEsperadoMultiple import RendimientoEsperadoMultiple
from view.rendimientoRequerido import RendimientoRequerido
from view.securityMarketLine import SecurityMarketLine
from view.varianza import Varianza


ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/mainWindow.ui')
class MainWindow():
    def __init__(self):
        self.ui = uic.loadUi(ruta_ui)
        self.ui.showMaximized()

        self.ui.qa_financiamiento_con_deuda.triggered.connect(self.openFinanciamientoConDeuda)
        self.ui.qa_CAMP.triggered.connect(self.openCAMP)
        self.ui.qa_financiamiento_acciones_preferentes.triggered.connect(self.financiamientoAccionesPreferentes)
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
        self.ui.qa_VP.triggered.connect(self.openVP)
        self.ui.qa_VPF.triggered.connect(self.openVPF)
        self.ui.qa_VPN.triggered.connect(self.openVPN)
        self.ui.qa_VF.triggered.connect(self.openVF)
        self.ui.qa_TIR.triggered.connect(self.openTIR)
        self.ui.qa_TMAR.triggered.connect(self.openTMAR)
        self.ui.qa_informacion.triggered.connect(self.openInformacion)
        self.ui.qa_acerca.triggered.connect(self.openAcercaDe)

    def openFinanciamientoConDeuda(self):
        self.financiamiento_con_deuda = FinanciamientoConDeuda()
        return self.financiamiento_con_deuda

    def openCAMP(self):
        self.camp = CAMP()
        return self.camp

    def financiamientoAccionesPreferentes(self):
        self.financiamiento_acciones_preferentes = FinanciamientoAccionesPreferentes()
        return self.financiamiento_acciones_preferentes

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

    def openVP(self):
        self.vp = VP()
        return self.vp

    def openVPF(self):
        self.vpf = VPF()
        return self.vpf

    def openVPN(self):
        self.vpn = VPN()
        return self.vpn

    def openVF(self):
        self.vf = VF()
        return self.vf

    def openTIR(self):
        self.tir = TIR()
        return self.tir


    def openTMAR(self):
        self.tmar = TMAR()
        return self.tmar

    def openInformacion(self):
        self.informacion = Informacion()
        return self.informacion

    def openAcercaDe(self):
        self.acerca_de = AcercaDe()
        return self.acerca_de