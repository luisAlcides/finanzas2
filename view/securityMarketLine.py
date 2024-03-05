import os

from PyQt6 import uic
from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields

ruta_ui = os.path.join(os.path.dirname(__file__), 'ui/securityMarketLine.ui')


class SecurityMarketLine():
    def __init__(self):
        self.ui = uic.loadUi(ruta_ui)
        self.ui.showMaximized()
        self.se_calculo = False
        self.datos_tabla_pdf = []
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []
        fields = [[self.ui.txt_rf, 'number', 'Rf'],
                  [self.ui.txt_erm, 'number', 'E(Rm)'],
                  [self.ui.txt_bi, 'number', 'βi']]

        if not validate_fields(fields):
            return

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        rf = float(self.ui.txt_rf.text().strip())
        erm = float(self.ui.txt_erm.text().strip())
        bi = float(self.ui.txt_bi.text().strip())

        ri = rf + bi * (erm - rf)

        resultado = [[rf, "Rf", "Tasa de retorno libre de riesgo", False, False, digito_select],
                     [erm, "E(Rm)", "Rendimiento esperado del mercado", False, False, digito_select],
                     [bi, "βi", "Beta", False, False, digito_select],
                     [(ri * 100), "Ri", "Rendimiento esperado", True, True, digito_select],
                     ]
        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['Rf', 'Tasa de retorno libre de riesgo', rf])
        self.datos_tabla_pdf.append(['E(Rm)', 'Rendimiento esperado del mercado', erm])
        self.datos_tabla_pdf.append(['βi', 'Beta', bi])
        self.datos_tabla_pdf.append(['Ri', 'Rendimiento esperado', ri])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_rf.clear()
        self.ui.txt_erm.clear()
        self.ui.txt_bi.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('Security Market Line', self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
