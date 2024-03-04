import numpy as np
from PyQt6 import uic
from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields


class Covarianza():
    def __init__(self):
        self.ui = uic.loadUi('view/ui/covarianza.ui')
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

        fields = [[self.ui.txt_xi, 'array', 'xi'],
                  [self.ui.txt_yi, 'array', 'yi']]

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
        yi_con_coma = self.ui.txt_yi.text().strip().split(',')
        yi = [float(i) for i in yi_con_coma]
        media_x = np.mean(xi)
        media_y = np.mean(yi)
        xi_menos_media = [i - media_x for i in xi]
        yi_menos_media = [i - media_y for i in yi]
        cov_muestra = np.cov(xi, yi, ddof=0)[0][1]
        cov_poblacion = np.cov(xi, yi, ddof=1)[0][1]

        resultado = [[cov_muestra, "Cov", "Covarianza Muestra", False, False, digito_select],
                     [cov_poblacion, "Cov", "Covarianza Población", False, False, digito_select]]
        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['Cov', 'Covarianza Muestra', cov_muestra])
        self.datos_tabla_pdf.append(['Cov', 'Covarianza Población', cov_poblacion])
        self.other_tabla_pdf.append(['N°', 'xi', 'yi', 'media_x', 'media_y', '(xi - media_x)', '(yi - media_y)'])
        for i in range(len(xi)):
            self.other_tabla_pdf.append([i + 1, xi[i], yi[i], media_x, media_y, xi_menos_media[i], yi_menos_media[i]])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_xi.clear()
        self.ui.txt_yi.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.other_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Covarianza', datos_tabla=self.datos_tabla_pdf, other_data=self.other_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')
