import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 12321                
s.bind((host, port))       

s.listen(5)                 
while True:
   c, addr = s.accept()     
   print ('Got connection from', addr)
  c.send('Thank you for connecting'))
   c.close()                # Close the connection
