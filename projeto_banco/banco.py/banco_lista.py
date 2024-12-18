class BancoLista:
    def __init__(self, taxa_juros=0.01):
        self.contas = []
        self.taxa_juros = taxa_juros

    def cadastrar(self, conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print("Conta não encontrada.")

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print("Conta não encontrada.")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.saldo
        else:
            print("Conta não encontrada.")
            return None

    def render_juros(self, numero):
        conta = self.procurar_conta(numero)
        if conta and hasattr(conta, "render_juros"):
            conta.render_juros(self.taxa_juros)
        else:
            print("Conta não encontrada ou não é uma poupança.")
