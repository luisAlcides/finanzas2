import numpy as np
from PyQt6 import uic
from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields


class Varianza():
    def __init__(self):
        self.ui = uic.loadUi('view/ui/varianza.ui')
        self.ui.showMaximized()
        self.se_calculo = False
        self.datos_tabla_pdf = []
        self.other_tabla_pdf = []
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []
        self.other_tabla_pdf = []

        fields = [[self.ui.txt_xi, 'array', 'xi']]

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

        xi_con_coma = self.ui.txt_xi.text().strip().split(',')
        xi = [float(i) for i in xi_con_coma]
        media = np.mean(xi)
        xi_menos_media = [np.power((i - media), 2) for i in xi]
        var_muestra = np.var(xi, ddof=0)
        var_poblacion = np.var(xi, ddof=1)

        resultado = [[var_muestra, "Var", "Varianza Muestra", False, False, digito_select],
                     [var_poblacion, "Var", "Varianza Población", False, False, digito_select]]
        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['Var', 'Varianza Muestra', var_muestra])
        self.datos_tabla_pdf.append(['Var', 'Varianza Población', var_poblacion])

        self.other_tabla_pdf.append(['N°', 'xi', '$\bar{x}$', '(xi - $\bar{x}$)^2'])
        for i in range(len(xi)):
            self.other_tabla_pdf.append([i + 1, xi[i], media, xi_menos_media[i]])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_xi.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.other_tabla_pdf = []
        self.se_calculo = False

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Varianza', datos_tabla=self.datos_tabla_pdf, other_data=self.other_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
