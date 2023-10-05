/*==========================================================================
// Author : Tony Yang, Nathan Duncan, Dainel Poon
// Project : Lab2 Prelab for MREN 318
// Description : 5 Hz rectangular waveform with an adjustable duty cycle
// Source-Code : squareWave.ino
// Date: 10/5/2023
//==========================================================================
*/

const int waveformPin = 7;                       // Pin 7 will output the waveform

void setup()
{
 Serial.begin(9600);
 delayMicroseconds(2);
 pinMode(waveformPin, OUTPUT);
  
 delay(2000);
 Serial.println("This Program outputs a square wave");
}
////////////////// Loop ///////////////////////////////
void loop()
{
  //Declarations may be moved to setup if constant
  int WF_frequency = 5;                          // waveform frequency [Hz]
  int WF_period = 1000/WF_frequency;             // waveform period [ms]
  int dutyCycle = 60;                            // duty cycle value 0-100
  int DC_duration = (WF_period*dutycycle)/100;   // High duration [ms]

  //Generate Waveform
  digitalWrite(waveformPin, HIGH);
  delayMicroseconds(DC_duration);
  digitalWrite(waveformPin, Low);
  delayMicroseconds(WF_period-DC_duration);
}
