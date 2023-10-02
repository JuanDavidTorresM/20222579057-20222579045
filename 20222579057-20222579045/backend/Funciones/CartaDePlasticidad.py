import math
import sympy
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

global LL,LP

def carta_de_plasticidad(LL,IP):
  print(LL)
  print(IP)
  #LL = int(input('Ingrese su límite líquido')) #límite líquido
  #IP = int(input('Ingrese su Indice plásticidad')) #Límite plástico
  x=np.array([0,100])
  y=np.array([0,100])
 
# Detalles de la grafica
  plt.title("CARTA DE PLASTICIDAD",fontsize=10) #Titulo 
  plt.xlabel("Limite liquido",fontsize=10) #Titulo eje x
  plt.ylabel("Indice de plasticidad",fontsize=10) #Titulo eje y
  plt.grid(color='grey', ls= '-.', lw= .2)

#establecemos limites en los ejes x,y
  plt.xlim(0,100)
  plt.ylim(0,60)
  
#linea A y U
  linea_u=(0.73)*(x-20)
  linea_A=(0.9*(x-8))
  
  plt.plot(x, linea_A,'r', label = "Linea A") #cambia de color , nombre linea 
  plt.plot(y, linea_u,'r', label = "Linea U") 
  #linea para diferenciar la plasticidad
  plt.vlines(50,0,60,'r')
  #lineas de frontera
  plt.hlines(7,15.7,29.5,'r')
  plt.hlines(4,12.4,25.5,'r')
  #etiquetas 
  plt.annotate('CL-ML',(15,5))
  plt.annotate('MH',(80,20))
  plt.annotate('CL',(30,15))
  plt.annotate('CH',(62,40))
  plt.annotate('ML',(35,5))
  
  plt.legend() # muestra la leyenda

  #graficamos parejas de puntos 

  w = np.array([IP])
  z = np.array([LL])
  plt.scatter(LL,IP)
  plt.figure(figsize=(5,12))
  #plt.show()

