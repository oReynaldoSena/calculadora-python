from cProfile import label
from tkinter import *
from tkinter import *
from tkinter import ttk
from unittest import result
cor1 = "#3c3e40"
cor2 = "#143657"
cor3 = '#3f6675'

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

#Variáveis

allInputValues = ''
valorTexto = StringVar()
# Criando Frames 
frame_tela = Frame(janela, width=235, height=55, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268, bg=cor1)
frame_corpo.grid(row=1, column=0)

# Criando Label

app_label = Label(frame_tela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=( 'ivy 17 bold'), bg=cor3, fg = '#fff')
app_label.place (x=0, y=0)

# Criando Função de Entrada de Dados
def inputValues(event):
    global allInputValues

    allInputValues = allInputValues + str(event)
    valorTexto.set(allInputValues)

# Criando Função p/ Calcular

def calcular():
    global allInputValues
    resultado = eval(allInputValues)
    valorTexto.set (resultado)
    allInputValues = str(resultado)

# Criando Função Clean

def limpar():
    global allInputValues
    allInputValues = ""
    valorTexto.set('')


# Criando Botões 

b_1 = Button(frame_corpo, text="C",command=limpar, width=11, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0) # Botão Clean

b_2 = Button(frame_corpo,command=lambda: inputValues('%'), text="%", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0) #Operador de Módulo

b_3 = Button(frame_corpo, command=lambda: inputValues('/'),text="/", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE, )
b_3.place(x=177, y=0) #Divisão

b_4 = Button(frame_corpo, command=lambda: inputValues('7'),text="7", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52) # Número 7

b_5 = Button(frame_corpo, command=lambda: inputValues('8'),text="8", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52) # Número 8

b_6 = Button(frame_corpo, command=lambda: inputValues('9'),text="9", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52) # Número 9

b_7 = Button(frame_corpo, command=lambda: inputValues('*'),text="*", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52) #Multiplicação

b_8 = Button(frame_corpo, command=lambda: inputValues('4'),text="4", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104) # Número 4

b_9 = Button(frame_corpo, command=lambda: inputValues('5'),text="5", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104) # Número 5

b_10 = Button(frame_corpo, command=lambda: inputValues('6'),text="6", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104) # Número 6

b_11 = Button(frame_corpo, command=lambda: inputValues("+"),text="+", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command=lambda: inputValues('1'),text="1", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, command=lambda: inputValues('2'),text="2", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, command=lambda: inputValues('3'),text="3", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, command=lambda: inputValues('-'),text="-", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command=lambda: inputValues('0'),text="0", width=11, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo, command=lambda: inputValues('.'),text=".", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo, command=calcular,text="=", width=5, height=2, font=( 'ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)






janela.mainloop()