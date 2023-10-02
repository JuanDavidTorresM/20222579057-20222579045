import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

inicio_izquierdo = html.Div([
    html.H3("Clasificación de los suelos"),
    html.P("Los suelos se pueden clasificar en dos tipos principales: Granulares y Finos, dependiendo de cómo está distribuido el material que pasa. Si más del 50% del material pasa a través de un tamiz más pequeño conocido como Tamiz número 200 (abreviado como T200), se considera que el suelo es FINO. Por otro lado, si menos del 50% del material pasa por este tamiz, entonces el material se clasifica como GRANULAR y puede ser grava o arena."),
])