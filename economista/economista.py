# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:15:09 2021

@author: UniverSapphireLotus
"""
import math
############################################
def interesSimple_Final(P, n, i):
    return P*(1+n*i)

def interesSimple_Presente(F, n, i):
    return F/(1+n*i)

def interesSimple_n(F, P, i):
    return ((F/P)-1)/(i)

def interesSimple_i(F, P, n):
    return ((F/P)-1)/(n)

def interesSimple_Interes_P_ni(P, n, i):
    return P*((1+n*i)-1)

def interes_Interes_F_P(F, P):
    return F-P
###########
def interesCompuesto_Final(P, n, i):
    return P*(1+i)**n

def interesCompuesto_Presente(F, n, i):
    return F/((1+i)**n)

def interesCompuesto_n(F, P, i):
    return (math.log((F/P))/math.log(1+i))

def interesCompuesto_i(F, P, n):
    return n*((F/P)**0.5)-1

############################################
def descuentoRacional_D_FP(F,P):
    return F-P

def descuentoRacionalSimple_Presente(F, n, i):
    return F/(1+i*n)

def descuentoRacionalSimple_Descuento(F, n, i):
    return (F*i*n)/(1+i*n)

def descuentoRacionalCompuesto_Presente(F, n, i):
    return F*(1/((1+i)**n))

def descuentoRacionalCompuesto_Descuento(F, n, i):
    return F*(1-(1/((1+i)**n)))
###########
def descuentoBancarioSimple_D(F, n, d):
    return F*d*n

def descuentoBancarioSimple_Final(P, n, d):
    return P/(1-d*n)

def descuentoBancarioSimple_Presente(F, n, d):
    return F*(1-d*n)

def descuentoBancarioSimple_d(F, D, n):
    return D/(F*n)

def descuentoBancarioSimple_n(F, D, d):
    return D/(F*d)
###########
def descuentoBancarioCompuesto_Final(P, n, d):
    return P/((1-d)**n)

def descuentoBancarioCompuesto_Presente(F, n, d):
    return F*(1-d)**n

def descuentoBancarioCompuesto_n(F, P, d):
    return math.log(P/F)/math.log(1-d)

def descuentoBancarioCompuesto_d(F, P, n):
    return n*((P/F)**0.5)+1

def descuentoBancarioCompuesto_Descuento(F, n, d):
    return F*(1-(1-d)**n)
###########
def decuentoCompercial_unitario_Final(P, d):
    return P*(1-d)

def decuentoCompercial_unitario_Descuento(P, d):
    return P*d
############################################
def anualidadVencida_Final(R, n, i):
    F=R*((1+i)**n-1)/i
    return F

def anualidadVencida_Renta_F(F, n, i):
    R=F*i/((1+i)**n-1)
    return R

def anualidadVencida_n_F(F, R, i):
    n= math.log((F*i)/R-1)/math.log(1+i)
    return n

def anualidadVencida_Renta_P(P, n, i):
    R=P*(((1+i)**n)*i)/((((1+i)**n)-1))
    return R

def anualidadVencida_n_P(P, R, i):
    n= math.log((1-P*i/R))/math.log(1+i)
    return n

###########
def anualidadAnticipada_Final(R, n, i):
    F=R*((1+i)**n-1)*(1+i)/i
    return F

def anualidadAnticipada_Renta_F(F, n, i):
    R=F*(1/(1+i))*(1/((1+i)**n)-1)
    return R

def anualidadAnticipada_n_F(F, R, i):
    n=math.log((F*i/(R*(1+i)))+1)/math.log(1+i)
    return n

def anualidadAnticipada_Renta_P(P, n, i):
    R=P*(1/(1+i))*((i*(1+i)**n)/(((1+i)**n)-1))
    return R
###########
def anualidad_Presente(R, n, i):
    P=R*-(1-(1+i)**-n)*(1+i)/i
    return P
############################################
def anualidadPerpetuaVencida_P(R,i):
    return R*(1/i)

def anualidadPerpetuaAnticipada_P(R,i):
    return R*(1+i)*(1/i)




R=823.2
i=0.23
k=5
n=10
F=25000

#ANUALIDADES VENCIDAS PERPETUAS
P=R/i

#ANUALIDADES ANTICIPADAS PERPETUAS
P=R*(1+i)/i

#ANUALIDADES PERPETUA DIFERIDA VENCIDA
P=R*(1/(1+i))**k/i

#ANUALIDADES PERPETUA DIFERIDA ANTICIPADA
P=R*(1+i)**(1-k)/i

#Valor Futuro de una Anualidad Vencida Diferida
F=R*((1+i)**n-1)/i

#Valor Presente de una Anualidad Vencida Diferida
P=R*(1/(1+i))**k*((1+i)**n-1)/((1+i)**n*i)

#Valor Futuro de una Anualidad Anticipada Diferida
F=R*(1+i)*((1+i)**n-1)/i

#Valor Presente de una Anualidad Anticipada Diferida
P=R*(1/(1+i))**k*(1+i)*((1+i)**n-1)/((1+i)**n*i)

#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
#Anualidad Anticipada Futura
F=R*((1+i)**n-1)*(1+i)/i
#Anualidad Anticipada Presente
P=R*(1-(1+i)**-n)*(1+i)/i
#Anualidad Vemcida Futura
F=R*((1+i)**n-1)/i
#Anualidad Vemcida Presente
P=R*(1-(1+i)**-n)*(1+i)/i
#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

#interes Anualidad Vemcida Futura
R=984.22
#i=(1+0.23)**(1/12)-1
n=10
#F=25000
P=25000
#Futruro
#h=(F/(R*n))**(2/(n-1))-1
#Presente
h=((R*n)/P)**(2/(n+1))-1

h=((R*(n-1))/(P-R))**(2/(n))-1


#interes
#i=h*((n+1)*h+12)/(2*(n+1)*h+12)
print(h)
i=h*((n-1)*h-12)/(2*(n-1)*h-12)

#Descuento racional simple

#Descuento racional compueste

#Descuento bancario simple

#Descuento bancario compuesto
#P=R*(1-(1+i)**-n)*(1+i)/i

F=R*((1+i)**n-1)/i
P=R*(1-(1+i)**-n)*(1+i)/i
print(h,i,P, F)