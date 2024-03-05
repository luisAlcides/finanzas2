import os

from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/rendimientoEsperado.ui')


class RendimientoEsperado:
    def __init__(self):
        self.ui = uic.loadUi(ruta_ui)
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
            [self.ui.txt_p0, 'number', "P0"],
            [self.ui.txt_g, 'number', "g"],
        ]

        if not validate_fields(fields):
            return

        Div1 = float(self.ui.txt_div1.text().strip())
        P0 = float(self.ui.txt_p0.text().strip())
        g = float(self.ui.txt_g.text().strip())

        rE = (Div1 / P0) + g
        rE = rE * 100

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [
            [rE, "rE", "Rendimiento Esperado", True, True, digito_select],
            [Div1, "Div1", "Dividendos", False, False, digito_select],
            [P0, "P0", "Precio de la acción hoy", False, False, digito_select],
            [g, "g", "Tasa de crecimiento", False, False, digito_select]
        ]
        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['rE', 'Rendimiento Esperado', rE])
        self.datos_tabla_pdf.append(['Div1', 'Dividendos', Div1])
        self.datos_tabla_pdf.append(['P0', 'Precio de la acción hoy', P0])
        self.datos_tabla_pdf.append(['g', 'Tasa de crecimiento', g])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_div1.clear()
        self.ui.txt_p0.clear()
        self.ui.txt_g.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Rendimiento Esperado', datos_tabla=self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
