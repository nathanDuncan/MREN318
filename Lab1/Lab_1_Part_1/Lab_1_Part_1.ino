/*==========================================================================
// Author : Tony Yang, Nathan Duncan, Dainel Poon
// Project : HC-SR04 Ultrasonic Sensor with Arduino Uno for MREN 318
// Description : HC-SR04 Distance Measure with Arduino and display
// on Serial Monitor.
// LiquidCrystal Library - Special Chars
// Source-Code : HC-SR04.ino
// Adapted from : Handson Technology
//==========================================================================
*/
int trig=3;
int echo=2;
int LED=7;
int duration;
float distance;
float meter;
void setup()
{
 Serial.begin(9600);
 pinMode(trig, OUTPUT);
 digitalWrite(trig, LOW);
 delayMicroseconds(2);
 pinMode(echo, INPUT);
 pinMode(LED, OUTPUT);
 delay(6000);
 Serial.println("Distance:");
}
void loop()
{
 digitalWrite(trig, HIGH);
 delayMicroseconds(10); 
 digitalWrite(trig, LOW);
 duration = pulseIn(echo, HIGH);
 distance = duration / 148.0;
 if (distance <= 9){
  Serial.print(distance);
  Serial.println(" inches");
  digitalWrite(LED,LOW);
  delay(200);
 }
 else if (distance < 19){
  Serial.print(distance);
  Serial.println(" inches");
  digitalWrite(LED,HIGH);
  delay(200);
 }
 else{
  Serial.print(distance);
  Serial.println(" inches");
  digitalWrite(LED, HIGH);
  delay(50);
  digitalWrite(LED, LOW);
  delay(50);
  digitalWrite(LED, HIGH);
  delay(50);
  digitalWrite(LED, LOW);
  delay(50);
 }

 delay(1000);
}
