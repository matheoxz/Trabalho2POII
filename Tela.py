from tkinter import *
from tkinter import messagebox
import fourFn
import funcoes
import matplotlib.pyplot as plt

def Grafico(f, d, a, b):
    x=[]
    y=[]

    x.append(a)
    y.append(fourFn.strToFunc(f.replace("x", str(a))))
    while(a<b):
        a+=d
        x.append(a)
        y.append(fourFn.strToFunc(f.replace("x", str(a))))
    plt.plot(x,y)
    plt.show()

def Info():
    messagebox.showinfo("Feito por", "Matheus Sinto Novaes - 181025981 \n Inaê Soares de Figueiredo - 181021651 \n Thiago La Scala - 181025655")


def Click():
    try:
        f = funcao.get()
        d = abs(float(delta.get()))
        a = float(aEntry.get())
        b = float(bEntry.get())
        if(a > b):
            aux = a
            a = b
            b = aux
        ep = abs(float(eEntry.get()))
        op = optionVar.get()
        gr = graficoVar.get()
        
    except Exception as e:
        messagebox.showwarning("Erro", "Coloque todos os valores nos campos!\n Caso a função não utilize o campo deixado vazio, coloque um 0")
    else:
        #abre nova janela
        resW = Toplevel()
        
        if(op == 0):
            resW.title("Coordenadas Cíclicas")
            #poe haders da tabela
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "x").grid(row = 0, column = 1)
            Label(resW, text= "f(x)").grid(row = 0, column = 2)
            Label(resW, text= "xk").grid(row = 0, column = 3)
            Label(resW, text= "f(xk)").grid(row = 0, column = 4)
            Label(resW, text= "f(xk) < f(x)?").grid(row = 0, column = 5)
            #executa funcao
            '''lista = funcoes.BuscaUniforme(f, d, a, b)
            r = 1
            c = 0
            for i in lista:
                if (type(i) is str):
                        Label(resW, text = i).grid(row = r, column = c, columnspan = 6)
                        r+=1
                        continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1'''

        elif(op == 1):
            resW.title("Hooke and Jeeves")
            #poe haders da tabela
            Label(resW, text= "k").grid(row = 0, column = 0)
            Label(resW, text = "a").grid(row = 0, column = 1)
            Label(resW, text = "b").grid(row = 0, column = 2)
            Label(resW, text= "(b-a)").grid(row = 0, column = 3)
            Label(resW, text= "x").grid(row = 0, column = 4)
            Label(resW, text= "z").grid(row = 0, column = 5)
            Label(resW, text= "f(x)").grid(row = 0, column = 6)
            Label(resW, text= "f(z)").grid(row = 0, column = 7)
            Label(resW, text= "f(x)>f(z)?").grid(row = 0, column = 8)
            
            #executa funcao
            '''lista = funcoes.BuscaDicotomica(f, d, a, b, ep)
            r = 1
            c = 0
            for i in lista:
                if (type(i) is str):
                        Label(resW, text = i).grid(row = r, column = c, columnspan = 2)
                        r+=1
                        continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1'''

        elif(op == 2):
            resW.title("Gradiente")
            #poe haders da tabela
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "a").grid(row = 0, column = 1)
            Label(resW, text= "b").grid(row = 0, column = 2)
            Label(resW, text= "(b-a)").grid(row = 0, column = 3)
            Label(resW, text= "µ").grid(row = 0, column = 4)
            Label(resW, text= "λ").grid(row = 0, column = 5)
            Label(resW, text= "f(µ)").grid(row = 0, column = 6)
            Label(resW, text= "f(λ)").grid(row = 0, column = 7)
            Label(resW, text= "f(µ) > ou < f(λ)?").grid(row = 0, column = 8)
            #executa funcao
            '''lista = funcoes.SecaoAurea(f, a, b, ep)
            r = 1
            c = 0
            for i in lista:
                if (type(i) is str):
                        Label(resW, text = i).grid(row = r, column = c, columnspan = 3)
                        r+=1
                        continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1'''

        elif(op == 3):
            resW.title('Newton')
             #poe haders da tabela
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "a").grid(row = 0, column = 1)
            Label(resW, text= "b").grid(row = 0, column = 2)
            Label(resW, text= "(b-a)").grid(row = 0, column = 3)
            Label(resW, text= "µ").grid(row = 0, column = 4)
            Label(resW, text= "λ").grid(row = 0, column = 5)
            Label(resW, text= "f(µ)").grid(row = 0, column = 6)
            Label(resW, text= "f(λ)").grid(row = 0, column = 7)
            Label(resW, text= "f(µ) > ou < f(λ)?").grid(row = 0, column = 8)
            #executa funcao
            '''lista = funcoes.SecaoFibonacci(f, a, b, ep)
            r = 1
            c = 0
            for i in lista:
                o = 0
                if (type(i) is str):
                        if(o == 1):
                            Label(resW, text = i).grid(row = r, column = c, columnspan = 5)
                            c+=5
                        else:
                            Label(resW, text = i).grid(row = r, column = c, columnspan = 2)
                            c+=2
                        o+=1
                        continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1'''

        elif(op == 4):
            resW.title("Gradiente Conjugado Generalizado")
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "a").grid(row = 0, column = 1)
            Label(resW, text= "b").grid(row = 0, column = 2)
            Label(resW, text= "x").grid(row = 0, column = 3)
            Label(resW, text= "f'(x)").grid(row = 0, column = 4)
            Label(resW, text= "f'(x) > 0?").grid(row = 0, column = 5)

            '''lista = funcoes.Bissecao(f, a, b, ep)
            r = 1
            c = 0
            for i in lista:
                if (type(i) is str):
                        Label(resW, text = i).grid(row = r, column = c, columnspan = 6)
                        r+=1
                        continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1'''
        
        elif(op == 5):
            resW.title("Fletcher and Reeves")
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "x").grid(row = 0, column = 1)
            Label(resW, text= "f'(x)").grid(row = 0, column = 2)
            Label(resW, text= "f''(x)").grid(row = 0, column = 3)
            Label(resW, text= "|f'(x)| > ε?").grid(row = 0, column = 4)
            Label(resW, text= "|xi-xi-1|/max{|xi|,1} > ε?").grid(row = 0, column = 5)

            '''lista = funcoes.Newton(f, a, ep)
            r = 1
            c = 0
            for i in lista:
                if (type(i) is str):
                        Label(resW, text = i).grid(row = r, column = c, columnspan = 6)
                        r+=1
                        continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1'''

        elif(op == 6):
            resW.title("Davison-Fletcher-Powell")
            Label(resW, text = "k").grid(row = 0, column = 0)
            Label(resW, text = "x").grid(row = 0, column = 1)
            Label(resW, text= "f'(x)").grid(row = 0, column = 2)
            Label(resW, text= "f''(x)").grid(row = 0, column = 3)
            Label(resW, text= "|f'(x)| > ε?").grid(row = 0, column = 4)
            Label(resW, text= "|xi-xi-1|/max{|xi|,1} > ε?").grid(row = 0, column = 5)

            '''lista = funcoes.Newton(f, a, ep)
            r = 1
            c = 0
            for i in lista:
                if (type(i) is str):
                        Label(resW, text = i).grid(row = r, column = c, columnspan = 6)
                        r+=1
                        continue
                for j in i:
                    Label(resW, text = str(j)).grid(row = r, column = c)
                    c+=1
                c=0
                r+=1'''

        if(gr):
            Grafico(f, 0.01, a, b)
        
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
funcao = Entry(dataF)
funcao.insert(0, "x^2-x*e^-x")
delta = Entry(dataF)
delta.insert(0, "0.04")
eEntry = Entry(dataF)
eEntry.insert(0, "0.01")
aEntry = Entry(dataF, width=5)
aEntry.insert(0, "0.1")
bEntry = Entry(dataF, width = 5)
bEntry.insert(0, "3")

#Botoes
info = Button(root, text = "i", command = Info).grid(row = 6, column = 1, sticky = E)
botao = Button(root, text = "Calcular!", command = Click).grid(row= 6, column = 2, sticky = W+E)


#Inserções na tela
#Labels
funcaoLabel = Label(dataF, text = "min f(x) = ").grid(row= 1, column = 1)
deltaLabel = Label(dataF, text = "Δ = ").grid(row= 2, column = 1)
epsolonLabel = Label(dataF, text = "ε = ").grid(row = 3, column = 1)
saLabel = Label(dataF, text = "s. a: { ").grid(row= 5, column= 1)
xLabel = Label(dataF, text = "≤x≤").grid(row= 5, column = 3)
#Entrys
funcao.grid(row = 1, column= 2, sticky=W+E, columnspan = 3)
delta.grid(row = 2, column= 2, sticky=W+E, columnspan = 3)
eEntry.grid(row = 3, column = 2, sticky = W+E, columnspan = 3)
aEntry.grid(row= 5, column = 2, sticky=W+E)
bEntry.grid(row= 5, column = 4, sticky=W+E)
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
#CheckButton
graficoCB.grid(row=6, column=0, sticky=W)


root.mainloop()