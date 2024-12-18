class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
