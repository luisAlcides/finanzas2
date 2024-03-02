import math
import matplotlib.pyplot as plt
import numpy as np

from PyQt6 import uic

from utils.validation import mostrar_resultado, validate_fields, mostrar_resultado_tablas


class DesviacionEstandar:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/desviacionEstandar.ui')
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        ri_con_comas = self.ui.txt_ri.text()
        ri_str = ri_con_comas.split(',')
        ri = [float(number) for number in ri_str]
        miu = float(self.ui.txt_miu.text())
        des = []
        des_tabla = []
        for i in range(0, len(ri)):
            operacion = math.pow((ri[i] - miu), 2)
            des.append(operacion)
        N = (len(ri) - 1)
        des = sum(des) / N
        des = math.sqrt(des)
        resultado = [
            [des, "σ", "Desviación estándar", True, False],
        ]

        miu_tabla = [miu * 1 for i in range(0, len(ri))]
        datos_tabla = [ri, miu_tabla]
        mostrar_resultado(resultado, self.ui.tb_resultado)
        mostrar_resultado_tablas(datos_tabla, self.ui.tb_tablas, 'ri', 'µ')
        self.graficar_desviacion_estandar(ri, des, miu)

    def limpiar(self):
        self.ui.txt_ri.clear()
        self.ui.txt_miu.clear()
        self.ui.tb_resultado.clear()
        self.ui.tb_tablas.clear()

    def graficar_desviacion_estandar(self, ri, desviacion_estandar, miu):
        x = np.arange(len(ri))

        plt.figure(figsize=(10, 5))  # Tamaño del gráfico
        plt.plot(x, ri, label='Rendimientos (ri)', marker='o', linestyle='-')
        plt.axhline(y=miu, color='r', linestyle='--', label='Media (µ)')

        plt.title('Desviación Estándar de Rendimientos')
        plt.xlabel('Observaciones')
        plt.ylabel('Rendimientos')
        plt.legend()

        # Muestra el gráfico
        plt.show()
