/* ------------- START CONFIG ------------- */
constexpr int BUTTON_PIN = 4;
constexpr int LED_PIN    = 5;
constexpr int RELAY_PIN  = 6;
constexpr int MOIST_PIN  = A0;
int  moisture;
boolean watering;
int rawMoisture = 0;
int waterTime;
/* ------------- END CONFIG ------------- */
//
//#include "thingProperties.h"
#include <Bounce2.h>

Bounce b;
unsigned long startedWatering;

void setup() {
  Serial.begin(9600);
  delay(1500);

  b.attach(BUTTON_PIN,INPUT_PULLUP);
  b.interval(25);
  pinMode(LED_PIN, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

  // Make sure the pump is not running
//  stopWatering();

  // Connect to Arduino IoT Cloud
//  initProperties();
//  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
//  setDebugMessageLevel(4);
//  ArduinoCloud.printDebugInfo();

  // Blink LED to confirm we're up and running
  for (int i = 0; i<=4; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
    delay(200);
  }

}

void loop() {
//  ArduinoCloud.update();
  
  // Read the sensor and convert its value to a percentage 
  // (0% = dry; 100% = wet)
  rawMoisture = analogRead(MOIST_PIN);
  moisture = map(rawMoisture, 853, 575, 0, 100); 
//  Serial.println(moisture);

buttonCheck();
serialCheck();
waterCheck();

}

void serialCheck(){
  if (Serial.available() > 0){
    int recieved = Serial.read();
    if (recieved == 97){
        digitalWrite(6, HIGH);
        delay(1900);
        digitalWrite(6, LOW);
    }
    // Serial.println(recieved);

  }

}




void buttonCheck(){
    b.update();
  if (b.changed() && b.read() == false) { // button pressed
   watering = true;
   digitalWrite(RELAY_PIN, HIGH);
   digitalWrite(LED_PIN, HIGH);
  }else{
    watering = false;
    digitalWrite(RELAY_PIN, LOW);
    digitalWrite(LED_PIN, LOW);
  }
}

void waterCheck() {
  // Set the behavior according to the moisture percentage or watering status
  if (watering) {
  digitalWrite(RELAY_PIN, HIGH);
  delay(10000);
  } else if (moisture > 40) {
  Serial.println("no water needed.");
  delay(100);
  } else if (moisture > 10) {
  Serial.println("Water needed immediately!"); 
   delay(100);
   
  } else {
  Serial.println("No water detected!");
  delay(100);
  }
  
  
}




// This function is triggered whenever the server sends a change event,
// which means that someone changed a value remotely and we need to do
// something. 
//void onWateringChange() {
//  if (watering) {
//    startWatering();
//  } else {
//    stopWatering();
//  }
//}


//void startWatering () {
//  watering = true;
//  startedWatering = millis();
//  digitalWrite(RELAY_PIN, HIGH);
//}
//
//void stopWatering () {
//  watering = false;
//  digitalWrite(RELAY_PIN, LOW);
//}
//
//void onWaterTimeChange()  {
  // Add your code here to act upon WaterTime change
//}