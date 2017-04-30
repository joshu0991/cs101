import bluetooth

port = 1
server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

print("Listening")
server_sock.bind(("", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()

print ("Accepted connection from", address)

while True:
    data = client_sock.recv(10)
    print (data)
    data = client_sock.recv(500000 * 2)
    fh = open("tmp.png", "w")
    fh.write(data)
    fh.close()
    #print "Received [%s]" % data
    
    print("Closing connection")
    client_sock.close()
    server_sock.close()
    print ("complete")
    server_sock.listen(1)
