import serial
import time

arduino_port = 'COM3'  # Change this to your Arduino's port
baud_rate = 9600
arduino = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for Arduino to initialize (adjust the delay as needed)

def send_command(command):
    arduino.write(command.encode('utf-8'))

def move_servo(servo_id, angle):
    command = f"MOVE {servo_id} {angle}\n"
    send_command(command)
    response = arduino.readline().decode('utf-8').strip()
    print("Response from Arduino:", response)

if __name__ == "__main":
    try:
        while True:
            user_input = input("Enter command (e.g., 'MOVE 1 90' to move servo 1 to 90 degrees, or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break  # Exit the loop if 'exit' is entered

            try:
                servo_id, angle = map(int, user_input.split()[1:])
                if 1 <= servo_id <= 2:  # Assuming valid servo IDs
                    move_servo(servo_id, angle)
                else:
                    print("Invalid servo ID. Please enter 1 or 2.")
            except (ValueError, IndexError):
                print("Invalid input format. Please use 'MOVE servo_id angle' format.")

    except KeyboardInterrupt:
        arduino.close()
