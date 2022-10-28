from abc import ABC, abstractmethod
from wizard import BaseSprite, Wizard, FireWizard, IceWizard, Golem, IceGolem, FireGolem


class AbstractSpriteFactory(ABC):
    @abstractmethod
    def create_sprite(self) -> BaseSprite:
        pass

    @abstractmethod
    def create_fire_sprite(self) -> BaseSprite:
        pass

    @abstractmethod
    def create_ice_sprite(self) -> BaseSprite:
        pass


class WizardFactory(AbstractSpriteFactory):

    def create_sprite(self) -> BaseSprite:
        return Wizard()

    def create_fire_sprite(self) -> BaseSprite:
        return FireWizard()

    def create_ice_sprite(self) -> BaseSprite:
        return IceWizard()


class GolemFactory(AbstractSpriteFactory):

    def create_sprite(self) -> BaseSprite:
        return Golem()

    def create_fire_sprite(self) -> BaseSprite:
        return FireGolem()

    def create_ice_sprite(self) -> BaseSprite:
        return IceGolem()