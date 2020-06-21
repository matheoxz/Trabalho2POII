from tkinter import *
from tkinter import messagebox
import funcoes
import sympy as sp


def Info():
    messagebox.showinfo("Feito por", "Matheus Sinto Novaes - 181025981 \n Inaê Soares de Figueiredo - 181021651 \n Thiago La Scala - 181025655")


def Click():
    try:
        f = funcao.get()
        e = abs(float(eEntry.get()))
        x00 = float(x00Entry.get())
        x01 = float(x01Entry.get())
        x = sp.Array([x00, x01])

        q11 = float(q11Entry.get())
        q12 = float(q12Entry.get())
        q21 = float(q21Entry.get())
        q22 = float(q22Entry.get())
        Q = [[q11, q12],[q21, q22]]

        b1 = float(b1Entry.get())
        b2 = float(b2Entry.get())
        b = [b1, b2]

        s11 = float(s11Entry.get())
        s12 = float(s12Entry.get())
        s21 = float(s21Entry.get())
        s22 = float(s22Entry.get())
        S = [[s11, s12],[s21, s22]]

        op = optionVar.get()
        gr = graficoVar.get()
        
    except Exception as e:
        messagebox.showwarning("Erro", "Coloque todos os valores nos campos!\n Caso a função não utilize o campo deixado vazio, coloque um 0")
    else:
        #abre nova janela
        resW = Toplevel()
        
        if(op == 0):
            resW.title("Coordenadas Cíclicas")
            #poe headers da tabela
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "xᵏ").grid(row = 0, column = 1)
            Label(resW, text= "j").grid(row = 0, column = 2)
            Label(resW, text= "dʲ").grid(row = 0, column = 3)
            Label(resW, text= "yʲ").grid(row = 0, column = 4)
            Label(resW, text= "λʲ").grid(row = 0, column = 5)
            Label(resW, text= "yʲ⁺¹").grid(row = 0, column = 6)
            Label(resW, text= "xᵏ⁺¹").grid(row = 0, column = 7)
            Label(resW, text= "||xᵏ⁺¹-xᵏ||").grid(row = 0, column = 8)
            #executa funcao
            resp = funcoes.ciclicas(f, x, e)
            z = 0
            w = 0
            for n, it in zip(range(len(resp)),resp):
                w += n+1
                for i, j in zip(range(len(it)), it):
                    
                    if i == 0:
                        for a, b in zip(range(2), j):
                            Label(resW, text = b).grid(row = w+z, column = a)
                    elif i == len(it)-1:
                        w -=1
                        for a, b in zip(range(7, 9), j):
                            Label(resW, text = b).grid(row = w+z, column = a)
                    else:
                        for q in j:
                            for a, b in zip(range(2, 7), q):
                                Label(resW, text = b).grid(row = w+z, column = a)
                            w+=1
            z = w+z
                    

        elif(op == 1):
            resW.title("Hooke and Jeeves")
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "xᵏ").grid(row = 0, column = 1)
            Label(resW, text= "j").grid(row = 0, column = 2)
            Label(resW, text= "yʲ").grid(row = 0, column = 4)
            Label(resW, text= "dʲ").grid(row = 0, column = 3)
            Label(resW, text= "λʲ").grid(row = 0, column = 5)
            Label(resW, text= "yʲ⁺¹").grid(row = 0, column = 6)
            Label(resW, text= "||xᵏ⁺¹-xᵏ||").grid(row = 0, column = 7)
            Label(resW, text= "d").grid(row = 0, column = 8)
            Label(resW, text= "λ").grid(row = 0, column = 9)
            Label(resW, text= "y").grid(row = 0, column = 10)
            #executa funcao
            resp = funcoes.hookeAndJeeves(f, x, e)
            z = 0
            w = 0
            for n, it in zip(range(len(resp)),resp):
                w = n+1
                for a, d in zip(it, range(len(it))):
                    
                    print(d, a)
                    if d == 0:
                        for i, j in zip(a, range(2)):
                            print(j, i)
                            Label(resW, text = str(i)).grid(row = w+z, column = j)
                    if d == 1:
                        x=0
                        for b in a:
                            for i, j in zip(b, range(2,7)):
                                Label(resW, text = str(i)).grid(row = w+z+x, column = j)
                            x+=1
                    
                    if d == 2:
                        Label(resW, text = str(a)).grid(row = w+z+1, column = 7)

                    if d == 3:
                        for i, j in zip(a, range(8, 12)):
                            Label(resW, text = str(i)).grid(row = w+z+1, column = j)
                z += w
                
                

        elif(op == 2):
            resW.title("Gradiente")
            #poe haders da tabela
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text= "∇f(x)").grid(row = 0, column = 1)
            Label(resW, text= "d").grid(row = 0, column = 2)
            Label(resW, text= "λ").grid(row = 0, column = 3)
            Label(resW, text= "xᵏ⁺¹").grid(row = 0, column = 4)
            Label(resW, text= "||∇f(x)||").grid(row = 0, column = 5)
            #executa funcao
            resp = funcoes.gradiente(f, x, e)
            for n, it in zip(range(len(resp)), resp):
                for i, j in zip(it, range(len(it))):
                    Label(resW, text = str(i)).grid(row = n+1, column = j)


        elif(op == 3):
            resW.title('Newton')
             #poe haders da tabela
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "xᵏ").grid(row = 0, column = 1)
            Label(resW, text= "∇f(x)").grid(row = 0, column = 2)
            Label(resW, text= "H(x)").grid(row = 0, column = 3)
            Label(resW, text= "H⁻¹(x)").grid(row = 0, column = 4)
            Label(resW, text= "d").grid(row = 0, column = 5)
            Label(resW, text= "xᵏ⁺¹").grid(row = 0, column = 6)
            #executa funcao
            resp = funcoes.newton(f, x, e)
            for n, it in zip(range(len(resp)), resp):
                for i, j in zip(it, range(len(it))):
                    Label(resW, text = str(i)).grid(row = n+1, column = j)

        elif(op == 4):
            resW.title("Gradiente Conjugado Generalizado")
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "g").grid(row = 0, column = 1)
            Label(resW, text= "||g||").grid(row = 0, column = 2)
            Label(resW, text= "d").grid(row = 0, column = 3)
            Label(resW, text= "β").grid(row = 0, column = 4)
            Label(resW, text= "y").grid(row = 0, column = 5)
            

            resp = funcoes.gradienteConjugadoGeneralizado(f, x, Q, b, e)
            
            for n, it in zip(range(len(resp)), resp):
                for i, j in zip(it, range(len(it))):
                    Label(resW, text = str(i)).grid(row = n+1, column = j)

        
        elif(op == 5):
            resW.title("Fletcher and Reeves")
            Label(resW, text = "i").grid(row = 0, column = 0)
            Label(resW, text = "∇f(x)").grid(row = 0, column = 1)
            Label(resW, text= "||∇f(x)||").grid(row = 0, column = 2)
            Label(resW, text= "d").grid(row = 0, column = 3)
            Label(resW, text= "λ").grid(row = 0, column = 4)
            Label(resW, text= "xᵏ⁺¹").grid(row = 0, column = 5)

            resp = funcoes.fletcherAndReeves(f, x, e)
            
            for n, it in zip(range(len(resp)), resp):
                for i, j in zip(it, range(len(it))): 
                    Label(resW, text = str(i)).grid(row = n+1, column = j)
            
        elif(op == 6):
            resW.title("Davison-Fletcher-Powell")
            Label(resW, text = "i").grid(row = 0, column = 0)
            Label(resW, text = "k").grid(row = 0, column = 1)
            Label(resW, text= "x").grid(row = 0, column = 2)
            Label(resW, text= "|g|").grid(row = 0, column = 3)
            Label(resW, text= "S").grid(row = 0, column = 4)
            Label(resW, text= "d").grid(row = 0, column = 5)
            Label(resW, text= "λ").grid(row = 0, column = 6)


            resp = funcoes.davidsonFletcherPowell(f, e, S, x)
            
            for n, it in zip(range(len(resp)), resp):
                for i, j in zip(it, range(len(it))): 
                    Label(resW, text = str(i)).grid(row = n+1, column = j)
            
        
