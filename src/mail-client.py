import bluetooth
import time
import RPi.GPIO as io
from camera import take_picture


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

while True:
    if (io.input(pir_pin)):
        take_picture()
        fp = open("/home/pi/cs101/src/recent.png", "r")
        string = fp.read()
        sock.send(str(len(string)))
        sock.send(string)
        print("Mails Here!")
        time.sleep(15)
