import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class Directory(rpyc.Service): # classe de implementação do servidor
    registry = {}

    def exposed_register(self, server_name, ip_address, port_number):#metodo para o servidor de aplicação fazer o registro, recebe o nome do servidor, ip e porta
        self.registry[server_name] = (ip_address, port_number) #registra no dicionario o ip e a porta associadas ao nome do servidor que está como indice
        print(self.registry) #imprime o servidor reagindo
        return "Registro OK" #retorna a confirmação de registro pro cliente que é o servidor de aplicação

    def exposed_lookup(self, server_name): #metodo paraos clientes  fazerem o lookup, recebe o nome do servidor do cliente
        print (self.registry) #imprime o servidor reagindo
        return self.registry[server_name] #retorna os dados referente ao servidor requisit^Z

if __name__ == "__main__": #cria uma thread dentro do processo capaz de rodar os metodos da classe Directory
    server = ThreadedServer(Directory, port = DIR_PORT)
    server.start()