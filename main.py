import sys

from workspace import criarEntrada, saida1, saida2

def menu():

    print("\nEscolha uma opção\n")
    print("-n para entrar com dados")
    print("-s1 para criar saida 1")
    print("-s2 para criar saida 2")
    print("'sair' para encerrar a aplicação\n")

    opcao = input("Digite uma opção: ")

    if opcao == "-n":
        criarEntrada()
        menu()
    elif opcao == "-s1":
        saida1()
        menu()
    elif opcao == "-s2":
        saida2()
        menu()
    elif opcao == "sair":
        sys.exit()

menu()