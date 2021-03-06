#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib.pyplot as plt
from pylab import * #permet d'eviter l'utilisation de plat devant les parametres graphiques

import methodes
import equations

# Résolution approchée de y' = 2-y avec y(0) = 3 pour t dans [0,5]
equations.a = -1. #on affecte a la valeur a dans equations la valeur de -1 en terme d'entier (presence du point apres le nombre)
equations.b = 2.  # on affecte a la veleur b de equations la valeur 2
t0,y0 = 0.,3.
T = 5.
# Avec un pas de 0.1, il faut donc 50 iterations
N,h = 50,0.1
[t,y1] = methodes.euler_explicite(t0,h,N,y0,equations.f_affine)
# Solution exacte aux mêmes instants
z1 = equations.sol_affine(t,y0)
# Calcul de l'erreur maximum relative
e1 = np.max(np.abs((z1-y1)/z1))
# Graphe des solutions exactes et approchées
plot(t,y1,'b-+',label='solution approchée h=0.1')
plot(t,z1,'r-',label='solution exacte')
xlabel('t')
ylabel('y')
title("Méthode d'Euler explicite")
legend()
savefig('eq_affine.png')
show()
print(len(y1))
print(len(z1))
# Écriture de l'erreur en fonction de h
print("{0} | {1}".format(h,e1))


