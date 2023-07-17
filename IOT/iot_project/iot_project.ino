#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <DHT.h>

char auth[] = "tpXxknPdIu5qjoWfPWFqg5fPYArtYhHx";//Enter your Auth token
char ssid[] = "V2037";//Enter your WIFI name
char pass[] = "archana2002";//Enter your WIFI password

DHT dht(D3, DHT11);//(sensor pin,sensor type)
BlynkTimer timer;

//Define component pins
#define rain A0
#define light D0


void setup() {
  Serial.begin(9600);
  pinMode(light, INPUT);

  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);
  dht.begin();
  
    //Call the functions
  timer.setInterval(100L, DHT11sensor);
  timer.setInterval(100L, rainSensor);
  timer.setInterval(100L, LDRsensor);
}

//Get the DHT11 sensor values
void DHT11sensor() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  Serial.print("Temperature...");
  Serial.println(t);
  Serial.print("Humidity...");
  Serial.println(h);
  Blynk.virtualWrite(V0, t);
  Blynk.virtualWrite(V1, h);
  
}

//Get the rain sensor values
void rainSensor() {
  int value = analogRead(rain);
  value = map(value, 0, 1024, 0, 100);
  Blynk.virtualWrite(V2, value);

  Serial.print("Rain sensor value..");
  Serial.println(value);
  delay(500);
}

//Get the LDR sensor values
void LDRsensor() {
  bool value = digitalRead(light);
  if (value == 0) {
    WidgetLED LED(V4);
    LED.on();
  } else {
    WidgetLED LED(V4);
    LED.off();
  }

}

void loop() {
  Blynk.run();
  timer.run();//Run the Blynk timer
}
