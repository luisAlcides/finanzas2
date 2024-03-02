import math
import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import uic

from utils.util import mostrar_resultado, generar_pdf_dialogo


class DesviacionEstandar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('view/ui/desviacionEstandar.ui', self)
        self.showMaximized()
        self.datos_tabla_pdf = []
        self.other_data_pdf = []
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):
        ri_con_comas = self.ui.txt_ri.text()
        ri_str = ri_con_comas.split(',')
        ri = [float(number) for number in ri_str]
        miu = float(self.ui.txt_miu.text())
        des = []
        ri_miu = []
        for i in range(0, len(ri)):
            operacion = math.pow((ri[i] - miu), 2)
            des.append(operacion)
            ri_miu.append(operacion)
        N = (len(ri) - 1)
        des = sum(des) / N
        des = math.sqrt(des)
        resultado = [
            [des, "σ", "Desviación estándar", False, False],
        ]

        mostrar_resultado(resultado, self.ui.tb_resultado)
        self.graficar_desviacion_estandar(ri, des, miu)

        self.datos_tabla_pdf.append(['N°', 'ri', 'µ', '(ri - µ)^2'])
        for i in range(len(ri)):
            self.datos_tabla_pdf.append([i + 1, ri[i], miu, ri_miu[i]])
        self.other_data_pdf.append(['Variable', 'Descripcion', 'Valor'])
        self.other_data_pdf.append(['σ', 'Desviación estándar', des])

    def limpiar(self):
        self.ui.txt_ri.clear()
        self.ui.txt_miu.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.other_data_pdf = []

    def graficar_desviacion_estandar(self, ri, desviacion_estandar, miu):
        x = np.arange(len(ri))

        plt.figure(figsize=(10, 5))
        plt.plot(x, ri, label='Rendimientos (ri)', marker='o', linestyle='-')
        plt.axhline(y=miu, color='r', linestyle='--', label='Media (µ)')

        plt.title('Desviación Estándar de Rendimientos')
        plt.xlabel('Observaciones')
        plt.ylabel('Rendimientos')
        plt.legend()
        plt.savefig('desviacion_estandar.png')
        plt.show()

    def generate_pdf(self):
        generar_pdf_dialogo('Desviación Estándar', self.datos_tabla_pdf, 'desviacion_estandar.png', self.other_data_pdf)
