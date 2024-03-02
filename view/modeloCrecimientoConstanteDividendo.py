from PyQt6 import uic

from utils.util import mostrar_resultado
from utils.validation import validate_fields


class ModeloCrecimientoConstanteDividendo:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/modeloCrecimientoConstanteDividendo.ui')
        self.fields = None
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        fields = [
            [self.ui.txt_D1, 'number', "D1"],
            [self.ui.txt_r, 'number', "r"],
            [self.ui.txt_g, 'number', "g"],
        ]

        if not validate_fields(fields):
            return

        D1 = float(self.ui.txt_D1.text())
        r = float(self.ui.txt_r.text())
        g = float(self.ui.txt_g.text())

        P0 = D1 / (r - g)
        r = r * 100
        g = g * 100
        resultado = [[P0, "P0", "Precio actual de la acción", True, False],
                     [D1, "D1", "Dividendo esperado en el próximo año", False, False],
                     [r, "r", "Tasa de rendimiento requerida", False, True],
                     [g, "g", "Tasa de crecimiento constante de los dividendos", False, True]]
        mostrar_resultado(resultado, self.ui.tb_resultado)

    def limpiar(self):
        self.ui.txt_D1.clear()
        self.ui.txt_r.clear()
        self.ui.txt_g.clear()
        self.ui.tb_resultado.clear()
