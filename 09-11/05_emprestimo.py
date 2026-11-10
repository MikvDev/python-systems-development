# Crie uma classe Livro com titulo e emprestado. O título é recebido na criação; emprestado começa como False.

# emprestar() deve mudar o estado para True e retornar True, desde que o livro ainda não esteja emprestado. Caso contrário, deve retornar False.
# devolver() deve mudar o estado para False e retornar True, desde que exista um empréstimo. Caso contrário, deve retornar False.
# Teste duas tentativas de empréstimo seguidas de duas tentativas de devolução. Mostre os retornos e o estado após cada operação.

# Conferência: os retornos são True, False, True, False.

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


Livro1 = Livro("1000 tons de cinza", False)
print(Livro1.emprestar())
print(Livro1.emprestar())
print(Livro1.devolver())
print(Livro1.devolver())

    