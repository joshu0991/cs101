import bluetooth

port = 1
server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

server_sock.bind(("", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()

print ("Accepted connection from", address)

while True:
    data = client_sock.recv(1024)
    print "Received [%s]" % data

    if data == "Terminate":
        print("Closing connection")
        client_sock.close()
        server_sock.close()
