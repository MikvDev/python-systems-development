# Crie a classe Conta, recebendo apenas titular. O saldo inicial deve ser zero.

# Implemente:

# depositar(valor): aceita somente valores positivos;
# sacar(valor): aceita somente valores positivos e menores ou iguais ao saldo;
# ambos os métodos retornam True quando realizam a operação e False quando a recusam, preservando o saldo em caso de recusa.
# Crie duas contas independentes. Na primeira, deposite 50, saque 20, tente sacar 40 e tente depositar -10. A segunda deve permanecer com saldo zero.

# Conferência: saldo final da primeira conta 30; retornos True, True, False, False.

class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    def depositar(self, valor):
       if valor > 0: 
            self.saldo += valor 
            return True
       return False
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False


conta1 = Conta("Miguel")
conta1.depositar(50)
conta1.sacar(20)
conta1.sacar(40)
conta1.depositar(-10)
conta2 = Conta("João")

print(conta1.saldo)