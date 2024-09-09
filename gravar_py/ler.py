import requests
import json

url = "https://dtspm-327f2-default-rtdb.firebaseio.com/contatos.json"

response = requests.get( url )

texto = response.text

print("Response: ", response)
print("Corpo: ", response.text)

contatos = json.loads(texto)

print("Chaves dos contatos: ")
# for chave in contatos.keys():
#     print(chave)

for contato in contatos.values():
    print(f"Nome: {contato['nome']}\nEmail: {contato['email']}")
    print("-"*50)