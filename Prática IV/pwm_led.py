import RPi.GPIO as GPIO
from time import sleep

LED_GPIO = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT)
GPIO.output(LED_GPIO, False)

pwm = GPIO.PWM(LED_GPIO, 200)
led_duty_cycle = 0

pwm.start(led_duty_cycle)

while True:
    pwm.ChangeDutyCycle(led_duty_cycle)
    sleep(0.1)
    led_duty_cycle += 1
    
    if led_duty_cycle == 100:
        led_duty_cycle = 0