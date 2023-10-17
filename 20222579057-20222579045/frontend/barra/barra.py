import dash_bootstrap_components as dbc
from dash import html

# Componente de pestañas
tabs = dbc.Tabs(
    [
        dbc.Tab(label="Inicio", tab_id="tab-inicio"),
        dbc.Tab(label="Programa Estudiantes", tab_id="tab-programa-estudiantes"),
    ],
    id="tabs",
    active_tab="tab-inicio",
)
