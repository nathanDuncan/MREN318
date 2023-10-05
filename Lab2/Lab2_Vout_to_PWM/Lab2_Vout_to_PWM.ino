/*==========================================================================
// Author : Tony Yang, Nathan Duncan, Dainel Poon
// Project : Lab2 vout to PWM for MREN 318
// Description : Collect and store data at 10 Hz
// Source-Code : Lab2_DataCollection.ino
// Date: 10/5/2023
//==========================================================================
*/
const int voutPin = A0;                          // Pin A0 will read Vout
const int waveformPin = 3;                       // Pin 3 will output the waveform

int WF_frequency = 5;                            // waveform frequency [Hz]
int WF_period = 1000/WF_frequency;               // waveform period [ms]
float dutyCycle = 80.0;                            // duty cycle value 0-100

void read_and_log();

void setup()
{
 Serial.begin(9600);
 delay(2);
 pinMode(voutPin, INPUT);
 pinMode(waveformPin, OUTPUT);

 delay(2000);
}
////////////////// Loop ///////////////////////////////
void loop()
{
  //Declarations may be moved to setup if constant
  dutyCycle = analogRead(voutPin)/1023.0;                // duty cycle value 0-100
  int DC_duration = (WF_period*dutyCycle);             // High duration [ms]

  //Generate Waveform
  digitalWrite(waveformPin, HIGH);
  Serial.print("Variable_1:");
  Serial.print(dutyCycle);
  Serial.print(",");
  Serial.print("Variable_2:");
  Serial.println(5);
  delay(DC_duration);
  digitalWrite(waveformPin, LOW);
  Serial.print("Variable_1:");
  Serial.print(dutyCycle);
  Serial.print(",");
  Serial.print("Variable_2:");
  Serial.println(0);
  delay(WF_period-DC_duration);
}

//////////////// Read and Log ////////////////////////
void read_and_log(){
  Serial.println(analogRead(voutPin));
}
