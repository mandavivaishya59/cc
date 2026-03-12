from wsgiref.simple_server import make_server
from spyne import rpc,Application ,ServiceBase,Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication 

class Square(ServiceBase):

    @rpc(Integer,_returns=Integer)
    def sq(self,a):
        return a*a
    

app=Application([Square],
                'square.soap',
                in_protocol=Soap11(),
                out_protocol=Soap11()
)

server=make_server('127.0.0.1',10000,WsgiApplication(app))
print("Server is running")
server.serve_forever()