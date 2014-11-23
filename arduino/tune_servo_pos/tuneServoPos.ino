
#include <Servo.h>

Servo rArm;

int pos = 90; //stores servo position; set at neutral = 90 deg

void setup(){
    Serial.begin(9600);
    rArm.attach(9);

}

void loop() {
    if (Serial.available() > 0){
        int inByte = Serial.read();

        switch(inByte){
        case 'i':
            pos +=1;
            break;
        case 'l':
            pos -=1;
            break;
        default:
            pos = 90;
            

        }
    }
}