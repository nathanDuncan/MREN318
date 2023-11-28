const int voutPin = A1;                       // Pin A0 will read Vout

void read_and_log();

void setup()
{
 Serial.begin(9600);
 delay(2);
 pinMode(voutPin, INPUT);

 delay(2000);
 Serial.println("Vout [mV]");
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
