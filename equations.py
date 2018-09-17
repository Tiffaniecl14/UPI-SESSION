#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from pylab import *
# Fonction f(t,y), second membre d'équations différentielles d'ordre 1
# écrite sous la forme d'un problème de Cauchy, y'(t) = f(t,y(t)) avec
# y(0)=y0

a = -1.  #a de a*x+b forme lineaire
b = 1.      # b de la forme a*x+b

def f_affine(t,y):
    """Fonction affine pour y' = ay+b. Les coefficients a et b sont des
    variables globales du module.

    """
    return a*y+b    
    
def f_polynome(t,y):
    """Fonction affine pour y' = ay+b. Les coefficients a et b sont des
    variables globales du module.

    """
    return a*(y**2)+b
    
def sol_affine(t,y0):
    """Pour une fonction affine, on connait la solution exacte. C'est
    y(t0+s) = y0*exp(a*s) - b*(1-exp(a*s))/a, soit y(t) =
    y0*exp(a*(t-t0)) - b*(1-exp(a*(t-t0)))/a

    """
    t0 = t[0]
    return y0*np.exp(a*(t-t0)) - b * (1.-np.exp(a*(t-t0)))/a

def nouvelle_fonction(t,y):
    return a*y**2+b
    
#probleme d'ajout de nouvelle fonction

def calcul_valexact(t0,y0,t):
    C=((1/(y0-1))+(1/2)*np.exp(-2*t0))/np.exp(2*t0)
    yex=1+(1/((C*exp(2*t))-(1/2)*exp(-2*t)))
    return yex
#calcul de la solution exacte verifié

