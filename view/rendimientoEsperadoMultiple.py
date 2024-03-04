from PyQt6 import uic

from utils.util import mostrar_resultado, mostrar_resultado_tablas, generar_pdf_dialogo, message
from utils.validation import validate_fields


class RendimientoEsperadoMultiple:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/rendimientoEsperadoMultiple.ui')
        self.ui.showMaximized()
        self.datos_tabla_pdf = []
        self.other_tabla_pdf = []
        self.se_calculo = False
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.other_tabla_pdf = []
        self.datos_tabla_pdf = []

        fields = [[self.ui.txt_rij, 'array', 'Rendimientos Rij'],
                  [self.ui.txt_pij, 'array', 'Probabilidades Pij']]

        if not validate_fields(fields):
            return

        pij_con_comas = self.ui.txt_pij.text()
        rij_con_comas = self.ui.txt_rij.text()
        pij_str = pij_con_comas.split(',')
        rij_str = rij_con_comas.split(',')
        pij = [float(number) for number in pij_str]
        rij = [float(number) for number in rij_str]
        eri = []

        if len(pij) != len(rij):
            message('Las listas de rendimientos y probabilidades deben tener la misma longitud')
            return

        for i in range(0, len(pij)):
            eri.append(pij[i] * rij[i])

        eri = sum(eri)
        eri = eri * 100

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'

        resultado = [
            [eri, "ERi", "Rendimiento esperado de la cartera", True, True, digito_select],
        ]

        mostrar_resultado(resultado, self.ui.tb_resultado)

        self.datos_tabla_pdf = [['Variable', 'Descripción', 'Valor']]
        self.datos_tabla_pdf.append(['ERi', 'Probabilidad de ocurrencia', eri])

        self.other_tabla_pdf.append(['N°', 'Rendimientos Rij', 'Probabilidad Pij'])
        for i in range(0, len(pij)):
            self.other_tabla_pdf.append([i + 1, rij[i], pij[i]])

        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_pij.clear()
        self.ui.txt_rij.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.other_tabla_pdf = []
        self.se_calculo = False
        self.ui.cb_digitos.setCurrentIndex(0)


    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo(title='Rendimiento promedio de las acciones, probabilidad ocurrencia', datos_tabla=self.datos_tabla_pdf, other_data=self.other_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')