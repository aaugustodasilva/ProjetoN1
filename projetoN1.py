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

def ordem_alfabetica():
    print(sorted(listaDeEmails))
    print(sorted(listaDeNomes))

def usuario_parte_lista():
    nome = input('Digite um nome especifico:')
    print(listaDeNomes. index(nome))

def email_parte_lista():
    email = input('Digite um e-mail especifico:')
    print(listaDeEmails. index(email))

def main():
    mostrarMenu()
    print(listaDeEmails)
    print(listaDeNomes)

if( __name__ == "__main__"):
    main()
