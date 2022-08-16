#include <DHT.h>
#define Type DHT11
int DHTPin = 2;
DHT HT(DHTPin, Type);
float humidity;
float tempC;
float tempF;
int redPin = 10;


int LDRPin = A0;
float lightVal;
int yellowPin = 12;

int mPin = A2;
float mValue;
int bluePin = 11;

int delayTime = 500;
int setTime = 500;

void setup() {
  Serial.begin(9600);
  
  pinMode(LDRPin, INPUT);
  pinMode(mPin, INPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  HT.begin();
  delay(setTime);
  

}

void lightControl(int Llimit) {
  lightVal = analogRead(LDRPin);
  lightVal = (lightVal)*100.0/1023.0;
  if (lightVal < Llimit) {
    digitalWrite(yellowPin, HIGH);
  } else {
    digitalWrite(yellowPin, LOW);
  }
  delay(delayTime);
}

void airControl(int Hlimit,int Tlimit) {
  humidity = HT.readHumidity();
  tempC = HT.readTemperature();
  tempF = HT.readTemperature(true);

  if (tempC > Tlimit) {
    digitalWrite(redPin, HIGH);
  } else {
    digitalWrite(redPin, LOW);
  }
  delay(delayTime);
}

void waterControl(int Wlimit) {
  mValue = analogRead(mPin); //1011 - 250 -> 0 - 100
  mValue = 120 - 0.116*mValue; //formula depends on location (chennai)
  if (mValue < 50) {
    digitalWrite(bluePin, HIGH);
  } else {
    digitalWrite(bluePin, LOW);
  }
  delay(delayTime);
}

void loop() {
  lightControl(20);
  airControl(40,30);
  waterControl(50);

  Serial.print(lightVal);
  Serial.print(" ");
  Serial.print(humidity);
  Serial.print(" ");
  Serial.print(tempC);
  Serial.print(" ");  
  Serial.print(tempF);
  Serial.print(" ");  
  Serial.print(mValue);
  Serial.println(" ");
}
