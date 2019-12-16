from socket import *
from pickle import *
from paquete import *
from constantes import *

def create_UDPsock():
	UDPsocket = socket(AF_INET, SOCK_DGRAM)
	return UDPsocket	
    
def rdt_send():                         # De la capa de aplicacion a la capa de transpórte.
    data=input('Mensaje: ') 
    return(data.encode('utf-8'))        # Transforma a utf-8
    
def make_pkt(data):                     # Se crea el paquete. 
    pkt = Packet(SOURCE_PORT, RECEIVER_PORT, data)
    return pkt  
    
def udp_send(socket, pkt):              # Envia utilisando la funcion "dumps".
    data = dumps(pkt)
    socket.sendto(data, (RECEIVER_IP, RECEIVER_PORT))
    
def close_socket(socket):
    socket.close()
    
if __name__ == "__main__":
    cliente=create_UDPsock()
    print('IP:',RECEIVER_IP, ', Port:',RECEIVER_PORT)
    print()
    
    while 1:  
        data=rdt_send()
        print (data)
       
        paquete=make_pkt(data)
        udp_send(cliente, paquete)

        # evaluar salida
        if not data:
            break

        
    close_socket(cliente)    
    