#executa tela
root = Tk()
root.title("Trabalho 1")
#frames
optionsF = LabelFrame(root, text="Opções")
dataF = LabelFrame(root, text="Dados")
#Variaveis
optionVar = IntVar()
graficoVar = IntVar()
#Radio Buttons
ciclicaRB = Radiobutton(optionsF, text="Coordenadas Cíclicas", variable = optionVar, value = 0)
hookeAndJeevesRB = Radiobutton(optionsF, text="Hooke and Jeeves", variable = optionVar, value = 1)
gradienteRB = Radiobutton(optionsF, text="Gradiente", variable = optionVar, value = 2)
newtonRB = Radiobutton(optionsF, text="Newton", variable = optionVar, value = 3)
gradienteConjugadoRB = Radiobutton(optionsF, text="Gradiente Conjugado Generalizado", variable = optionVar, value = 4)
fletcherAndReevesRB = Radiobutton(optionsF, text="Flecther and Reeves", variable = optionVar, value = 5)
davidsonPowell = Radiobutton(optionsF, text = 'Davidson-Fletcher-Powell', variable = optionVar, value = 6)

#CheckBox
graficoCB = Checkbutton(root, text="Gerar Gráfico", variable = graficoVar)
#Entradas
funcao = Entry(dataF, width = 25)
funcao.insert(0, "4*x1^2+x1*x2+(1/2)*x2^2-18*x1-4*x2")
eEntry = Entry(dataF)
eEntry.insert(0, "0.001")
x00Entry = Entry(dataF, width = 5)
x00Entry.insert(0, "1")
x01Entry = Entry(dataF, width = 5)
x01Entry.insert(0, "1")
q11Entry = Entry(dataF, width = 5)
q11Entry.insert(0, "5")
q12Entry = Entry(dataF, width = 5)
q12Entry.insert(0, "1")
q21Entry = Entry(dataF, width = 5)
q21Entry.insert(0, "1")
q22Entry = Entry(dataF, width = 5)
q22Entry.insert(0, "2")
b1Entry = Entry(dataF, width = 5)
b1Entry.insert(0, "24")
b2Entry = Entry(dataF, width = 5)
b2Entry.insert(0, "12")
s11Entry = Entry(dataF, width = 5)
s11Entry.insert(0, "1")
s12Entry = Entry(dataF, width = 5)
s12Entry.insert(0, "0")
s21Entry = Entry(dataF, width = 5)
s21Entry.insert(0, "0")
s22Entry = Entry(dataF, width = 5)
s22Entry.insert(0, "1")


