import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT) #Conecta com o servidor de diretorio
    (addr, port) = conn_directory.root.exposed_lookup("DBList") #faz o lookup no servidor de diretorio
    print (addr, port) #após receber o endereço e porta ele imprime apenas para o conhecimento    conn = rpyc.connect(addr, port) #Usa o endereço IP e porta recebidos para se conectar ao servidor de aplicação
    conn.root.exposed_append(2)        #Chama a operação append
    conn.root.exposed_append(4)        #Chama a operação append
    print (conn.root.exposed_value())    #Imprime o resultado