import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Contenido de inicio_izquierdo con la lista desplegable
inicio_izquierdo = html.Div([
    html.H3("Clasificación de los suelos"),
    html.P("Los suelos se pueden clasificar en dos tipos principales: Granulares y Finos, dependiendo de cómo está distribuido el material que pasa. Si más del 50% del material pasa a través de un tamiz más pequeño conocido como Tamiz número 200 (abreviado como T200), se considera que el suelo es FINO. Por otro lado, si menos del 50% del material pasa por este tamiz, entonces el material se clasifica como GRANULAR y puede ser grava o arena."),
    
    # Lista desplegable para seleccionar el concepto
    dcc.Dropdown(
        id='concepto-dropdown',
        options=[
            {'label': 'Granulares', 'value': 'granulares'},
            {'label': 'Finos', 'value': 'finos'}
        ],
        value='granulares'  # Valor predeterminado
    ),
    
    # Div para mostrar la descripción del concepto
    html.Div(id='concepto-descripcion')
])

def actualizar_descripcion(selected_concept):
    if selected_concept == 'granulares':
        return "Los suelos granulares se caracterizan por tener menos del 50% de material que pasa por el Tamiz número 200 (T200). Estos suelos pueden incluir grava y arena."
    elif selected_concept == 'finos':
        return "Los suelos finos se caracterizan por tener más del 50% de material que pasa por el Tamiz número 200 (T200). Estos suelos son considerados suelos finos y pueden incluir limo y arcilla."
