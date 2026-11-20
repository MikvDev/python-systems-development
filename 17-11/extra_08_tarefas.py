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

import os
import time


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
    def reabrir(self):
        if self.concluida != False:
            self.concluida = False
            return True
        else:
            return False
    def __str__(self):

       status  = "sim" if self.concluida else 'pendente'
       return(f"{self.descricao} - concluida: {status}")
  
listaTarefas = []



while True:
    
    print("\n1 - Cadastrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Reabrir tarefa")
    print("5 - Resumo")
    print("0 - Sair")

    op = input("\n<| -> Digite uma opção:")
    if op == '1':
    
        descricao = input("<| -> Digite a descricao da tarefa: ").strip().lower()

        existe = any(t.descricao == descricao for t in listaTarefas)
        if descricao == "" or existe:
            print("\nDescrição vazia ou já está na lista")
        else:
            newTarefa = Tarefa(descricao) 
            listaTarefas.append(newTarefa)
    elif op == '2':
        if not listaTarefas:
            print("Nenhuma tarefa cadastrada!")
        else:
            i = 0
            print("\nLista de tarefas")
            for tarefa in listaTarefas:
                i+=1
            
                print(f"<| -> {i} - {tarefa.descricao}")
    elif op == '3':
        busca =  input("Digite a descricao da tarefa que deseja concluir: ").strip().lower()
        encontrada = False
        for tarefa in listaTarefas:
            if tarefa.descricao == busca:   
                if tarefa.concluir():
                    encontrada = True
                    
                    print("Tarefa concluida!")
                else:
                    print("Terafa já está concluida!")
                break
        if not encontrada:
            print("Tarefa não foi enconutrada!")
    elif op == '4':
        busca =  input("Digite a descricao da tarefa que deseja reabrir: ").strip().lower()
        existe = False
        for tarefa in listaTarefas:
            if tarefa.reabrir():
                existe = True
                print("Tarefa foi reaberta!")   
            else:
                print("Esta tarefa já está aberta!")
            break

        if not existe:
            print("Tarefa não foi encontrada!")
        pass
    elif op == '5':
        if len(listaTarefas) > 0:
            total = 0
            concluidas = 0
            pendentes =0 

            os.system('cls' if os.name == 'nt' else 'clear')
            print('<| - Tarefas - |>')
            for tarefa in listaTarefas:
              if tarefa.concluida == True:
                  concluidas += 1
              else:
                  pendentes += 1 
              print(tarefa)
            print("\nTotal:", len(listaTarefas))
            print("Pendentes:", pendentes)
            print("Concluidas:", concluidas)
            time.sleep(4)
        else:
            print("Nenhuma tarefa criada")
    elif op == '0':
        break
    else:
        print("Opção invalida!")
            