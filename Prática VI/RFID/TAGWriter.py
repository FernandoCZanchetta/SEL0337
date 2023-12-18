import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

data = "12547962"

print("Aproxime a TAG do leitor para realizar a gravação!")

reader.write(data)
print("Texto gravado com sucesso!")