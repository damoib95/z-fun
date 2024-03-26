#Algoritmos y programacion basica
#Seccion 30
#22-05-2014
#Diego Morales 14012
#Z-Fun 2.0
#Programa que calcula ceros racionales de funciones polinomiales
#y graficadora
#Modulo Principal Z-Fun 2.0
#Este modulo posee todas las funciones del programa, desde este modulo
#se piden los datos que seran enviados como parametros a las diferentes
#funciones de los modulos para llevar efectuar un proceso

#Importacion del modulo Factores que devuelve los ceros de la funcion polinomial
import Factores
#Importacion del modulo Inicio que posee el menu de inicio y presentacion del programa
import Inicio
#Importacion del modulo Funcion que grafica los parametros enviados de las funciones
import Funcion
import smtplib
import poplib
from random import randint
import sys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.parser import Parser

import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import numpy as np
import os

def enviargrafica():
    #Mensaje Compuesto
    mensaje=MIMEMultipart()
    mensaje['From']=servidor
    mensaje['To']=cliente
    mensaje['Subject']="Grafica"
    #Adjuntar Texto
    mensaje.attach(MIMEText("""Texto"""))
    #Adjuntar Imagen
    file=open(os.getcwd()+Grafica,"rb")
    contenido=MIMEImage(file.read())
    contenido.add_header('Content-Disposition', 'attachment; filename ='+Grafica)
    mensaje.attach(contenido)
    #Enviar Mensaje
    mailServer.sendmail(servidor,
                        cliente,
                        mensaje.as_string())
def nombre():
    name=""
    while len(name)<10:
        x=randint(0, 9)
        name+=str(x)
    name+=".jpg"
    return name

#Imprime el titulo del programa
print(Inicio.title())
#Presentacion al usuario del programa
print("\nBienvenido a ZFun, la calculadora de ceros racionales de ")
print("funciones polinomiales y graficadora\n")

