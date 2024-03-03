from utils.util import message


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


def validate_array(fields, lbl):
    for i in range(0, len(fields.text().strip().split(','))):
        try:
            float(fields.text().strip().split(',')[i])
        except ValueError:
            message(f'El campo {lbl} debe ser un arreglo de números')
            return False
    return True
