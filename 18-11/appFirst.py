import tkinter as tk


window = tk.Tk()

window.geometry('300x200')
window.resizable(False,False)
window.title('Minha primeira aplicação')

lblWelcome = tk.Label(text="Olá, mundo!", font=("Poppins",20), pady=50)

lblWelcome.pack()
window.mainloop()