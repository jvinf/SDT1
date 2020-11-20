No repositório existem 4 arquivos utilizados nessa primeira tarefa

server.py: esse é o codigo fonte do servidor de aplicação, que tem os metodos requisitados pelo client. Sua função básica é aceitar conexões, as funções detalhadas estão comentadas no arquivo fonte. 

serverDIR.py: Arquivo do servidor de diretórios, onde existe a classe Directory com os métodos de registro e de lookup no servidor de diretorio
 
client.py: O Client se conecta com o servidor de diretório e após é feito o lookup, após receber os dados com ip e porta o client faz a conexão com o servidor de aplicação.

constRPYC.py: Nesse arquivo estão o IP e a porta do servidor de diretório que é estático. Esses dados precisam estar nesse arquivo, pois o servidor de diretório precisa ser achado facilmente, pois é através dele que vão ser encontrados os outros servidores.
