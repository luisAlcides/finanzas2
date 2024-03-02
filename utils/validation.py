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


def mostrar_resultado(fields, tb_resultado):
    tb_resultado.clear()
    style = "<style>"
    style += "table { border-collapse: collapse; width: 100%; }"
    style += "th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }"
    style += "th { background-color: #f2f2f2; }"
    style += "tr:hover { background-color: #f5f5f5; }"
    style += ".highlighted { background-color: #BFDA7F; }"
    style += "</style>"

    table = "<table>"
    table += "<tr><th>Variable</th><th>Nombre de la variable</th><th>Valor</th></tr>"
    for i in range(0, len(fields)):
        if fields[i][4]:
            if fields[i][3]:
                table += f"<tr><td class='highlighted'>{fields[i][1]}</td><td class='highlighted'>{fields[i][2]}</td><td class='highlighted'>{fields[i][0]:.2f}%</td></tr>"
            else:
                table += f"<tr><td>{fields[i][1]}</td><td>{fields[i][2]}</td><td>{fields[i][0]:.2f}%</td></tr>"
        else:
            if fields[i][3]:
                table += f"<tr><td class='highlighted'>{fields[i][1]}</td><td class='highlighted'>{fields[i][2]}</td><td class='highlighted'>{fields[i][0]:.2f}</td></tr>"
            else:
                table += f"<tr><td>{fields[i][1]}</td><td>{fields[i][2]}</td><td>{fields[i][0]:.2f}</td></tr>"

    table += "</table>"

    tb_resultado.setHtml(style + table)


def mostrar_resultado_tablas(datos, tb_resultado, column1, column2):
    tb_resultado.clear()
    style = "<style>"
    style += "table { border-collapse: collapse; width: 100%; }"
    style += "th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }"
    style += "th { background-color: #f2f2f2; }"
    style += "tr:hover { background-color: #f5f5f5; }"
    style += ".highlighted { background-color: #BFDA7F; }"
    style += "</style>"

    table = "<table>"
    table += f"<tr><th>N°</th><th>{column1}</th><th>{column2}</th></tr>"
    row1, row2 = datos
    for i in range(0, len(row1)):
        table += f"<tr><td>{i + 1}</td><td>{row1[i]:.2f}</td><td>{row2[i]:.2f}</td>"


    table += "</table>"

    tb_resultado.setHtml(style + table)