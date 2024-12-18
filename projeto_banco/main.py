from banco import BancoLista
from contas import Conta, ContaPoupanca

# Criando o banco
banco = BancoLista(taxa_juros=0.02)

# Criando contas
conta1 = Conta(101, 500)  # Conta comum
conta2 = ContaPoupanca(202, 1000) 


banco.cadastrar(conta1)
banco.cadastrar(conta2)


banco.creditar(101, 200)  
banco.debitar(202, 50)    
banco.render_juros(202)   


print(f"Saldo conta 101: R${banco.saldo(101):.2f}")
print(f"Saldo conta 202: R${banco.saldo(202):.2f}")
