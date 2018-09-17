#Tiffanie CARLIER
# -*- coding: utf-8 -*-
#deuxieme question TP1
import numpy as np
from pylab import *

import methodes
import equations
#from equations import valexact

a1=-1
b1=1
def f_polynome(t,y):
    """Fonction affine pour y' = ay+b. Les coefficients a et b sont des
    variables globales du module.

    """
    return a1*(y**2)+b1

#Resolution approchée de y'=1-y^2 avec y(0)=0 dans [0,1]
equations.a=-1.
equations.b=1.
t0=0.
y0=0.
T=1.
h=[0.2,0.1,0.05,0.025,0.0125,0.00625]
N=[5,10,20,40,80,160]
erreur=zeros(6)
#on calcul en fonction du la condition initiale la valeur du paramètre C
C=((1/(y0-1))-(1/2)*np.exp(2*t0))/np.exp(-2*t0)
for i in range(1,6,1):
    # t tableau des subdivisions ( c'est un vecteur)
    # y vecteurs des solutions calculees au subdivisons t
    [t,ycal]=methodes.euler_explicite(t0,h[i],N[i],y0,f_polynome)
    #valeur obtenue par calcul sur feuille
    yexact=1+(1/((C*np.exp(-2*t))+(1/2)*np.exp(2*t)))
    erreur[i]=max(abs((ycal-yexact)))
    #Ecriture de l erreur en fonction de h
    print("Valeur de h : "+str(h[i])+"et son erreur associe "+str(erreur[i]))

plot(h,erreur)
#yscale('log')
#plusieurs methodes pour mettre en echelle logarithmique
#loglog() #met les deux axes en echelles logarithmiques
show()
