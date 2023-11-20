import serial

ser = serial.Serial(
    port='COM4',  # Adjust the port to your micro:bit's serial port
    baudrate=115200
)

def robot_function(action):
    print("Requested action:", action)
    command = str(action)
    out = command + "\n"
    out2 = out.encode('utf_8')
    ser.write(out2)

# Additional setup code for serial communication as needed
