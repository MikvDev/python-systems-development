# Utilize a classe Produto e uma lista com três instâncias. Percorra a lista para mostrar nome, estoque e valor em estoque de cada uma.

# Mostre também:

# o valor total em estoque;
# a quantidade de produtos cujo estoque é zero.
# Teste com Produto("Caderno", 10.0, 2), Produto("Caneta", 3.0, 0) e Produto("Borracha", 2.0, 5).

# Resultado esperado: total 30.0 e um produto sem estoque. Repita com uma lista vazia: o total e a contagem devem ser zero.


class Produto:
    def __init__(self,nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def __str__(self):
        return f"Nome: {self.nome} | preço:{self.preco} | estoque: {self.estoque}"
    def valorTotalEstoque(self):
        return self.preco * self.estoque

productsList = [Produto("Caderno", 10.0, 2),Produto("Caneta", 3.0, 0), Produto("Borracha", 2.0, 5) ]
for produto in productsList:
    print(f"{produto}")



totalPrice = 0
outProductStock = 0
for produto in productsList:
    price = 0
    price += produto.valorTotalEstoque()
    print(f"Produto: {produto.nome} | valor em estoque: {produto.valorTotalEstoque()}")
    totalPrice += price

    if produto.estoque == 0:
        outProductStock += 1

print(f"Valor total em estoque: {totalPrice}")
print(f"Quantidade de produtos sem estoque: {outProductStock}")
