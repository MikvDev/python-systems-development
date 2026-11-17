# Uma sala possui duas lâmpadas que podem ser ligadas e desligadas separadamente.

# Identifique a classe, dois atributos e dois comportamentos que representam esse problema.
# Implemente a classe Lampada, recebendo local e iniciando o atributo ligada como False.
# Crie ligar() e desligar(). Cada método deve retornar True se mudar o estado e False se a lâmpada já estiver no estado solicitado.
# Crie uma lâmpada para a entrada e outra para o fundo da sala.
# Na lâmpada da entrada, execute ligar(), ligar(), desligar() e desligar(), nessa ordem.
# Conferência: os retornos são True, False, True e False. As duas lâmpadas terminam desligadas; a do fundo não sofre alterações durante as chamadas.

# Para explicar: qual é a diferença entre o retorno de desligar() e o valor de ligada após uma operação bem-sucedida?


class Lampada:   
    def __init__(self, local):
             self.ligado = False
             self.local= local
    def ligar(self):
         if self.ligado == True:
              return False
         else:
              self.ligado = True
              return True
    def desligar(self):
          pass
         
    
        
entrada = Lampada('entrada')
fundoSala = Lampada('fundoSala')
entrada.ligar()
entrada.ligar()
entrada.desligar()
entrada.desligar()







