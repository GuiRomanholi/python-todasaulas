import socket

HOST = "127.0.0.1"
PORT = 10000
servidor = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)

print("Servidor Criado")

servidor.bind( (HOST,PORT ) )
print(f"Servidor conectado com a interface {HOST} na porta {PORT}")

servidor.listen()
print(f"Aguardando cliente se conectar na porta {PORT}")

cliente_conexao, cliente_addr = servidor.accept()
print(f"Cliente no endereço: {cliente_addr} conectou no servidor")

cliente_conexao.sendall("Olá eu sou o servidor feito em Python...".encode("utf-8"))

while True:
    menssagem_bytes = cliente_conexao.recv(1024)
    texto = menssagem_bytes.decode("utf-8")
    # print("Menssagem Recebida", texto)
    print(texto, end="")
    if texto == "X":
        break


cliente_conexao.close()

