import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib.pyplot as plt # importamos la librería que utilizaremos para graficar
from scipy.interpolate import interp1d # importamos la librería que utilizaremos para interpolar
import matplotlib.path as mpath # importamos la librería que utilizaremos para operaciones
from frontend.izquierdo.programa_estudiantes_izquierdo import granulometria


plt.figure(figsize=(14,4)) # el figsize define el tamaño de la figura, el primer dato es X y el segundo es Y
plt.plot(granulometria["abertura"][0:10],granulometria["porcentaje_pasa"][0:10], "darkblue", label= "Curva Granulométrica") # Graficamos x= abertura en mm y y= % pasa, [0:10] le dice al programa que grafique los 10 primeros datos, el ultimo no se grafica porque el fondo genera error en la grafica por ser un texto
plt.xlabel("Diámetro (mm)", fontsize=12) # Pone el título del eje x, fontsize es para el tamaño
plt.ylabel("Porcentaje pasa acumulado (%)", fontsize=12) # Pone el título del eje Y, fontsize es para el tamaño
plt.grid(color="grey", ls = "dashed", lw= 0.5 ) # En esta línea se definen los datos de la grilla, como el color de la grilla, ls es el estilo de la grilla y por ultimo lw es el tamaño de la grilla
plt.title("Curva Granulométrica", fontsize=16, fontweight='bold', color='darkorange') # En esta línea se crea el título del gráfico (Curva granulométrica), fontsize es para el tamaño del título, fontweight='bold' hace que el título se muestre en negrita y por último se define el color
f= interp1d(granulometria["porcentaje_pasa"][0:10], granulometria["abertura"][0:10]) # Realizamos la interpolación líneal de los datos

# Calcular D60 D30 D10

# Valores de entrada
y1_coord = 60 # Definimos el valor de y=60
y2_coord = 30 # Definimos el valor de y=30
y3_coord = 10 # Definimos el valor de y=10

# Realizamos la interpolación:
x1_coord = f(y1_coord) # Calcula el valor de x a partir de la interpolacion para y=60
x2_coord = f(y2_coord) # Calcula el valor de x a partir de la interpolacion para y=30
x3_coord = f(y3_coord) # Calcula el valor de x a partir de la interpolacion para y=10

# Representamos los valores con dos decimales:
x1_formatted = '{:.2f}'.format (x1_coord) # Ajusta el valor proporcionado para que tenga únicamente dos decimales
print ("El dato de D60 es",x1_formatted) # Nos muestra el valor de D60 con dos decimales
x2_formatted = '{:.2f}'.format (x2_coord) # Ajusta el valor proporcionado para que tenga únicamente dos decimales
print ("El dato de D30 es",x2_formatted) # Nos muestra el valor de D30 con dos decimales
x3_formatted = '{:.2f}'.format (x3_coord) # Ajusta el valor proporcionado para que tenga únicamente dos decimales
print ("El dato de D10 es",x3_formatted) # Nos muestra el valor de D10 con dos decimales

# Ubica los puntos en el plano
plt.scatter(x1_coord, y1_coord, marker ='s', s =50, color='k', label='D60='+x1_formatted) # Se crea el punto D60, se registran las coordenadas ya calculadas, el tipo de punto, el tamaño, el color y el nombre
plt.scatter(x2_coord, y2_coord, marker ='<', s =50, color='k', label='D30='+x2_formatted) # Se crea el punto D30, se registran las coordenadas ya calculadas, el tipo de punto, el tamaño, el color y el nombre
plt.scatter(x3_coord, y3_coord, marker ='>', s =50, color='k', label='D10='+x3_formatted) # Se crea el punto D10, se registran las coordenadas ya calculadas, el tipo de punto, el tamaño, el color y el nombre
plt.legend()
# Se crean líneas punteadas que conecta donde nos da el valor de D10, D30 y D10
plt.plot([x1_coord, x1_coord], [0, y1_coord], color="red", linestyle="--", lw="1.5") # Se crea plt plot por linea donde se ubican las coordenadas para que conecten con el punto, luego se le define el color, el tipo de linea y el tamaño de las líneas
plt.plot([100, x1_coord], [y1_coord, y1_coord], color="red", linestyle="--", lw="1.5") # Se crea plt plot por linea donde se ubican las coordenadas para que conecten con el punto, luego se le define el color, el tipo de linea y el tamaño de las líneas
plt.plot([x2_coord, x2_coord], [0, y2_coord], color="green", linestyle="--", lw="1.5") # Se crea plt plot por linea donde se ubican las coordenadas para que conecten con el punto, luego se le define el color, el tipo de linea y el tamaño de las líneas
plt.plot([100, x2_coord], [y2_coord, y2_coord], color="green", linestyle="--", lw="1.5") # Se crea plt plot por linea donde se ubican las coordenadas para que conecten con el punto, luego se le define el color, el tipo de linea y el tamaño de las líneas
plt.plot([x3_coord, x3_coord], [0, y3_coord], color="blue", linestyle="--", lw="1.5") # Se crea plt plot por linea donde se ubican las coordenadas para que conecten con el punto, luego se le define el color, el tipo de linea y el tamaño de las líneas
plt.plot([100, x3_coord], [y3_coord, y3_coord], color="blue", linestyle="--", lw="1.5") # Se crea plt plot por linea donde se ubican las coordenadas para que conecten con el punto, luego se le define el color, el tipo de linea y el tamaño de las líneas

