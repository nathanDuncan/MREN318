/*==========================================================================
// Author : Tony Yang, Nathan Duncan, Daniel Poon
// Project : HC-SR04 Ultrasonic Sensor with Arduino Uno for MREN 318
// Description : HC-SR04 Distance Measure with Arduino and display
// on Serial Monitor.
// LiquidCrystal Library - Special Chars
// Source-Code : HC-SR04.ino
// Adapted from : Handson Technology
//==========================================================================
*/
int trig=9;
int echo=8;
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
 delay(6000);
 Serial.println("Distance:");
}
void loop()
{
 digitalWrite(trig, HIGH);
 delayMicroseconds(10); 
digitalWrite(trig, LOW);
 duration = pulseIn(echo, HIGH);
 if(duration>=38000){
 Serial.print("Out range");
 }
 else{
 distance = duration/58;
 Serial.print(distance);
 Serial.print("cm");
 meter=distance/100;
 Serial.print("\t");
 Serial.print(meter);
 Serial.println("m");
 }
 delay(1000);
}
