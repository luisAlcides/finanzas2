from PyQt6 import uic

from utils.validation import validate_fields, clean_fields


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
        self.mostrar_resultado(ki_porcentaje, rf_porcentaje, bj, km_porcentaje, kmrf_porcentaje, bj_kmrf_porcentaje)

    def mostrar_resultado(self, ki, rf, bj, km, kmrf, bj_kmrf):
        self.ui.tb_resultado.clear()
        style = "<style>"
        style += "table { border-collapse: collapse; width: 100%; }"
        style += "th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }"
        style += "th { background-color: #f2f2f2; }"
        style += "tr:hover { background-color: #f5f5f5; }"
        style += ".highlighted { background-color: #ffe6e6; }"
        style += "</style>"

        table = "<table>"
        table += "<tr><th>Variable</th><th>Nombre de la variable</th><th>Valor</th></tr>"
        table += f"<tr><td>Ki</td><td>Rendimiento Requerido del Activo (CAPM)</td><td class='highlighted'>{ki:.2f}%</td></tr>"
        table += f"<tr><td>RF</td><td>Tasa de rendimiento libre de riesgo</td><td>{rf:.2f}%</td></tr>"
        table += f"<tr><td>bj</td><td>Coeficiente beta</td><td>{bj:.2f}</td></tr>"
        table += f"<tr><td>Km</td><td>Rendimiento del mercado</td><td>{km:.2f}%</td></tr>"
        table += f"<tr><td>Km – RF</td><td>Prima de riesgo del mercado</td><td>{kmrf:.2f}%</td></tr>"
        table += f"<tr><td>bj * (Km – RF)</td><td>Prima de riesgo del activo</td><td class='highlighted'>{bj_kmrf:.2f}%</td></tr>"
        table += "</table>"

        self.ui.tb_resultado.setHtml(style + table)

    def limpiar(self):
        fields = [
            self.ui.txt_rf,
            self.ui.txt_bj,
            self.ui.txt_km
        ]
        for field in fields:
            field.clear()
        self.ui.tb_resultado.clear()
