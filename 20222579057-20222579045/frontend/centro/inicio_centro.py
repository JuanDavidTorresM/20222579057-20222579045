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

# Estilo CSS para la tabla
tabla_style = {
    'textAlign': 'center',
    'font-weight': 'bold'
}

# Crear la tabla en formato HTML
tabla_html = html.Table([
    html.Tr([html.Th("Tipo de Suelo"), html.Th("Prefijo"), html.Th("Subgrupo"), html.Th("Sufijo")], className="table-info", style=tabla_style),
    *[html.Tr([html.Td(item) for item in row], className="table-info", style=tabla_style) for row in data]
], className="table table-striped table-bordered table-hover")

# Contenido de inicio_derecho con la tabla
inicio_centro = html.Div([
    html.H3("Símbolos utilizados en la Clasificación SUCS"),
    tabla_html  # Agrega la tabla aquí
])

app = dash.Dash(__name__)

app.layout = html.Div([inicio_centro])

if __name__ == '__main__':
    app.run_server(debug=True)
