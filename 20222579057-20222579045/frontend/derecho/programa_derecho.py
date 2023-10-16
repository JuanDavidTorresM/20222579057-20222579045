import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import matplotlib.path as mpath
import matplotlib.pyplot as plt

programa_derecho = html.Div([
    html.H3("Contenido de la pestaña Programa Est. PARTE centro"),
    html.P("Este es el contenido de la pestaña ESTUDIANTES."),
])

# Inicializa tu aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Importa las bibliotecas necesarias, incluyendo matplotlib y numpy

def cartaPlasticidad(limiteLiquido, indicePlasticidad):
  ll = range (1,101) # Crea los valores de 0 a 100
  linea_A=[] # Crea la lista para la línea A de la carta de plasticidad
  linea_U=[] # Crea la lista para la línea U de la carta de plasticidad

  for i in ll:
    ecuacionA = 0.73*(i-20) # Definimos la ecuación de la línea A
    linea_A.append(ecuacionA) # Almacena los valores de la ecuacionA a la lista para generar la línea
    ecuacionU =0.9*(i-8) # Definimos la ecuación de la línea U
    linea_U.append(ecuacionU) #Almacena los valores de la ecuacionU a la lista para generar la línea

  plt.figure(figsize=(10,5)) # el figsize define el tamaño de la figura, el primer dato es X y el segundo es Y
  plt.plot(ll,linea_A, "darkblue", label= "Línea A") # Hace el plot de x (ll) contra y(linea_A), se establece con el color darkblue y por último se le coloca la etiqueta de Línea A con el label
  plt.plot(ll,linea_U, "cornflowerblue", label= "Línea U") # Hace el plot de x (ll) contra y(linea_U), se establece con el color cornflowerblue y por último se le coloca la etiqueta de Línea U con el label
  plt.grid(color="grey", ls = "dashed", lw= 0.5 ) # En esta línea se definnen los datos de la grilla, como el color de la grilla, ls es el estilo de la grilla y por ultimo lw es el tamaño de la grilla
  plt.xlabel("Límite Líquido (LL-%)", fontsize=10) # Pone el título del eje x, fontsize es para el tamaño
  plt.ylabel("Indice de Plasticidad (IP-%)", fontsize=10) # Pone el título del eje Y, fontsize es para el tamaño
  plt.annotate('Línea A', (80,40), rotation =37) # Agrega un comentario en el gráfico, se define el nombre, las coordenadas donde se ubica el texto y por último la rotación del texto en grados
  plt.annotate('Línea U', (60,45), rotation =37) # Agrega un comentario en el gráfico, se define el nombre, las coordenadas donde se ubica el texto y por último la rotación del texto en grados
  plt.annotate('NO EXISTE IP', (24,35)) # Agrega un comentario en el gráfico, se define el nombre según la ubicación (NO EXISTE IP) y las coordenadas donde se ubica el texto
  plt.annotate('ML', (38,5))# Agrega un comentario en el gráfico, se define el nombre según la ubicación (ML) y las coordenadas donde se ubica el texto
  plt.annotate('MH', (80,20))# Agrega un comentario en el gráfico, se define el nombre según la ubicación (MH) y las coordenadas donde se ubica el texto
  plt.annotate('CL', (35,20))# Agrega un comentario en el gráfico, se define el nombre según la ubicación (CL) y las coordenadas donde se ubica el texto
  plt.annotate('CH', (65,40))# Agrega un comentario en el gráfico, se define el nombre según la ubicación (CH) y las coordenadas donde se ubica el texto
  plt.annotate('CL-ML', (18,4.5))# Agrega un comentario en el gráfico, se define el nombre según la ubicación (CL-ML) y las coordenadas donde se ubica el texto
  plt.title("Carta de plasticidad", fontsize=16, fontweight='bold', color='darkorange') # En esta línea se crea el título del gráfico (Carta de plasticidad), fontsize es para el tamaño del título, fontweight='bold' hace que el título se muestre en negrita y por último se define el color

  plt.fill_between([50, 50, 100, 100, 50], [21.9, 0, 0, 58.4, 21.9], color='#CD853F', alpha=0.5, label='MH') # Los códigos de todos los colores se tomaron de "https://python-charts.com/es/colores/", ésta línea rellena el área para MH entre los puntos definidos, en el primer rango[] los valores del eje x, en el segundo rango[] los valores del eje y, ya creados los puntos, se define el color del relleno, alpha controla la transparencia que le queremos dar al color y label asigna la etiqueta correspondiente
  plt.fill_between([8, 50, 50, 25.47945,12.44444, 8], [0, 0, 21.9, 4,4, 0], color='#98FB98', alpha=0.5, label='ML')#ésta línea rellena el área para ML entre los puntos definidos, en el primer rango[] los valores del eje x, en el segundo rango[] los valores del eje y, ya creados los puntos, se define el color del relleno, alpha controla la transparencia que le queremos dar al color y label asigna la etiqueta correspondiente
  plt.fill_between([12.44444, 25.47945, 29.58904, 15.77777, 12.44444], [4, 4, 7, 7, 4], color='#DA70D6', alpha=0.5, label='CL-ML')#ésta línea rellena el área para CL-ML entre los puntos definidos, en el primer rango[] los valores del eje x, en el segundo rango[] los valores del eje y, ya creados los puntos, se define el color del relleno, alpha controla la transparencia que le queremos dar al color y label asigna la etiqueta correspondiente
  plt.fill_between([15.77777,29.58904,50,50,15.77777], [7, 7,21.9,37.8,7 ], color='#FFFF00', alpha=0.5, label='CL')#ésta línea rellena el área para CL entre los puntos definidos, en el primer rango[] los valores del eje x, en el segundo rango[] los valores del eje y, ya creados los puntos, se define el color del relleno, alpha controla la transparencia que le queremos dar al color y label asigna la etiqueta correspondiente
  plt.fill_between([50,50,102.19178,74.66666,50], [37.8,21.9,60,60,37.8 ], color='#6495ED', alpha=0.5, label='CH')#ésta línea rellena el área para CH entre los puntos definidos, en el primer rango[] los valores del eje x, en el segundo rango[] los valores del eje y, ya creados los puntos, se define el color del relleno, alpha controla la transparencia que le queremos dar al color y label asigna la etiqueta correspondiente

  plt.vlines(x=50, ymin=0, ymax=37.8, color='red', linestyle='--') # Agregar una línea vertical. y=0.73(x-20), siendo x=50, ymin = 21.9 ; y = 0.9(x-8), siendo x = 50, ymax= 37.8
  plt.hlines(y=4, xmin=12.44444, xmax=25.47945, color='red', linestyle='--') # Agregar una línea horizontal  y=0.73(x-20), siendo y=4, xmax=25.479452 ; y = 0.9(x-8), siendo y=4, x min=12.44444
  plt.hlines(y=7, xmin=15.77777, xmax=29.58904, color='red', linestyle='--') # Agregar una línea horizontal  y=0.73(x-20), siendo y=7, xmax=29.58904 ; y = 0.9(x-8), siendo y=7, xmin =15.777

  region_MH = np.array([[50,0],[50,22],[100,58],[100,0]]) # En esta línea se delimitan la región MH , se usa array definiendo las coordenadas
  region_ML = np.array([[25.5,4],[12.4,4],[8,0],[20,0],[50,0],[50,22]]) # En esta línea se delimitan la región ML, se usa array definiendo las coordenadas
  region_CH = np.array([[50,22],[100,58],[100,60],[75,60],[50,38]]) # En esta línea se delimitan la región CH, se usa array definiendo las coordenadas
  region_CL_ML = np.array([[29.5,7],[15.7,7],[12.4,4],[25.5,4]]) # En esta línea se delimitan la región CL_ML, se usa array definiendo las coordenadas
  region_CL = np.array([[15.7,7],[29.5,7],[50,22],[50,38]]) # En esta línea se delimitan la región CL, se usa array definiendo las coordenadas

  path_MH = mpath.Path(region_MH) # En esta línea se convierten los puntos en regiones para MH
  path_ML = mpath.Path(region_ML) # En esta línea se convierten los puntos en regiones para ML
  path_CH = mpath.Path(region_CH) # En esta línea se convierten los puntos en regiones para CH
  path_CL_ML = mpath.Path(region_CL_ML) # En esta línea se convierten los puntos en regiones para CL_ML
  path_CL = mpath.Path(region_CL) # En esta línea se convierten los puntos en regiones para CL

  point = np.array([limiteLiquido, indicePlasticidad]) # Creamos un punto donde ubica el limite liquido e indice de plasticidad
  if path_MH.contains_point(point): # Se establece que si el punto se ubica dentro de la zona MH, nos de el resultado descrito
    print('El punto se encuentra en la zona MH')
  elif path_ML.contains_point(point): # Se establece que si el punto se ubica dentro de la zona ML, nos de el resultado descrito
      print('El punto se encuentra en la zona ML')
  elif path_CH.contains_point(point): # Se establece que si el punto se ubica dentro de la zona CH, nos de el resultado descrito
      print('El punto se encuentra en la zona CH')
  elif path_CL_ML.contains_point(point): # Se establece que si el punto se ubica dentro de la zona CL_ML, nos de el resultado descrito
      print('El punto se encuentra en la zona CL_ML')
  elif path_CL.contains_point(point): # Se establece que si el punto se ubica dentro de la zona CL, nos de el resultado descrito
      print('El punto se encuentra en la zona CL')
  else:
    print('El punto no existe IP') # De no cumplir con alguno de los parámetros definidos, dará como resultado que no existe IP

  plt.scatter(limiteLiquido, indicePlasticidad, c='red', marker='D', s=70) # En esta línea modificamos las propiedades del punto, c='red': Esto cambia el color del punto a rojo, marker='D': esto cambia la forma del punto a un diamante y s=70:cambia el tamaño del punto
  plt.legend()# Añade a nuestro gráfico todos las leyendas que hayamos creado
  plt.xlim(0, 100) #Limites de la grafica en el eje x
  plt.ylim(0, 60) #Limites de la grafica en el eje y
  plt.show() # Nos muestra el gráfico que definimos anteriormente