#Botoes
info = Button(root, text = "i", command = Info).grid(row = 6, column = 1, sticky = E)
botao = Button(root, text = "Calcular!", command = Click).grid(row= 6, column = 2, sticky = W+E)

#Inserções na tela
#Labels
funcaoLabel = Label(dataF, text = "min f(x) = ").grid(row= 1, column = 1, sticky = E)
epsolonLabel = Label(dataF, text = "ε = ").grid(row = 2, column = 1, sticky = E)
x0Label = Label(dataF, text = 'x₀ = [ ').grid(row = 3, column = 1, sticky = E)
virguLabel = Label(dataF, text = ' ,  ').grid(row = 3, column = 3)
fechaLabel = Label(dataF, text = ']ᵗ').grid(row = 3, column = 5, sticky = W)
QLabel = Label(dataF, text = 'Q = ').grid(row = 4, column = 1, sticky = E)
bLabel = Label(dataF, text = 'b = ').grid(row = 4, column = 4)
SLabel = Label(dataF, text = 'S = ').grid(row = 7, column = 1, sticky = E)

#Entrys
funcao.grid(row = 1, column= 2, sticky=W+E, columnspan = 4)
eEntry.grid(row = 2, column = 2, sticky = W+E, columnspan = 4)
x00Entry.grid(row = 3, column = 2, sticky = W+E)
x01Entry.grid(row = 3, column = 4, sticky = W+E)
q11Entry.grid(row = 4, column = 2)
q12Entry.grid(row = 4, column = 3)
q21Entry.grid(row = 5, column = 2)
q22Entry.grid(row = 5, column = 3)
b1Entry.grid(row = 4, column = 5)
b2Entry.grid(row = 5, column = 5)
s11Entry.grid(row = 7, column = 2)
s12Entry.grid(row = 7, column = 3)
s21Entry.grid(row = 8, column = 2)
s22Entry.grid(row = 8, column = 3)

#Radio Buttons
ciclicaRB.grid(row= 1, column= 3, sticky = W)
hookeAndJeevesRB.grid(row= 2, column= 3, sticky = W)
gradienteRB.grid(row= 3, column=3, sticky = W)
newtonRB.grid(row= 4, column=4, sticky = W)
gradienteConjugadoRB.grid(row=1, column=4, sticky = W)
fletcherAndReevesRB.grid(row=2, column=4, sticky = W)
davidsonPowell.grid(row = 3, column = 4, sticky = W)

#Frames
dataF.grid(row=0, column=0, sticky= W+E+N+S, columnspan = 2)
optionsF.grid(row=0, column=2, sticky= W+E+N+S)


root.mainloop()