import serial

PORT = "/dev/ttyS0"
BAUDRATE = 4800 # Adjust as needed

ser = serial.Serial(PORT, BAUDRATE)

while 1:
  data = ser.readline() #.decode("utf-8").rstrip()
  print(data)
