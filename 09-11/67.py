# Altura total do desenho
altura = 7

# Desenhando linha por linha
while altura:
 for linha in range(altura):
    # --- Desenho do Número 6 ---
    if linha == 0 or linha == 3 or linha == 6:
        print("6666 ", end="")  # Topo, meio e base do 6
    elif linha < 3:
        print("6    ", end="")  # Lateral superior esquerda do 6
    else:
        print("6  6 ", end="")  # Corpo inferior do 6 (duas laterais)

    # Espaço de separação entre os números
    print("   ", end="")

    # --- Desenho do Número 7 ---
    if linha == 0:
        print("77777", end="")  # Topo do 7
    elif linha == 1:
        print("    7", end="")  # Começo da descida
    elif linha == 2:
        print("   7 ", end="")
    elif linha == 3:
        print("  7  ", end="")  # Diagonal descendo
    elif linha == 4:
        print(" 7   ", end="")
    else:
        print("7    ", end="")  # Base do 7

    # Pula para a próxima linha do terminal
    print()
