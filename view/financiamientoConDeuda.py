import os

from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/financiamentoConDeuda.ui')

class FinanciamientoConDeuda:
    def __init__(self):
        self.ui = uic.loadUi(ruta_ui)
        self.ui.showMaximized()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []

        fields = [
            [self.ui.txt_i, 'number', "Tasa de Interés Nominal (%)"],
            [self.ui.txt_tc, 'number', "Tasa Impositiva Corporativa (%)"],
            [self.ui.txt_principal, 'number', "Principal de la Deuda"]]
        if not validate_fields(fields):
            return

        i = float(self.ui.txt_i.text().strip())
        tc = float(self.ui.txt_tc.text().strip())
        principal = float(self.ui.txt_principal.text().strip())

        kd = i * (1 - tc)
        financial_charge = principal * (kd + 1)

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[(kd * 100), 'kd', "Costo de la Deuda", True, True, digito_select],
                     [financial_charge, '', "Carga Financiera", False, False, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['kd', 'Costo de la Deuda', kd])
        self.datos_tabla_pdf.append(['', 'Carga Financiera', financial_charge])
        self.datos_tabla_pdf.append(['', 'Principal de la Deuda', principal])
        self.datos_tabla_pdf.append(['i', 'Tasa de Interés Nominal', i])
        self.datos_tabla_pdf.append(['T', 'Tasa Impositiva Corporativa', tc])
        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_i.clear()
        self.ui.txt_tc.clear()
        self.ui.txt_principal.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Financiamiento con Deuda',
                                datos_tabla=self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
