#Algoritmos y programacion basica
#Seccion 30
#02-04-2014
#Diego Morales, 14012
#Bryan Santos
#Maria Fonseca, 13691
#Z-Fun
#Programa que calcula ceros racionales de funciones polinomiales
#y graficadora
#Modulo de Funcion
#Este modulo recibe los datos ingresados y presenta un esbozo de la funcion

import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import numpy as np
import Factores

def Funcion(valor_a,valor_b):
    fig, ax = plt.subplots()
    x = np.linspace(-10.0, 10.0, 1000)
    #Se le asigan un valor a y par luego ser sustituido 
    y = 0
    #Se establecen parametros en el eje
    ax.axis([x[0], x[-1], x[0], x[-1]])
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['left']
    ax.spines['bottom']
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ticks = []
    #Evalua posibles valores de x
    for i in range(int(x[0]), int(x[-1] + 1), 1):
        ticks.append(i)
    ticks.remove(0)
    #Se configura los ejes "X" y "Y"
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    #Se asigna un titulo
    plt.title(u'Calculadora graficadora')
    plt.suptitle(u'Z-Fun')
    plt.rc('font', size = 15)  
    plt.plot(0,1)
    #Se establce el cuadriculado
    ax.grid(color='#ECECEC', linestyle='-', linewidth=1)
    #Ecuacion de la funcion
    y = ((valor_a)*(x)) + (valor_b)
    #Se grafica
    ax.plot(x,y)
    plt.show()
    

def Funcion2(valor_a,valor_b,valor_c):
    fig, ax = plt.subplots()
    x = np.linspace(-10.0, 10.0, 1000)
    #Se le asigan un valor a y par luego ser sustituido 
    y = 0
    #Se establecen parametros en el eje
    ax.axis([x[0], x[-1], x[0], x[-1]])
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['left']
    ax.spines['bottom']
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ticks = []
    #Evalua posibles valores de x
    for i in range(int(x[0]), int(x[-1] + 1), 1):
        ticks.append(i)
    ticks.remove(0)
    #Se configura los ejes "X" y "Y"
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    #Se asigna un titulo
    plt.title(u'Calculadora graficadora')
    plt.suptitle(u'Z-Fun')
    plt.rc('font', size = 15)  
    plt.plot(0,1)
    ax.grid(color='#ECECEC', linestyle='-', linewidth=1)
    #Ecuacion de la funcion
    y = (valor_a)*(x**(2)) + (valor_b)*(x) + valor_c
    #Se grafica 
    ax.plot(x,y)
    plt.show()
def Funcion3 (valor_a,valor_b,valor_c,valor_d):
    fig, ax = plt.subplots()
    x = np.linspace(-10.0, 10.0, 1000)
    #Se le asigan un valor a y par luego ser sustituido
    y = 0
    #Se establecen parametros en el eje
    ax.axis([x[0], x[-1], x[0], x[-1]])
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['left']
    ax.spines['bottom']
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ticks = []
    #Evalua posibles valores de x
    for i in range(int(x[0]), int(x[-1] + 1), 1):
        ticks.append(i)
    ticks.remove(0)
    #Se configura los ejes "X" y "Y"
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    #Se asigna un titulo
    plt.title(u'Calculadora graficadora')
    plt.suptitle(u'Z-Fun')
    plt.rc('font', size = 15)  
    plt.plot(0,1)
    ax.grid(color='#ECECEC', linestyle='-', linewidth=1)
    #Ecuacion de la funcion
    y = (valor_a)*(x**(3)) + ((valor_b)*(x**(2))) + (valor_c)*(x)+ valor_d
    #La grafica 
    ax.plot(x,y)
    plt.show()
def Funcion4 (valor_a,valor_b,valor_c,valor_d,valor_e):
    fig, ax = plt.subplots()
    x = np.linspace(-10.0, 10.0, 1000)
    #Se le asigan un valor a y par luego ser sustituido
    y = 0
    #Se establecen parametros en el eje
    ax.axis([x[0], x[-1], x[0], x[-1]])
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['left']
    ax.spines['bottom']
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ticks = []
    #Evalua posibles valores de x
    for i in range(int(x[0]), int(x[-1] + 1), 1):
        ticks.append(i)
    ticks.remove(0)
    #Se configura los ejes "X" y "Y"
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    #Se asigna un titulo
    plt.title(u'Calculadora graficadora')
    plt.suptitle(u'Z-Fun')
    plt.rc('font', size = 15)  
    plt.plot(0,1)
    ax.grid(color='#ECECEC', linestyle='-', linewidth=1)
    #Ecuacion de la funcion
    y = (valor_a)*(x**(4)) + ((valor_b)*(x**(3))) + ((valor_c)*(x**(2))) + (valor_d)*(x) + valor_e
    ax.plot(x,y)
    #Se grafica
    plt.show()
def Funcion5 (valor_a,valor_b,valor_c,valor_d,valor_e,valor_f):
    fig, ax = plt.subplots()
    x = np.linspace(-10.0, 10.0, 1000)
    #Se le asigan un valor a y par luego ser sustituido
    y = 0
    ax.axis([x[0], x[-1], x[0], x[-1]])
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['left']
    ax.spines['bottom']
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ticks = []
    #Evalua posibles valores de x
    for i in range(int(x[0]), int(x[-1] + 1), 1):
        ticks.append(i)
    ticks.remove(0)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    plt.title(u'Calculadora graficadora')
    plt.suptitle(u'Z-Fun')
    plt.rc('font', size = 15)  
    plt.plot(0,1)
    ax.grid(color='#ECECEC', linestyle='-', linewidth=1)
    #Ecuacion de la funcion
    y = (valor_a)*(x**(5)) + (valor_b)*(x**(4)) + (valor_c)*(x**(3)) + (valor_d)*(x**(2)) + (valor_e)*(x) +(valor_f)
    #Grafica
    ax.plot(x,y)
    plt.show()

