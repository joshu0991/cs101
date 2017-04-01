import bluetooth
import time
import RPi.GPIO as io


io.setmode(io.BCM)
pir_pin = 18
io.setup(pir_pin, io.IN)

target_name = "raspberrypi"
target_address="B8:27:EB:7D:B5:8E"
port = 1

nearby_devices = bluetooth.discover_devices()

for dev in nearby_devices:
    print dev
    if target_name == bluetooth.lookup_name(dev):
        target_address = dev
        break
    
if target_address is not None:
    print("Found target device")
else:
    print("Could not find device to pair with trying default address")

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))

counter = 0
while True:
    if (io.input(pir_pin)):
        ++counter
        sock.send("<Mail Received/>")
        print("Mails Here!")

        if counter == 20:
            counter = 0
            sock.close()
            time.sleep(15)
            sock.connect((target_address, port))
            
