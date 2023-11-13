#include <Wire.h>

#define I2CBUS_ADDRESS 0x8
#define LED_PIN LED_BUILTIN
#define LOOP_DELAY 100

void I2CHandler(int howMany) {
  while (Wire.available()) {
    char ledState = Wire.read();
    digitalWrite(LED_PIN, ledState);
  }
}

void setup() {
  Wire.begin(I2CBUS_ADDRESS);

  Wire.onReceive(I2CHandler);

  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  delay(LOOP_DELAY);
}