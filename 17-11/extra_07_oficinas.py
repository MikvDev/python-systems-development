# # Crie a classe Oficina, com nome, capacidade e inscritos. Receba nome e capacidade na criação; inicie inscritos com zero. Considere a capacidade um inteiro positivo.

# # Implemente:

# # inscrever(): adiciona uma pessoa se houver vaga;
# # cancelar(): remove uma pessoa se existir pelo menos uma inscrição;
# # vagas_disponiveis(): retorna a quantidade de vagas restantes.
# # Os métodos que alteram o estado retornam True quando realizam a operação e False quando a recusam.
# Use os métodos para realizar as tentativas. Depois, percorra a lista e mostre:

# nome, inscritos e vagas disponíveis de cada oficina;
# total de pessoas inscritas;
# total de vagas disponíveis;
# quantidade de oficinas lotadas.
# Conferência: Robótica tem 2 inscritos, Desenho tem 1 e Música tem 0. O relatório apresenta 3 inscritos, 3 vagas disponíveis e 1 oficina lotada.

# Repita o relatório com uma lista vazia: os três totais devem ser zero. Em um teste separado, cancele duas vezes uma oficina com apenas uma inscrição e confira que a segunda tentativa preserva zero inscritos.

class Oficina:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.inscritos = 0
    def inscrever(self):
        if self.inscritos < self.capacidade:
            self.inscritos += 1
            return True
        else:
            return False
    def cancelar(self):
        if self.inscritos >= 1:
            self.inscritos -= 1
            return True
        else:
            return False
    def vagas_disponiveis(self):
        return self.capacidade - self.inscritos
    def __str__(self):
       return( f"Nome: {self.nome} \n capacidade: {self.capacidade} \n vagas disponiveis: {self.vagas_disponiveis()}")


of1 = Oficina("Robotica", 2)
of2 = Oficina("Desenho", 3)
of3 = Oficina("Musica", 1)

of1.inscrever()
of1.inscrever()
of1.inscrever()
of2.inscrever()

oficinas = [of1,of2,of3]

for oficina in oficinas:
    print(oficina)