#Mientras que el programa este encendido, aparece el menu y se selecciona una opcion
Program=True 
while Program==True:    
    #Menu de grados de funciones polinomiales
    Inicio.menugrados()

    #Ingresar el grado de la funcion
    grado=int(input("\n Seleccione una opcion (1-7):"))
    
    #Si la funcion es de grado 1
    #Se ingresan los valores de la funcion
    if grado==1:
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:[a]X + ind")
        a1=float(input("Valor coeficiente a de X: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a1),"X + [ind]")
        ind=float(input("Valor independiente: "))
        #Imprime la funcion ingresada
        print("------------\n| Funcion: |",(a1),"X +",(ind),"\n------------")
        Inicio.cargando()
        print("\nCeros:")
        #Se muestran los ceros de la funcion, si los hay
        Factores1=Factores.funcion1(a1,ind)
        #Grafica la funcion ingresada
        Funcion.Funcion(a1,ind)
        print("\nFinalizado")
        print("\n_____________\n")

    #Si la funcion es de grado 2
    #Se ingresan los valores de la funcion
    if grado==2:
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:[a]X2 + bX + ind")
        a2=float(input("Valor coeficiente a de X a la 2: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a2),"X2 +[b]X + ind")
        a1=float(input("Valor coeficiente b de X: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a2),"X2 +",(a1),"X + [ind]")
        ind=float(input("Valor independiente: "))
        #Imprime la funcion ingresada
        print("------------\n| Funcion: |",(a2),"X2 +",(a1),"X +",(ind),"\n------------")
        Inicio.cargando()
        print("\nCeros:")
        #Se muestran los ceros de la funcion, si los hay
        Factores2= Factores.funcion2(a2,a1,ind)
        #Grafica la funcion ingresada
        Funcion.Funcion2(a2,a1,ind)
        print("\nFinalizado")
        print("\n_____________\n")

    #Si la funcion es de grado 3
    #Se ingresan los valores de la funcion
    if grado==3:
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:[a]X3 + bX2 + cX + ind")
        a3=float(input("Valor coeficiente a de X a la 3: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a3),"X3 + [b]X2 + cX +ind")
        a2=float(input("Valor coeficiente b de X a la 2: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a3),"X3 + ",(a2),"X2 + [c]X +ind")
        a1=float(input("Valor coeficiente c de X: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a3),"X3 + ",(a2),"X2 + ",(a1),"X +[ind]")
        ind=float(input("Valor independiente: "))
        #Imprime la funcion ingresada
        print("------------\n| Funcion: |",(a3),"X3 +",(a2),"X2 +",(a1),"X +",(ind),"\n------------")
        Inicio.cargando()
        print("\nCeros:")
        #Se muestran los ceros de la funcion, si los hay
        Factores3= Factores.funcion3(a3,a2,a1,ind)
        #Grafica la funcion ingresada
        Funcion.Funcion3(a3,a2,a1,ind)
        print("\nFinalizado")
        print("\n_____________\n")

    #Si la funcion es de grado 4
    #Se ingresan los valores de la funcion
    if grado==4:
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:[a]x4 + bx3 + cx2 + dx + ind")
        a4=float(input("Valor coeficiente a de X a la 4: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a4),"x4 + [b]x3 + cx2 + dx + ind")
        a3=float(input("Valor coeficiente b de X a la 3: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a4),"x4 + ",(a3),"x3 + [c]x2 + dx + ind")
        a2=float(input("Valor coeficiente c de X a la 2: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a4),"x4 + ",(a3),"x3 + ",(a2),"x2 + [d]x + ind")
        a1=float(input("Valor coeficiente d de X: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a4),"x4 + ",(a3),"x3 +",(a2),"x2 + ",(a1),"x + [ind]")
        ind=float(input("Valor independiente: "))
        #Imprime la funcion ingresada
        print("------------\n| Funcion: |",(a4),"X4 +",(a3),"X3 +",(a2),"X2 +",(a1),"X +",(ind),"\n------------")
        Inicio.cargando()
        print("\nCeros:")
        #Se muestran los ceros de la funcion, si los hay
        Factores4= Factores.funcion4(a4,a3,a2,a1,ind)
        #Grafica la funcion ingresada
        Funcion.Funcion4(a4,a3,a2,a1,ind)
        print("\nFinalizado")
        print("\n_____________\n")


    #Si la funcion es de grado 5
    #Se ingresan los valores de la funcion
    if grado==5:
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:[a]x5 + bx4 + cx3 + dx2 + ex + ind")
        a5=float(input("Valor coeficiente a de X a la 5: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a5),"x5 + [b]x4 + cx3 + dx2 + ex + ind")
        a4=float(input("Valor coeficiente b de X a la 4: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a5),"x5 + ",(a4),"x4 + [c]x3 + dx2 + ex + ind")
        a3=float(input("Valor coeficiente c de X a la 3: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a5),"x5 + ",(a4),"x4 + ",(a3),"x3 + [d]x2 + ex + ind")
        a2=float(input("Valor coeficiente d de X a la 2: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a5),"x5 + ",(a4),"x4 + ",(a3),"x3 + ",(a2),"x2 + [e]x + ind")
        a1=float(input("Valor coeficiente e de X: "))
        #Se imprime la funcion indicando el dato a asignar
        print("\nFuncion:",(a5),"x5 + ",(a4),"x4 + ",(a3),"x3 + ",(a2),"x2 + ",(a1),"x + [ind]")
        ind=float(input("Valor independiente: "))
        #Imprime la funcion ingresada
        print("------------\n| Funcion: |",(a5),"X5 +",(a4),"X4 +",(a3),"X3 +",(a2),"X2 +",(a1),"X +",(ind),"\n------------")
        Inicio.cargando()
        print("\nCeros:")
        #Se muestran los ceros de la funcion, si los hay
        Factores5= Factores.funcion5(a5,a4,a3,a2,a1,ind)
        #Grafica la funcion ingresada
        Funcion.Funcion5(a5,a4,a3,a2,a1,ind)
        print("\nFinalizado")
        print("\n_____________\n")

    #Finalizar programa
    if grado==6:
        print('deprecated')
        print('Starting on September 30, 2024, less secure apps, third-party apps, or devices that have you sign in with only your username and password will no longer be supported for Google Workspace accounts.')      
        #deprecated            
        ###CONEXION AL SERVIDOR GMAIL
        #Correos servidor y cliente
        # servidor="servidorzfun@gmail.com"
        # cliente="clientezfun@gmail.com"
        # contrasena="zfun2014"
        # #Conexion con el servidor smtp Gmail
        # mailServer=smtplib.SMTP('smtp.gmail.com',587)
        # mailServer.ehlo()
        # mailServer.starttls()
        # mailServer.ehlo()
        # mailServer.login(servidor,contrasena)

        # print(mailServer.ehlo())

        # SERVER=False
        # while SERVER==False:
        #     print("Esperando conexion")
        #     m=poplib.POP3_SSL('pop.gmail.com',995)
        #     m.user(servidor)
        #     m.pass_(contrasena)
        #     numero=len(m.list()[1])
        #     if numero>0:
        #         Grafica=nombre()
        #         for i in range(numero):
        #             print("\nMensaje numero"+str(i+1))
        #             print("---------")
        #             response, headerLines, bytes= m.retr(i+1)
        #             mensaje='\n'.join(headerLines)
        #             p=Parser()
        #             email=p.parsestr(mensaje)
        #             #Imprime from, to y subject
        #             print("From: "+str(email["From"]))
        #             print("To: "+str(email["To"]))
        #             print("Subject: "+str(email["Subject"]))
        #             #print("ID: "+email['message-id']
        #             print("\n ---Funcion recibida---\n")
                    
        #             ###FUNCIONES
                    
        #             #Si el subject es Funcion Lineal                                
        #             if email["Subject"]=="Funcion Lineal":
        #                 for part in email.get_payload():
        #                     tipo=part.get_content_type()
        #                     if ("text/plain" ==tipo):
        #                         #FUNCION LINEAL ENCONTRADA
        #                         funcionlinealencontrada= part.get_payload(decode=True)
        #                         print(funcionlinealencontrada)
        #                         aON=True
        #                         bON=False
        #                         stringa=""
        #                         stringb=""
        #                         #RECOGER INT DE STR
        #                         ###NEEDS WORK
        #                         for i in funcionlinealencontrada:
        #                             if aON==True:
        #                                 if aON==True:
        #                                     if i!=" ":
        #                                         stringa+=i
        #                                     if i==" ":
        #                                         a=int(stringa)
        #                                         aON=False
        #                                         i="0"
        #                                         bON=True
        #                             if bON==True:
        #                                 stringb+=i
        #                                 b=int(stringb)                               
        #                         print("Funcion lineal encontrada")
        #                         #Se crea la figura
        #                         fig, ax = plt.subplots()
        #                         #Se define el parametro del color de margen de la figura
        #                         fig.patch.set_facecolor('white')
        #                         #Se define el rango del eje x de -10 a 10
        #                         x = np.linspace(-10.0, 10.0, 1000)
        #                         #Se establecen parametros en el eje
        #                         ax.axis([x[0], x[-1], x[0], x[-1]])
        #                         #Se establecen los parametros de posicion de los ejes
        #                         ax.spines['left'].set_position('center')
        #                         ax.spines['bottom'].set_position('center')
        #                         #Se establecen los parametros de color de los ejes
        #                         ax.spines['left'].set_color('red')
        #                         ax.spines['bottom'].set_color('red')
        #                         #Se establecen los parametros de color de los numeros de los ejes
        #                         ax.tick_params(axis='x', colors='green')
        #                         ax.tick_params(axis='y', colors='green')
        #                         #Se establece la posicion de los numeros
        #                         ax.xaxis.set_ticks_position('bottom')
        #                         ax.yaxis.set_ticks_position('left')
        #                         ticks = []
        #                         #Se evaluan los valores de x
        #                         for i in range(int(x[0]), int(x[-1] + 1), 1):
        #                             ticks.append(i)
        #                         ticks.remove(0)
        #                         #Se configuran los ejes X y Y
        #                         ax.set_xticks(ticks)
        #                         ax.set_yticks(ticks)
        #                         #Se asigna la fuente y tamano de los textos
        #                         matplotlib.rc('font', family='sans-serif') 
        #                         matplotlib.rc('font', serif='Helvetica Neue') 
        #                         matplotlib.rc('text', usetex='false') 
        #                         matplotlib.rcParams.update({'font.size': 8})
        #                         #Se escribe el titulo de la grafica y su fuente
        #                         plt.suptitle(u'Z-Fun', fontsize=20, color='black')
        #                         #Se establen los parametros de la cuadricula
        #                         ax.grid(color='#a5a5a5', linestyle='-', linewidth=1)
        #                         #Se define el color del fondo de la grafica
        #                         ax.patch.set_facecolor('white')
        #                         #Se define el string de la ecuacion
        #                         FuncionLineal=str(a)+"x +"+str(b)
        #                         #Se escribe la ecuacion en la grafica
        #                         plt.title(FuncionLineal, fontsize=14, color='black')
        #                         #Ecuacion de la funcion
        #                         y = ((a)*(x)) + (b)
        #                         #Se grafica
        #                         ax.plot(x, y, 'b', linewidth=2)
        #                         savefig(Grafica)
        #                         #plt.show()
        #                 enviargrafica()
        #                 print("\n---Funcion enviada---\n")
        #                 m.quit()

                        
        #             #Si el subject es Funcion Cuadratica                               
        #             if email["Subject"]=="Funcion Cuadratica":
        #                 for part in email.get_payload():
        #                     tipo=part.get_content_type()
        #                     if ("text/plain" ==tipo):
        #                         #Funcion cuadratica encontrada
        #                         funcioncuadraticaencontrada= part.get_payload(decode=True)
        #                         print(funcioncuadraticaencontrada)
        #                         aON=True
        #                         bON=False
        #                         cON=False
        #                         stringa=""
        #                         stringb=""
        #                         stringc=""
        #                         #RECOGER INT DE STR
        #                         ###NEEDS WORK
        #                         for i in funcioncuadraticaencontrada:
        #                             if aON==True:
        #                                 if i!=" ":
        #                                     stringa+=i
        #                                 if i==" ":
        #                                     a=int(stringa)
        #                                     aON=False
        #                                     i="0"
        #                                     bON=True
        #                             if bON==True:
        #                                 if i!=" ":
        #                                     stringb+=i
        #                                 if i==" ":
        #                                     b=int(stringb)
        #                                     bON=False
        #                                     i="0"
        #                                     cON=True
        #                             if cON==True:
        #                                 stringc+=i
        #                                 c=int(stringc)
        #                         print("Funcion cuadratica encontrada")
        #                         #Se crea la figura
        #                         fig, ax = plt.subplots()
        #                         #Se define el parametro del color de margen de la figura
        #                         fig.patch.set_facecolor('white')
        #                         #Se define el rango del eje x de -10 a 10
        #                         x = np.linspace(-10.0, 10.0, 1000)
        #                         #Se establecen parametros en el eje
        #                         ax.axis([x[0], x[-1], x[0], x[-1]])
        #                         #Se establecen los parametros de posicion de los ejes
        #                         ax.spines['left'].set_position('center')
        #                         ax.spines['bottom'].set_position('center')
        #                         #Se establecen los parametros de color de los ejes
        #                         ax.spines['left'].set_color('red')
        #                         ax.spines['bottom'].set_color('red')
        #                         #Se establecen los parametros de color de los numeros de los ejes
        #                         ax.tick_params(axis='x', colors='green')
        #                         ax.tick_params(axis='y', colors='green')
        #                         #Se establece la posicion de los numeros
        #                         ax.xaxis.set_ticks_position('bottom')
        #                         ax.yaxis.set_ticks_position('left')
        #                         ticks = []
        #                         #Se evaluan los valores de x
        #                         for i in range(int(x[0]), int(x[-1] + 1), 1):
        #                             ticks.append(i)
        #                         ticks.remove(0)
        #                         #Se configuran los ejes X y Y
        #                         ax.set_xticks(ticks)
        #                         ax.set_yticks(ticks)
        #                         #Se asigna la fuente y tamano de los textos
        #                         matplotlib.rc('font', family='sans-serif') 
        #                         matplotlib.rc('font', serif='Helvetica Neue') 
        #                         matplotlib.rc('text', usetex='false') 
        #                         matplotlib.rcParams.update({'font.size': 8})
        #                         #Se escribe el titulo de la grafica y su fuente
        #                         plt.suptitle(u'Z-Fun', fontsize=20, color='black')
        #                         #Se establen los parametros de la cuadricula
        #                         ax.grid(color='#a5a5a5', linestyle='-', linewidth=1)
        #                         #Se define el color del fondo de la grafica
        #                         ax.patch.set_facecolor('white')
        #                         #Se define el string de la ecuacion
        #                         FuncionCuadratica=str(a)+"x2 +"+str(b)+"x +"+str(c)
        #                         #Se escribe la ecuacion en la grafica
        #                         plt.title(FuncionCuadratica, fontsize=14, color='black')
        #                         #Ecuacion de la funcion
        #                         y = (a)*(x**(2)) + (b)*x + c
        #                         #Se grafica
        #                         ax.plot(x, y, 'b', linewidth=2)
        #                         savefig(Grafica)
        #                         #plt.show()
        #                 enviargrafica()
        #                 print("\n---Funcion enviada---\n")
        #                 m.quit()


                        
        #             #Si el subject es Funcion Tercer Grado                                
        #             if email["Subject"]=="Funcion Tercer Grado":
        #                 for part in email.get_payload():
        #                     tipo=part.get_content_type()
        #                     if ("text/plain" ==tipo):
        #                         #FUNCION TERCER GRADO ENCONTRADA
        #                         funciontercergradoencontrada= part.get_payload(decode=True)
        #                         print(funciontercergradoencontrada)
        #                         aON=True
        #                         bON=False
        #                         cON=False
        #                         dON=False
        #                         stringa=""
        #                         stringb=""
        #                         stringc=""
        #                         stringd=""
        #                         #RECOGER INT DE STR
        #                         ###NEEDS WORK
        #                         for i in funciontercergradoencontrada:
        #                             if aON==True:
        #                                 if i!=" ":
        #                                     stringa+=i
        #                                 if i==" ":
        #                                     a=int(stringa)
        #                                     aON=False
        #                                     i="0"
        #                                     bON=True
        #                             if bON==True:
        #                                 if i!=" ":
        #                                     stringb+=i
        #                                 if i==" ":
        #                                     b=int(stringb)
        #                                     bON=False
        #                                     i="0"
        #                                     cON=True
        #                             if cON==True:
        #                                 if i!=" ":
        #                                     stringc+=i
        #                                 if i==" ":
        #                                     c=int(stringc)
        #                                     cON=False
        #                                     i="0"
        #                                     dON=True
        #                             if dON==True:
        #                                 stringd+=i
        #                                 d=int(stringd)                              
        #                         print("Funcion de tercer grado encontrada")
        #                          #Se crea la figura
        #                         fig, ax = plt.subplots()
        #                         #Se define el parametro del color de margen de la figura
        #                         fig.patch.set_facecolor('white')
        #                         #Se define el rango del eje x de -10 a 10
        #                         x = np.linspace(-10.0, 10.0, 1000)
        #                         #Se establecen parametros en el eje
        #                         ax.axis([x[0], x[-1], x[0], x[-1]])
        #                         #Se establecen los parametros de posicion de los ejes
        #                         ax.spines['left'].set_position('center')
        #                         ax.spines['bottom'].set_position('center')
        #                         #Se establecen los parametros de color de los ejes
        #                         ax.spines['left'].set_color('red')
        #                         ax.spines['bottom'].set_color('red')
        #                         #Se establecen los parametros de color de los numeros de los ejes
        #                         ax.tick_params(axis='x', colors='green')
        #                         ax.tick_params(axis='y', colors='green')
        #                         #Se establece la posicion de los numeros
        #                         ax.xaxis.set_ticks_position('bottom')
        #                         ax.yaxis.set_ticks_position('left')
        #                         ticks = []
        #                         #Se evaluan los valores de x
        #                         for i in range(int(x[0]), int(x[-1] + 1), 1):
        #                             ticks.append(i)
        #                         ticks.remove(0)
        #                         #Se configuran los ejes X y Y
        #                         ax.set_xticks(ticks)
        #                         ax.set_yticks(ticks)
        #                         #Se asigna la fuente y tamano de los textos
        #                         matplotlib.rc('font', family='sans-serif') 
        #                         matplotlib.rc('font', serif='Helvetica Neue') 
        #                         matplotlib.rc('text', usetex='false') 
        #                         matplotlib.rcParams.update({'font.size': 8})
        #                         #Se escribe el titulo de la grafica y su fuente
        #                         plt.suptitle(u'Z-Fun', fontsize=20, color='black')
        #                         #Se establen los parametros de la cuadricula
        #                         ax.grid(color='#a5a5a5', linestyle='-', linewidth=1)
        #                         #Se define el color del fondo de la grafica
        #                         ax.patch.set_facecolor('white')
        #                         #Se define el string de la ecuacion
        #                         FuncionTercerGrado=str(a)+"x3 +"+str(b)+"x2 +"+str(c)+"x +"+str(d)
        #                         #Se escribe la ecuacion en la grafica
        #                         plt.title(FuncionTercerGrado, fontsize=14, color='black')
        #                         #Ecuacion de la funcion
        #                         y = (a)*(x**(3)) + (b)*(x**(2)) + (c)*(x) + (d)
        #                         #Se grafica
        #                         ax.plot(x, y, 'b', linewidth=2)
        #                         savefig(Grafica)
        #                         #plt.show()
        #                 enviargrafica()
        #                 print("\n---Funcion enviada---\n")
        #                 m.quit()


                        
        #             #Si el subject es Funcion Cuarto Grado                               
        #             if email["Subject"]=="Funcion Cuarto Grado":
        #                 for part in email.get_payload():
        #                     tipo=part.get_content_type()
        #                     if ("text/plain" ==tipo):
        #                         #FUNCION CUARTO GRADO ENCONTRADA
        #                         funcioncuartogradoencontrada= part.get_payload(decode=True)
        #                         print(funcioncuartogradoencontrada)
        #                         aON=True
        #                         bON=False
        #                         cON=False
        #                         dON=False
        #                         eON=False
        #                         stringa=""
        #                         stringb=""
        #                         stringc=""
        #                         stringd=""
        #                         stringe=""
        #                         #RECOGER INT DE STR
        #                         ###NEEDS WORK
        #                         for i in funcioncuartogradoencontrada:
        #                             if aON==True:
        #                                 if i!=" ":
        #                                     stringa+=i
        #                                 if i==" ":
        #                                     a=int(stringa)
        #                                     aON=False
        #                                     i="0"
        #                                     bON=True
        #                             if bON==True:
        #                                 if i!=" ":
        #                                     stringb+=i
        #                                 if i==" ":
        #                                     b=int(stringb)
        #                                     bON=False
        #                                     i="0"
        #                                     cON=True
        #                             if cON==True:
        #                                 if i!=" ":
        #                                     stringc+=i
        #                                 if i==" ":
        #                                     c=int(stringc)
        #                                     cON=False
        #                                     i="0"
        #                                     dON=True
        #                             if dON==True:
        #                                 if i!=" ":
        #                                     stringd+=i
        #                                 if i==" ":
        #                                     d=int(stringd)
        #                                     dON=False
        #                                     i="0"
        #                                     eON=True
        #                             if eON==True:
        #                                 stringe+=i
        #                                 E=int(stringe)                               
        #                         print("Funcion de cuarto grado encontrada")
        #                         #Se crea la figura
        #                         fig, ax = plt.subplots()
        #                         #Se define el parametro del color de margen de la figura
        #                         fig.patch.set_facecolor('white')
        #                         #Se define el rango del eje x de -10 a 10
        #                         x = np.linspace(-10.0, 10.0, 1000)
        #                         #Se establecen parametros en el eje
        #                         ax.axis([x[0], x[-1], x[0], x[-1]])
        #                         #Se establecen los parametros de posicion de los ejes
        #                         ax.spines['left'].set_position('center')
        #                         ax.spines['bottom'].set_position('center')
        #                         #Se establecen los parametros de color de los ejes
        #                         ax.spines['left'].set_color('red')
        #                         ax.spines['bottom'].set_color('red')
        #                         #Se establecen los parametros de color de los numeros de los ejes
        #                         ax.tick_params(axis='x', colors='green')
        #                         ax.tick_params(axis='y', colors='green')
        #                         #Se establece la posicion de los numeros
        #                         ax.xaxis.set_ticks_position('bottom')
        #                         ax.yaxis.set_ticks_position('left')
        #                         ticks = []
        #                         #Se evaluan los valores de x
        #                         for i in range(int(x[0]), int(x[-1] + 1), 1):
        #                             ticks.append(i)
        #                         ticks.remove(0)
        #                         #Se configuran los ejes X y Y
        #                         ax.set_xticks(ticks)
        #                         ax.set_yticks(ticks)
        #                         #Se asigna la fuente y tamano de los textos
        #                         matplotlib.rc('font', family='sans-serif') 
        #                         matplotlib.rc('font', serif='Helvetica Neue') 
        #                         matplotlib.rc('text', usetex='false') 
        #                         matplotlib.rcParams.update({'font.size': 8})
        #                         #Se escribe el titulo de la grafica y su fuente
        #                         plt.suptitle(u'Z-Fun', fontsize=20, color='black')
        #                         #Se establen los parametros de la cuadricula
        #                         ax.grid(color='#a5a5a5', linestyle='-', linewidth=1)
        #                         #Se define el color del fondo de la grafica
        #                         ax.patch.set_facecolor('white')
        #                         #Se define el string de la ecuacion
        #                         FuncionCuartoGrado=str(a)+"x4 +"+str(b)+"x3 +"+str(c)+"x2 +"+str(d)+"x +"+str(E)
        #                         #Se escribe la ecuacion en la grafica
        #                         plt.title(FuncionCuartoGrado, fontsize=14, color='black')
        #                         #Ecuacion de la funcion
        #                         y = (a)*(x**(4)) + (b)*(x**(3)) + (c)*(x**(2)) + (d)*(x) + (E)
        #                         #Se grafica
        #                         ax.plot(x, y, 'b', linewidth=2)
        #                         savefig(Grafica)
        #                         #plt.show()
        #                 enviargrafica()
        #                 print("\n---Funcion enviada---\n")
        #                 m.quit()


                        
        #             #Si el subject es Funcion Quinto Grado                               
        #             if email["Subject"]=="Funcion Quinto Grado":
        #                 for part in email.get_payload():
        #                     tipo=part.get_content_type()
        #                     if ("text/plain" ==tipo):
        #                         #FUNCION QUINTO GRADO ENCONTRADA
        #                         funcionquintogradoencontrada= part.get_payload(decode=True)
        #                         print(funcionquintogradoencontrada)
        #                         aON=True
        #                         bON=False
        #                         cON=False
        #                         dON=False
        #                         eON=False
        #                         fON=False
        #                         stringa=""
        #                         stringb=""
        #                         stringc=""
        #                         stringd=""
        #                         stringE=""
        #                         stringf=""
        #                         #RECOGER INT DE STR
        #                         ###NEEDS WORK
        #                         for i in funcionquintogradoencontrada:
        #                             if aON==True:
        #                                 if i!=" ":
        #                                     stringa+=i
        #                                 if i==" ":
        #                                     a=int(stringa)
        #                                     aON=False
        #                                     i="0"
        #                                     bON=True
        #                             if bON==True:
        #                                 if i!=" ":
        #                                     stringb+=i
        #                                 if i==" ":
        #                                     b=int(stringb)
        #                                     bON=False
        #                                     i="0"
        #                                     cON=True
        #                             if cON==True:
        #                                 if i!=" ":
        #                                     stringc+=i
        #                                 if i==" ":
        #                                     c=int(stringc)
        #                                     cON=False
        #                                     i="0"
        #                                     dON=True
        #                             if dON==True:
        #                                 if i!=" ":
        #                                     stringd+=i
        #                                 if i==" ":
        #                                     d=int(stringd)
        #                                     dON=False
        #                                     i="0"
        #                                     eON=True
        #                             if eON==True:
        #                                 if i!=" ":
        #                                     stringE+=i
        #                                 if i==" ":
        #                                     E=int(stringE)
        #                                     eON=False
        #                                     i="0"
        #                                     fON=True
        #                             if fON==True:
        #                                 stringf+=i
        #                                 f=int(stringf)
        #                         print("Funcion de quinto grado encontrada")
        #                         #Se crea la figura
        #                         fig, ax = plt.subplots()
        #                         #Se define el parametro del color de margen de la figura
        #                         fig.patch.set_facecolor('white')
        #                         #Se define el rango del eje x de -10 a 10
        #                         x = np.linspace(-10.0, 10.0, 1000)
        #                         #Se establecen parametros en el eje
        #                         ax.axis([x[0], x[-1], x[0], x[-1]])
        #                         #Se establecen los parametros de posicion de los ejes
        #                         ax.spines['left'].set_position('center')
        #                         ax.spines['bottom'].set_position('center')
        #                         #Se establecen los parametros de color de los ejes
        #                         ax.spines['left'].set_color('red')
        #                         ax.spines['bottom'].set_color('red')
        #                         #Se establecen los parametros de color de los numeros de los ejes
        #                         ax.tick_params(axis='x', colors='green')
        #                         ax.tick_params(axis='y', colors='green')
        #                         #Se establece la posicion de los numeros
        #                         ax.xaxis.set_ticks_position('bottom')
        #                         ax.yaxis.set_ticks_position('left')
        #                         ticks = []
        #                         #Se evaluan los valores de x
        #                         for i in range(int(x[0]), int(x[-1] + 1), 1):
        #                             ticks.append(i)
        #                         ticks.remove(0)
        #                         #Se configuran los ejes X y Y
        #                         ax.set_xticks(ticks)
        #                         ax.set_yticks(ticks)
        #                         #Se asigna la fuente y tamano de los textos
        #                         matplotlib.rc('font', family='sans-serif') 
        #                         matplotlib.rc('font', serif='Helvetica Neue') 
        #                         matplotlib.rc('text', usetex='false') 
        #                         matplotlib.rcParams.update({'font.size': 8})
        #                         #Se escribe el titulo de la grafica y su fuente
        #                         plt.suptitle(u'Z-Fun', fontsize=20, color='black')
        #                         #Se establen los parametros de la cuadricula
        #                         ax.grid(color='#a5a5a5', linestyle='-', linewidth=1)
        #                         #Se define el color del fondo de la grafica
        #                         ax.patch.set_facecolor('white')
        #                         #Ecuacion de la funcion
        #                         y = (a)*(x**(5)) + (b)*(x**(4)) + (c)*(x**(3)) + (d)*(x**(2)) + (E)*(x) + (f)
        #                         #Se define el string de la ecuacion
        #                         FuncionQuintoGrado=str(a)+"x5 +"+str(b)+"x4 +"+str(c)+"x3 +"+str(d)+"x2 +"+str(E)+"x +"+str(f)
        #                         #Se escribe la ecuacion en la grafica
        #                         plt.title(FuncionQuintoGrado, fontsize=14, color='black')
        #                         #Se grafica
        #                         ax.plot(x, y, 'b', linewidth=2)
        #                         savefig(Grafica)
        #                         #plt.show()
        #                 enviargrafica()
        #                 print("\n---Funcion enviada---\n")
        #                 m.quit()

    if grado==7:        
        #Se imprime programa finalizado y deja de aparecer el menu
        print("Programa finalizado")
        sys.exit
        Program=False

