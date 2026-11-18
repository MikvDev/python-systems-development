import tkinter as tk



window = tk.Tk() ## Cria a janela

window.title("Essa é minha janela") ## Definimos o nome da janela
window.geometry("500x500") ## Dwfinimos o tamanho da janela

container = tk.Frame(window
)
welcomeLabel = tk.Label(container)
def SingUp():
    age = inputAge.get()
    name = inputName.get()
    email = inputEmail.get()
    city = inputCity.get()
    if age == "" or name == "" or email == '':
        print("Valores de entrada dos inputs estão vazios ")
        return
    else:
        
        
        welcomeLabel.configure(text=f"Olá {name}, idade: {age} Seu email de cadatro é: {email}, cidade que reside: {city}" )
    


# Componente de texto
texto = tk.Label(
    window,
    text = "Seja Bem-vindo",
    font=("Times New Roman", 14),
    fg="#000"
)

# Componete de botão 
botao = tk.Button(container,
    text="Cadastrar",
    border=2,
    borderwidth=4,
    width=25,
    command=SingUp
)




container.pack()
lblName = tk.Label(container,text="Nome:")
lblName.grid(row=0, column=0, padx=10, pady=10, sticky='w')
inputName = tk.Entry(container,width=30)
inputName.grid(row=0,column=1,padx=10, pady=10)



lblAge = tk.Label(container,text="Idade:")
lblAge.grid(row=1, column=0)
inputAge = tk.Entry(container,width=30)
inputAge.grid(row=1,column=1,padx=20, pady=20)



lblEmail = tk.Label(container,text="Email:")
lblEmail.grid(row=2, column=0)
inputEmail = tk.Entry(container,width=30)
inputEmail.grid(row=2,column=1,padx=20, pady=20)

lblCity = tk.Label(container,text="Cidade:")
lblCity.grid(row=3, column=0)
inputCity = tk.Entry(container,width=30)
inputCity.grid(row=3,column=1,padx=20, pady=20)
botao.grid(row=4, column=1)

welcomeLabel = tk.Label(window, text="Olá, preencha o formulário.", font=("Arial", 9))
welcomeLabel.pack(pady=20, padx=10)


window.mainloop()  ## mantem a janela ativa

