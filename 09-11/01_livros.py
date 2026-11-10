class livro:
    def __init__(self, titulo,autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Titulo: {self.titulo} | autor: {self.autor} | quantidade de páginas: {self.paginas}"
    





livro1 = livro("Livro 1","Teste autor 1","300")
livro2 = livro("Livro 2","Teste autor 2","350")

# Para explicar: quais são a classe, as instâncias e os atributos? A alteração afetou os dois livros?

# A classe é livro, suas instancias são livro1 e livro2, seus atributos são titulo, autor e páginas. A mudança só afeta o objeto livro2 que teve seu atributo de numero de páginas alterado.

print(livro1)
print(livro2)

print("Mudando quantidade de páginas do livro 2:")
livro2.paginas = 20
print(livro2)