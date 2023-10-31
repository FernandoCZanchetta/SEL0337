from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sounds = {
    Button(18): Sound("samples/drum_heavy_kick.wav"),
    Button(15): Sound("samples/drum_cymbal_pedal.wav"),
    Button(14): Sound("samples/drum_snare_hard.wav"),
    Button(20): Sound("samples/drum_splash_hard.wav"),
    Button(21): Sound("samples/drum_tom_mid_hard.wav"),
}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play
    
pause()