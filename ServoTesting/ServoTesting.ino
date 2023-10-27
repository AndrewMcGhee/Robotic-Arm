#include <Servo.h>

Servo servo;

void setup() {
  Serial.begin(9600);
  servo.attach(9);  // Attach servo to digital pin 9
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();
    
    // Ensure that the angle is within the valid range (0 to 180)
    if (angle >= 0 && angle <= 180) {
      servo.write(angle);
      Serial.print("Servo angle set to: ");
      Serial.println(angle);
    }
  }
}
