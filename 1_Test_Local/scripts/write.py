import serial
import time

PORT = "/dev/ttyS0"
BAUDRATE = 9600

ser = serial.Serial(PORT, BAUDRATE)

def writeSerial(counter):
  msg = "Counter: {}\n".format(counter)
  ser.write(bytes(msg, "utf-8"))
  print(msg, end="")

counter = 0
while 1:
  writeSerial(counter)
  time.sleep(1)
  counter += 1
