#include <Servo.h>
Servo rightArm;
Servo leftLeg;

void setup() {
  rightArm.attach(9);
  leftLeg.attach(10);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    if (cmd == 'P') { // punch
      rightArm.write(0);
      delay(300);
      rightArm.write(90);
    } else if (cmd == 'K') { // kick
      leftLeg.write(0);
      delay(300);
      leftLeg.write(90);
    } else if (cmd == 'F') { // walk forward
      leftLeg.write(45);
      delay(200);
      leftLeg.write(90);
    } else if (cmd == 'B') { // walk backward
      leftLeg.write(135);
      delay(200);
      leftLeg.write(90);
    }
  }
}
