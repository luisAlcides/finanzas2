from PyQt6 import uic

from utils.validation import validate_fields, clean_fields


class FinanciamientoConDeuda:
    def __init__(self):
        self.ui = uic.loadUi('view/ui/financiamentoConDeuda.ui')
        self.fields = None
        self.ui.show()
        self.ui.btn_calcular.clicked.connect(self.resolver)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)

    def resolver(self):
        fields = [
            [self.ui.lineEdit_interestRate, 'number', "Tasa de Interés Nominal (%)"],
            [self.ui.lineEdit_taxRate, 'number', "Tasa Impositiva Corporativa (%)"],
            [self.ui.lineEdit_debtPrincipal, 'number', "Principal de la Deuda"],
            [self.ui.lineEdit_ebit, 'number', "Ganancias antes de Intereses e Impuestos (EBIT)"]
        ]
        if not validate_fields(fields):
            return

        i = float(self.ui.lineEdit_interestRate.text())
        tc = float(self.ui.lineEdit_taxRate.text())
        principal = float(self.ui.lineEdit_debtPrincipal.text())
        ebit = float(self.ui.lineEdit_ebit.text())

        kd = i * (1 - tc)
        self.ui.label_result.setText(f'Costo de Deuda (kd): {kd}\n')

        financial_charge = principal * i
        self.ui.label_result.setText(
            self.ui.label_result.text() + f'Carga Financiera: {financial_charge}\n')

        interest_coverage_ratio = ebit / financial_charge
        self.ui.label_result.setText(
            self.ui.label_result.text() + f'Cobertura de Intereses: {interest_coverage_ratio:.2f}')

    def limpiar(self):
        fields = [
            self.ui.lineEdit_interestRate,
            self.ui.lineEdit_taxRate,
            self.ui.lineEdit_debtPrincipal,
            self.ui.lineEdit_ebit,
        ]
        for field in fields:
            field.clear()
        self.ui.label_result.clear()
