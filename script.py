# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:01:28 2018

@author: panda
"""

import funcs
import numpy
import matplotlib.pyplot as plt


var = ["x", "y", "theta", "psi", "phi"]
consts = ["M", "II", "JJ", "R", "g"]

L = ".5*M*((xdot+R*thetadot*cos(theta)*cos(phi)-R*phidot*sin(theta)*sin(phi))**2+(ydot+R*thetadot*cos(theta)*cos(phi)+R*phidot*sin(theta)*cos(phi))**2+(R*thetadot*sin(theta))**2)\
 + .5*II*((psidot-phidot*sin(theta))**2) + .5*JJ*((thetadot)**2+(phidot*cos(theta))**2)-M*g*R*cos(theta)"

A = [["1","0","0","-R*cos(phi)","0"],["0","1","0","-R*sin(phi)","0"]]

availableControls = [False,False,True,True,True]

func = funcs.funcCreator(L,var,consts,A,availableControls)

numIter=100
x0 = [0,0,0,0,0]
xdot0 = [1,0,0,1,0]
k = [1,2/5,3/5,1,9.8]
h = .1
u = numpy.zeros((numIter,sum(availableControls)))

x = funcs.integratorCreator(func,x0,xdot0, u, k, h, 2, numIter)

plt.plot(x[:,0],x[:,1])

