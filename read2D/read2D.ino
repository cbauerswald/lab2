#include <Servo.h>
Servo upDownServo;
int pos = 0;
int servoPin = 11;

const int analogInPin = A0;
int sensorVals[180];
int sensorValue;
int sensorValue1;
int sensorValue2;
int sensorValue3;
int calibratedValue;
int distance;
int lowerAngle = 50;
int higherAngle = 95;

void setup() {
  Serial.begin(9600);
  upDownServo.attach(servoPin);
}

void loop() {
  // Serial.write("test\n");
  
  for (pos = lowerAngle; pos <= higherAngle; pos += 1) { //test what 90 degrees we really want 
    upDownServo.write(pos);
    delay(240);
    sensorValue1 = analogRead(analogInPin);
    sensorValue2 = analogRead(analogInPin);
    sensorValue3 = analogRead(analogInPin);
    sensorValue = (sensorValue1 + sensorValue2 + sensorValue3)/3;
    //calibratedValue = map(sensorValue, 0, 1023, 0, 255);
    //sensorVals[pos] = calibratedValue;
    //Serial.print("sensorValue");
    Serial.print(sensorValue);
    Serial.print(';');
    //Serial.print("pos");
    Serial.print(pos-45);
    Serial.print("/");
  }
//
//  for (pos = higherAngle; pos >= lowerAngle; pos -= 1) { //test what 90 degrees we really want 
//    upDownServo.write(pos);
//    delay(240);
//    sensorValue1 = analogRead(analogInPin);
//    sensorValue2 = analogRead(analogInPin);
//    sensorValue3 = analogRead(analogInPin);
//    sensorValue = (sensorValue1 + sensorValue2 + sensorValue3)/3;
//    //calibratedValue = map(sensorValue, 0, 1023, 0, 255);
//    //sensorVals[pos] = calibratedValue;
//    //Serial.print("sensorValue");
//    Serial.print(sensorValue);
//    Serial.print(';');
//    //Serial.print("pos");
//    Serial.print(pos-45);
//    Serial.print("/");
//  }
  Serial.println();
  // Serial.print(sensorVals[0]);
}
