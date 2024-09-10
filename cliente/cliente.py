import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect(('localhost', 12345))

# Enviando uma mensagem para o servidor
continuar = True

while(continuar):
    message = input("Diga algo ao servidor: ")
    client_socket.sendall(message.encode())
    
    # Recebendo a resposta do servidor
    data = client_socket.recv(1024)
    print(f"Resposta do servidor: {data.decode()}")

    #Checando se deseja continuar a conexão
    while(True):
        confirmacao = input("Deseja enviar mais mensagens? [S/N]")

        if confirmacao.lower() == "s":
            break
        elif confirmacao.lower() != "s" and confirmacao.lower() != "n":
            print("Insira uma resposta válida.")
        else:
            continuar = False
            break

client_socket.close()

