from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

import numpy_financial as npf


class TIR:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/TIR.ui')
        self.ui.showMaximized()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []

        fields = [
            [self.ui.txt_ft, 'array', "Ft"],
        ]
        if not validate_fields(fields):
            return

        ft_con_comas = self.ui.txt_ft.text().strip().split(',')
        ft = [float(number) for number in ft_con_comas]

        tir = npf.irr(ft)

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[(tir * 100), 'TIR', 'Tasa Interna de Retorno', False, True, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['TIR', 'Tasa Interna de Retorno', tir])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_ft.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('TIR',
                                datos_tabla=self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
