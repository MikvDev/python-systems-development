saldo = 80
saldo_anterior = saldo

saldo = saldo - 25
saldo = saldo + 10

print("Saldo anterior:", saldo_anterior) # 80
print("Saldo atual:", saldo) # 65


# Anote em comentários os valores que serão mostrados.
# Execute o código para conferir.
# Explique por que saldo_anterior mantém o valor que recebeu na atribuição, mesmo depois das mudanças em saldo.
# Acrescente uma despesa de 15 ao saldo atual e mostre novamente as duas variáveis.


saldo = saldo - 15
print("Saldo anterior:", saldo_anterior) # 80
print("Saldo atual:", saldo) # 50
    
# O saldo anterior mantém o valor que recebeu na atribuição porque ele foi definido antes das alterações no saldo. Quando fazemos a atribuição `saldo_anterior = saldo`, o valor de `saldo` naquele momento (80) é copiado para `saldo_anterior`. Alterações subsequentes em `saldo` não afetam `saldo_anterior`, pois são variáveis independentes.