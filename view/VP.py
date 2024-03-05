import os

from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

import numpy_financial as npf

ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/VP.ui')



class VP:
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
            [self.ui.txt_vf, 'number', "VF"],
            [self.ui.txt_i, 'number', "i"],
            [self.ui.txt_n, 'number', "n"]
        ]
        if not validate_fields(fields):
            return

        vf = float(self.ui.txt_vf.text().strip())
        i = float(self.ui.txt_i.text().strip())
        n = float(self.ui.txt_n.text().strip())

        vp = npf.pv(rate=i, nper=n,pmt=0, fv=vf)
        vp = vp * -1

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[vp, 'VP', 'Valor presente', True, False, digito_select],
                     [vf, 'VF', 'Valor futuro', False, False, digito_select],
                     [(i*100), 'i', 'Tasa de interés', False, True, digito_select],
                     [n, 'n', 'Número de periodos', False, False, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['VP', 'Valor presente', vp])
        self.datos_tabla_pdf.append(['VF', 'Valor futuro', vf])
        self.datos_tabla_pdf.append(['i', 'Tasa de interés', i])
        self.datos_tabla_pdf.append(['n', 'Número de periodos', n])
        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_vf.clear()
        self.ui.txt_i.clear()
        self.ui.txt_n.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('Valor Presente', self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
