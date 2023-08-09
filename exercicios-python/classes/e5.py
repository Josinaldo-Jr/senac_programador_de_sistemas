'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.'''

class ContaCorrete(object): 
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero  
        self.nome = nome   
        self.saldo = saldo   
   
    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito de R${}, realizado com sucesso!".format(self.saldo))
        else:
            print("O valor do depósito deve ser maior que zero.")
    
    def saque(self, valor):
        if (valor <= 0) or (self.saldo <= 0):
            print("O valor do saque deve ser maior que zero.")   
            
        else:
            self.saldo -= valor    
   
    def informacoes(self):
        print(f"Número da conta corrente: {self.numero}".format(self.numero))
        print(f"Nome do correntista: {self.nome}".format(self.nome))
        print(f"Saldo da conta: R$ {self.saldo}".format(self.saldo))



conta1 = ContaCorrete(123456, "João", 150)
conta2 = ContaCorrete(654321, "Maria", 300)

print ('----------------------')
conta1.alterarNome("Afonso")
conta1.deposito(150)
conta1.saque(50)
print ('----------------------')
conta1.informacoes()