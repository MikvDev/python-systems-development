# Criar uma calculadora com interface tkinter

import tkinter as tk

window = tk.Tk()
window.geometry('500x500')





def sum():
    numberOne= inputNumberOne.get()
    numberTwo= inputNumberTwo.get()
    if numberOne == '' or numberTwo == '':
        return
    else:
        sumNumbers = float(numberOne) + float(numberTwo)
        
    
        lblResult.configure(text=f"{numberOne} + {numberTwo} = {sumNumbers}")


def subtract():
    numberOne= inputNumberOne.get()
    numberTwo= inputNumberTwo.get()
    if numberOne == '' or numberTwo == '':
        return
    else:
        sumNumbers = float(numberOne) - float(numberTwo)
        
    
        lblResult.configure(text=f"{numberOne} - {numberTwo} = {sumNumbers}")


def division():
    numberOne= inputNumberOne.get()
    numberTwo= inputNumberTwo.get()
    if numberOne == '' or numberTwo == '':
        lblResult.configure(text="Preencha os dois campos!")
        return
    try:
        n1 = float(numberOne)
        n2 = float(numberTwo)
    except ValueError:
        lblResult.configure(text="Digite apenas números!")
        return
    if n2 == 0:
        lblResult.configure(text="Não possivel divisão por 0")
        return
    r = float(numberOne) / float(numberTwo)
    
    lblResult.configure(text=f"{numberOne} / {numberTwo} = {r}")


def multiplication():
    numberOne= inputNumberOne.get().strip()
    numberTwo= inputNumberTwo.get().strip()
    
    if numberOne == '' or numberTwo == '':
        return
    else:
        sumNumbers = float(numberOne) * float(numberTwo)
        
    
        lblResult.configure(text=f"{numberOne} * {numberTwo} = {sumNumbers}")


welcomeTitle = tk.Label(text="Calculadora")
welcomeTitle.pack()


## Container de botões

btnsContainer = tk.Frame(
)
## Label e input numero 1
lblNumberOne = tk.Label(text="Numero 1")
lblNumberOne.pack()
inputNumberOne = tk.Entry(width=30)
inputNumberOne.pack()


## Label e input numero 2
lblNumberTwo = tk.Label(text="Numero 2")   
lblNumberTwo.pack()
inputNumberTwo = tk.Entry(width=30)
inputNumberTwo.pack()
## Botões de operações
btnResult = tk.Button(btnsContainer,text="+", command=sum)
btnSubtract =  tk.Button(btnsContainer,text="-", command=subtract)
btnMultiplication =  tk.Button(btnsContainer,text="*", command=multiplication)
btndivision =  tk.Button(btnsContainer,text="/", command=division)

## Label de resultado
lblResult = tk.Label(window, text="Resultado: ", font=("Arial", 12))

## subtitulo
lblOperations = tk.Label(text='Operações:', pady=10)
lblOperations.pack()
btnsContainer.pack(pady=20)
btnResult.grid(row=0, column=0,padx=5, pady=5)
btndivision.grid(row=0,column=1,padx=5, pady=5)
btnMultiplication.grid(row=1,column=0, padx=5, pady=5)
btnSubtract.grid(row=1,column=1,padx=5, pady=5)
lblResult.pack(pady=20)

window.mainloop()

