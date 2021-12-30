int period = 2000;
unsigned long time_now = 0;
int pushButton = 3;
long pulse = 0;
bool st = false;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
Serial.print("BPM : ");
Serial.print(pulse);
Serial.println("/ 1 Min");
  time_now = millis();
  pulse = 0;
      while(millis() < time_now + period){
//        if(digitalRead(pushButton)==0){
//          st = true;
//        }
//        else{
//          if(st){
//          pulse +=1;
//        }
//        st = false;
//        }
if(digitalRead(pushButton)==0){
  pulse +=1;
  delay(2);
  while(digitalRead(pushButton)==0);
  
}
    }
   
   int time = 60/(period/1000);
   Serial.print("BPM : ");
   Serial.print(pulse);
   Serial.println("/ 3 Sec");
   if(pulse > 10)pulse = 0;
   pulse = pulse*(time);
}
