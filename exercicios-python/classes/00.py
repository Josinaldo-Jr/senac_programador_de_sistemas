'''Classe Escola: Crie uma classe que modele uma escola:

Métodos: cadastrar, editar, listar e deletar.
Limite de 10 alunos'''

class Escola(object): 
    def __init__(self):
        self.alunos = [] 
        self.vagas = 0
   
    def cadastrar(self):
        if self.vagas < 2:
            self.alunos.append(str(input("Digite o nome do aluno para cadastrar: ")))
            self.vagas += 1   
            print("Aluno cadastrado com sucesso.")   

        else:
            print("Sem vagas no sistema.") 

    def editar(self, nome_antigo, nome_novo):
        if nome_antigo in self.alunos:
            indice_aluno = self.alunos.index(nome_antigo)
            self.alunos[indice_aluno] = nome_novo
            print(f"O aluno '{nome_antigo}' foi alterado para '{nome_novo}' com sucesso.")
        else:
            print(f"O nome '{nome_antigo}' não foi encontrado.")

    def excluir(self, nome_del):
        if nome_del in self.alunos:
            self.alunos.remove(nome_del)
            print(f"O aluno '{nome_del}' foi excluído com sucesso.")
        else:
            print(f"O aluno '{nome_del}' não foi encontrado.")


    def mostrar(self):
                


            






                  

    

escola = Escola()

# menu = -1
# while != 0:
while True:
    print("------\nSistema Escolar:\n------")
    print("1-Cadastrar aluno\n2-Editar aluno\n3-Excluir aluno\n4-Mostrar alunos\n0-Sair")
    print("------")

    menu = int(input("Escolha uma opção: "))

    if menu == 0:
        print("------\nSistema Encerrado.\n------")

        break

    elif menu == 1:
         print("------\nCadastrar Aluno: ")
         escola.cadastrar()         

    elif menu == 2:
         print("------\nEditar Aluno:\n------")  

         nome_antigo = str(input("Digite o nome do aluno que você quer alterar: "))
         nome_novo = str(input("Digite o novo nome: "))         

         escola.editar(nome_antigo, nome_novo)

    elif menu == 3:
         print("------\nExcluir Aluno:\n------")

         nome_del = str(input("Digite o nome do aluno que você quer excluir: "))
         escola.excluir(nome_del)

    elif menu == 4:
         print("------\nMostrar Alunos:\n------")   

    else:
        print("------\nOpção inválida.")        

          



        