import serial

# Initialize the serial connection (change the port as needed)
ser = serial.Serial('COM51', 9600)  # Change 'COM3' to the correct serial port

while True:
    try:
        angle = input("Enter an angle (0 to 180): ")
        angle = int(angle)

        # Ensure that the input is within the valid range
        if 0 <= angle <= 180:
            ser.write(str(angle).encode())
        else:
            print("Invalid angle. Please enter a value between 0 and 180.")
    
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 180.")
