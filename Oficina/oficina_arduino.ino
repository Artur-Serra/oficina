const int buttonPin = 5;
const int ledPin = 8;
bool estadoled = HIGH;

void setup() {
  pinMode(ledPin,OUTPUT);
  pinMode(buttonPin,INPUT);
  Serial.begin(9600);
  // Serial.setTimeout(1);
  digitalWrite(ledPin, estadoled);
  //Serial.println("testando");
}
void loop() { 
    // Serial.println("testando");

  if (Serial.available()>0){
    String teststr = Serial.readString();
    teststr.trim();
    if (teststr=="a"){
      Serial.println(estadoled);
    }

    else if (teststr=="b"){
      Serial.println(digitalRead(buttonPin));
    }

    else if (teststr=="c"){
      estadoled=!estadoled;
      digitalWrite(ledPin, estadoled);
      Serial.println("Inverti o led!");
    }
    
    else{
      int num = teststr.toInt();
      for (int i=0;i<2*num;i++){
        estadoled=!estadoled;
        digitalWrite(ledPin, estadoled);
        delay(200);
      }
       Serial.print("Pisquei o led ");
       Serial.print(num);
       Serial.println(" vezes!");
    }    
  }
  delay(300);   
}
 
