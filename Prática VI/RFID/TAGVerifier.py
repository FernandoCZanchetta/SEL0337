import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

RED_LED_GPIO = 20
GREEN_LED_GPIO = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED_GPIO, GPIO.OUT)
GPIO.setup(RED_LED_GPIO, GPIO.OUT)
GPIO.output(GREEN_LED_GPIO, GPIO.LOW)
GPIO.output(RED_LED_GPIO, GPIO.LOW)

ID_DB = {219505142786,
         16625018518}

reader = SimpleMFRC522()

print("Aproxime a TAG do leitor para realizar a leitura!")

while True:
    GPIO.output(GREEN_LED_GPIO, GPIO.LOW)
    GPIO.output(RED_LED_GPIO, GPIO.LOW)
    id, texto = reader.read()
    if id in ID_DB:
        GPIO.output(GREEN_LED_GPIO, GPIO.HIGH)
        print("Acesso liberado!")
    else:
        GPIO.output(RED_LED_GPIO, GPIO.HIGH)
        print("Acesso negado!")
    sleep(1)
