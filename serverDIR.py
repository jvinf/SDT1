class Directory(rpyc.Service):
    registry = {}

    def exposed_register(self, server_name, ip_address, port_number):  #Registra o servidor
        message = 'Registrado'
        registered = True

        if server_name not in self.registry: # Condição que verifica se o nome do servidor não está no registro
            self.registry[server_name] = (ip_address, port_number)
        elif self.registry[server_name][0] == ip_address:
            self.registry[server_name] = (ip_address, port_number)
        else:
            message = 'O servidor já está registrado'
            registered = False
        print (self.registry)
        return (registered, message)

    def exposed_unregister(self, server_name): #Método que faz o unregister do servidor
        if server_name in self.registry:
            del self.registry[server_name]
            return f'Servidor {server_name} foi desregistrado'
        else:
            return f'Nome do servidor não existe'


    def exposed_lookup(self, server_name):
        if server_name in self.registry: #Condição que verifica se o servidor existe
            print (self.registry)
            return self.registry[server_name]
        else:
            print ('O nome do servidor não existe')
