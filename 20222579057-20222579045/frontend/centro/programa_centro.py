import dash
from dash import dcc, html
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from frontend.izquierdo.programa_izquierdo import granulometria

programa_centro = html.Div([
    html.H3("Contenido de la pestaña Programa Est. PARTE centro"),
    html.P("Este es el contenido de la pestaña ESTUDIANTES."),
])