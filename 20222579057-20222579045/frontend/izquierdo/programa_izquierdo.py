import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import dash_table
import pandas as pd
from dash.dependencies import Input, Output, State

# Definir tus datos
malla = [ # Ingresamos todos los datos de las mallas que hay en el video: "https://www.youtube.com/watch?v=GL3q7I2U4K4"
    "1 1/2 in", # tamiz de 1 1/2"
    "1 in", # tamiz de 1"
    "3/4 in", # tamiz de 3/4"
    "3/8 in", # tamiz de 3/8"
    "No 4", # tamiz #4
    "No 10", # tamiz #10
    "No 20", # tamiz #20
    "No 40", # tamiz #40
    "No 60", # tamiz #60
    "No 100", # tamiz #100
    "No 200", # tamiz #200
    "fondo", # Fondo del juego de tamices
]

abertura = [ # Ingresamos todos los datos de abertura de los tamices, estos datos son numéricos
    37.5, # tamiz de 1 1/2"
    25, # tamiz de 1"
    19, # tamiz de 3/4"
    9.5, # tamiz de 3/8"
    4.75, # tamiz #4
    2, # tamiz #10
    0.85, # tamiz #20
    0.425, # tamiz #40
    0.25, # tamiz #60
    0.15, # tamiz #100
    0.075, # tamiz #200
    0, # Fondo del juego de tamices
]
retenido = [ # Ingresamos todos los datos de material retenido de los tamices, estos datos son numéricos
    0, # Cantidad de muestra retenida tamiz de 1 1/2"
    0, # Cantidad de muestra retenida tamiz de 1"
    0, # Cantidad de muestra retenida tamiz de 3/4"
    0, # Cantidad de muestra retenida tamiz de 3/8"
    5, # Cantidad de muestra retenida tamiz #4
    5, # Cantidad de muestra retenida tamiz #10
    70, # Cantidad de muestra retenida tamiz #20
    70, # Cantidad de muestra retenida tamiz #40
    70, # Cantidad de muestra retenida tamiz #60
    270, # Cantidad de muestra retenida tamiz #100
    10, # Cantidad de muestra retenida tamiz #200
    35, # Cantidad de muestra fondo del tamiz
]

# Crear DataFrame
granulometria = pd.DataFrame({
    "malla": malla,
    "abertura": abertura,
    "retenido": retenido
})

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Define el diseño de la aplicación
programa_izquierdo = html.Div([
    html.H4("Tabla de Granulometría"),
    dash_table.DataTable(
        id='tabla-granulometria',
        columns=[
            {'name': 'Malla', 'id': 'malla', 'editable': False},
            {'name': 'Abertura', 'id': 'abertura', 'editable': False},
            {'name': 'Retenido', 'id': 'retenido', 'editable': True},
            {'name': 'Retenido Acumulado', 'id': 'retenido_acumulado', 'editable': False},
            {'name': 'Pasa G', 'id': 'pasa_g', 'editable': False},
            {'name': 'Porcentaje Pasa', 'id': 'porcentaje_pasa', 'editable': False},
        ],
        data=granulometria.to_dict('records'),
        editable=True,
    ),
    
    # Botón para calcular
    html.Button("Calcular", id="calcular-button"),
])

# Callback para calcular los valores
@app.callback(
    Output('tabla-granulometria', 'data'),
    Input('calcular-button', 'n_clicks'),
    [State('tabla-granulometria', 'data')]
)
def calcular_valores(n_clicks, data):
    if n_clicks is not None:
        df = pd.DataFrame(data)
        df_copy = df.copy()  # Crear una copia del DataFrame

        # Calcular retenido acumulado
        df_copy["retenido_acumulado"] = df_copy["retenido"].cumsum()

        # Calcular pasa_g
        df_copy["pasa_g"] = df_copy["retenido_acumulado"].iloc[-1] - df_copy["retenido_acumulado"]

        # Calcular porcentaje_pasa
        df_copy["porcentaje_pasa"] = (df_copy["pasa_g"] / df_copy["retenido_acumulado"].iloc[-1] * 100).round(3)

        return df_copy.to_dict('records')
    else:
        return data