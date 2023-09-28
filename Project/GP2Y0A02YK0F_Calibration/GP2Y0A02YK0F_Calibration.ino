/*==========================================================================
// Author : Tony Yang, Nathan Duncan, Dainel Poon
// Project : GP2Y0A02YK0F SHARP Sensor calibration for MREN 318
// Description : GP2Y0A02YK0F Distance Measure with Arduino and display
// on Serial Monitor.
// Source-Code : GP2Y0A02YK0F_Calibration.ino
// Adapted from : Lab_1_Part_2.ino
//==========================================================================
*/
int ir_signal=A0;
int LED=7;
float distance;
float ir_value;
void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   delayMicroseconds(2);
   pinMode(LED, OUTPUT);
   delay(2000);
}

void loop() {
  // put your main code here, to run repeatedly:
  ir_value = analogRead(ir_signal)* 5.0/1023.0; //take input and scale to be a range 0-5 volts
  Serial.println(ir_value);
}
