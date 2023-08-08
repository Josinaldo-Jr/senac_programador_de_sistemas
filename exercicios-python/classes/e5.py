'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.'''

class ContaCorrete(object): 
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero  
        self.nome = nome   
        self.saldo = saldo   
   
    def alterarNome(self, nome):
        nome = str(input("Para qual nome você quer alterar? "))
        self.nome = nome

        # return "{} agora tem {} anos...".format(self.nome, self.idade)  

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
        print(f"Número da conta corrente: {self.nome}".format(self.nome))
        print(f"Nome do correntista: {self.idade} anos".format(self.idade))
        print(f"Saldo da conta: {self.peso} kg".format(self.peso))

'''nome = str(input("Digite um nome: "))
idade = int(input("Digite uma idade: "))
peso = float(input("Digite um peso: "))
altura = float(input("Digite uma altura: "))

pessoa0 = Pessoa(nome, idade, peso, altura)'''

conta1 = ContaCorrete(123456, "João", 150)
conta2 = ContaCorrete(654321, "Maria", 300)

print ('----------------------')
pessoa1.envelhecer(), pessoa1.engordar(), pessoa1.crescer(), pessoa1.emagrecer()
print ('----------------------')
pessoa1.informacoes()