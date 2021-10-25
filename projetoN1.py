def mostrarMenu():
    print("--------------Sistema de Cadastro de Alunos---------------")
    print("1 - Cadastrar Nome e Emails: ")
    print("2 - Exibir cadastrados por ordem de cadastro: ")
    print("3 - Exibir cadastrados por ordem Alfabética: ")
    print("4 - Buscar se usuário faz parte de uma lista: ")
    print("5 - Remover usuário: ")
    print("6 - Alterar nome de usuário: ")
    print("7 - Sair: ")

# criando uma lista de nomes vazia
listaDeNomes = []

# criando uma lista de e-mails vazia
listaDeEmails = []

def cadastro_nome():
    listaDeNomes = list
    listaDeNomes = listaDeNomes.append(input('Digite seu nome:\n'))

def cadastro_email():
    listaDeEmails = list 
    listaDeEmails = listaDeEmails.append(input('Digite seu email:\n'))

def ordem_cadastro():
    print("Lista de nomes por ordem de cadastro: " + listaDeNomes +"")

def ordem_alfabetica():
    print(sorted(listaDeEmails))
    print(sorted(listaDeNomes))

def usuario_parte_lista():
    nome = input('Digite um nome especifico:')
    print(listaDeNomes. index(nome))

def email_parte_lista():
    email = input('Digite um e-mail especifico:')
    print(listaDeEmails. index(email))

def escolher_menu():
    return int(input())

def remover_nome():
    print(listaDeNomes)
    Nome_Remover = input("Escolha o nome a ser removido:")
    if(Nome_Remover == listaDeNomes.index(Nome_Remover)):
        listaDeNomes.pop(Nome_Remover)
    else:
        print("Nome não existente")

def alterar_nome():
    Nome_Novo = print = input("Digite o nome para substituir:")
    print(listaDeNomes)
    Indice_Alterar = int(input("Escolha o nome a ser alterado: Obs.: o primeiro começa com 0"))
    listaDeNomes[Indice_Alterar] = Nome_Novo
    print(listaDeNomes)

def main():
    mostrarMenu()
    opcaoEscolhida = escolher_menu()

    while (opcaoEscolhida != 7):
        if(opcaoEscolhida == 1):
            cadastro_nome(listaDeNomes)
            cadastro_email(listaDeEmails)
        elif(opcaoEscolhida ==2):
            ordem_cadastro(listaDeNomes)
        elif(opcaoEscolhida ==3):
            ordem_alfabetica(listaDeNomes)
        elif(opcaoEscolhida ==4):
            usuario_parte_lista(listaDeNomes)
        elif(opcaoEscolhida ==5):
            remover_nome(listaDeNomes)
        elif(opcaoEscolhida ==6):
            alterar_nome(listaDeNomes)

if( __name__ == "__main__"):
    main()
