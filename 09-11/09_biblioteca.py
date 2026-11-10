# Utilize a classe Livro do exercício 05 e uma lista com três livros de títulos diferentes. Construa um menu:

# 1 - Mostrar livros e disponibilidade
# 2 - Emprestar um livro
# 3 - Devolver um livro
# 0 - Sair
# Nas opções 2 e 3, leia o título e procure o objeto com um for. Considere a correspondência exata entre os textos.

# Se encontrar, chame o método adequado e apresente uma mensagem conforme seu retorno.
# Se não encontrar, informe Livro não encontrado.
# Trate opções desconhecidas com uma mensagem.
# Repita o menu até escolher 0.
# Teste: emprestar um livro disponível, tentar emprestá-lo novamente, devolvê-lo, tentar devolver um livro disponível e procurar um título inexistente.

# As regras de empréstimo devem permanecer nos métodos. O menu fica responsável por receber entradas, localizar o objeto e mostrar os resultados.

import time
import os


class Livro:
    def __init__(self, titulo, emprestado):
        self.titulo = titulo 
        self.emprestado = emprestado

    def emprestar(self):
        if self.emprestado == False:
            self.emprestado = True
            return True
        else:
            return False
    def devolver(self):
        if self.emprestado == True:
            self.emprestado = False
            return True
        else:
            return False



# class Biblioteca:
#     def __init__(self, livros):
#         self.livros = livros[Livro]

#     def mostrar

livros = [Livro("0 tons de cinza",False), Livro("O iluminado",True ), Livro("A empregada", False)]
        

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n1 - Mostrar livros e disponibilidade")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("0 - Sair")


    op = int(input("Digite uma opção: "))
    if op == 1:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\----------- Livros -----------/")
        for livro in livros:
            print(f"Nome: {livro.titulo}")
            print(f"Emprestado: {livro.emprestado}")
        time.sleep(4)
        
    elif op == 2:
        buscaTitulo = input("Digite o nome do titulo que deseja retirar:").strip()
        encontrado = False
        for busca in livros:
            if buscaTitulo == busca.titulo:
                encontrado = True
                if busca.emprestar():
                    
                    print(f"Livro '{busca.titulo}' foi retirado! Fique atendo com a data de renovação ou devolução")
                else:
                    print("Este livro já foi retirado!")
                break
        if not encontrado:
            print("\nLivro não foi encontrado!")
            print("Tente alterar os termos de busca.")
        time.sleep(4)
    elif op == 3:
        buscaTitulo = input("Digite o nome do titulo que deseja devolver:").strip()
        encontrado = False
        for busca in livros:
            if buscaTitulo == busca.titulo:
                encontrado = True
                if busca.devolver():
                    print(f"Livro {busca.titulo} foi devolvido!")
                else:
                    print("Este livro já estava disponivel na biblioteca!")
                break
        if not encontrado:
            print("Livro não encontrado")
        time.sleep(3)
    elif op == 0:
        print("Saindo...")
        break
    else:
        print("Opção invalida!")
        
        
