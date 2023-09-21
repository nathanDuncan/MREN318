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
int ir_signal=A0;
int LED=7;
float distance;
float ir_value;
void setup()
{
 Serial.begin(9600);
 delayMicroseconds(2);
 pinMode(LED, OUTPUT);
 delay(2000);
 Serial.println("Distance:");
}
void loop()
{
 ir_value = analogRead(ir_signal)* 5.0/1023.0;
 distance = distance/2.54;
 if (ir_value > 2.6){
  Serial.println("<=9 inches");
  digitalWrite(LED,LOW);
  delay(200);
 }
 else if (ir_value > 1.6){
  Serial.println("9-19 inches");
  digitalWrite(LED,HIGH);
  delay(200);
 }
 else if (ir_value < 1.6){
  Serial.println(">19 inches");
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
