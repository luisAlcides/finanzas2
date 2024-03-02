from PyQt6 import uic

from utils.validation import mostrar_resultado, validate_fields


class RendimientoRequerido:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/rendimientoRequerido.ui')
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        fields = [
            [self.ui.txt_r_real, 'number', "r*"],
            [self.ui.txt_ip, 'number', "IP"],
            [self.ui.txt_rpj, 'number', "RPj"],
        ]

        if not validate_fields(fields):
            return

        r_real = float(self.ui.txt_r_real.text())
        IP = float(self.ui.txt_ip.text())
        RPj = float(self.ui.txt_rpj.text())

        rj = r_real + IP + RPj

        rj = rj * 100
        r_real = r_real * 100
        resultado = [
            [rj, "rj", "Rendimiento requerido sobre la inversión j", True, True],
            [r_real, "r*", "Tasa de rendimiento real", False, True],
            [IP, "IP", "Prima de inflación esperada", False, False],
            [RPj, "RPj", "Prima de riesgo de la inversión j", False, False]
        ]
        mostrar_resultado(resultado, self.ui.tb_resultado)

    def limpiar(self):
        self.ui.txt_r_real.clear()
        self.ui.txt_ip.clear()
        self.ui.txt_rpj.clear()
        self.ui.tb_resultado.clear()
