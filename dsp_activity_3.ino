/**
 * Created by Francisc Jerhone Camillo
 * Created by Shella May Cantos
 * Bachelor of Science in Computer Engineering 4-3
 * Digital Signal Processing
 * DSP Activity #3
 * Submitted to Professor Ligayu
 */

// Arduino Libraries Used
#include<NewPing.h>
#include<LiquidCrystal.h>
#include<Servo.h>


//Ultrasonic Variable Declaration
#define trigPin 13
#define echoPin 12
#define buzzer 11

//LCD Variable Declaration
LiquidCrystal lcd(7,6,2,3,4,5);
String message;

//Servo Motor Declarations
int ypos;
int xpos = 0;
String actualYAngle;
String actualXAngle;
Servo yPositionServo;
Servo xPositionServo;

//Serial Declarations
String response;
int serialDelay = 1000;

/*
 * The setup function for arduino components
 */
void setup() {
                                

  //setup Serial
  Serial.begin (115200);

  //setup Servo
  yPositionServo.attach(8);                         //YPosition Servo attached to digital pin 8 of arduino
  xPositionServo.attach(9);                         //XPosition Servo attached to digital pin 9 of arduino
  zerooutservos();

  //setup Ultrasonic
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzer, OUTPUT);

  //setup LCD
  lcd.begin(16,2);
  lcd.clear();
  lcd.setCursor(0, 0);
}

/*
 *  The arduino loop function contains the main loop program
 */
 
void loop(){
  zerooutservos();
  ypositionmove();
}

/*
 * -----------------Functions-------------------
 * Table of Contents for functions
 * 1. scan();                 -->
 * 2. beep();                 -->
 * 3. ypositionmove();        -->
 * 4. xpositionmove();        -->
 * 5. zerooutservos();        -->
 * 6. writeSerialMessages();  -->
 * ---------------------------------------------
 */

void scan() {
  long duration, distance;
  digitalWrite(trigPin, LOW);     
  delayMicroseconds(2);           
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);          
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;
  

  if (distance < 70) {                    
    message = "Distance";                                  //Instantiate the "Distance: "  to the variable message
    message.concat(distance);                                   //Concat the distance gathered to variable message
    Serial.println(message);
    delay(serialDelay);
    lcd.clear();
    lcd.print(message);
    beep(50);                                                   // Length of tone
    delay(50);                                                  //Set delay for preparation of next scan
  }
  else if (distance >= 70 && distance < 120) {
    message ="Distance: ";
    message.concat(distance);                                   // Yellow alert: Obstacle Approaching
    Serial.println(message);                                    // Send to Android for text to speech
    delay(serialDelay);
    lcd.clear();
    lcd.print(message);
    beep(50);
    delay(50);                                                  // Interval of beep. This longer interval means that the object a bit far.
  }
  else if (distance >= 75 || distance == 0){    
    message = "Distance: ";
    message.concat(distance);
    Serial.println(message);        // Send to Android for text to speech
    delay(serialDelay);
    lcd.clear();
    lcd.print(message);
    beep(50);
    delay(50);  
  }
}

void beep(unsigned char delayms){
    analogWrite(buzzer, 20);        // Almost any value can be used except 0 and 255                                    // experiment to get the best tone
    delay(delayms);                 // wait for a delayms ms
    analogWrite(buzzer, 0);         // 0 turns it off
    delay(delayms);                 // wait for a delayms ms   
}

void ypositionmove(){
  for (ypos = 0; ypos<=180; ypos+=1){
      //sets the position of the servo
      yPositionServo.write(ypos);

      //
      message = "YAngle: ";
      message.concat(ypos);
      actualYAngle = "Actual Angles is: ";
      actualYAngle.concat(yPositionServo.read());
      Serial.println(message);
      delay(serialDelay);
      //initiate the scan function
      scan();
      Serial.println(actualYAngle);
      delay(100);
    }
    if (ypos == 181){
      xpositionmove();
    }
}
void xpositionmove(){
  xpos++;
  xPositionServo.write(xpos);
  message = "XAngle: "; 
  message.concat(xpos);
  Serial.println(message);
  delay(serialDelay);
  Serial.println(actualXAngle);
  delay(500);
}

void zerooutservos(){
  yPositionServo.write(0);
  xPositionServo.write(0);  
}

