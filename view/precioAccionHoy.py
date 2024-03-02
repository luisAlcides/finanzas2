from PyQt6 import uic

from utils.validation import validate_fields, mostrar_resultado


class PrecioAccionHoy:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/precioAccionHoy.ui')
        self.fields = None
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        fields = [
            [self.ui.txt_div1, 'number', "D1"],
            [self.ui.txt_p1, 'number', "P1"],
            [self.ui.txt_re, 'number', "rE"],
        ]

        if not validate_fields(fields):
            return

        Div1 = float(self.ui.txt_div1.text())
        P1 = float(self.ui.txt_p1.text())
        re = float(self.ui.txt_re.text())

        dividendo = Div1 + P1
        divisor = 1 + re
        P0 = dividendo/divisor
        print(P0)

        resultado = [[P0, "P0", "Precio de la acción hoy", True, False],
                     [Div1, "Div1", "Dividendos", False, False],
                     [P1, "P1", "Precio de acción", False, False],
                     [re, "rE", "Rendimiento Esperado", False, False]]
        mostrar_resultado(resultado, self.ui.tb_resultado)

    def limpiar(self):
        self.ui.txt_div1.clear()
        self.ui.txt_re.clear()
        self.ui.txt_p1.clear()
        self.ui.tb_resultado.clear()
