#include <Wire.h>

#define SERIAL_BAUD_RATE 115200
#define I2CBUS_ADDRESS 0x8
#define LOOP_DELAY 100
#define POTENTIOMETER_PIN A0

void I2CRequestHandler() {
  int pot_read = analogRead(POTENTIOMETER_PIN);
  
  Wire.write(highByte(pot_read));
  Wire.write(lowByte(pot_read));

  Serial.println(pot_read);
}

void setup() {
  Serial.begin(SERIAL_BAUD_RATE);
  Wire.begin(I2CBUS_ADDRESS);

  Wire.onRequest(I2CRequestHandler);
}

void loop() {
  delay(LOOP_DELAY);
}