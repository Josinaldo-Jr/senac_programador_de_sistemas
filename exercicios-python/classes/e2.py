'''Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''

class Quadrado(object): 
    def __init__(self, lado, novo_lado):
        self.lado = lado   
        self.novo_lado = novo_lado     
   
    def trocaLado(self):
        return "O Lado do quadrado era {} e foi mudado para: {}".format(self.lado, self.novo_lado)       

    def mostraLado(self):
        return self.lado
    
    def mostraArea(self):
        if self.novo_lado < self.lado:
            return self.lado * self.lado
        else:
            return self.novo_lado ** 2
    
quadrado1 = Quadrado(5, 10) 

print ("O Lado do quadrado é:", quadrado1.mostraLado())
print (quadrado1.trocaLado())
print ("A Área do quadro é:", quadrado1.mostraArea())