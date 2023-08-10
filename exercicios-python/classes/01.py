class Escola:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self, nome):
        if len(self.alunos) < 10:
            aluno = {"nome": nome}
            self.alunos.append(aluno)
            print("Aluno cadastrado com sucesso.")
        else:
            print("Limite máximo de alunos atingido.")

    def editar_aluno(self, indice, novo_nome):
        if 0 <= indice < len(self.alunos):
            self.alunos[indice]["nome"] = novo_nome
            print("Nome do aluno atualizado com sucesso.")
        else:
            print("Índice de aluno inválido.")

    def excluir_aluno(self, indice):
        if 0 <= indice < len(self.alunos):
            aluno_removido = self.alunos.pop(indice)
            print(f"Aluno '{aluno_removido['nome']}' removido com sucesso.")
        else:
            print("Índice de aluno inválido.")

    def mostrar_alunos(self):
        print("Lista de Alunos:")
        for indice, aluno in enumerate(self.alunos):
            print(f"{indice}: {aluno['nome']}")

# TESTE DA CLASSE
escola = Escola()

menu = -1
while menu != 0:
    print("------\nSistema Escolar:\n------")
    print("1-Cadastrar aluno\n2-Editar aluno\n3-Excluir aluno\n4-Mostrar alunos\n0-Sair")
    print("------")
    
    menu = int(input("Escolha uma opção: "))
    
    if menu == 1:
        nome_aluno = input("Informe o nome do aluno: ")
        escola.cadastrar_aluno(nome_aluno)
    elif menu == 2:
        indice_aluno = int(input("Informe o índice do aluno a ser editado: "))
        novo_nome_aluno = input("Informe o novo nome do aluno: ")
        escola.editar_aluno(indice_aluno, novo_nome_aluno)
    elif menu == 3:
        indice_aluno = int(input("Informe o índice do aluno a ser excluído: "))
        escola.excluir_aluno(indice_aluno)
    elif menu == 4:
        escola.mostrar_alunos()
    elif menu == 0:
        print("Sistema Encerrado.")
    else:
        print("Opção inválida.")
