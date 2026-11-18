class Marcador:
    def __init__(self, valor):
        self.valor = valor

    def somar(self, quantidade):
        self.valor = self.valor + quantidade


primeiro = Marcador(10)
atalho = primeiro
segundo = Marcador(10)

atalho.somar(5) # 15
segundo.somar(2) # 2
print(primeiro.valor) # 15
print(atalho.valor) # 15
print(segundo.valor) # 12

atalho = segundo # 12
atalho.somar(3) # 15 
print(segundo.valor) # 15


# Explique quantos objetos foram criados e por que a atribuição não cria um terceiro.
# Foram criados apenas 2 objetos, a variavel atalho é apenas uma copia do primeiro objeto em tempo de execução
# Altere a criação inicial de atalho para que ele seja um objeto independente de valor 10. Execute novamente e explique a mudança nas saídas.


primeiro = Marcador(10)
atalho = Marcador(10)
segundo = Marcador(10)

atalho.somar(5) # 15
segundo.somar(2) # 2
print(primeiro.valor) # 10
print(atalho.valor) # 15
print(segundo.valor) # 12

atalho = segundo # 12
atalho.somar(3) # 15 
print(segundo.valor) # 15
