import os

from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/TMAR.ui')


class TMAR:
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
            [self.ui.txt_i, 'number', "i"],
            [self.ui.txt_f, 'number', "f"],
        ]
        if not validate_fields(fields):
            return

        i = float(self.ui.txt_i.text().strip())
        f = float(self.ui.txt_f.text().strip())

        tmar = i + f + (i * f)

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[tmar, 'TMAR', 'Tasa Mínima Aceptable de Rendimiento', False, False, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['TMAR', 'Tasa Mínima Aceptable de Rendimiento', tmar])
        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_f.clear()
        self.ui.txt_i.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('TMAR', self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
