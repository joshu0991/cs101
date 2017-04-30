import bluetooth
from Gmail2 import send_mail
from restapi import restful_request
from restapi import init

port = 1
server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

print("Listening")
server_sock.bind(("", port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
init()
print ("Accepted connection from", address)
while True:
    data = client_sock.recv(10)
    print (data)
    fh = open("tmp.png", "w")
    counter = 0
    while 'done' not in data:
        counter = counter + 1024
        print ("Getting data " + str(counter))
        data = client_sock.recv(1024)
        fh.write(data)
    fh.close()
    print("print sending")
    send_mail()
    print ("print restful request")
    restful_request()

    print ("complete")
