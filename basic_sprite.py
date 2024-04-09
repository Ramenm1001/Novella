import pygame
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, window, sprite, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.window = window

    def update(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))


if __name__ == "__main__":


    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600

    pygame.init()

    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Проект на Акселератор")

    # main_char_sprites = {}
    # scale = 1  # размер спрайта
    # happy = pygame.image.load("sprite.png")
    # size = happy.get_size()
    # happy = pygame.transform.scale(happy, (size[0] * scale, size[1] * scale))
    #
    # main_char_sprites["happy"] = happy  # добавление спрайта

    # main_char_sprites = {"happy": pygame.Sprite()}  условный вид словаря спрайтов
    # happy = main_char_sprites["happy"] получение спрайта

    scale = 0.5  # размер спрайта
    main_char_sprites = {}
    car = pygame.image.load("car.png")
    size = car.get_size()
    car = pygame.transform.scale(car, (size[0] * scale, size[1] * scale))

    main_char_sprites["car"] = car  # добавление спрайта

    # main_char_sprites = {"happy": pygame.Sprite()}  условный вид словаря спрайтов
    # happy = main_char_sprites["happy"] получение спрайта


    clock = pygame.time.Clock()
    run = True

    decorations = pygame.sprite.Group()

    car_obj1 = BaseSprite(win, main_char_sprites["car"], 50, 50)
    car_obj2 = BaseSprite(win, main_char_sprites["car"], 150, 150)
    car_obj3 = BaseSprite(win, main_char_sprites["car"], 350, 350)

    car_obj1.add(decorations)
    car_obj2.add(decorations)
    car_obj3.add(decorations)

    while run:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                run = False
            elif eve.type == pygame.KEYUP:
                pass

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass


        #win.blit(background, (0, 0))
        win.fill((0,0,0))
        decorations.update()
        pygame.display.update()
        clock.tick_busy_loop(60)

    pygame.quit()
