# Leia a quantidade de alunos. Se for menor ou igual a zero, informe que a quantidade é inválida. Para uma quantidade válida, leia e armazene as notas, solicitando novamente qualquer nota fora da faixa de 0 a 10.

# Mostre todas as notas, a média, a maior nota, a menor nota e quantas atingiram pelo menos 7.

# Teste com apenas um aluno, com notas repetidas e com uma nota inválida seguida de uma válida.
listGradesStudents = []
aboveSevenGrade = 0
QuantityStudents = int(input("Digite a quantidade de alunos: "))

if QuantityStudents < 0:
    print("Quantidade invalida!")
else:
    for grades in range(1,QuantityStudents + 1):
        grade = int(input(f"Digite a nota do aluno {grades}: "))
        while grade < 0 or grade > 10:
             grade = int(input("Valor invalido! Digite novamente sua nota:  ")) 
        if grade >= 7:
            aboveSevenGrade += 1 
        listGradesStudents.append(grade)    
avarageGrades = sum(listGradesStudents) / len(listGradesStudents)
print("\n==============================")
print("Todas as notas dos alunos:", listGradesStudents)
print("Media das notas dos alunos:", avarageGrades)
print("Maior das notas dos alunos:", max(listGradesStudents))
print("Menor das notas dos alunos:", min(listGradesStudents))
print("Menor das notas dos alunos:", aboveSevenGrade)