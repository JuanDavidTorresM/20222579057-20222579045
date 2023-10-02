import dash_bootstrap_components as dbc
from dash import html

# Contenido de las pestañas
tab_inicio_content = html.Div([
    html.H3("Contenido de la pestaña Inicio"),
    html.P("Este es el contenido de la pestaña Inicio."),
])

tab_programa_estudiantes_content = html.Div([
    html.H3("Contenido de la pestaña Programa Estudiantes"),
    html.P("Este es el contenido de la pestaña Programa Estudiantes."),
])

tab_programa_profesional_content = html.Div([
    html.H3("Contenido de la pestaña Programa Profesional"),
    html.P("Este es el contenido de la pestaña Programa Profesional."),
])

# Componente de pestañas
tabs = dbc.Tabs(
    [
        dbc.Tab(label="Inicio", tab_id="tab-inicio"),
        dbc.Tab(label="Programa Estudiantes", tab_id="tab-programa-estudiantes"),
        dbc.Tab(label="Programa Profesional", tab_id="tab-programa-profesional"),
    ],
    id="tabs",
    active_tab="tab-inicio",
)
