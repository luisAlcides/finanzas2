import os

from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

import numpy_financial as npf


ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/VPN.ui')


class VPN:
    def __init__(self):
        self.ui = uic.loadUi(ruta_ui)
        self.ui.showMaximized()
        self.datos_tabla_pdf = []
        self.other_data_pdf = []
        self.se_calculo = False
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []
        self.other_data_pdf = []

        fields = [
            [self.ui.txt_ct, 'array', "Ct"],
            [self.ui.txt_i, 'number', "i"]
        ]
        if not validate_fields(fields):
            return

        ct_con_comas = self.ui.txt_ct.text().strip().split(',')
        ct = [float(number) for number in ct_con_comas]
        i = float(self.ui.txt_i.text().strip())
        ct_values = []
        n = 0

        for j in range(len(ct)):
            n = j
            ct_values.append(npf.pv(rate=i, nper=n, pmt=0, fv=-ct[j]))

        VPN = npf.npv(i, ct)

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[VPN, 'VP', 'Valor presente', True, False, digito_select],
                     [(i * 100), 'i', 'Tasa de interés', False, True, digito_select],
                     [n, 'n', 'Número de periodos', False, False, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['VPN', 'Valor presente', VPN])
        self.datos_tabla_pdf.append(['i', 'Tasa de interés', i])
        self.datos_tabla_pdf.append(['n', 'Número de periodos', n])

        self.other_data_pdf.append(
            ['Año', 'Flujo de Caja','Valor Presente', 'Valor Presente Acumulado'])

        valor_presente_acumulado = 0
        for j in range(len(ct)):
            if j == 0:
                factor_descuento = 1
            else:
                factor_descuento = (1 + i) ** j

            valor_presente = ct[j] / factor_descuento
            valor_presente_acumulado += valor_presente

            self.other_data_pdf.append([str(j), str(ct[j]),valor_presente,
                                        valor_presente_acumulado])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_ct.clear()
        self.ui.txt_i.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.other_data_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('Valor Presente Neto',
                                datos_tabla=self.datos_tabla_pdf, other_data=self.other_data_pdf)
        else:
            message('No se ha realizado ningún cálculo')
