#Z-Fun4A 2.0
#DIEGO MORALES 14012

####Z-Fun4A 2.0
#---Ingreso por texto o vox
#---Interfaz grafica para android
#---Fondo animado de matrix
#---Trabaja con funciones de hasta quinto grado
#---Encuentra los ceros P/S de la funcion (si los hay)
#---*Genera graficas enviandolas a Z-Fun2.0 (PC/MAC) utilizando la opcion de Servidor
#*Se requiere de acceso  internet y un servidor Z-Fun 2.0 para graficar

#Algoritmos y programacion basica
#Seccion 30
#20-05-2014
#Z-Fun4A 2.0
#Programa que calcula ceros racionales de funciones polinomiales y graficadora
#Modulo Z-Fun4A 2.0
#Este modulo posee todas las funciones del programa, desde este modulo
#se piden los datos que seran enviados como parametros a las diferentes
#funciones para efectuar un proceso

import sys
import time
import random
import smtplib
import poplib
import mimetypes

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.parser import Parser
from android import Android
droid=Android()

#Funcion que imprime el nombre del programa y version al iniciar
def title():
    matrix()
    droid.dialogCreateAlert(
        'Z-Fun4A',
        'Version 2.0 - 2014')
    droid.dialogSetPositiveButtonText('Iniciar')
    droid.dialogShow()                           
    #droid.ttsSpeak('Bienvenido a zifon 0.7 para Android')
    response= droid.dialogGetResponse().result
    droid.dialogDismiss()
    if not 'which' in response or response['which']!='positive':
        #droid.ttsSpeak('Hasta luego')
        return False
    else:
        return True

#Funcion que imprime un fondo de numeros y letras aleatorias
def matrix():
    On=True
    ContadorON=0
    while On==True:
        x=""
        if ContadorON<1500:
            while len(x)<49:
                x+=random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")
                ContadorON+=1
            print x
        else:
            print "Diego Morales"
            On=False
            
#Funcion que muestra la informacion del programa
def informacion():
    matrix()
    droid.dialogCreateAlert(
        'Informacion',
        'Version 2.0 - 2014\nDiego Morales\nmor14012@uvg.edu.gt')
    droid.dialogSetPositiveButtonText('Ok')
    droid.dialogShow()                           
    response= droid.dialogGetResponse().result
    droid.dialogDismiss()

#Funcion que muestra informacion sobre la graficadora
def informaciongraficar():
    droid.dialogCreateAlert(
        'Advertencia',
        'Para graficar funciones polinomiales se requiere:\n1. Z-Fun2.0 (PC/MAC) en la opcion de servidor\n2. Conexion a internet (ambos dispositivos)')
    droid.dialogSetPositiveButtonText('Entendido')
    droid.dialogShow()                           
    response= droid.dialogGetResponse().result
    droid.dialogDismiss()

#Funcion que muestra el menu de opciones
def menuopcion():
    matrix()
    droid.dialogCreateAlert('Opciones')
    droid.dialogSetItems(['Metodo de entrada', 'Graficar', 'Informacion'])
    droid.dialogShow()
    response=droid.dialogGetResponse().result
    droid.dialogDismiss()
    return response['item']
    
