import pygame
import sys
from factory import GolemFactory, WizardFactory

pygame.init()


x = 640
y = 480

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Wizard - Game")

bg = pygame.image.load("assets/bg/bg_1.png").convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

wizard_fire = WizardFactory().create_fire_sprite()
golem_ice = GolemFactory().create_ice_sprite()
wizard_ice = WizardFactory().create_ice_sprite()
golem_fire  = GolemFactory().create_fire_sprite()

sprint_group = pygame.sprite.Group()

sprint_group.add(wizard_ice, wizard_fire, golem_fire, golem_ice)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg, (0, 0))
    sprint_group.draw(screen)
    sprint_group.update()
    pygame.display.flip()