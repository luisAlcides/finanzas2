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
        self.fields = [[self.ui.txt_ingresos,'number', self.ui.lbl_ingresos],
                  [self.ui.txt_pagos,'number', self.ui.lbl_pagos],
                  ]

        if not validate_fields(self.fields):
            return False

        ingresos = float(self.ui.txt_ingresos.text())
        pagos = float(self.ui.txt_pagos.text())
        resultado = ingresos - pagos
        self.ui.lbl_response.setText(f'Flujo de efectivo de financiamiento: {resultado}')


    def limpiar(self):
        clean_fields(self.fields)
        self.ui.lbl_response.setText('')