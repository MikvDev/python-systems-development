import os

# Inicialização da lista principal
listPoints = []

while True:
    print("\n1 - Registrar pontuação")
    print("2 - Mostrar relatório")
    print("3 - Desfazer o último registro")
    print("0 - Sair")

    op = int(input("Digite um número: "))
    
    if op == 1:
        points = int(input("Digite a pontuação (0 a 100): "))
        while points < 0 or points > 100:
            print("Número inválido! Digite valores apenas de 0 a 100.")
            points = int(input("Digite a pontuação novamente: ")) 
        
        listPoints.append(points)
        print(f"Pontuação {points} registrada com sucesso!")

    elif op == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----- RELATÓRIO -----")
        
        if len(listPoints) == 0:
            print("Não há missões registradas.")
        else:
            print("Pontuações na ordem de registro:")
            for idx, point in enumerate(listPoints, start=1):
                print(f"Missão {idx}: {point} pontos")
            
            # Cálculos automáticos baseados no estado atual da lista
            quantidade = len(listPoints)
            total = sum(listPoints)
            media = total / quantidade
            maior = max(listPoints)
            
            # Contagem de missões com pelo menos 70 pontos (pelo menos significa >= 70)
            missionAbove70 = sum(1 for p in listPoints if p >= 70)
            
            # DESAFIO ADICIONAL: Nova lista contendo apenas pontuações >= 70
            lista_filtrada = [p for p in listPoints if p >= 70]
            
            print(f"\nQuantidade de missões: {quantidade}")
            print(f"Total de pontos: {total}")
            print(f"Média das pontuações: {media:.1f}")
            print(f"Maior pontuação: {maior}")
            print(f"Missões com pelo menos 70 pontos: {missionAbove70}")
            print(f"Lista de altas pontuações (Desafio): {lista_filtrada}")

    elif op == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----- DESFAZER ÚLTIMO REGISTRO -----")
        
        if len(listPoints) == 0:
            print("Não há registro para desfazer.")
        else:
            # O enunciado pede para remover a ÚLTIMA pontuação usando pop() sem argumentos
            removido = listPoints.pop()
            print(f"O último registro ({removido} pontos) foi removido!")

    elif op == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Saindo do programa... Até logo!")
        break
        
    else:
        print("\nOpção inválida! Escolha um número entre 0 e 3.")
