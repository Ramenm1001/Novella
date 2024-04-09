from basic_sprite import BaseSprite
from text_draw import get_text_surf, draw_text
from imocii import main_char_sprites

import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 1000

pygame.init()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Проект на Акселератор")

run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
        elif eve.type == pygame.KEYUP:
            pass

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pass

    # win.blit(background, (0, 0))   # если есть фон
    win.fill((0, 0, 0))
    #decorations.update()
    win.blit(main_char_sprites["happy"], (150, 150)) # персонаж
    pygame.display.update()

pygame.quit()
