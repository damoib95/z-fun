#Algoritmos y programacion basica
#Seccion 30
#02-04-2014
#Diego Morales, 14012
#Bryan Santos
#Maria Fonseca, 13691
#Z-Fun
#Programa que calcula ceros racionales de funciones polinomiales
#y graficadora
#Modulo Inicio
#Este modulo imprime el nombre del programa y version, ademas muestra las
#opciones del programa, y un texto de cargando


#Importacion de modulo del sistema
import sys
#importacion de modulo tiempo de Phython
import time

#Funcion que imprime el nombre del programa y version al iniciar
def title():
    print"  _____      ______            "
    print" |___  /    |  ____|           "
    print"    / /_____| |__ _   _ _ __   "
    print"   / /______|  __| | | | '_ \  "
    print"  / /__     | |  | |_| | | ||  "
    print" /_____|    |_|   \__,_|_| |_| "
    return "Version 2.0 - 2014\n"
                               
#Funcion que muestra las posibles opciones del programa
def menugrados():
    print "1 Funcion lineal: ax + b"
    print "2 Funcion cuadratica: ax2 + bx + c"
    print "3 Funcion de tercer grado: ax3 + bx2 + cx + d"
    print "4 Funcion de cuarto grado: ax4 + bx3 + cx2 + dx + e"
    print "5 Funcion de quinto grado: ax5 + bx4 + cx3 + dx2 + ex + f"
    print "6 Servidor para Z-Fun4A 2.0"
    print "7 Salir del programa"
    return ""

#Funcion que simula un texto de cargando
def cargando():
    #Se escribe cargando al inicio
    sys.stdout.write('Cargando')
    #Se cierra la cadena
    sys.stdout.flush()
    #Por tres espacios se realiza lo siguiente
    for _ in range(3):
        #Espera 0.1 de tiempo
        time.sleep(0.1)
        #Abre la cadena y agrega un punto
        sys.stdout.write('.')
        #Cierra la cadena
        sys.stdout.flush()
    
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 

