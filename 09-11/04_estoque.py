# Implemente a classe Produto com os métodos repor, vender e valor_em_estoque apresentados na aula.

# Crie um produto de preço 5.0 e estoque 4. Execute, nesta ordem:

# Venda de 2 unidades.
# Tentativa de venda de 3 unidades.
# Reposição de 5 unidades.
# Tentativa de reposição de 0 unidades.
# Registre o retorno e o estoque após cada chamada. Ao final, mostre o valor em estoque.

# Conferência: os estoques devem ser 2, 2, 7 e 7. O valor final deve ser 35.0.

class Produto:
    def __init__(self, preco, estoque):
        self.preco = preco
        self.estoque = estoque


    def repor(self, quantidadeRepor):
        if quantidadeRepor <= 0:
            print("Valores negativos não são permitidos! Tente novamente com valores validos.")
            return
        self.estoque += quantidadeRepor
    def vender(self, quantidadeVender):
        if quantidadeVender > self.estoque:
            print("Valor excede estoque! Tente novamente com um valor valido.")
            return
        self.estoque -= quantidadeVender
    def valorEmEstoque(self):
        return f"Valor em estoque: {self.estoque}"


produto1 = Produto(5.0,4)
produto1.vender(2)
print(produto1.estoque)
produto1.vender(3)
print(produto1.estoque)
produto1.repor(5)
print(produto1.estoque)
produto1.repor(0)
print(produto1.estoque)