# Creamos cuadros de texto para D60, D30 y D10
plt.text(3, 65, f'D60 = {x1_formatted}', color='red', fontsize=10, bbox=dict(facecolor='white', edgecolor='red', boxstyle='round')) # Crea un cuadro por cada punto, primero definimos las coordenadas donde se ubica el recuadro, luego usamos f-string para insertar el nombre y valor correspondiente, le damos un color, el tamaño del texto(fontsize), y el bbox crea las propiedades de cada cuadro: facecolor es para el fondo del cuadro, edgecolor para el color del borde y boxstyle para el estilo en este caso redondeado
plt.text(1, 35, f'D30 = {x2_formatted}', color='green', fontsize=10, bbox=dict(facecolor='white', edgecolor='green', boxstyle='round')) # Crea un cuadro por cada punto, primero definimos las coordenadas donde se ubica el recuadro, luego usamos f-string para insertar el nombre y valor correspondiente, le damos un color, el tamaño del texto(fontsize), y el bbox crea las propiedades de cada cuadro: facecolor es para el fondo del cuadro, edgecolor para el color del borde y boxstyle para el estilo en este caso redondeado
plt.text(0.2, 15, f'D10 = {x3_formatted}', color='blue', fontsize=10, bbox=dict(facecolor='white', edgecolor='blue', boxstyle='round')) # Crea un cuadro por cada punto, primero definimos las coordenadas donde se ubica el recuadro, luego usamos f-string para insertar el nombre y valor correspondiente, le damos un color, el tamaño del texto(fontsize), y el bbox crea las propiedades de cada cuadro: facecolor es para el fondo del cuadro, edgecolor para el color del borde y boxstyle para el estilo en este caso redondeado

ax1= plt.gca() # Creamos un objeto en el eje actual
ax1.invert_xaxis() # Esta línea invierte el eje x
ax1.set_xscale("log") # Esta línea establece una escala logarítmica

ax2 = ax1.twiny() # Esta línea crea un nuevo objeto de ejes 'ax2' que comparte el mismo eje y (vertical) con 'ax1'
ax2.set_xscale("log") # Esta línea establece una escala logarítmica
ax2.set_xticks(granulometria["abertura"][0:10]) # Esta línea establece etiquetas en el eje x utilizando los primeros 10 valores de abertura
ax2.set_xticklabels(granulometria["malla"][0:10],rotation=90,fontsize=8) # Esta línea establece las etiquetas del eje x del objeto de ejes ax2 utilizando los primeros 10 valores de malla, también rota las etiquetas en 90 grados y establece el tamaño de fuente en 8.
ax2.set_xlabel('Tamices') # Esta línea establece la etiqueta del eje ax como Tamices
ax2.set_xlim(0.075,4.75) # Esta línea establece los límites del eje x
ax2.invert_xaxis() # Esta línea invierte el eje x

x_values = [4,3,2,1,0.9,0.8,0.7,
            0.6,0.5,0.4,0.3,
            0.2,0.1,0.09,0.08] # Se crea un conjunto de valores para graficar una grilla según la Curva granulometrica
for x in x_values:
    plt.axvline(x=x, color="grey", ls="-", lw="0.3") # Creamos las lineas con el conjunto de valores definidos anteriormente, definimos color, tipo de línea y tamaño.

#plt.scatter(granulometria["abertura"][0:10],granulometria["porcentaje_pasa"][0:10], c='red', marker='D', s=70)
plt.xlim(0.075, 4.75) #Limites de la grafica en el eje x
plt.ylim(0, 100) #Limites de la grafica en el eje y
plt.legend()# Añade a nuestro gráfico todos las leyendas que hayamos creado
plt.show() # Nos muestra el gráfico que definimos anteriormente

# Convertir el gráfico de Matplotlib en una imagen base64
def plot_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("utf-8")
    buf.close()
    return data

# Crear una aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definir el layout de la aplicación
app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div([
            html.H3("Contenido de la pestaña Programa Est. PARTE DERECHA"),
            html.P("Este es el contenido de la pestaña ESTUDIANTES."),
        ]), width=6),
        dbc.Col(html.Div([
            # Insertar la imagen del gráfico de Matplotlib
            html.Img(src=f"data:image/png;base64,{plot_to_base64(plt)}", style={"width": "100%"}),
        ]), width=6),
    ]),
])
