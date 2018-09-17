#Tiffanie CARLIER
# -*- coding: utf-8 -*-
#premiere question TP1
import numpy as np
from pylab import *

import methodes
import equations

#Resolution approchée de y'=1-y avec y(0)=5 dans [0,1]
equations.a=-1.
equations.b=1.
t0=0.
y0=5.
T=1.
h=[0.2,0.1,0.05,0.025,0.0125,0.00625]
N=[5,10,20,40,80,160]
erreur=zeros(6) #de taille 6 car l'on considere 6 h differents
for i in range(1,6,1):
    # t tableau des subdivisions ( c'est un vecteur)
    # y vecteurs des solutions calculees au subdivisons t
    [t,ycal]=methodes.euler_explicite(t0,h[i],N[i],y0,equations.f_affine)
    yexact=equations.sol_affine(t,y0)
    erreur[i]=max(abs((ycal-yexact)/yexact))
    #Ecriture de l erreur en fonction de h
    print("Valeur de h : "+str(h[i])+" et son erreur associe "+str(erreur[i]))

plot(h,erreur)
xscale('log')
title("Erreur en fonction du pas h en echelle logarithmique")
xlabel('erreur logarithmique')
ylabel('pas de subdivision')
grid("on")
#plusieurs methodes pour mettre en echelle logarithmique
#loglog() met les deux axes en echelles logarithmiques
show()
    
