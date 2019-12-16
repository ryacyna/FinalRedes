# https://wiki.python.org/moin/HowTo/Sockets
# http://elrincondebackbone.blogspot.com/2014/11/introduccion-sockets-en-python.html
# https://unipython.com/programacion-de-redes-en-python-sockets/


from socket import *
from pickle import *
from paquete import *
from constantes import *

def create_UDPsocket(IP, PORT):
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	UDPsocket.bind((IP, PORT))
	return UDPsocket
    
def deliver_data(data): # Selecciona los datos, eliminando el encabezado de red, y lo muestra por pantalla.
    print(data)

def extract(pocket):    #. 
    data=pocket.get_data() 
    return data
    
def rdt_rcv (socket):   #. 
    data=socket.recv(2048)

    return data
    
def close_socket(socket):
    socket.close()

def udt_rcv(socket):
    dato=socket.recv(2048)
    paquete=loads(dato)
    return paquete

    
if __name__ == "__main__":
    servidor=create_UDPsocket(RECEIVER_IP, RECEIVER_PORT)
    print('IP:',RECEIVER_IP, ', Port:',RECEIVER_PORT)
    print()
    
    while 1:
        paquete=udt_rcv(servidor)

        #evaluar salida.
        if not paquete:
            break

        checksum = calculate_checksum(paquete)
        paquete.set_checksum(checksum)
        new_checksum = calculate_checksum(paquete)
        print('Checksum: ', new_checksum)
       
        
        data=extract(paquete)
        deliver_data(data)
        
    close_socket(servidor)
