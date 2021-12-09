import socket
import psutil
import pickle

endereco = socket.gethostname()
porta = 9999
bufferSize = 1024

msg_servidor = 'Conectado'
bytesToSend = str.encode(msg_servidor)

info_disco = psutil.virtual_memory()
envio_bytes = pickle.dumps(info_disco)

# Create a datagram socket
servidor_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to endereco and ip
servidor_socket.bind((endereco, porta))

print('Aguardando conexão')

while True:
    endereco_par = servidor_socket.recvfrom(bufferSize)
    mensagem = endereco_par[0].decode('ascii')
    endereco = endereco_par[1]

    msg_cliente = f'Cliente:{mensagem}'
    ip_cliente = f'Endereço cliente:{endereco}'

    print(msg_cliente)
    print(ip_cliente)

    # Sending a reply to client
    servidor_socket.sendto(envio_bytes, endereco)