#Funcion que conecta al cliente al servidor de ZFun, enviar la funcion
#seleccionada. El Subject indica el grado de la funcion y el mensaje
#contiene los coeficientes de la funcion como string.
#Luego espera por la respuesta del servidor. Guarda la imagen y la muestra
def enviarserver(x,y):
    droid.dialogCreateSpinnerProgress('Generando Grafica', 'Conectando al servidor')
    droid.dialogShow()
    #Correos servidor y cliente
    servidor="servidorzfun@gmail.com"
    cliente="clientezfun@gmail.com"
    contrasena="zfun2014"
    #Conexion con el servidor smtp Gmail
    mailServer=smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(cliente,contrasena)
    #print mailServer.ehlo()
    droid.dialogDismiss()
    droid.dialogCreateSpinnerProgress('Generando Grafica', 'Enviando funcion')
    droid.dialogShow()
    #Mensaje Compuesto
    mensaje=MIMEMultipart()
    mensaje['From']=cliente
    mensaje['To']=servidor
    mensaje['Subject']=x
    #Adjuntar Texto
    mensaje.attach(MIMEText(y))
    #Enviar Mensaje
    mailServer.sendmail(cliente,
                        servidor,
                        mensaje.as_string())
    #Esperar por respuesta, guardar y generar grafica
    droid.dialogDismiss()
    droid.dialogCreateSpinnerProgress('Generando Grafica', 'Esperando grafica')
    droid.dialogShow()
    WAITING=True
    while WAITING==True:
        m=poplib.POP3_SSL('pop.gmail.com',995)
        m.user(cliente)
        m.pass_(contrasena)
        numero=len(m.list()[1])
        if numero>0:
            for i in range(numero):
                #print "\nMensaje numero"+str(i+1)
                #print "---------"
                response, headerLines, bytes= m.retr(i+1)
                mensaje='\n'.join(headerLines)
                p=Parser()
                email=p.parsestr(mensaje)
                #Imprime from, to y subject
                #print "From: "+str(email["From"])
                #print "To: "+str(email["To"])
                #print "Subject: "+str(email["Subject"])
                #print "ID: "+email['message-id']
                #Si es un mensaje compuesto
                if (email.is_multipart()):
                    # bucle para cada parte del mensaje
                    for part in email.get_payload():
                        tipo=part.get_content_type()
                        if ("image/jpeg" == tipo):
                            #Si es imagen, se extrae el nombre del fichero
                            #adjunto y se guarda la imagen
                            nombre_fichero=part.get_filename()
                            fp = open(nombre_fichero,'wb')
                            fp.write(part.get_payload(decode=True))
                            fp.close()
                            m.quit()
                            #Asignacion del nombre del fichero
                            grafica=str(nombre_fichero)
                            #Abre grafica
                            droid.dialogDismiss()
                            droid.view("file:/storage/emulated/0/sl4a/"+grafica,"image/*" )
                            WAITING=False

#Funcion que pregunta al usuario el metodo de entrada para las funciones
#False= Voz; True=Teclado
def inputmethod():
    matrix()
    droid.dialogCreateAlert(
        'Metodo de entrada',
        'Seleccione si desea ingresar los datos de las funciones por voz o con el teclado')
    droid.dialogSetPositiveButtonText('Teclado')
    droid.dialogSetNegativeButtonText('Voz')
    droid.dialogShow()
    response= droid.dialogGetResponse().result
    droid.dialogDismiss()
    if not 'which' in response or response ['which']!='positive':
        return False
    else:
        return True
    
#Funcion que pregunta al usuario si desea graficar las funciones
    #False= No Graficar True= Graficar
def inputgrafica():
    droid.dialogCreateAlert(
        'Graficar',
        'Seleccione si desea graficar las funciones ingresadas')
    droid.dialogSetPositiveButtonText('Si')
    droid.dialogSetNegativeButtonText('No')
    droid.dialogShow()
    response= droid.dialogGetResponse().result
    droid.dialogDismiss()
    if not 'which' in response or response ['which']!='positive':
        return False
    else:
        return True


#Funcion que muestra las opciones del menu y regresa el item seleccionado
def menugrados():
    matrix()
    droid.dialogCreateAlert('Menu')
    droid.dialogSetItems(['ax + b','ax2 + bx + c','ax3 + bx2 + cx + d','ax4 + bx3 + cx2 + dx + e','ax5 + bx4 + cx3 + dx2 + ex + f','Opciones'])
    droid.dialogShow()
    response=droid.dialogGetResponse().result
    droid.dialogDismiss()
    return response['item']

#Funcion que pide al usuario ingresar un numero valido en el input de voz
def errornum():
    matrix()
    droid.dialogCreateAlert("Error", "Ingrese un numero valido")
    droid.dialogSetPositiveButtonText("Entendido")
    droid.dialogShow()
    droid.dialogGetResponse().result
    droid.dialogDismiss()

