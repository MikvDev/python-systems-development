class Leitura:
    def __init__(self,titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.paginas_lidas = 0

    # avancar(quantidade): aceita um inteiro positivo, desde que o total lido não ultrapasse o tamanho do livro; retorna True ou False;
    # paginas_restantes(): retorna quantas páginas faltam;
    # concluida(): retorna True se todas as páginas foram lidas e False caso contrário.

    def avancar(self,quantidade):
        if quantidade > 0:
            self.paginas_lidas += quantidade
            return True
        else:
            return False
    def paginas_restantes(self):
        print(self.total_paginas - self.paginas_lidas)
    def concluido(self):
        if self.paginas_lidas <= self.total_paginas:
            return True
        else:
            return False

l1 = Leitura('Neon Genesis Evangelion', 120)
l2 = Leitura('Neon Genesis Evangelion - You can(not) redo', 80)
l1.avancar(30)
l1.avancar(100)
l1.avancar(90)

# Para explicar: chamar concluida() duas vezes deve alterar o progresso? Justifique.
# Não este metodo só retorna se o total de páginas lidas é igual ao total de páginas do livro