from PyQt6 import uic

from utils.validation import validate_fields, clean_fields, mostrar_resultado


class FinanciamientoConDeuda:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/financiamentoConDeuda.ui')
        self.fields = None
        self.ui.showMaximized()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        fields = [
            [self.ui.txt_i, 'number', "Tasa de Interés Nominal (%)"],
            [self.ui.txt_tc, 'number', "Tasa Impositiva Corporativa (%)"],
            [self.ui.txt_principal, 'number', "Principal de la Deuda"],
            [self.ui.txt_ebit, 'number', "Ganancias antes de Intereses e Impuestos (EBIT)"]
        ]
        if not validate_fields(fields):
            return

        i = float(self.ui.txt_i.text())
        tc = float(self.ui.txt_tc.text())
        principal = float(self.ui.txt_principal.text())
        ebit = float(self.ui.txt_ebit.text())

        kd = i * (1 - tc)
        financial_charge = principal * i
        interest_coverage_ratio = ebit / financial_charge

        resultado = [[kd, 'kd',"Costo de la Deuda", False, False],
                     [financial_charge,'',"Carga Financiera", False, False],
                     [interest_coverage_ratio,'', "Índice de Cobertura de Intereses", False, False]]
        mostrar_resultado(resultado, self.ui.tb_resultado)

    def limpiar(self):
        fields = [
            self.ui.txt_i,
            self.ui.txt_tc,
            self.ui.txt_principal,
            self.ui.txt_ebit,
        ]
        for field in fields:
            field.clear()
        self.ui.tb_resultado.clear()
