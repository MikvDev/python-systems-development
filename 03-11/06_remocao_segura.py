# Comece com ["Ana", "Bruno", "Ana", "Carla"]. Leia um nome e remova apenas sua primeira ocorrência, se existir. Caso contrário, mostre uma mensagem. Ao final, apresente a lista e a quantidade restante.

# Teste com Ana e com um nome ausente em execuções separadas.

listNames = ["Ana", "Bruno", "Ana", "Carla"]
name = input("Digite um nome:")
i = 0
if name in listNames:
        listNames.remove(name)
        print("Item removido!")
else:
    print("Não tem itens para remover!")
print(listNames)
