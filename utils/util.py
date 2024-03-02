import os

from PyQt6.QtWidgets import QMessageBox, QLineEdit, QFileDialog
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image


def message(message):
    mBox = QMessageBox()
    mBox.setText(message)
    mBox.exec()


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


def generar_pdf_dialogo(title, datos_tabla, grafica='', other_data=''):
    fileName, _ = QFileDialog.getSaveFileName(None, "Guardar reporte", "", "PDF Files (*.pdf)")
    if fileName:
        if not fileName.endswith('.pdf'):
            fileName += '.pdf'
        generar_pdf(fileName, title, datos_tabla, grafica, other_data)
    else:
        print("Generación de PDF cancelada.")


def generar_pdf(fileName, title, datos_tabla, grafica='', other_data=''):
    pdf = SimpleDocTemplate(fileName, pagesize=letter)
    flowables = []

    styles = getSampleStyleSheet()
    titulo = Paragraph(title, styles["Heading1"])
    flowables.append(titulo)

    tabla = Table(datos_tabla)



    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    tabla.setStyle(style)
    flowables.append(tabla)

    if other_data != '':
        tabla2 = Table(other_data)
        tabla2.setStyle(style)
        flowables.append(tabla2)

    if os.path.exists(grafica):
        imagen = Image(grafica, width=400, height=200)
        flowables.append(imagen)

    pdf.build(flowables)
    message(f"PDF generado con éxito y guardado en: {fileName}")