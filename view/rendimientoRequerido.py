import os

from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/rendimientoRequerido.ui')

class RendimientoRequerido:
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
            [self.ui.txt_r_real, 'number', "r*"],
            [self.ui.txt_ip, 'number', "IP"],
            [self.ui.txt_rpj, 'number', "RPj"],
        ]

        if not validate_fields(fields):
            return

        r_real = float(self.ui.txt_r_real.text().strip())
        IP = float(self.ui.txt_ip.text().strip())
        RPj = float(self.ui.txt_rpj.text().strip())

        rj = r_real + IP + RPj

        rj = rj * 100
        r_real = r_real * 100

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [
            [rj, "rj", "Rendimiento requerido sobre la inversión j", True, True, digito_select],
            [r_real, "r*", "Tasa de rendimiento real", False, True, digito_select],
            [IP, "IP", "Prima de inflación esperada", False, False, digito_select],
            [RPj, "RPj", "Prima de riesgo de la inversión j", False, False, digito_select]
        ]
        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['rj', 'Rendimiento requerido sobre la inversión j', rj])
        self.datos_tabla_pdf.append(['r*', 'Tasa de rendimiento real', r_real])
        self.datos_tabla_pdf.append(['IP', 'Prima de inflación esperada', IP])
        self.datos_tabla_pdf.append(['RPj', 'Prima de riesgo de la inversión j', RPj])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_r_real.clear()
        self.ui.txt_ip.clear()
        self.ui.txt_rpj.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Rendimiento Requerido', datos_tabla=self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
