#Algoritmos y programacion basica
#Seccion 30
#22-05-2014
#Diego Morales, 14012
#Z-Fun
#Programa que calcula ceros racionales de funciones polinomiales
#y graficadora
#Modulo Factores
#Este modulo obtiene los factores p/s y los evalua en la funcion
#si uno de los factores valuados da como resultado cero, entonces
#se imprime en pantalla

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
    #Asignacion de variables que sirven de contador
    f=0
    fa=0
    contador=0
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
                    print Cero
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor

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
                    print Cero
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor

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
                    print Cero
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor

    else:
        while f<ind:
            factor=factores(ind,f)
            while fa<a1:
                factor2=factores(a1, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a1)*(FACTORES)))+ ind==0:
                    Cero=FACTORES
                    print Cero
                    contador+=1
                if (((a1)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
    if contador==0:
        print "No se han encontrado ceros con los factores P/S"
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion            
def funcion2(a2,a,ind):
    f=0
    fa=0
    contador=0
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
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**2))+((a)*(FACTORESN)))+ ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
    if contador==0:
        print "No se han encontrado ceros con los factores P/S"
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion
def funcion3(a2,a,b,ind):
    f=0
    fa=0
    contador=0
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
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador==0:
            print "No se han encontrado ceros con los factores P/S"
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
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador==0:
            print "No se han encontrado ceros con los factores P/S"
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
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
        if contador==0:
            print "No se han encontrado ceros con los factores P/S"
    else:
        while f<ind:
            factor=factores(ind,f)
            while fa<a2:
                factor2=factores(a2, fa)
                FACTORES=(float(factor)/float(factor2))
                FACTORESN= (FACTORES*(-1))
                if (((a2)*(FACTORES**3))+((a)*(FACTORES**2)))+ ((b)*(FACTORES)) + ind==0:
                    Cero=FACTORES
                    print Cero
                    contador+=1
                if (((a2)*(FACTORESN**3))+((a)*(FACTORESN**2)))+ ((b)*(FACTORESN)) + ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
    if contador==0:
        print "No se han encontrado ceros con los factores P/S"
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion
def funcion4(a2,a,b,c,ind):
    f=0
    fa=0
    contador=0
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**4))+((a)*(FACTORESN**3))+((b)*(FACTORESN**2))+((c)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
    if contador==0:
        print "No se han encontrado ceros con los factores P/S"
#Funcion que encuentra los ceros racionales de los factores p/s de una funcion
def funcion5(a2,a,b,c,d,ind):
    f=0
    fa=0
    contador=0
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
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
                    print Cero
                    contador+=1
                if ((a2)*(FACTORESN**5))+((a)*(FACTORESN**4))+((b)*(FACTORESN**3))+((c)*(FACTORESN**2))+((d)*(FACTORESN))+ind==0:
                    Cero=FACTORESN
                    print Cero
                    contador+=1
                fa=factor2
            fa=0
            f=factor
    if contador==0:
        print "No se han encontrado ceros con los factores P/S"


