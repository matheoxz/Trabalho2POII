import sympy as sp
import numpy as np
import math

def FunctionReplace(f, x):
    f = f.replace('^', '**')
    f = f.replace('x1', '(x1)')
    f = f.replace('x2', '(x2)')
    f = f.replace('x1', str(x[0]))
    f = f.replace('x2', str(x[1]))
    return f



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

            fr = FunctionReplace(f, x1)
            fr = sp.sympify(fr)

            der = sp.Derivative(fr, L)
            der = der.doit()

            sol = sp.solve(der, L, rational = None, cubics = True)
            
            a = []
            for i in sol:
                b = i.evalf()
                if 'I' not in str(b):
                    a.append(b)
            
            l = min(a)
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


def hookeAndJeeves():
    pass


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