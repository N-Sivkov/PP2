import pygame
import os
import time


def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect


pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
baza, min, sec = pygame.image.load("baza.png"), pygame.image.load("min.png"), pygame.image.load("sec.png")
clock = pygame.time.Clock()

while not done:
    screen.blit(baza, (0, 0))
    MinAngle = time.localtime().tm_min * -6
    SecAngle = time.localtime().tm_sec * -6
    RMin, PosMin = rot_center(min, MinAngle, 250, 250)
    RSec, PosSec = rot_center(sec, SecAngle, 250, 250)
    screen.blit(RMin, PosMin)
    screen.blit(RSec, PosSec)
    pygame.display.update()
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True