import socket
import pickle
from psutil._common import bytes2human

msg_cliente = 'Conectado'
envio_bytes = msg_cliente.encode('ascii')

endreco_e_porta = (socket.gethostname(), 9999)
bufferSize = 1024
cliente_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
cliente_socket.settimeout(5)
cliente_socket.sendto(envio_bytes, endreco_e_porta)
verificador = False

while not verificador:
    try:
        msg_servidor = cliente_socket.recvfrom(bufferSize)
        _msg = pickle.loads(msg_servidor[0])
        verificador = True
        for n in _msg._fields:
            value = getattr(_msg, n)
            if n == 'total' or n == 'available':
                value = bytes2human(value)
                print(n.capitalize(), value)
    except socket.timeout:
        print('Tempo excedido!')

cliente_socket.close()
