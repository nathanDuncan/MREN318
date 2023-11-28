#include <AccelStepper.h>

AccelStepper stepper(1, 2, 5); // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
const int ultrasonic_voltage = A0;
const int fsr_voltage = A1;

// Global variables 
unsigned long fsr_prev_time = 0;
unsigned long ultrasonic_prev_time = 0;

const unsigned long fsr_period = 10000;
const unsigned long ultrasonic_period = 5000;

boolean is_food_dropped = false;
 
void setup()
{  
    Serial.begin(9600);

    startMillis = millis();

    // Initialize stepper motor
    stepper.setMaxSpeed(200.0);
    stepper.setAcceleration(100.0);
    stepper.runToNewPosition(0); // sets the starting position of the motor as 0, locks motor as well
}
 
void loop()
{        
    unsigned long current_time = millis();

    if (Serial.available())
    {
        TurnMotor(Serial.readString().toInt());
        fsr_prev_time = current_time;
    }

    if ((current_time - fsr_prev_time >= fsr_period) && is_food_dropped == true)
    {
        GetWeight();
        is_food_dropped = false;
    }
    
    if (current_time - ultrasonic_prev_time >= ultrasonic_period) 
    {
        Serial.println(GetFoodAmount());
        ultrasonic_prev_time = current_time;
    }
}


// Turns the motor to a new position, 200 is a full rotation
void TurnMotor(int new_position)
{
    stepper.runToNewPosition(new_position);
    is_food_dropped = true;
}

float GetWeight()
{
    return analog
}

String GetFoodAmount()
{
    int ultrasonic_value = analogRead(ultrasonic_voltage)* 5.0/1023.0; //take input and scale to be a range 0-5 volts
    float distance = 27.165*pow(ultrasonic_value, -1.336);          //Convert to distance using calibration curve

    if (distance <= )
    {
        return "uEmpty";
    }
    else if (distance > && distance < )
    {
        return "uHalf";
    }
    else 
    {
        return "uFull"
    }
}
