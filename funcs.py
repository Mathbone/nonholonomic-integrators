# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 10:55:35 2018

@author: panda
"""

import sympy
import numpy
from sympy.utilities.iterables import flatten
from scipy.optimize import fsolve

def funcCreator(lagrangian,variables,constants,constraintMatrix,control):
    vardot = [x+"dot" for x in variables]
    var0 = [x+"0" for x in variables]
    var1 = [x+"1" for x in variables]
    var2 = [x+"2" for x in variables]
    uvar = ["u"+x for x in variables]
    
    c = sympy.symbols(" ".join(constants))
    v = sympy.symbols(" ".join(variables))
    vdot = sympy.symbols(" ".join(vardot))
    v0 = sympy.symbols(" ".join(var0))
    v1 = sympy.symbols(" ".join(var1))
    v2 = sympy.symbols(" ".join(var2))
    u = sympy.symbols(" ".join(uvar))
    h = sympy.symbols("h")
    L = sympy.sympify(lagrangian)
    A = sympy.sympify(constraintMatrix)
    omega = sympy.Matrix(A)*sympy.Matrix(vdot)
    lmbda = sympy.symbols("lambda:" + str(len(A)))
    
    
    pairs1 = []
    pairs2 = []
    for i in range(len(variables)):
        pairs1.append((v[i],(v1[i]+v0[i])/2))
        pairs1.append((vdot[i],(v1[i]-v0[i])/h))
        pairs2.append((v[i],(v2[i]+v2[i])/2))
        pairs2.append((vdot[i],(v2[i]-v1[i])/h))
    
    Ld1 = h*L.subs(pairs1)
    Ld2 = h*L.subs(pairs2)
    
    eq = []
    for i in range(len(variables)):
        forces = 0
        for j in range(len(A)):
            forces+=lmbda[j]*A[j][i]
        if control[i]:
            forces+= u[i]   
        eq.append((sympy.diff(Ld1,v1[i])+sympy.diff(Ld2,v1[i])-forces))
    
    for row in omega:
        eq.append(row)
        
    print(eq)
        
    f = sympy.lambdify(list(v2)+[h]+list(v1)+list(v0)+list(c),eq,"numpy")
    
    def func(x,y):
        return f(*flatten((x,y)))
    
    return func

def integratorCreator(func, x0, xdot0, k, h, numIter):
    x = numpy.zeros((numIter,len(x0)))
    x[0] = numpy.array(x0)
    x[1] = numpy.array(xdot0)*h+x[0]
    
    for i in range(2,len(x)):
        x[i] = fsolve(func,2*x[i-1]-x[i-2],args = [h]+list(x[i-1])+list(x[i-2])+k)
    return x
    
    
    
    
    
    
    
    
    