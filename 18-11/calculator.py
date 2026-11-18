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


welcomeTitle = tk.Label(text="Calculadora")
welcomeTitle.pack()
btnResult = tk.Button(text="=", command=sum)

lblNumberOne = tk.Label(text="Numero 1")
lblNumberOne.pack()
inputNumberOne = tk.Entry(width=30)
inputNumberOne.pack()
  


lblNumberTwo = tk.Label(text="Numero 2")   
lblNumberTwo.pack()
inputNumberTwo = tk.Entry(width=30)
inputNumberTwo.pack()
btnResult.pack(pady=10)
lblResult = tk.Label(window, text="Resultado: ", font=("Arial", 12))


lblResult = tk.Label()
lblResult.pack(pady=20)
window.mainloop()

