import RPi.GPIO as GPIO                 # Importa a biblioteca RPi.GPIO
from time import sleep                  # Da biblioteca time, importa a função sleep

LED_GPIO = 21                           # Define o pino GPIO do LED como sendo o 21

GPIO.setmode(GPIO.BCM)                  # Define o modo da placa como BCM (permitindo uso da notação GPIO)
GPIO.setup(LED_GPIO, GPIO.OUT)          # Configura o pino LED_GPIO como saída
GPIO.output(LED_GPIO, False)            # Coloca nível lógico baixo no pino LED_GPIO, desligando o LED

pwm = GPIO.PWM(LED_GPIO, 200)           # Associa o pino LED_GPIO com uma instância pwm de frequência 200 Hz
led_duty_cycle = 0                      # Define o duty cycle do LED como sendo 0, inicialmente

pwm.start(led_duty_cycle)               # Inicia o PWM da instânca pwm com o duty cycle contido em led_duty_cycle

while True:                             # Loop Infinito
    pwm.ChangeDutyCycle(led_duty_cycle) # Altera o valor do duty cycle da instância pwm para o valor contido em led_duty_cycle
    sleep(0.1)                          # Aguarda 100ms
    led_duty_cycle += 1                 # Incrementa a variável led_duty_cycle
    
    if led_duty_cycle == 100:           # Verifica se o valor contido em led_duty_cycle é 100
        led_duty_cycle = 0              # Caso seja, zera o valor de led_duty_cycle