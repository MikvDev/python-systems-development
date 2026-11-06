# Crie uma lista vazia e um menu com as opções:

# 1 - Adicionar pessoa ao final da fila
# 2 - Atender a primeira pessoa
# 3 - Mostrar a fila e sua quantidade de pessoas
# 0 - Sair
# Utilize append() para adicionar e pop(0) para atender. Antes de atender, verifique se há alguém na fila. Opções desconhecidas devem apresentar uma mensagem de erro.

# Teste atender com a fila vazia e adicionar Ana e Bruno para conferir a ordem dos atendimentos.


clientList = []



while True:
    print("\n======================================")
    print("1 - Adicionar pessoa ao final da fila")
    print("2 - Atender a primeira pessoa")
    print("3 - Mostrar a fila e sua quantidade de pessoas")
    print("0 - Sair")
    option = int(input("Digite uma opção: "))
    if option == 1:
        client = input("Digite o nome do cliente: ")
        clientList.append(client)
    elif option == 2:
        if len(clientList) > 0:
            print("Atendendo:", clientList.pop(0))
        else:
            print("Fila vazia!")
    elif option == 3:
        print("\n===================================")
        print(f"\nPessoas na fila: {clientList}")
        print(f"\nQuantidade de pessoas na fila {len(clientList)}")
    elif option == 0:
        print("saindo..")
        break
    