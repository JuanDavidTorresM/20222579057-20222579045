import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Datos para la tabla
data = [
    ["Grava", "G", "Bien Gradada", "W"],
    ["Arena", "S", "Probablemente Gradada", "P"],
    ["Limo", "M", "Limoso", "M"],
    ["Arcilla", "C", "Arcilloso", "C"],
]

# Crear la tabla en formato HTML
tabla_html = html.Table([
    html.Tr([html.Th("Tipo de Suelo"), html.Th("Prefijo"), html.Th("Subgrupo"), html.Th("Sufijo")], className="table-striped"),
    *[html.Tr([html.Td(item) for item in row], className="table-info") for row in data]
], className="table table-striped table-bordered table-hover")

# Contenido de inicio_derecho con la tabla
inicio_derecho = html.Div([
    html.H3("Símbolos utilizados en la Clasificación SUCS"),
    tabla_html  # Agrega la tabla aquí
])