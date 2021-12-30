#include <OneWire.h> 
#include <DallasTemperature.h>
#include <ArduinoJson.h>

#define ONE_WIRE_BUS 5
#define resProbe A0 
OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);
int period = 2000;
unsigned long time_now = 0;
int pushButton = 3;
long pulse = 0;
bool st = false;
 DynamicJsonDocument doc(1024);
 String data ="{\"Temp\":0.0,\"BPM\":0.0,\"Resistance\":0}";
 JsonObject obj;
void setup(void) 
{ 
 Serial.begin(9600); 
 pinMode(resProbe,INPUT);
 sensors.begin();
 deserializeJson(doc, data);
 obj = doc.as<JsonObject>();
  
} 
void loop(void) 
{ 
 int skinR = 1023-analogRead(resProbe);
 sensors.requestTemperatures();
 obj[String("Temp")] = sensors.getTempCByIndex(0);
 obj[String("BPM")] = pulse;
 obj[String("Resistance")] =skinR; 
 String output;
 serializeJson(doc, output);
 Serial.println(output);
 time_now = millis();
 pulse = 0;
 while(millis() < time_now + period){
 if(digitalRead(pushButton)==0){
 pulse +=1;
 delay(15);
 while(digitalRead(pushButton)==0);
  }
  }
   int time = 60/(period/1000);
//   Serial.print("BPM : ");
//   Serial.print(pulse);
//   Serial.println(" / ");
   // if(pulse > 10)pulse = 0;
   //pulse = pulse*(time);
  }
 
