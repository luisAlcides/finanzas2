from PyQt6 import uic
from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields


class CapitalMarketLine():
    def __init__(self):
        self.ui = uic.loadUi('view/ui/capitalMarketLine.ui')
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
                  [self.ui.txt_des_m, 'number', 'σm'],
                  [self.ui.txt_des_p, 'number', 'σp']]

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
        des_m = float(self.ui.txt_des_m.text().strip())
        des_p = float(self.ui.txt_des_p.text().strip())

        rp = rf + ((erm - rf) / des_m) * des_p

        resultado = [[rf, "Rf", "Tasa de retorno libre de riesgo", False, False, digito_select],
                     [erm, "E(Rm)", "Rendimiento esperado del mercado", False, False, digito_select],
                     [des_m, "σm", "Desviación estándar del mercado", False, False, digito_select],
                     [des_p, "σp", "Desviación estándar de la cartera", False, False, digito_select],
                     [(rp * 100), "Rp", "Rendimiento esperado de cartera de inversiones", True, True, digito_select],
                     ]
        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['Rf', 'Tasa de retorno libre de riesgo', rf])
        self.datos_tabla_pdf.append(['E(Rm)', 'Rendimiento esperado del mercado', erm])
        self.datos_tabla_pdf.append(['σm', 'Desviación estándar del mercado', des_m])
        self.datos_tabla_pdf.append(['σp', 'Desviación estándar de la cartera', des_p])
        self.datos_tabla_pdf.append(['Rp', 'Rendimiento esperado de cartera de inversiones', rp])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_rf.clear()
        self.ui.txt_erm.clear()
        self.ui.txt_des_m.clear()
        self.ui.txt_des_p.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('Capital Market Line', self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
