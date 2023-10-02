import math
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import AutoMinorLocator, FixedLocator


def granulometria():
    x = [4.750, 2, 0.850, 0.425, 0.250, 0.106, 0.075, 0]
    y = [211.1, 185.2, 124.8, 84.6, 43.4, 28.2, 15,0]
    #x = abertura # EJE X ES LA ABERTURA QUE ESTA EN MM
    #y = granulometria["% PASA"] # EJE Y ES EL PORCENTAJE QUE PASA

    plt.figure(figsize=(10,8)) #TAMAÑO DEL GRAFICO

    #fig, ax = plt.subplots() #PLOTEAR FIGURA CON LOS VALORES DE X

    #ax.grid(which = "minor",ls='-.',lw=0.5) #LA FIGURA AX TENDRA UNA GRILLA "MENOR", LA FORMA DE LA LINEA ES -., Y EL  TAMAÑO ES DE 0.5 
    #ax.xaxis.set_minor_locator(AutoMinorLocator(x)) #EN EL EJE X VA SELECCIONAR LA GRILLA "MENOR" CON LOS VALORES DE ABERTURA
    plt.plot(x,y, marker='d', color='black', label='GRANULOMETRIA') #PLOTEAR EJE X Y Y, LOS PUNTOS CON FORMA 'D', COLOR NEGRO, ETIQUETA DE LA GRAFICA
    #plt.xaxis.set_minor_locator(AutoMinorLocator(x)) #EN EL EJE X VA SELECCIONAR LA GRILLA "MENOR" CON LOS VALORES DE ABERTURA
    plt.grid(which = "minor",ls='-.',lw=0.5) #LA FIGURA AX TENDRA UNA GRILLA "MENOR", LA FORMA DE LA LINEA ES -., Y EL  TAMAÑO ES DE 0.5 
    plt.xscale("log") #EJE X EN ESCALA LOGARITMICA
    plt.grid(color='grey', ls= '-.', lw= 1) #GRILLA, COLOR GRIS, VA PUNTEADA, EL TAMAÑO ES DE 1d
    plt.xlabel("ABERTURA (mm) - Es. log",fontsize=10) #TITULO EJE X
    plt.ylabel("% PASA" , fontsize=10) #TITULO EJE Y
    plt.gca().invert_xaxis() #INVERTIR EJE X
    plt.legend(loc='center right') #MOSTRAR ETIQUETA DEL GRAFICO, LUGAR DONDE SE MUESTRA
    plt.title('CURVA GRANULOMETRIA',fontsize=10) #TITULO GRAFICA
    plt.show()