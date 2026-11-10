# Crie a classe Turma, com nome e uma lista própria alunos, inicialmente vazia. Implemente matricular(nome_aluno) e quantidade_alunos(), que retorna o tamanho da lista.

# Crie duas turmas. Matricule duas pessoas na primeira e uma na segunda. Mostre o nome de cada turma, seus alunos e sua quantidade.

# Nomes repetidos são permitidos neste exercício. Explique onde a lista deve ser criada para que uma turma não receba os alunos da outra.
# A lista é criada no construtor da classe turma, nela cada objeto possui sua instancia da lista de alunos, assim cada uma possui seus alunos sem interferir na outra
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular(self, nomeAluno):
        self.alunos.append(nomeAluno)
    def quantidade_alunos(self):
        print(f"\nQuantidade de alunos na turma {self.nome}: {len(self.alunos)}")
        for nome in self.alunos:
            print(f"Aluno: {nome}")

turma1 = Turma("241T")
turma2 = Turma("251T")
turma1.matricular("Miguel")
turma1.matricular("João")
turma2.matricular("Kima")
turma1.quantidade_alunos()
turma2.quantidade_alunos()
        