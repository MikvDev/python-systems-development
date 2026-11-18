# Crie a classe Tarefa, recebendo descricao e iniciando concluida com False.

# concluir() muda o estado para True se a tarefa estiver pendente.
# reabrir() muda o estado para False se a tarefa estiver concluída.
# Os dois métodos retornam True quando alteram o estado e False caso contrário.
# Mantenha uma lista de objetos Tarefa e implemente o menu:



# Regras:

# Inicie com uma lista vazia.
# No cadastro, recuse descrição vazia ou exatamente igual à de uma tarefa existente.
# Na listagem, mostre descrição e situação de cada tarefa. Se não houver tarefas, informe isso.
# Nas opções 3 e 4, procure a descrição exata com um for. Informe quando não encontrar a tarefa; quando encontrar, apresente uma mensagem de acordo com o retorno do método.
# No resumo, mostre o total de tarefas, quantas estão pendentes e quantas estão concluídas. Percorra os objetos para calcular as contagens.
# Informe opções desconhecidas e repita o menu até receber 0.
# O menu recebe entradas, procura objetos e apresenta resultados. As mudanças entre pendente e concluída ficam nos métodos da classe.

# Roteiro de conferência: liste e consulte o resumo antes de cadastrar qualquer tarefa; cadastre Estudar POO e Revisar listas; tente repetir o primeiro cadastro; conclua Estudar POO duas vezes; procure uma descrição inexistente; reabra a primeira tarefa duas vezes; tente cadastrar "" pressionando apenas Enter; informe uma opção desconhecida e encerre.

# Resultados de referência: após concluir a primeira tarefa, o resumo deve indicar 2 tarefas, 1 pendente e 1 concluída. Após reabri-la, deve indicar 2 pendentes e 0 concluídas. Tentativas recusadas não alteram esses totais.

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False
    def concluir(self):
        if self.concluida != True:
            self.concluida = True
            return True
        else:
            return False
  

listaTarefas = []


while True:
    # arrume esse menu com prints 
    print("\n1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Reabrir tarefa")
    print("5 - Resumo")
    print("0 - Sair")

    op = input("\n<| -> Digite uma opção:")
    if op == '1':
        descricao = input("<| -> Digite a descricao da tarefa: ")
        if descricao == "" or descricao in listaTarefas:
            pass
        else:
            listaTarefas.append(Tarefa(descricao))
    elif op == '2':
        i = 0
        print("\nLista de tarefas")
        for tarefa in listaTarefas:
            i+=1
            
            print(f"<| -> {i} - {tarefa.descricao}")
    elif op == '3':
        concluirTarefa =  input("Digite a descrição da tarefa que deseja concluir")
        if concluirTarefa in listaTarefas:
               
    elif op == '0':
        break
            