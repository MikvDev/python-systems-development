# Leia seis números inteiros e guarde todos em uma lista. Mostre a lista, a soma, a média, o maior e o menor valor.

# Teste com 3, -2, 0, 7, 7, -3: soma 12, média 2.0, maior 7 e menor -3.



listNumbers = []
numbersSum = 0
for numbers in range(1,7):
    number = int(input("Digite um numero:"))
    listNumbers.append(number)


avarage = sum(listNumbers) / 6
print("Lista de numeros:", listNumbers)
print("Soma dos numeros:", sum(listNumbers) )
print("Media de numeros da lista", avarage)
print("Maior valor:", max(listNumbers))
print("Menor valor:", min(listNumbers))

