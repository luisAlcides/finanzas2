from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields


class ModeloCrecimientoConstanteDividendo:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/modeloCrecimientoConstanteDividendo.ui')
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []
        fields = [
            [self.ui.txt_D1, 'number', "D1"],
            [self.ui.txt_r, 'number', "r"],
            [self.ui.txt_g, 'number', "g"],
        ]

        if not validate_fields(fields):
            return

        D1 = float(self.ui.txt_D1.text().strip())
        r = float(self.ui.txt_r.text().strip())
        g = float(self.ui.txt_g.text().strip())

        P0 = D1 / (r - g)
        r = r * 100
        g = g * 100

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [[P0, "P0", "Precio actual de la acción", True, False, digito_select],
                     [D1, "D1", "Dividendo esperado en el próximo año", False, False, digito_select],
                     [r, "r", "Tasa de rendimiento requerida", False, True, digito_select],
                     [g, "g", "Tasa de crecimiento constante de los dividendos", False, True, digito_select]]
        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['P0', 'Precio actual de la acción', P0])
        self.datos_tabla_pdf.append(['D1', 'Dividendo esperado en el próximo año', D1])
        self.datos_tabla_pdf.append(['r', 'Tasa de rendimiento requerida', r])
        self.datos_tabla_pdf.append(['g', 'Tasa de crecimiento constante de los dividendos', g])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_D1.clear()
        self.ui.txt_r.clear()
        self.ui.txt_g.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)


    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Modelo del crecimiento constante del dividendo', datos_tabla=self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')