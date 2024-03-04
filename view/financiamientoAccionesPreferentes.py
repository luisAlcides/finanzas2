from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields


class FinanciamientoAccionesPreferentes:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/financiamientoAccionesPreferentes.ui')
        self.ui.showMaximized()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []
        fields = [
            [self.ui.txt_dp, 'number', "Dp"],
            [self.ui.txt_np, 'number', "Np"],
        ]

        if not validate_fields(fields):
            return

        dp = float(self.ui.txt_dp.text().strip())
        np = float(self.ui.txt_np.text().strip())

        kp = dp / np
        kp = kp * 100

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[kp, "Kp", "Costo de las acciones preferentes", True, True, digito_select],
                     [dp, "Dp", "Dividendos preferentes", False, False, digito_select],
                     [np, "Np", "Precio de las acciones preferentes", False, False, digito_select]]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['Kp', 'Costo de las acciones preferentes', kp])
        self.datos_tabla_pdf.append(['Dp', 'Dividendos preferentes', dp])
        self.datos_tabla_pdf.append(['Np', 'Precio de las acciones preferentes', np])
        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_dp.clear()
        self.ui.txt_np.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Financiamiento Acciones Preferentes', datos_tabla=self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
