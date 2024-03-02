from PyQt6 import uic

from utils.util import mostrar_resultado, mostrar_resultado_tablas
from utils.validation import validate_fields


class RendimientoEsperadoMultiple:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/rendimientoEsperadoMultiple.ui')
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        pij_con_comas = self.ui.txt_pij.text()
        rij_con_comas = self.ui.txt_rij.text()
        pij_str = pij_con_comas.split(',')
        rij_str = rij_con_comas.split(',')
        pij = [float(number) for number in pij_str]
        rij = [float(number) for number in rij_str]
        eri = []
        for i in range(0, len(pij)):
            eri.append(pij[i] * rij[i])

        eri = sum(eri)
        eri = eri * 100
        resultado = [
            [eri, "ERi", "Rendimiento esperado de la cartera", True, True],
        ]

        datos_pij_rij = [pij, rij]
        mostrar_resultado(resultado, self.ui.tb_resultado)
        mostrar_resultado_tablas(datos_pij_rij, self.ui.tb_tablas, 'pij', 'rij')

    def limpiar(self):
        self.ui.txt_pij.clear()
        self.ui.txt_rij.clear()
        self.ui.tb_resultado.clear()
        self.ui.tb_tablas.clear()
