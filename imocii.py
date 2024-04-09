import pygame



#чтобы вызывать для примера

#main_char_sprites = {"happy": pygame.Sprite()}
#happy = main_char_sprites["happy"]
#вместо happy может быть basic sad tired anger

if __name__ == "__main__":
    pygame.init()
    width = 800
    height = 600
    win = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("эмоции", 40)

main_char_sprites = {}
scale = 1


name = "Alex"
#радость
happy = pygame.image.load(f"sprites/{name}_happy.png")
size = happy.get_size()
happy = pygame.transform.scale(happy, (size[0] * scale, size[1] * scale))
main_char_sprites["happy"] = happy

#обычное
basic = pygame.image.load(f"sprites/{name}_basic.png")
size1 = basic.get_size()
basic = pygame.transform.scale(basic, (size1[0] * scale, size1[1] * scale))
main_char_sprites["basic"] = basic
'''
#грусть
sad = pygame.image.load("sprite2.png")
size2 = sad.get_size()
sad = pygame.transform.scale(basic, (size2[0] * scale, size2[1] * scale))
main_char_sprites["sad"] = sad


#усталость
tired = pygame.image.load("sprite3.png")
size3 = tired.get_size()
tired = pygame.transform.scale(basic, (size3[0] * scale, size3[1] * scale))
main_char_sprites["tired"] = tired


#злость
anger = pygame.image.load("sprite4.png")
size4 = anger.get_size()
anger = pygame.transform.scale(anger, (size4[0] * scale, size4[1] * scale))
main_char_sprites["anger"] = anger
'''
