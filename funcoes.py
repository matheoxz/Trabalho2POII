import sympy as sp
import numpy as np
import math

def FunctionReplace(f, x):
    f = f.replace('^', '**')
    f = f.replace('x1', '(x1)')
    f = f.replace('x2', '(x2)')
    f = f.replace('x1', str(x[0]))
    f = f.replace('x2', str(x[1]))
    f = f.replace('e', 'E')
    return f

def MinimizaEDelta(f, x1, L):
    fr = FunctionReplace(f, x1)
    fr = sp.sympify(fr)

    der = sp.Derivative(fr, L)
    der = der.doit()

    sol = sp.solve(der, L, rational = None, cubics = True)

    if len(sol) > 1:
        a = []
        for i in sol:
            b = i.evalf()
            if 'I' not in str(b):
                a.append(b)
        sol = a

    return min(sol)

def ciclicas(f, x, eps):
    Resposta = []
    #declara lambda
    L = sp.Symbol('λ')
    d = sp.Array([[1,0], [0,1]])
    k = 1
    y = sp.Array(x)
    while True:
        xA = y
        K = []
        K.append([k, xA])
        for j in range(len(x)):
            J = []

            x1 = y + L*d[j]

            l = MinimizaEDelta(f, x1, L)
            ya = y
            y = y + l*d[j]

            J.append([j, d[j], ya, l, y])
            print(J)
            K.append(J)

        dist = np.array(y-xA, dtype = np.float)
        dist = np.linalg.norm(dist)

        K.append([y, dist])
        Resposta.append(K)

        k+=1
        if(dist < eps):
            break

    return Resposta


def hookeAndJeeves(f, x, eps):
    Resposta = []
    #declara lambda
    L = sp.Symbol('λ')
    d = sp.Array([[1,0], [0,1]])
    k = 1
    y = sp.Array(x)
    y1 = y

    while True:
        xA = y
        K = []
        K.append([k, xA])

        #busca exploratória
        J = []
        for j in range(len(x)):
            yAux = y1 + L*d[j]

            l = MinimizaEDelta(f,yAux, L)
            ya = y
            y = y1 + l*d[j]
            y1 = y
            J.append([j, d[j], ya, l, y])
        K.append(J)
        xP = y

        #teste distância
        dist = np.array(xP-xA, dtype = np.float)
        dist = np.linalg.norm(dist)
        K.append(dist)
        if(dist < eps):
            Resposta.append(K)
            break
        
        #busca conjugada
        d_ = xP - xA
        y1 = xP + L*d_
        l = MinimizaEDelta(f, y1, L)
        y1 = xP + l*d_
        C = [d_, l, y1]
        K.append(C)

        k += 1

        Resposta.append(K)


    return Resposta
            


def gradiente():
    pass


def newton():
    pass


def gradienteConjugadoGeneralizado():
    pass


def fletcherAndReeves():
    pass


def davidsonFletcherPowell():
    pass


#a = ciclicas('(1-x1)^2+5*(x2-x1^2)^2', sp.Array([2,0]), 0.1)
#print(a)