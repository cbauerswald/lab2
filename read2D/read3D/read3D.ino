#include <Servo.h>
Servo upDownServo;
int pos = 0;
int servoPin = 11;

const int analogInPin = A0;
int sensorVals[180];
int sensorValue;
int calibratedValue;
int distance;

void setup() {
  Serial.begin(9600);
  upDownServo.attach(servoPin);
}

void loop() {
  for (pos = 0; pos <= 90; pos += 1) { //test what 90 degrees we really want 
    upDownServo.write(pos);
    delay(15);
    sensorValue = analogRead(analogInPin);
    calibratedValue = map(sensorValue, 0, 1023, 0, 255);
    sensorVals[pos] = calibratedValue;
  }

  for (pos = 90; pos >= 0; pos -= 1) { //test what 90 degrees we really want 
    upDownServo.write(pos);
    delay(15);
    sensorValue = analogRead(analogInPin);
    calibratedValue = map(sensorValue, 0, 1023, 0, 255);
    sensorVals[pos] = calibratedValue;
  }
//  Serial.print(sensorVals);
}
