import pygame
from random import randrange

class BaseSprite(pygame.sprite.Sprite):
    IMAGES = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        for image in self.IMAGES:
            self.sprites.append(pygame.image.load(image))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(35 * 3, 35* 3))
        self.rect = self.image.get_rect()
        self.rect.topleft = randrange(200),randrange(280)

    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image,(35 * 3, 35* 3))


class FireWizard(BaseSprite):
    IMAGES = [
        "assets/wizard_fire/1_IDLE_000.png",
        "assets/wizard_fire/1_IDLE_001.png",
        "assets/wizard_fire/1_IDLE_002.png",
        "assets/wizard_fire/1_IDLE_003.png",
        "assets/wizard_fire/1_IDLE_004.png",
    ]


class Wizard(BaseSprite):
    IMAGES = [
        "assets/wizard/1_IDLE_000.png",
        "assets/wizard/1_IDLE_001.png",
        "assets/wizard/1_IDLE_002.png",
        "assets/wizard/1_IDLE_003.png",
        "assets/wizard/1_IDLE_004.png",
    ]


class IceWizard(BaseSprite):
    IMAGES = [
        "assets/wizard_ice/1_IDLE_000.png",
        "assets/wizard_ice/1_IDLE_001.png",
        "assets/wizard_ice/1_IDLE_002.png",
        "assets/wizard_ice/1_IDLE_003.png",
        "assets/wizard_ice/1_IDLE_004.png",
    ]


class IceGolem(BaseSprite):
    IMAGES = [
        "assets/golem_ice/0_Golem_Idle_000.png",
        "assets/golem_ice/0_Golem_Idle_001.png",
        "assets/golem_ice/0_Golem_Idle_002.png",
        "assets/golem_ice/0_Golem_Idle_003.png",
        "assets/golem_ice/0_Golem_Idle_004.png",
        "assets/golem_ice/0_Golem_Idle_005.png",
        "assets/golem_ice/0_Golem_Idle_006.png",
        "assets/golem_ice/0_Golem_Idle_007.png",
        "assets/golem_ice/0_Golem_Idle_008.png",
        "assets/golem_ice/0_Golem_Idle_009.png",
        "assets/golem_ice/0_Golem_Idle_010.png",
        "assets/golem_ice/0_Golem_Idle_011.png",
        "assets/golem_ice/0_Golem_Idle_012.png",
        "assets/golem_ice/0_Golem_Idle_013.png",
        "assets/golem_ice/0_Golem_Idle_014.png",
        "assets/golem_ice/0_Golem_Idle_015.png",
    ]


class FireGolem(BaseSprite):
    IMAGES = [
        "assets/golem_fire/0_Golem_Idle_000.png",
        "assets/golem_fire/0_Golem_Idle_001.png",
        "assets/golem_fire/0_Golem_Idle_002.png",
        "assets/golem_fire/0_Golem_Idle_003.png",
        "assets/golem_fire/0_Golem_Idle_004.png",
        "assets/golem_fire/0_Golem_Idle_005.png",
        "assets/golem_fire/0_Golem_Idle_006.png",
        "assets/golem_fire/0_Golem_Idle_007.png",
        "assets/golem_fire/0_Golem_Idle_008.png",
        "assets/golem_fire/0_Golem_Idle_009.png",
        "assets/golem_fire/0_Golem_Idle_010.png",
        "assets/golem_fire/0_Golem_Idle_011.png",
        "assets/golem_fire/0_Golem_Idle_012.png",
        "assets/golem_fire/0_Golem_Idle_013.png",
        "assets/golem_fire/0_Golem_Idle_014.png",
        "assets/golem_fire/0_Golem_Idle_015.png",
    ]


class Golem(BaseSprite):
    IMAGES = [
        "assets/golem/0_Golem_Idle_000.png",
        "assets/golem/0_Golem_Idle_001.png",
        "assets/golem/0_Golem_Idle_002.png",
        "assets/golem/0_Golem_Idle_003.png",
        "assets/golem/0_Golem_Idle_004.png",
        "assets/golem/0_Golem_Idle_005.png",
        "assets/golem/0_Golem_Idle_006.png",
        "assets/golem/0_Golem_Idle_007.png",
        "assets/golem/0_Golem_Idle_008.png",
        "assets/golem/0_Golem_Idle_009.png",
        "assets/golem/0_Golem_Idle_010.png",
        "assets/golem/0_Golem_Idle_011.png",
        "assets/golem/0_Golem_Idle_012.png",
        "assets/golem/0_Golem_Idle_013.png",
        "assets/golem/0_Golem_Idle_014.png",
        "assets/golem/0_Golem_Idle_015.png",
    ]
