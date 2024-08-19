lista = ["Ola", "João", "Maria", "Jose", "Sara"]

match lista:
    case [cumprimento,*nomes]:
        for nome in nomes:
            print("Nomes: ", nome)
            print("Cumprimento: ", cumprimento)