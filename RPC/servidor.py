import rpyc
import time

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
        # código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_get_answer(self): # este é um método exposto
        return 42
    
    exposed_the_real_answer_though = 43 # este é um atributo exposto

    #def exposed_get_question(self): # este método não é exposto
    def get_question(self):
        return "Qual é a cor do cavalo branco de Napoleão?"

#Para iniciar o servidor
#start = time.time()
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
#end = time.time()
#print(end-start)
