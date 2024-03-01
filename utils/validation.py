from PyQt6.QtWidgets import QMessageBox, QLineEdit


def message(message):
    mBox = QMessageBox()
    mBox.setText(message)
    mBox.exec()


def validate_number(number, lbl):
    if not number.text():
        message(f'El campo {lbl} no puede estar vacio')
        number.setFocus()
        return False
    try:
        float(number.text())
    except ValueError:
        message(f'El campo {lbl} debe ser un número')
        number.setFocus()
        return False
    return True


def validate_fields(fields):
    for i in range(0, len(fields)):
        if fields[i][1] == 'number':
            if not validate_number(fields[i][0], fields[i][2]):
                return False
    return True


def clean_fields(fields):
    for i in range(0, len(fields)):
        if type(fields[i][0]) == QLineEdit:
            fields[i][0].setText('')
