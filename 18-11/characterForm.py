# Desenvolva uma interface gráfica para cadastrar personagens de um RPG. Cada personagem deverá possuir nome, classe, nível e quantidade de pontos de vida.

# Ao clicar no botão "Cadastrar personagem", o programa deverá validar as informações, adicionar o personagem a uma lista e apresentar os personagens cadastrados na interface.

import tkinter as tk

window = tk.Tk()
window.geometry('500x500')
window.resizable(False, False)



# classe character 

## Nome
## Classe
## Nivel
## Quantidade de pontos de vida


listUser = []

class Charater:
    def __init__(self, name, userClass,xp, life):
        self.name = name
        self.userClass = userClass
        self.xp = xp
        self.life = life
    def __str__(self):
        return f"{self.name} ({self.userClass}) | Nv.{int(self.xp)} | HP:{int(self.life)}"

    
# função de cadastro

def singUp():
    name = inputName.get().strip()
    userClass = inputClass.get().strip()
    xp = inputXP.get().strip()
    life = inputLife.get().strip()

   
    

    if name == '' or userClass == '' or xp == '' or life == '':
            lblInfo.configure(text="preecha todos os campos vazios.")
            return
    try:
        xp =float(xp)
        life =float(life)
        if xp < 0 or life <= 0:
            lblInfo.configure(text="campos de xp e vida devem ser positivos ou maiores que 0.")
            return
        newCharacter = Charater(name, userClass, xp, life)
        listUser.append(newCharacter)
        ListCharacters.insert(tk.END,newCharacter)

        # Limpeza dos buffers dos campos 
        inputName.delete(0, tk.END)
        inputClass.delete(0, tk.END)
        inputXP.delete(0, tk.END)
        inputLife.delete(0, tk.END)
        lblInfo.configure(text="Personagem cadastrado com sucesso!")


    except ValueError:
        lblInfo.configure(text="Valores numericos não podem ser caracteres")
        print("Valores numericos não podem ser caracteres")


def remove():
    indice = ListCharacters.curselection()
    values = [ListCharacters.get(i) for i in indice]
    ListCharacters.delete(values)
    



    
        


# Frame

mainContainer = tk.Frame()
containerForm = tk.Frame(mainContainer,padx=20, pady=50)
# Labels 

lblName = tk.Label(containerForm,text='Nome', font=('Poppins',12))
lblClass = tk.Label(containerForm,text='Classe', font=('Poppins',12))
lblXP = tk.Label(containerForm, text='Nivel', font=('Poppins',12))
lblLife = tk.Label(containerForm,text='Vida', font=('Poppins',12))
lblInfo = tk.Label(mainContainer,text='')

# Lista 


ListCharacters = tk.Listbox(mainContainer,selectmode=tk.EXTENDED, width=30)
# Inputs

inputName = tk.Entry(containerForm)
inputClass = tk.Entry(containerForm)
inputXP = tk.Entry(containerForm)
inputLife = tk.Entry(containerForm)


# Botão

singUpBtn = tk.Button(containerForm,text='Cadastrar', command=singUp, width=17)
removeBtn = tk.Button(containerForm,text='Remover', command= remove  ,width=17)
# Posicionamento no grid

lblName.grid(row=0,column=0)
lblClass.grid(row=1,column=0)
lblXP.grid(row=2,column=0)
lblLife.grid(row=3,column=0)

inputName.grid(row=0,column=1)
inputClass.grid(row=1,column=1)
inputXP.grid(row=2,column=1)
inputLife.grid(row=3,column=1)



singUpBtn.grid(row=4,column=1, pady=5)
removeBtn.grid(row=5, column=1)
lblInfo.grid(row=7, column=1, )

ListCharacters.grid(row=0,column=1)
mainContainer.pack()
containerForm.grid(row=0, column=0)








window.mainloop()