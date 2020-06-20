import sympy as sp
import numpy as np
import math

def FunctionStandard(f):
    f = f.replace('^', '**')
    f = f.replace('x1', '(x1)')
    f = f.replace('x2', '(x2)')
    f = f.replace('e', 'E')
    return f

def FunctionReplace(f, x):
    f = FunctionStandard(f)
    f = f.replace('x1', str(x[0]))
    f = f.replace('x2', str(x[1]))
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
            
def Gradiente_Diff(f, y):
    fr = FunctionStandard(f)

    g1 = sp.Derivative(fr, 'x1')
    g1 = g1.doit()

    g1 = g1.subs('x1', y[0])
    g1 = g1.subs('x2', y[1])

    g2 = sp.Derivative(fr, 'x2')
    g2 = g2.doit()

    g2 = g2.subs('x1', y[0])
    g2 = g2.subs('x2', y[1])

    grad = sp.Array([g1, g2])

    return grad

def gradiente(f, x, eps):

    Resposta = []
    L = sp.Symbol('λ')
    k = 1
    y = x

    while True:
        #calculo do gradiente
        grad = Gradiente_Diff(f, y)
        
        d = (-1)*grad

        y1 = y + L*d
        l = MinimizaEDelta(f, y1, L)
        y = y + l*d

        #distancia
        dist = np.array(grad, dtype = np.float)
        dist = np.linalg.norm(dist)
        Resposta.append([k, grad, d, l, y, dist])

        if(dist < eps):
            break

        k += 1

    return Resposta

def Hessiana(f, y):
    fr = FunctionStandard(f)

    g1 = sp.Derivative(fr, 'x1')
    g1 = g1.doit()

    H1 = sp.Derivative(g1, 'x1')
    H2 = sp.Derivative(g1, 'x2')

    H1 = H1.doit()
    H2 = H2.doit()

    H1 = H1.subs('x1', y[0])
    H1 = H1.subs('x2', y[1])

    H2 = H2.subs('x1', y[0])
    H2 = H2.subs('x2', y[1])
    
    g2 = sp.Derivative(fr, 'x2')
    g2 = g2.doit()

    H3 = sp.Derivative(g2, 'x1')
    H4 = sp.Derivative(g2, 'x2')

    H3 = H3.doit()
    H4 = H4.doit()

    H3 = H3.subs('x1', y[0])
    H3 = H3.subs('x2', y[1])

    H4 = H4.subs('x1', y[0])
    H4 = H4.subs('x2', y[1])

    hess = sp.Matrix([[H1, H2], [H3, H4]])

    return hess

def newton(f, x, eps):
    Resposta = []
    k = 1
    y = x

    while True:
        G = sp.Matrix(Gradiente_Diff(f, y))
        H = Hessiana(f, y)

        HInversa = H**(-1)
        d = (-1)*HInversa*G

        yA = y
        d = d.transpose()
        d = d.tolist()
        y = y + sp.Array(d[0])

        dist = np.array(G, dtype = np.float)
        dist = np.linalg.norm(dist)

        Resposta.append([k, yA, G, H, HInversa, d, y])

        if(dist < eps):
            break

        k += 1

    return Resposta


def gradienteConjugadoGeneralizado(f, x, Q, b, e):
    Resposta = []

    Q = sp.Matrix(Q)
    b = sp.Matrix(b)
    x = sp.Matrix(x)
    d = sp.Matrix([0,0])
    B = 0
    y = x
    k = 1

    g = Q*y-b

    while True:

        d = B*d - g
        l1 = (g.transpose()*d)
        l2 = (d.transpose()*Q*d)
        L = l1[0]/l2[0] * (-1)

        y = y + L*d

        g = Q*y-b

        dist = np.array(g, dtype = np.float)
        dist = np.linalg.norm(dist)
        if(dist<e):
            Resposta.append([k, g, dist])
            break


        bt1 = (g.transpose()*Q*d)
        bt2 = (d.transpose()*Q*d)
        B = bt1[0]/bt2[0]

        
        Resposta.append([k, g, dist, d, B, y])

        k += 1

    return Resposta
        


    

def fletcherAndReeves():
    pass


def davidsonFletcherPowell():
    pass


