'''Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa(object): 
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome   
        self.idade = idade    
        self.peso = peso   
        self.altura = altura  
   
    def envelhecer(self):
        anos = int(input("Quantos anos a pessoa envelheceu? "))

        self.idade += anos
        if (self.idade < 21):
            self.altura += (anos * 0.5)

        # return "{} agora tem {} anos...".format(self.nome, self.idade)  
             

    def engordar(self):
        mais_peso = float(input("Quantos kg a pessoa ganhou? "))
        self.peso += mais_peso
        # return "{} agora pesa {} kg...".format(self.nome, self.peso)  
    
    def emagrecer(self):
        menos_peso = float(input("Quantos kg a pessoa perdeu? "))
        self.peso += menos_peso
        # return "{} agora pesa {} kg...".format(self.nome, self.peso)  
    
    def crescer(self):
        mais_altura = float(input("Quantos cm a pessoa ganhou? "))
        self.altura += mais_altura
        # return "{} agora mede {} cm...".format(self.nome, self.altura)  

    def informacoes(self):
        print(f"Nome: {self.nome}".format(self.nome))
        print(f"Idade atual: {self.idade} anos".format(self.idade))
        print(f"Peso atual: {self.peso} kg".format(self.peso))
        print(f"Altura atual: {self.altura} cm".format(self.altura))    
    

'''nome = str(input("Digite um nome: "))
idade = int(input("Digite uma idade: "))
peso = float(input("Digite um peso: "))
altura = float(input("Digite uma altura: "))

pessoa0 = Pessoa(nome, idade, peso, altura)'''

pessoa1 = Pessoa('Maria', 18, 50, 160)
pessoa2 = Pessoa('José', 21, 58, 175)

print ('----------------------')
pessoa1.envelhecer(), pessoa1.engordar(), pessoa1.crescer(), pessoa1.emagrecer()
print ('----------------------')
pessoa1.informacoes()