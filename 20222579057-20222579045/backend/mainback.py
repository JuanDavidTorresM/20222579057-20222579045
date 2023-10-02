import math
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


global LL,LP
LL = int(input('Ingrese su límite líquido: ')) #límite líquido
IP = int(input('Ingrese su Indice plásticidad: ')) #Límite plástico

from ClasificacionDeSuelos import ClasificacionDeSuelosFuncion

ClasificacionDeSuelosFuncion(LL,IP)