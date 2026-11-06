# Use a lista ["corda", "água", "mapa", "água"]. Leia o nome de um item e informe se ele existe e quantas vezes aparece. Diferencie maiúsculas e minúsculas.

# Teste com água (duas ocorrências), mapa (uma) e lanterna (nenhuma).

lista = ["corda", "água", "mapa", "água"]
foundElement = 0
objectName = input("Digite um nome:")

for name in lista:
    if objectName == name:
      
        foundElement += 1

if foundElement > 0:
    print("Este item existe na lista!")
    print("Quantidade do item digitado na lista:", foundElement)
else:
    print("Este item não existe na lista")

