from PyQt6 import uic

from utils.util import mostrar_resultado
from utils.validation import validate_fields


class CAMP:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/CAMP.ui')
        self.fields = None
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
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

        resultado = [
            [ki_porcentaje, "Ki",'Rendimiento Requerido del Activo (CAPM)', True, True],
            [rf_porcentaje, "Rf",'Tasa de rendimiento libre de riesgo', False, True],
            [bj, 'β','Coeficiente beta', False, False],
            [km_porcentaje,"Km",'Rendimiento del mercado', False, True],
            [kmrf_porcentaje, "Km - Rf",'Prima de riesgo del mercado', False, True],
            [bj_kmrf_porcentaje, "β * (Km - Rf)",'Prima de riesgo del activo', True, True]
        ]

        mostrar_resultado(resultado, self.ui.tb_resultado)


    def limpiar(self):
        fields = [
            self.ui.txt_rf,
            self.ui.txt_bj,
            self.ui.txt_km
        ]
        for field in fields:
            field.clear()
        self.ui.tb_resultado.clear()
