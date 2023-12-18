import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

print("Aproxime a TAG do leitor para realizar a leitura!")

while True:
    id, texto = reader.read()
    print("ID: {}\nTexto: {}".format(id, texto))
    sleep(3)