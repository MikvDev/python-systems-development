# Leia oito inteiros e armazene-os em uma lista. Percorra essa lista para criar outra contendo apenas os números pares. Mostre as duas listas. Preserve a ordem e os repetidos.

# Lembre-se: numero % 2 == 0 identifica um par, incluindo zero e pares negativos. Teste também uma execução sem nenhum par.



listNumber = []
pairNumbers = []
for numbers in range(1,9):
    number = int(input("Digite um numero: "))
    listNumber.append(number)
    if number % 2 == 0:
        pairNumbers.append(number)

print("TODOS OS NUMEROS = ", listNumber)
print("LISTA NUMEROS PARES =", pairNumbers)




