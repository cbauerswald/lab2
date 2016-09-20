#include <Servo.h>
Servo upDownServo;
Servo leftRightServo;
int pos = 0;
int upDownServoPin = 11;
int leftRightServoPin = 12;

const int analogInPin = A0;
int sensorVals[180];
int sensorValue;
int calibratedValue;
int distance;

void setup() {
  Serial.begin(9600);
  upDownServo.attach(upDownServoPin);
  leftRightServo.attach(leftRightServoPin);
}

void loop() {
  for (lrPos = 0; lrPos <=90; lrPos += 1) {
    leftRightServo.write(pos)
    for (udPpos = 0; udPos <= 90; udPos += 1) { //test what 90 degrees we really want 
      upDownServo.write(pos);
      delay(15);
      sensorValue = analogRead(analogInPin);
      calibratedValue = map(sensorValue, 0, 1023, 0, 255);
      sensorVals[pos] = calibratedValue;
    }
  
    for (udPos = 90; udPos >= 0; udPos -= 1) { //test what 90 degrees we really want 
      upDownServo.write(pos);
      delay(15);
      sensorValue = analogRead(analogInPin);
      calibratedValue = map(sensorValue, 0, 1023, 0, 255);
      sensorVals[pos] = calibratedValue;
    }
  }
//  Serial.print(sensorVals);
}
