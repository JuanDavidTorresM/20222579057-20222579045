import math
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

global LL,LP
# DataFrame
# DataFrame de la Granulometria
# Alli se obtienen valores de entrada
# Variables
tamiz_200 = 9 #Valor de DataFrame
tamiz_4 = 40 #Valor de 
Cu = 9 #se interpola en la curva granulometrica, es D60/D10
Cc = 2 #se interpola en la curva granulometrica, D30^2/D60*D10

from Funciones.CartaDePlasticidad import carta_de_plasticidad
carta_de_plasticidad(LL,IP)

def ClasificacionDeSuelosFuncion(tamiz_200,tamiz_4):

  if tamiz_200 > 50: #FINOS
    carta_de_plasticidad()
  else: #GRUESOS
    if tamiz_4 > 50: #Arenas
      if tamiz_200 < 5:  #Analizar Cu y Cc
        if Cu > 6 and Cc < 3:
          print("SW")
        else:
          print("SP")
      elif 5 < tamiz_200 < 12: #Analizar Cu, Cu y Carta de Plasticidad
        if Cu > 6 and Cc < 3:
          print("SW")
          carta_de_plasticidad()
        else:
          print("SP")
          carta_de_plasticidad()
      else: #Analizar unicamente Carta de Plasticidad
        carta_de_plasticidad()
    else: #Gravas
      if tamiz_200 < 5:  #Analizar Cu y Cc
        if Cu > 6 and Cc < 3:
          print("GW") #Bien gradada
        else:
          print("GP") #Mal gradada
      elif 5 < tamiz_200 < 12: #Analizar Cu, Cu y Carta de Plasticidad, debe tener dos valores bien gradada y/o limosa o arcillosa
        if Cu > 6 and Cc < 3:
          print("SW")
          carta_de_plasticidad()
        else:
          print("SP")
          carta_de_plasticidad()
      else: #mayor del 12%
        carta_de_plasticidad()