# Define el diseño de la pestaña con la Carta de Plasticidad
carta_plasticidad_tab = dbc.Container([
    html.H3("Carta de Plasticidad"),
    dcc.Input(id="limite-liquido-input", type="number", placeholder="Límite Líquido"),
    dcc.Input(id="indice-plasticidad-input", type="number", placeholder="Índice de Plasticidad"),
    html.Button("Calcular", id="calcular-button"),
    dcc.Graph(id="carta-grafica"),
    html.Div(id="resultado-carta"),
], fluid=True)

# Define el diseño general de la aplicación, que incluye las pestañas.
app.layout = html.Div([
    dbc.Tabs([
        dbc.Tab(label="Programa Estudiantes", children=programa_derecho),
        dbc.Tab(label="Carta de Plasticidad", children=carta_plasticidad_tab),
    ]),
])

# Define una devolución de llamada para mostrar el resultado de la carta de plasticidad
@app.callback(
    Output("resultado-carta", "children"),
    [Input("limite-liquido-input", "value"),
     Input("indice-plasticidad-input", "value")]
)
def mostrar_resultado_carta(limite_liquido, indice_plasticidad):
    if limite_liquido is not None and indice_plasticidad is not None:
        resultado = cartaPlasticidad(float(limite_liquido), float(indice_plasticidad))
        return html.Div(f"Resultado de la carta de plasticidad: {resultado}")
    return ""
