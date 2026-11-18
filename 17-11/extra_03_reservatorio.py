# Crie a classe Reservatorio, recebendo capacidade e iniciando nivel com zero. Considere a capacidade positiva e todas as medidas em litros inteiros.

# Implemente:

# adicionar(litros): aceita uma quantidade positiva apenas se ela couber integralmente no reservatório;
# retirar(litros): aceita uma quantidade positiva apenas se houver água suficiente;
# espaco_disponivel(): retorna a diferença entre a capacidade e o nível atual.
# Os dois primeiros métodos devem retornar booleanos. Não aceite uma operação parcialmente: se alguém tentar adicionar mais água do que cabe, recuse toda a quantidade.

# Crie um reservatório de capacidade 100 e execute as operações abaixo em sequência. Complete a tabela antes de rodar o programa.

class Reservatorio:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.nivel = 0
    def adicionar(self,litros):
        if litros > 0 and litros <= self.capacidade:
            self.nivel += litros
            return True
        else:
            return False
    def remover(self,litros):
        if litros > 0 or litros <= self.nivel:
            self.nivel -= litros
            return True
        else:
            return False
    def espaco_disponivel(self):
        print( f"{self.capacidade - self.nivel  }")

r = Reservatorio(100)
r.adicionar(60)
r.remover(50)
r.espaco_disponivel()