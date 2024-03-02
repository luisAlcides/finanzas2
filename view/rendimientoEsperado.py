from PyQt6 import uic

from utils.validation import mostrar_resultado, validate_fields


class RendimientoEsperado:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/rendimientoEsperado.ui')
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        fields = [
            [self.ui.txt_div1, 'number', "D1"],
            [self.ui.txt_p0, 'number', "P0"],
            [self.ui.txt_g, 'number', "g"],
        ]

        if not validate_fields(fields):
            return

        Div1 = float(self.ui.txt_div1.text())
        P0 = float(self.ui.txt_p0.text())
        g = float(self.ui.txt_g.text())

        rE = (Div1 / P0) + g
        rE = rE * 100
        resultado = [
            [rE, "rE", "Rendimiento Esperado", True, True],
            [Div1, "Div1", "Dividendos", False, False],
            [P0, "P0", "Precio de la acción hoy", False, False],
            [g, "g", "Tasa de crecimiento", False, False]
        ]
        mostrar_resultado(resultado, self.ui.tb_resultado)

    def limpiar(self):
        self.ui.txt_div1.clear()
        self.ui.txt_p0.clear()
        self.ui.txt_g.clear()
        self.ui.tb_resultado.clear()
