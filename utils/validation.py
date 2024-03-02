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
                table += f"<tr><td class='highlighted'>{fields[i][1]}</td><td class='highlighted'>{fields[i][2]}</td><td class='highlighted'>{fields[i][0]:.4f}%</td></tr>"
            else:
                table += f"<tr><td>{fields[i][1]}</td><td>{fields[i][2]}</td><td>{fields[i][0]:.4f}%</td></tr>"
        else:
            if fields[i][3]:
                table += f"<tr><td class='highlighted'>{fields[i][1]}</td><td class='highlighted'>{fields[i][2]}</td><td class='highlighted'>{fields[i][0]:.4f}</td></tr>"
            else:
                table += f"<tr><td>{fields[i][1]}</td><td>{fields[i][2]}</td><td>{fields[i][0]:.4f}</td></tr>"

    table += "</table>"

    tb_resultado.setHtml(style + table)




def mostrar_resultado_tablas(datos_listas, tb_resultado, *nombres_columnas):
    tb_resultado.clear()
    style = """
    <style>
    table { border-collapse: collapse; width: 100%; }
    th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
    th { background-color: #f2f2f2; }
    tr:hover { background-color: #f5f5f5; }
    .highlighted { background-color: #BFDA7F; }
    </style>
    """

    # Genera las cabeceras de la tabla dinámicamente basadas en nombres_columnas
    table = "<table><tr><th>N°</th>"
    for nombre in nombres_columnas:
        table += f"<th>{nombre}</th>"
    table += "</tr>"

    # Asume que todas las listas tienen la misma longitud
    for i in range(len(datos_listas[0])):
        table += f"<tr><td>{i + 1}</td>"
        for lista in datos_listas:
            try:
                number = float(lista[i])
                table += f"<td>{number:.2f}</td>"
            except ValueError:
                table += "<td>NA</td>"
        table += "</tr>"

    table += "</table>"

    tb_resultado.setHtml(style + table)