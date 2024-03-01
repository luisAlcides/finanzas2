from PyQt6 import uic

from utils.validation import validate_fields


class CostoAccionesPreferentes:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/CostoAccionesPreferentes.ui')
        self.fields = None
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        fields = [
            [self.ui.txt_dp, 'number', "Dp"],
            [self.ui.txt_np, 'number', "Np"],
        ]

        if not validate_fields(fields):
            return

        dp = float(self.ui.txt_dp.text())
        np = float(self.ui.txt_np.text())

        kp = dp / np
        kp = kp * 100
        self.ui.tb_resultado.setText(f"Kp = {kp:.2f} %")

    def limpiar(self):
        self.ui.txt_dp.clear()
        self.ui.txt_np.clear()
        self.ui.tb_resultado.clear()
