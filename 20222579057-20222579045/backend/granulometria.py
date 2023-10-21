import pandas as pd
import numpy as np

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

granulometria["Retenido_acum"]= granulometria["Retenido"].cumsum() #se crea una columna para retenido acummulado y se aplica cumsum a la columna retenido para hallar su acumulado
granulometria["Pasa"]= granulometria["Retenido"].sum()-granulometria["Retenido_acum"] #Se crea la columna Pasa y se realiza la resta del total de la muestra menos el retenido acumulado en cada fila
granulometria["Por_Pasa"]= round(granulometria["Pasa"]*100/granulometria["Retenido"].sum(),2) #Se crea la columna % pasa y se realiza la operació entre la columna pasa por 100 dividido en el total de la muetra

