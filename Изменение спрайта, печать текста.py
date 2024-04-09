import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, coords, sound, group, sprite=None):
        super().__init__()
        sound.play()
        self.rect = pygame.Rect(*coords, 5, 5)
        group.add(self)
        if sprite:
            self.sprite = pygame.image.load(sprite)
        else:
            self.sprite = sprite

    def draw(self):
        if self.sprite:
            win.blit(self.sprite, (self.rect.x, self.rect.y))
        else:
            pygame.draw.rect(win, (100, 100, 255), self.rect)

    def move(self):
        self.rect = self.rect.move(0, -5)
        if self.rect.y < 0:
            self.kill()

    def update(self):
        self.move()
        self.draw()


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


class Alien(BaseSprite):
    def __init__(self, window, sprites: dict, x, y, group):
        super().__init__(window, sprites["basic"], x, y)

        self.sprites = sprites
        self.hit_cooldown = 0
        group.add(self)

    def change_sprite(self, name):
        self.image = self.sprites[name]

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.change_sprite("basic")
        if keys[pygame.K_2]:
            self.change_sprite("basic2")
        if keys[pygame.K_SPACE]:
            self.hit_cooldown = 100

        if self.hit_cooldown:
            self.hit_cooldown -= 1
            self.change_sprite("hit")


alien_sprites = {}
scale = 1
basic = pygame.image.load("sprite/1.bmp")
size = basic.get_size()
basic = pygame.transform.scale(basic, (size[0] * scale, size[1] * scale))
alien_sprites["basic"] = basic

basic = pygame.image.load("sprite/2.bmp")
size = basic.get_size()
basic = pygame.transform.scale(basic, (size[0] * scale, size[1] * scale))
alien_sprites["basic2"] = basic

hit = pygame.image.load("sprite/1hit.bmp")
size = hit.get_size()
hit = pygame.transform.scale(hit, (size[0] * scale, size[1] * scale))
alien_sprites["hit"] = hit


pygame.init()
win = pygame.display.set_mode((800, 600))

pygame.mixer.music.load("music/Sergey_Eybog_-_Raindrops_(patefon.org).mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

laser_sound = pygame.mixer.Sound("sounds/laserSmall_000.ogg")
laser_group = pygame.sprite.Group()

alien_group = pygame.sprite.Group()
alien = Alien(win, alien_sprites, 50, 50, alien_group)

font1 = pygame.font.Font(None, 32)


def get_text_surf(text, font, color=(255,255,255)):
    return font.render(text, True, color)


def draw_text(text_surf, x, y):
    pygame.draw.rect(win, (0,110,0), (x, y, 200, 50))
    win.blit(text_surf, (x + 5, y + 5))

text = get_text_surf("Какой то текст", font1)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
        if eve.type == pygame.KEYUP:
            if eve.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        if eve.type == pygame.MOUSEBUTTONDOWN:
            # laser_sound.play()
            Laser(eve.pos, laser_sound, laser_group)  # новый выстрел
    # win.blit(background, (0,0))
    win.fill((0, 0, 0))
    laser_group.update()  #  рисуем все лазеры
    alien_group.update()
    draw_text(text, 50, 150)
    pygame.display.update()
pygame.quit()
