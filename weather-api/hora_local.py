import requests

while True:
    print("----------------")
    print(" 1 - Pesquisar")
    print(" 2 - Sair")
    print("----------------")
    opcao = input()
    if opcao == "1":
        local = input("Bota o local ai: ")
        response = requests.get(f"http://api.weatherapi.com/v1/timezone.json?key=dcd8c76f43294f32b7e120215240710&q={local}")
        dicionario = {
            'name': response.json()['location']['name'],
            'region': response.json()['location']['region'],
            'localtime': response.json()['location']['localtime']
        }
        print("Em " + dicionario['name'] + ", o hórario é " + dicionario['localtime'] + " da região " + dicionario['region'])
    else:
        print("Até Breve")
        break