#Funcion que permite ingresar un numero utilizando la voz
#Analiza que el input sea un valor valido y lo regresa al programa
def numvoice(x,z):
    droid.dialogCreateAlert(x,z)
    droid.dialogSetPositiveButtonText('OK')
    droid.dialogShow()
    continuar=droid.dialogGetResponse().result
    droid.dialogDismiss()
    NumToVoice=droid.recognizeSpeech()
    NumeroOK=False
    while NumeroOK!=True:
        try:
            y=int(NumToVoice[1])+1
        except:
            errornum()
            NumToVoice=droid.recognizeSpeech()
        else:
            NumeroOK=True
    return int(NumToVoice[1])

#Funcion que permite ingresar un numero utilizando el teclado
#Analiza que el input sea un valor valido y lo regresa al programa
def numtext(x, z, c):
    droid.dialogGetInput(x, z, c)
    numa1= droid.dialogGetResponse().result
    NumeroOK=False
    while NumeroOK!=True:
        try:
            y=int(numa1['value'])+1
        except:
            errornum()
            droid.dialogGetInput(x, z, c)
            numa1= droid.dialogGetResponse().result
        else:
            NumeroOK=True
    return int(numa1['value'])

#Funcion que muestra los resultados de los ceros encontrados, si los hay
def resultados(x, y):
    droid.dialogCreateAlert(x, y)
    droid.dialogSetPositiveButtonText('OK')
    droid.dialogShow()
    continuar=droid.dialogGetResponse().result
    droid.dialogDismiss()

#Funcion que obtiene los factores de un numero
def factores(x,f):
    y=0
    while y<x or y>=0:
        y+=1
        if x%y==0 and y>f:
            return y
        
