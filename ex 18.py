#Como fazer um programa abrir uma música em mp3



import pygame

pygame.init()
pygame.mixer.music.load('xuxa.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()