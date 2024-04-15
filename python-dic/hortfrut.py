print("Inicio do programa")
lista = []
executando = True

while executando:
    menu = ''' 
        S I S T E M A    P A R A     H O R T - F R U T
        (A)dicionar um novo produto
        (L)istar todos os produtos
        (p)esquisar por um produto especifico
        (S)air do sistema
        \n\n\n
        Digite a opção desejada ==>
        '''
    print(menu)
    opcao = input().lower()[0]

    if opcao == 'a':
        dic = {}
        nome = input("Qual o nome do produto? ")
        cor = input("Qual a cor do produto? ")
        preco = float(input("Qual o preço do produto? "))
        unidade_medida = input("Qual a unidade de medida do produto? ")
        dic = {"nome": nome, "cor": cor, "preco": preco, "unidade de medida": unidade_medida}
        lista.append(dic)
    elif opcao == 'l':
        for p in lista:
            print("Nome: ", {p["nome"]})
            print(f"Cor: {p['cor']}  Nome: {p['nome']}  Preço: {p['preco']}  {p['unidade de medida']}")
    elif opcao == 'p':
        print("Digite o nome do produto a ser pesquisado")
        n1 = input()
        for p in lista:
            if n1 == p["nome"]:
                print("Nome: ", p["nome"])
                print(f"Cor: {p['cor']}  Nome: {['nome']}  Preço: {p['preco']}  {p['unidade de medida']}")
    elif opcao == 's':
        print("\n\nObrigado pro usar nosso sistema!")
        executando = False