/*==========================================================================
// Author : Tony Yang, Nathan Duncan, Dainel Poon
// Project : Lab2 402 FSR collection for MREN 318
// Description : Collect and store data at 10 Hz
// Source-Code : Lab2_DataCollection.ino
// Date: 10/5/2023
//==========================================================================
*/
const int voutPin = A0;                       // Pin A0 will read Vout

void read_and_log();

void setup()
{
 Serial.begin(9600);
 delay(2);
 pinMode(voutPin, INPUT);

 delay(2000);
 Serial.println("This logs output voltage at 10 Hz");
}
////////////////// Loop ///////////////////////////////
void loop()
{
  delay(100);      // Wait for a 10 Hz period (100ms)
  read_and_log();              // Read and log data every period
}

//////////////// Read and Log ////////////////////////
void read_and_log(){
  Serial.println(analogRead(voutPin));
}
