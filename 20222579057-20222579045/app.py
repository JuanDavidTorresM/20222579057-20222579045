import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html
from frontend.navegador.navegador import navegador
from frontend.izquierdo.inicio_izquierdo import inicio_izquierdo
from frontend.izquierdo.programa_izquierdo import programa_izquierdo 
from frontend.derecho.inicio_derecho import inicio_derecho
from frontend.derecho.programa_derecho import programa_derecho
from frontend.centro.inicio_centro import inicio_centro
from frontend.centro.programa_centro import programa_centro
from frontend.barra.barra import tabs

# Inicializa la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

# Define el diseño de la aplicación
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(navegador, md=12, style={'background-color': 'teal', 'text-align': 'center'}),
    ]),
    dbc.Row([
        dbc.Col(tabs, md=12),  # Asegúrate de que 'tabs' esté definido en alguna parte
    ]),
    dbc.Row([
        dbc.Col(id="contenido-izquierdo", md=8, style={'background-color': 'papayawhip'}),
        dbc.Col(id="contenido-derecho", md=4, style={'background-color': 'snow'}),
    ]),
    dbc.Row([
        dbc.Col(id="contenido-centro", md=12, style={'background-color': 'snow'}),
    ]),
])

# Define la devolución de llamada para mostrar el contenido según la pestaña seleccionada
@app.callback(
    [Output("contenido-izquierdo", "children"), Output("contenido-derecho", "children"), Output("contenido-centro", "children")],
    [Input("tabs", "active_tab")]
)
def render_tab_content(active_tab):
    if active_tab == "tab-inicio":
        return inicio_izquierdo, inicio_derecho, inicio_centro
    elif active_tab == "tab-programa-estudiantes":
        return programa_izquierdo, programa_derecho, programa_centro
    return "Error", ""

if __name__ == '__main__':
    app.run_server(debug=True)