#Las funciones siguientes realizan el mismo proceso pero cambia el ingreso de las variables 
        
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion
def funcion1(a1,ind):
    matrix()
    #Asignacion de variables que sirven de contador
    f=0
    fa=0
    contador=0
    CEROS=""
    if a1<0 and ind>0:
        a1a=a1*-1
        #Mientras f sea menor que el factor ingresado
        while f<ind:
            #se utiliza la funcion de factores para obtener el primer factor
            factor=factores(ind,f)
            #Mientras fa sea menor que el factor ingresado
            while fa<a1a:
                #se utiliza la funcion de factores para obtener el segundo factor
                factor2=factores(a1a, fa)
                #se divide el primer factor dentro del segundo (p/s)
                FACTORES=(float(factor)/float(factor2))
                #se multiplica el factor por menos 1
                FACTORESN= (FACTORES*(-1))
                #Se evalua el factor en la funcion
                if (((a1)*(FACTORES)))+ ind==0:
                    #Si da cero entonces se imprime el cero
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
            ######
        if contador>0:
            return CEROS
        else:
            return "No se han encontrado ceros con los factores P/S" 

    elif ind<0 and a1>0:
        inda=ind*-1
        while f<inda: 
            factor=factores(inda,f)
            while fa<a1:
                factor2=factores(a1, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a1)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador>0:
            return CEROS
        else:
            return "No se han encontrado ceros con los factores P/S" 

    elif a1<0 and ind<0:
        a1a=a1*-1
        inda=ind*-1
        while f<inda:
            factor=factores(inda,f)
            while fa<a1a:
                factor2=factores(a1a, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a1)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador>0:
            return CEROS
        else:
            return "No se han encontrado ceros con los factores P/S" 

    else:
        while f<ind:
            factor=factores(ind,f)
            while fa<a1:
                factor2=factores(a1, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a1)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador>0:
            return CEROS
        else:
            return "No se han encontrado ceros con los factores P/S" 
    
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion            
def funcion2(a2,a,ind):
    matrix()
    f=0
    fa=0
    contador=0
    CEROS=""
    if a2<0 and ind>0:
        a2a=a2*-1
        while f<ind:
            factor=factores(ind,f)
            #print "Factor ind:",factor
            while fa<a2a:
                factor2=factores(a2a, fa)
                #print "Factor a:",factor2
                #print "Primeros factores:",factor,factor2
                FACTORES=(float(factor)/float(factor2))
                #print "\nPrimer posible cero:", FACTORES
                FACTORESN= (FACTORES*(-1))
                #print "Primer posible cero N:",FACTORESN
                if (((a2)*(FACTORES**2))+((a)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    elif ind<0 and a2>0:
        inda=ind*-1
        while f<inda: #O igual
            factor=factores(inda,f)
            #print "Factor ind:",factor
            while fa<a2: #O igual
                factor2=factores(a2, fa)
                #print "Factor a:",factor2
                #print "Primeros factores:",factor,factor2
                FACTORES=(float(factor)/float(factor2))
                #print "\nPrimer posible cero:", FACTORES
                FACTORESN= (FACTORES*(-1))
                #print "Primer posible cero N:",FACTORESN
                if (((a2)*(FACTORES**2))+((a)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    elif a2<0 and ind<0:
        a2a=a2*-1
        inda=ind*-1
        while f<inda:
            factor=factores(inda,f)
            #print "Factor ind:",factor
            while fa<a2a:
                factor2=factores(a2a, fa)
                #print "Factor a:",factor2
                #print "Primeros factores:",factor,factor2
                FACTORES=(float(factor)/float(factor2))
                #print "\nPrimer posible cero:", FACTORES
                FACTORESN= (FACTORES*(-1))
                #print "Primer posible cero N:",FACTORESN
                if (((a2)*(FACTORES**2))+((a)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    else:
        while f<ind: #O igual
            factor=factores(ind,f)
            #print "Factor ind:",factor
            while fa<a2: #O igual
                factor2=factores(a2, fa)
                #print "Factor a:",factor2
                #print "Primeros factores:",factor,factor2
                FACTORES=(float(factor)/float(factor2))
                #print "\nPrimer posible cero:", FACTORES
                FACTORESN= (FACTORES*(-1))
                #print "Primer posible cero N:",FACTORESN
                if (((a2)*(FACTORES**2))+((a)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
    if contador>0:
        return CEROS
    else:
        return "No se han encontrado ceros con los factores P/S"
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion
def funcion3(a2,a,b,ind):
    matrix()
    f=0
    fa=0
    contador=0
    CEROS=""
    if a2<0 and ind>0:
        a2a=a2*-1
        while f<ind:
            factor=factores(ind,f)
            while fa<a2a:
                factor2=factores(a2a, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a2)*(FACTORES**3))+((a)*(FACTORES**2)))+ ((b)*(FACTORES)) + ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
            
    elif ind<0 and a2>0:
        inda=ind*-1
        while f<inda:
            factor=factores(inda,f)
            while fa<a2: 
                factor2=factores(a2, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a2)*(FACTORES**3))+((a)*(FACTORES**2)))+ ((b)*(FACTORES)) + ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
  
    elif a2<0 and ind<0:
        a2a=a2*-1
        inda=ind*-1
        while f<inda:
            factor=factores(inda,f)
            while fa<a2a:
                factor2=factores(a2a, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a2)*(FACTORES**3))+((a)*(FACTORES**2)))+ ((b)*(FACTORES)) + ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    else:
        while f<ind:
            factor=factores(ind,f)
            while fa<a2:
                factor2=factores(a2, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a2)*(FACTORES**3))+((a)*(FACTORES**2)))+ ((b)*(FACTORES)) + ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador>0:
            return CEROS
        else:
            return "No se han encontrado ceros con los factores P/S"
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion
def funcion4(a2,a,b,c,ind):
    matrix()
    f=0
    fa=0
    contador=0
    CEROS=""
    if a2<0 and ind>0:
        a2a=a2*-1
        while f<ind:
            factor=factores(ind,f)
            while fa<a2a:
                factor2=factores(a2a, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**4))+((a)*(FACTORES**3))+((b)*(FACTORES**2))+((c)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    elif ind<0 and a2>0:
        inda=ind*-1
        while f<inda: 
            factor=factores(inda,f)
            while fa<a2:
                factor2=factores(a2, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**4))+((a)*(FACTORES**3))+((b)*(FACTORES**2))+((c)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1            
                fa=factor2
            fa=0
            f=factor

    elif a2<0 and ind<0:
        a2a=a2*-1
        inda=ind*-1
        while f<inda:
            factor=factores(inda,f)
            while fa<a2a:
                factor2=factores(a2a, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**4))+((a)*(FACTORES**3))+((b)*(FACTORES**2))+((c)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    else:
        while f<ind: 
            factor=factores(ind,f)
            while fa<a2: 
                factor2=factores(a2, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**4))+((a)*(FACTORES**3))+((b)*(FACTORES**2))+((c)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador>0:
            return CEROS
        else:
            return "No se han encontrado ceros con los factores P/S"

#Funcion que encuentra los ceros racionales de los factores p/s de una funcion
def funcion5(a2,a,b,c,d,ind):
    matrix()
    f=0
    fa=0
    contador=0
    CEROS=""
    if a2<0 and ind>0:
        a2a=a2*-1
        while f<ind:
            factor=factores(ind,f)
            while fa<a2a:
                factor2=factores(a2a, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**5))+((a)*(FACTORES**4))+((b)*(FACTORES**3))+((c)*(FACTORES**2))+((d)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contaodr+=1
                fa=factor2
            fa=0
            f=factor

    elif ind<0 and a2>0:
        inda=ind*-1
        while f<inda:
            factor=factores(inda,f)
            while fa<a2: 
                factor2=factores(a2, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**5))+((a)*(FACTORES**4))+((b)*(FACTORES**3))+((c)*(FACTORES**2))+((d)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    elif a2<0 and ind<0:
        a2a=a2*-1
        inda=ind*-1
        while f<inda:
            factor=factores(inda,f)
            while fa<a2a:
                factor2=factores(a2a, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**5))+((a)*(FACTORES**4))+((b)*(FACTORES**3))+((c)*(FACTORES**2))+((d)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    else:
        while f<ind:
            factor=factores(ind,f)
            while fa<a2:
                factor2=factores(a2, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if ((a2)*(FACTORES**5))+((a)*(FACTORES**4))+((b)*(FACTORES**3))+((c)*(FACTORES**2))+((d)*(FACTORES))+ind==0:
                    Cero=FACTORES
                    CEROS+=str(Cero)
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    CEROS+=str(Cero)
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador>0:
            return CEROS
        else:
            return "No se han encontrado ceros con los factores P/S"

#Presentacion del programa
Program=title()
Inputmethod=inputmethod()
Inputgrafica=inputgrafica()
if Inputgrafica==True:
    informaciongraficar()
#Mientras que el programa este encendido, aparece el menu y se selecciona una opcion
while Program==True:    
    #Menu de grados de funciones polinomiales que permite ingresar el grado de la funcion
    grado= menugrados()
    if grado==5:
        opcion=menuopcion()
        if opcion==0:
            Inputmethod=inputmethod()
        if opcion==1:
            Inputgrafica=inputgrafica()
            if Inputgrafica==True:
                informaciongraficar()
        if opcion==2:
            informacion()
    #Si el metodo de entrada es True (Texto)
    if Inputmethod==True:
        #Si la funcion es de grado 1
        if grado==0:
            matrix()
            #Input del factor a de x
            a=numtext('Funcion Lineal', '[a]x + b', '')
            #Input del factor independiente
            ind=numtext('Funcion Lineal', str(a)+'x + [b]', '')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores1=funcion1(a,ind)
            resultados('Funcion:'+str(a)+'x +'+str(ind), Factores1)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(ind)
                enviarserver("Funcion Lineal", mensaje)

        if grado==1:
            matrix()
            #Input del factor a de x a la 2
            a=numtext('Funcion Cuadratica', '[a]x2 + bx + c', '')
            #Input del factor b de x
            b=numtext('Funcion Cuadratica', str(a)+'x2 + [b]x + c', '')
            #Input del factor independiente
            ind=numtext('Funcion Cuadratica', str(a)+'x2 + '+str(b)+'x + [c]', '')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores2=funcion2(a, b, ind)
            resultados('Funcion:'+str(a)+'x2 + '+str(b)+'x + '+str(ind), Factores2)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(b)+" "+str(ind)
                enviarserver("Funcion Cuadratica", mensaje)


        if grado==2:
            matrix()
            #Input del factor a de x a la 3
            a=numtext('Funcion de Tercer Grado','[a]x3 + bx2 + cx + d', '')
            #Input del factor b de x a la 2
            b=numtext('Funcion de Tercer Grado',str(a)+'x3 + [b]x2 + cx + d', '')
            #Input del factor c de x
            c=numtext('Funcion de Tercer Grado',str(a)+'x3 + '+str(b)+'x2 + [c]x + d', '')
            #Input del factor independiente
            ind=numtext('Funcion de Tercer Grado',str(a)+'x3 + '+str(b)+'x2 + '+str(c)+'x + [d]', '')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores3=funcion3(a, b, c, ind)
            resultados('Funcion: '+str(a)+'x3 + '+str(b)+'x2 + '+str(c)+'x + '+str(ind), Factores3)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(b)+" "+str(c)+" "+str(ind)
                enviarserver("Funcion Tercer Grado", mensaje)
            
        if grado==3:
            matrix()
            #Input del factor a de x a la 4
            a=numtext('Funcion de Cuarto Grado','[a]x4 + bx3 + cx2 + dx + e', '')
            #Input del factor b de x a la 3
            b=numtext('Funcion de Cuarto Grado',str(a)+'x4 + [b]x3 + cx2 + dx + e', '')
            #Input del factor c de x a la 2
            c=numtext('Funcion de Cuarto Grado',str(a)+'x4 + '+str(b)+'x3 + [c]x2 + dx + e', '')
            #Input del factor d de x
            d=numtext('Funcion de Cuarto Grado',str(a)+'x4 + '+str(b)+'x3 + '+str(c)+'x2 + [d]x + e', '')
            #Input del factor independiente
            ind=numtext('Funcion de Cuarto Grado',str(a)+'x4 + '+str(b)+'x3 + '+str(c)+'x2 + '+str(d)+'x + [e]', '')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores4=funcion4(a, b, c, d, ind)
            resultados('Funcion: '+str(a)+'x4 + '+str(b)+'x3 + '+str(c)+'x2 + '+str(d)+'x + '+str(ind), Factores4)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(ind)+" "+str(c)+" "+str(d)+" "+str(ind)
                enviarserver("Funcion Cuarto Grado", mensaje)

        if grado==4:
            matrix()
            #Input del factor a de x a la 5
            a=numtext('Funcion de Quinto Grado','[a]x5 + bx4 + cx3 + dx2 + ex + f', '')
            #Input del factor b de x a la 4
            b=numtext('Funcion de Quinto Grado',str(a)+'x5 + [b]x4 + cx3 + dx2 + ex + f', '')
            #Input del factor c de x a la 3
            c=numtext('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + [c]x3 + dx2 + ex + f', '')
            #Input del factor d de x a la 2
            d=numtext('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + [d]x2 + ex + f', '')
            #Input del factor d de x
            e=numtext('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + '+str(d)+'x2 + [e]x + f', '')
            #Input del factor independiente
            ind=numtext('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + '+str(d)+'x2 + '+str(e)+'x [f]', '')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores5=funcion5(a, b, c, d, e, ind)
            resultados('Funcion: '+str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + '+str(d)+'x2 + '+str(e)+'x +'+str(ind), Factores5)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(ind)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(ind)
                enviarserver("Funcion Quinto Grado", mensaje)

    #Si el metodo de entrada es False (Voz)                      
    if Inputmethod==False:
        #Si la funcion es de grado 1  
        if grado==0: 
            matrix()
            #Input del factor a de x
            a1=numvoice('Funcion Lineal', '[a]x + b')
            #Input del factor independiente
            ind=numvoice('Funcion Lineal', str(a1) +'x + [b]')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores1=funcion1(a1,ind)
            resultados('Funcion:'+str(a1)+'x +'+str(ind), Factores1)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(ind)
                enviarserver("Funcion Lineal", mensaje)
                
        #Si la funcion es de grado 2
        if grado==1:
            matrix()
            #Input del factor a de x a la 2
            a=numvoice('Funcion Cuadratica', '[a]x2 + bx + c')
            #Input del factor b de x
            b=numvoice('Funcion Cuadratica', str(a)+'x2 + [b]x + c')
            #Input del factor independiente
            ind=numvoice('Funcion Cuadratica', str(a)+'x2 + '+str(b)+'x + [c]')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores2=funcion2(a, b, ind)
            resultados('Funcion:'+str(a)+'x2 + '+str(b)+'x + '+str(ind), Factores2)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(b)+" "+str(ind)
                enviarserver("Funcion Cuadratica", mensaje)

        #Si la funcion es de grado 3
        if grado==2:
            matrix()
            #Input del factor a de x a la 3
            a=numvoice('Funcion de Tercer Grado','[a]x3 + bx2 + cx + d')
            #Input del factor b de x a la 2
            b=numvoice('Funcion de Tercer Grado',str(a)+'x3 + [b]x2 + cx + d')
            #Input del factor c de x
            c=numvoice('Funcion de Tercer Grado',str(a)+'x3 + '+str(b)+'x2 + [c]x + d')
            #Input del factor independiente
            ind=numvoice('Funcion de Tercer Grado',str(a)+'x3 + '+str(b)+'x2 + '+str(c)+'x + [d]')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores3=funcion3(a, b, c, ind)
            resultados('Funcion: '+str(a)+'x3 + '+str(b)+'x2 + '+str(c)+'x + '+str(ind), Factores3)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(b)+" "+str(c)+" "+str(ind)
                enviarserver("Funcion Tercer Grado", mensaje)

        #Si la funcion es de grado 4
        if grado==3:
            matrix()
            #Input del factor a de x a la 4
            a=numvoice('Funcion de Cuarto Grado','[a]x4 + bx3 + cx2 + dx + e')
            #Input del factor b de x a la 3
            b=numvoice('Funcion de Cuarto Grado',str(a)+'x4 + [b]x3 + cx2 + dx + e')
            #Input del factor c de x a la 2
            c=numvoice('Funcion de Cuarto Grado',str(a)+'x4 + '+str(b)+'x3 + [c]x2 + dx + e')
            #Input del factor d de x
            d=numvoice('Funcion de Cuarto Grado',str(a)+'x4 + '+str(b)+'x3 + '+str(c)+'x2 + [d]x + e')
            #Input del factor independiente
            ind=numvoice('Funcion de Cuarto Grado',str(a)+'x4 + '+str(b)+'x3 + '+str(c)+'x2 + '+str(d)+'x + [e]')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores4=funcion4(a, b, c, d, ind)
            resultados('Funcion: '+str(a)+'x4 + '+str(b)+'x3 + '+str(c)+'x2 + '+str(d)+'x + '+str(ind), Factores4)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(ind)+" "+str(c)+" "+str(d)+" "+str(ind)
                enviarserver("Funcion Cuarto Grado", mensaje)

        #Si la funcion es de grado 5
        if grado==4:
            matrix()
            #Input del factor a de x a la 5
            a=numvoice('Funcion de Quinto Grado','[a]x5 + bx4 + cx3 + dx2 + ex + f')
            #Input del factor b de x a la 4
            b=numvoice('Funcion de Quinto Grado',str(a)+'x5 + [b]x4 + cx3 + dx2 + ex + f')
            #Input del factor c de x a la 3
            c=numvoice('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + [c]x3 + dx2 + ex + f')
            #Input del factor d de x a la 2
            d=numvoice('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + [d]x2 + ex + f')
            #Input del factor d de x
            e=numvoice('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + '+str(d)+'x2 + [e]x + f')
            #Input del factor independiente
            ind=numvoice('Funcion de Quinto Grado',str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + '+str(d)+'x2 + '+str(e)+'x [f]')
            #Encuentra los ceros (si los hay) y muestra el resultado
            Factores5=funcion5(a, b, c, d, e, ind)
            resultados('Funcion: '+str(a)+'x5 + '+str(b)+'x4 + '+str(c)+'x3 + '+str(d)+'x2 + '+str(e)+'x +'+str(ind), Factores5)
            if Inputgrafica==True:
                mensaje= str(a)+" "+str(ind)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(ind)
                enviarserver("Funcion Quinto Grado", mensaje)





    
