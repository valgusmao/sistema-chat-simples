import socket
import re

def checarPalavra(palavra):
    return re.compile(r'\b({0})\b'.format(palavra), flags=re.IGNORECASE).search

# Criando um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando o socket ao endereço e porta
server_socket.bind(('localhost', 12345))

# Escutando por conexões
server_socket.listen(5)
print("Servidor escutando na porta...")

# Aceitando conexões de clientes
while (True):
    conn, addr = server_socket.accept()
    print(f"Conectado por {addr}")

    while (True):
        # Recebendo mensagem do cliente
        data = conn.recv(1024)

        # Encerra conexão se não tiver mais mensagens
        if not data:
            break

        # Respondendo ao cliente de forma personalizada
        mensagem_cliente = data.decode()
        print(f"Mensagem recebida: {data.decode()}")

        if checarPalavra('olá')(mensagem_cliente) or checarPalavra('oi')(mensagem_cliente):
            conn.sendall(b"Ola para voce!")

        elif checarPalavra('tudo bem')(mensagem_cliente):
            conn.sendall(b"Tudo bem por aqui!")
        
        elif checarPalavra('clima')(mensagem_cliente):
            conn.sendall(b"Tem feito muito calor ultimamente. Cuidado com o sol!")

        else:
            conn.sendall(b"Pois e'.")
        
    conn.close()