#include <Servo.h>
Servo upDownServo;
Servo leftRightServo;
int posLR = 0;
int posUD = 0;
int upDownServoPin = 11;
int leftRightServoPin = 10;

const int analogInPin = A0;

int sensorValue;
int sensorValue1;
int sensorValue2;
int sensorValue3;

int lowerAngleUD = 50;
int higherAngleUD = 95;
int lowerAngleLR = 50;
int higherAngleLR = 95;

void setup() {
  Serial.begin(9600);
  upDownServo.attach(upDownServoPin);
  leftRightServo.attach(leftRightServoPin);
}

void loop() {
  //sweep over each left-right position in a predetermined range NOTE: the distance range at which the object can be scanned should be noted here
  for (posLR = lowerAngleLR; posLR <= higherAngleLR; posLR += 1) { //test what degrees we really want 
    
    leftRightServo.write(posLR);
    delay(240);
    //Serial.print("POSLR");
    //Serial.print(posLR);

    //for each left-right servo position, do an updown servo scan
    for (posUD = lowerAngleUD; posUD <= higherAngleUD; posUD += 1) {
      upDownServo.write(posUD);
      delay(240);

      //average over three values because there can be variation NOTE: we might want to do something to get rid of serious outliers
      sensorValue1 = analogRead(analogInPin);
      sensorValue2 = analogRead(analogInPin);
      sensorValue3 = analogRead(analogInPin);
      sensorValue = (sensorValue1 + sensorValue2 + sensorValue3)/3;

      //Write to the serial output so that the data can be read in by the python code
      Serial.print(sensorValue);
      Serial.print(';');
      Serial.print(posUD-45); //NOTE: think about the -45 more
      Serial.print(';');
      Serial.print(posLR-45); //NOTE: think about the -45 more
      Serial.print("/");
    }
  }

  Serial.println();
}
