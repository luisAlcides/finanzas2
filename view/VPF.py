import os

from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

import numpy_financial as npf

ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/VPF.ui')


class VPF:
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
            [self.ui.txt_ft, 'array', "Ft"],
            [self.ui.txt_i, 'number', "i"]
        ]
        if not validate_fields(fields):
            return

        ft_con_comas = self.ui.txt_ft.text().strip().split(',')
        ft = [float(number) for number in ft_con_comas]
        i = float(self.ui.txt_i.text().strip())
        ft_values = []
        n = 0

        for j in range(len(ft)):
            n = (j + 1)
            ft_values.append(npf.pv(rate=i, nper=n, pmt=0, fv=-ft[j]))

        vp = sum(ft_values)

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[vp, 'VP', 'Valor presente', True, False, digito_select],
                     [(i * 100), 'i', 'Tasa de interés', False, True, digito_select],
                     [n, 'n', 'Número de periodos', False, False, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['VP', 'Valor presente', vp])
        self.datos_tabla_pdf.append(['i', 'Tasa de interés', i])
        self.datos_tabla_pdf.append(['n', 'Número de periodos', n])

        self.other_data_pdf.append(['N°', 'flujos de caja', 'Sumatoria de flujos de caja'])
        for j in range(len(ft)):
            self.other_data_pdf.append([j + 1, ft[j], ft_values[j]])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_ft.clear()
        self.ui.txt_i.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.other_data_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('Valor Presente de una serie de flujos de caja',
                                datos_tabla=self.datos_tabla_pdf, other_data=self.other_data_pdf)
        else:
            message('No se ha realizado ningún cálculo')
