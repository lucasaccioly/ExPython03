def exibir_menu():
    print("Menu:")
    print("1 - Ir")
    print("2 - Sair")

while True:
    exibir_menu()
    opcao = input("Escolha: ")

    if opcao == '1':
        print("Indo")
    elif opcao == '2':
        print("Você saiu.")
        break
    else:
        print("1 ou 2 burro")