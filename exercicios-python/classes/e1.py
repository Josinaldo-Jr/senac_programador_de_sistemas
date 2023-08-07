'''Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor'''

class Bola(object): 
    def __init__(self, cor, circunferência, material):
        self.cor = cor
        self.circunferência = circunferência
        self.material = material

    def trocaCor(self):
        return "A cor {} da bola será trocada...".format(self.cor)    
    
    def mostraCor(self):
        return "A bola está com a cor {}...".format(self.cor)
    
bola = Bola("laranja", "20cm", "borracha")  
print (bola.mostraCor())  


