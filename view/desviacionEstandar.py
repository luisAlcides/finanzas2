import math
import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout
from PyQt6 import uic
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from utils.util import mostrar_resultado, generar_pdf_dialogo, message
from utils.validation import validate_array, validate_fields


class DesviacionEstandar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('view/ui/desviacionEstandar.ui', self)
        self.showMaximized()
        self.se_calculo = False
        self.datos_tabla_pdf = []
        self.other_data_pdf = []
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_generar_pdf.clicked.connect(self.generate_pdf)

    def resolver(self):

        if not validate_array(self.ui.txt_ri, 'Rendimientos'):
            return

        if not validate_fields([[self.ui.txt_miu, 'number', 'Media (µ)']]):
            return

        ri_con_comas = self.ui.txt_ri.text()
        ri_str = ri_con_comas.split(',')
        ri = [float(number) for number in ri_str]
        miu = float(self.ui.txt_miu.text())
        des = []
        ri_miu = []
        try:
            for i in range(0, len(ri)):
                operacion = math.pow((ri[i] - miu), 2)
                des.append(operacion)
                ri_miu.append(operacion)
            N = (len(ri) - 1)
            des = sum(des) / N
            des = math.sqrt(des)
        except ZeroDivisionError:
            message('Rendimientos debe ser un array ejemplo: 1,2,3')
            self.limpiar()
            return
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
        self.se_calculo = True

    def limpiar(self):
        self.ui.txt_ri.clear()
        self.ui.txt_miu.clear()
        self.ui.tb_resultado.clear()
        self.datos_tabla_pdf = []
        self.other_data_pdf = []
        self.se_calculo = False

        if self.ui.widgetGrafico.layout() is not None:
            while self.ui.widgetGrafico.layout().count():
                child = self.ui.widgetGrafico.layout().takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()

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

        # Crea la figura y el eje para el gráfico
        fig = Figure(figsize=(10, 5))
        ax = fig.add_subplot(111)

        # Generar los datos para el gráfico
        x = np.arange(len(ri))
        ax.plot(x, ri, 'o-', label='Rendimientos (ri)')
        ax.axhline(y=miu, color='r', linestyle='--', label='Media (µ)')

        # Configuraciones del gráfico
        ax.set_title('Desviación Estándar de Rendimientos')
        ax.set_xlabel('Observaciones')
        ax.set_ylabel('Rendimientos')
        ax.legend()

        # Comprueba si el QWidget tiene ya un layout; si no, crea uno nuevo
        if self.ui.widgetGrafico.layout() is None:
            layout = QVBoxLayout(self.ui.widgetGrafico)
            self.ui.widgetGrafico.setLayout(layout)
        else:
            # Limpia el layout existente
            while self.ui.widgetGrafico.layout().count():
                child = self.ui.widgetGrafico.layout().takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Incrusta el gráfico y la barra de herramientas en el QWidget
        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, self)
        self.ui.widgetGrafico.layout().addWidget(toolbar)
        self.ui.widgetGrafico.layout().addWidget(canvas)

    def generate_pdf(self):
        if self.se_calculo:
            generar_pdf_dialogo('Desviación Estándar', self.datos_tabla_pdf, 'desviacion_estandar.png',
                                self.other_data_pdf)
        else:
            message('No se ha realizado ningún cálculo')
