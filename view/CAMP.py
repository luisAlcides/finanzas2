from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_fields


class CAMP:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/CAMP.ui')
        self.ui.showMaximized()
        self.datos_tabla_pdf = []
        self.se_calculo = False
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        self.datos_tabla_pdf = []

        fields = [
            [self.ui.txt_rf, 'number', "Rf"],
            [self.ui.txt_bj, 'number', "β"],
            [self.ui.txt_km, 'number', "Km"]
        ]
        if not validate_fields(fields):
            return

        rf = float(self.ui.txt_rf.text())
        bj = float(self.ui.txt_bj.text())
        km = float(self.ui.txt_km.text())
        kmrf = km - rf

        ki = rf + (bj * kmrf)

        ki_porcentaje = ki * 100
        rf_porcentaje = rf * 100
        km_porcentaje = km * 100
        kmrf_porcentaje = kmrf * 100
        bj_kmrf_porcentaje = (bj * kmrf) * 100

        digito_select = self.ui.cb_digitos.currentText()

        if digito_select == 'Todos':
            digito_select = '50'
        else:
            if digito_select != 'Digitos':
                digito_select = self.ui.cb_digitos.currentText()
            else:
                digito_select = '2'


        resultado = [
            [ki_porcentaje, "Ki",'Rendimiento Requerido del Activo (CAPM)', True, True, digito_select],
            [rf_porcentaje, "Rf",'Tasa de rendimiento libre de riesgo', False, True, digito_select],
            [bj, 'β','Coeficiente beta', False, False, digito_select],
            [km_porcentaje,"Km",'Rendimiento del mercado', False, True, digito_select],
            [kmrf_porcentaje, "Km - Rf",'Prima de riesgo del mercado', False, True, digito_select],
            [bj_kmrf_porcentaje, "β * (Km - Rf)",'Prima de riesgo del activo', True, True, digito_select]
        ]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.datos_tabla_pdf.append(['Variable', 'Descripción', 'Valor'])
        self.datos_tabla_pdf.append(['Ki', 'Rendimiento Requerido del Activo (CAPM)', ki_porcentaje])
        self.datos_tabla_pdf.append(['Rf', 'Tasa de rendimiento libre de riesgo', rf_porcentaje])
        self.datos_tabla_pdf.append(['β', 'Coeficiente beta', bj])
        self.datos_tabla_pdf.append(['Km', 'Rendimiento del mercado', km_porcentaje])
        self.datos_tabla_pdf.append(['Km - Rf', 'Prima de riesgo del mercado', kmrf_porcentaje])
        self.datos_tabla_pdf.append(['β * (Km - Rf)', 'Prima de riesgo del activo', bj_kmrf_porcentaje])
        self.se_calculo = True
    def limpiar(self):
        fields = [
            self.ui.txt_rf,
            self.ui.txt_bj,
            self.ui.txt_km
        ]
        for field in fields:
            field.clear()
        self.ui.tb_resultado.clear()


    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('CAMP', self.datos_tabla_pdf)
        else:
            message('No se ha realizado ningún cálculo')


