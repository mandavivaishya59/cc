from zeep import Client 

client=Client("http://127.0.0.1:10000/?wsdl")

sq=client.service.sq(10)
print("Square of 5 is", sq)