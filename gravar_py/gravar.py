import requests

url = "https://dtspm-327f2-default-rtdb.firebaseio.com/contatos.json"


contato = {
    "nome": "Alberto Santos", 
    "telefone": "(13) 1432-2532",
    "email": "albert@teste.com"
}

response = requests.post( url, json=contato )
print(response)