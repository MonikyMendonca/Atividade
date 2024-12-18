from .conta import Conta

class ContaPoupanca(Conta):
    def render_juros(self, taxa_juros):
        self.saldo += self.saldo * taxa_juros
