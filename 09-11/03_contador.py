# Crie a classe Contador. Cada instância deve começar com valor = 0 e oferecer os métodos incrementar() e zerar().

# Crie dois contadores. Incremente o primeiro três vezes e o segundo uma vez. Mostre os valores, zere somente o primeiro e mostre novamente.

# Resultado esperado: primeiro 3 e 1; depois 0 e 1.
class contador:
    def __init__(self, i):
        self.i = i

    def __init__(self):
        self.i = 0

    def incrementar(self):
        self.i += 1
    def zerar(self):
        self.i = 0


contador1 = contador()
contador2 = contador()


contador1.incrementar()
contador1.incrementar()
contador1.incrementar()
print(f"Contador 1: {contador1.i}")
contador2.incrementar()
print(f"Contador 2: {contador2.i}")
contador1.zerar()
print(f"Contador 1: {contador1.i}")
print(f"Contador 2: {contador2.i}")

