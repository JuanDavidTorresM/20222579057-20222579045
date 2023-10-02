import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import html
from frontend.navegador.navegador import navegador

from frontend.izquierdo.inicio_izquierdo import inicio_izquierdo
from frontend.izquierdo.programa_estudiantes_izquierdo import programa_estudiantes_izquierdo
from frontend.izquierdo.programa_profesional_izquierdo import programa_profesional_izquierdo
from frontend.derecho.inicio_derecho import inicio_derecho
from frontend.derecho.programa_estudiantes_derecho import programa_estudiantes_derecho
from frontend.derecho.programa_profesional_derecho import programa_profesional_derecho
from frontend.barra.barra import tabs

# Inicializa la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Contenido de la página
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(navegador, md=12, style={'background-color': 'teal', 'text-align': 'center'}),
    ]),
    dbc.Row([
        dbc.Col(tabs, md=12),  # Mueve la barra de pestañas arriba del contenido
    ]),
    dbc.Row([
        dbc.Col(id="contenido-izquierdo", md=8, style={'background-color':'papayawhip'}),
        dbc.Col(id="contenido-derecho", md=4, style={'background-color':'snow'}),
    ]),
])

# Callback para mostrar el contenido de la pestaña seleccionada
@app.callback(
    [Output("contenido-izquierdo", "children"), Output("contenido-derecho", "children")],
    [Input("tabs", "active_tab")]
)
def render_tab_content(active_tab):
    if active_tab == "tab-inicio":
        return inicio_izquierdo, inicio_derecho
    elif active_tab == "tab-programa-estudiantes":
        return programa_estudiantes_izquierdo, programa_estudiantes_derecho
    elif active_tab == "tab-programa-profesional":
        return programa_profesional_izquierdo, programa_profesional_derecho
    return "Error", ""

if __name__ == '__main__':
    app.run_server(debug=True)
