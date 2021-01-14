empty_object = bytes(16)
 print (type(empty_object))
 print (empty_object)


--------------
buf = b''
while message_not_complete(buf):
    buf += read_from_socket()
