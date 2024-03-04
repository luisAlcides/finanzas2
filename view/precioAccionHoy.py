from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields


class PrecioAccionHoy:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/precioAccionHoy.ui')
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []
        fields = [
            [self.ui.txt_div1, 'number', "D1"],
            [self.ui.txt_p1, 'number', "P1"],
            [self.ui.txt_re, 'number', "rE"],
        ]

        if not validate_fields(fields):
            return

        Div1 = float(self.ui.txt_div1.text().strip())
        P1 = float(self.ui.txt_p1.text().strip())
        re = float(self.ui.txt_re.text().strip())

        dividendo = Div1 + P1
        divisor = 1 + re
        P0 = dividendo / divisor

        rd = Div1 / P0
        ganancia_capital_esperada = P1 - P0
        tasa_ganancia = ganancia_capital_esperada / P0

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[P0, "P0", "Precio de la acción hoy", True, False, digito_select],
                     [Div1, "Div1", "Dividendos", False, False, digito_select],
                     [P1, "P1", "Precio de acción", False, False, digito_select],
                     [(re * 100), "rE", "Rendimiento Esperado", False, True, digito_select],
                     [(rd * 100), "rd", "Rendimiento por Dividendo", False, True, digito_select],
                     [ganancia_capital_esperada, "ge", "Ganancia Capital Esperada", False, False,
                      digito_select],
                     [(tasa_ganancia * 100), "tg", "Tasa de Ganancia", False, True, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['P0', 'Precio de la acción hoy', P0])
        self.datos_tabla_pdf.append(['Div1', 'Dividendos', Div1])
        self.datos_tabla_pdf.append(['P1', 'Precio de acción', P1])
        self.datos_tabla_pdf.append(['rE', 'Rendimiento Esperado', re])
        self.datos_tabla_pdf.append(['rd', 'Rendimiento por Dividendo', rd])
        self.datos_tabla_pdf.append(['ge', 'Ganancia Capital Esperada', ganancia_capital_esperada])
        self.datos_tabla_pdf.append(['tg', 'Tasa de Ganancia', tasa_ganancia])
        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_div1.clear()
        self.ui.txt_re.clear()
        self.ui.txt_p1.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Precio de la acción hoy (P0)', datos_tabla=self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
