import rpyc
import socket
from constRPYC import * #-
from rpyc.utils.server import ForkingServer

class DBList(rpyc.Service):
    value = [ ] #lista

    def exposed_append(self, data): #metodo que anexa um valor na lista
        self.value = self.value + [data]
        print ("Appended value: ", data)
        return self.value

    def exposed_value(self):# metodo que obtém um valor na lista
        return self.value

if __name__ == "__main__":
        server = ForkingServer(DBList, port = 12345) #define o tipo de servidor
        conn = rpyc.connect(DIR_SERVER, DIR_PORT) #conecta com o servidor de diretorio, os parametros vem do arquivo ConstRPYC.py
        my_addr = socket.gethostbyname(socket.gethostname()) #Obtem o endereço IP da maquina que está rodando atraves da biblioteca de sockets
        (registered, message) = conn.root.exposed_register('DBList', my_addr, HOST_PORT)
        print (message)

        if registered:
            server.start()

~                                                 ~                                                 ~                             