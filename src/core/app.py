from components.mate import Mate
from components.systemtraymanager import systemtraymanager
from core import constants
import os
import pygame

from utils.sprite import SpriteSheet

pygame.init()
game_directory = os.path.dirname(__file__)
parent_directory = os.path.abspath(os.path.join(game_directory, ".."))
asset_directory = os.path.join(parent_directory, "assets")


def app(icon_path, css_path):
    sprite_sheet = SpriteSheet(os.path.join(asset_directory, "sprite_sheet.png"))
    mate_image = sprite_sheet.get_sprite(1, 1, 50, 50)
    mate = Mate(mate_image)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(mate)
    constants.SCREEN.fill(constants.TRANSPARENT)
    all_sprites.draw(constants.SCREEN)
    systemtraymanager(all_sprites, icon_path, css_path)
