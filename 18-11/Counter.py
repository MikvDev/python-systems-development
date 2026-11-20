import tkinter as tk

window = tk.Tk()


window.geometry("500x200")
window.resizable(False,False)

number = 0 ## global

def counter():
    global number ## Avisamos para utilizar a variavel number de escopo global
    number += 1
    labelNumbers.configure(text=f'Cliques: {number}')



labelTitle = tk.Label(window, text='Contador de Cliques', font=('Poppins', 14))
labelTitle.pack()


labelNumbers = tk.Label(window,text='Cliques:',pady=20)

btn = tk.Button(window, text='Clique aqui', width=20, pady=7,command=counter)
labelNumbers.pack()
btn.pack()


window.mainloop()