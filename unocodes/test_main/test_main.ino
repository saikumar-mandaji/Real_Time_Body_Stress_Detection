#define USE_ARDUINO_INTERRUPTS true
#include <OneWire.h> 
#include <DallasTemperature.h>
#include <ArduinoJson.h>
#include <PulseSensorPlayground.h>

#define ONE_WIRE_BUS 5
#define resProbe A0 
const int PulseWire = A1; 
int Threshold = 720;
int period = 1000;
unsigned long time_now = 0;
long pulse = 0;


OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);
PulseSensorPlayground pulseSensor;
DynamicJsonDocument doc(1024);
 String data ="{\"BPM\":0.0,\"Temp\":0.0,\"SR\":0}";
 JsonObject obj;
  String output ="";
void setup(void) 
{ 
 Serial.begin(9600); 
 pinMode(resProbe,INPUT);
 sensors.begin();
 deserializeJson(doc, data);
 obj = doc.as<JsonObject>();
 pulseSensor.analogInput(PulseWire);
 pulseSensor.setThreshold(Threshold);
  if (pulseSensor.begin()) {
    ;
      }
  } 
void loop(void) 
{ 
 int skinR = 1023-analogRead(resProbe);
 skinR = map(skinR,0,1024,0,500);
 float myBPM = pulseSensor.getBeatsPerMinute();
 myBPM = myBPM/2.85;
 if(myBPM < 56)myBPM = 0;
 if(myBPM > 160)myBPM = 160;
 if (pulseSensor.sawStartOfBeat())pulse = myBPM;
 sensors.requestTemperatures();
 obj[String("Temp")] = sensors.getTempCByIndex(0);
 obj[String("BPM")] = pulse;
 obj[String("SR")] =skinR; 
 output ="";
 serializeJson(doc, output);
 if(millis() >= time_now + period){
        time_now += period;
        Serial.println(output);
    }
 pulse = 0;
 delay(20);
 }
 
