import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer_music.load('ratsasan.mp3')
pygame.mixer_music.play()
sleep(5)

pygame.mixer_music.load('scary.mp3')
pygame.mixer_music.play()
sleep(1)

image = pygame.image.load('1.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(3)