class Placar:
    def __init__(self, jogador):
        self.jogador = jogador
        self.pontos = 0

    def marcar(self,quantidade):
        if quantidade < 0:
            return False
        else:
            self.pontos = self.pontos + quantidade
            return True
    def consultar_pontos(self):
        return self.pontos

placar = Placar("Lia")
placar.marcar(3)
placar.marcar(2)
placar.marcar(0)
placar.marcar(-1)
print(placar.jogador, placar.pontos)
pontos = placar.consultar_pontos() 
print("Dobro dos pontos: ", pontos * 2)

# Corrija a inicialização dos atributos e a definição do método.
# Faça marcar(quantidade) aceitar apenas inteiros positivos, retornando True quando somar os pontos e False quando recusar o valor. Considere que o argumento já é inteiro.
# Acrescente consultar_pontos(), que retorna a pontuação sem alterá-la.
# Execute marcar(3), marcar(2), marcar(0) e marcar(-1).
# Guarde o retorno de consultar_pontos() em uma variável e mostre seu dobro.
# Conferência: os retornos das marcações são True, True, False e False. A pontuação final é 5, e seu dobro é 10.

# Para explicar: por que escrever apenas pontos = 0 em __init__ não cria um atributo do objeto?
# Por que dessa maneira o usuário não pode passar nenhum atributo para a classe, ela já vem setada com 0 desde o inicio, é uma maneira de criar seu construtor.

