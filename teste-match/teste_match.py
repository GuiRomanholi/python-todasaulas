while True:
    print("M E N U - O P C O E S")
    print("(C)adastrar")
    print("(M)ostrar")
    print("(R)emover")
    print("(A)tualizar")
    print("(S)air")

    opcao = input("Adicione sua opcao: ").upper()[0]

    match opcao:
        case "C": 
            print("Bem Vindo Ao Cadastro")
        case "M":
            print("Bem Vindo Ao Mostrar")
        case "R":
            print("Bem Vindo Ao Remover")
        case "A":
            print("Bem Vindo Ao Atualizar")
        case "S":
            print("Até Breve!")
            break
        case _:
            print("Opcao invalida")
