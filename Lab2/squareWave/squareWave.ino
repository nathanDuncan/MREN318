/*==========================================================================
// Author : Tony Yang, Nathan Duncan, Dainel Poon
// Project : Lab2 Prelab for MREN 318
// Description : 5 Hz rectangular waveform with an adjustable duty cycle
// Source-Code : squareWave.ino
// Date: 10/5/2023
//==========================================================================
*/

const int waveformPin = 3;                       // Pin 3 will output the waveform

int WF_frequency = 5;                            // waveform frequency [Hz]
int WF_period = 1000/WF_frequency;               // waveform period [ms]

void setup()
{
 Serial.begin(9600);
 delay(1);
 pinMode(waveformPin, OUTPUT);

 delay(2000);
 Serial.println("This Program outputs a square wave");
}
////////////////// Loop ///////////////////////////////
void loop()
{
  //Declarations may be moved to setup if constant
  int dutyCycle = 80;                            // duty cycle value 0-100
  int DC_duration = (WF_period*dutyCycle)/100;   // High duration [ms]

  //Generate Waveform
  digitalWrite(waveformPin, HIGH);
  delay(DC_duration);
  digitalWrite(waveformPin, LOW);
  delay(WF_period-DC_duration);
}
