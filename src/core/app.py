from components.appmanager import AppManager
from components.mate import Mate
from core import constants
import os
import pygame

from utils.sprite import SpriteSheet


pygame.init()
asset_directory = os.path.join(os.path.dirname(__file__), "..", "assets")
# NOTE: In the rewrite those two under there are gonna go through a util function
sprite_sheet_path = os.path.join(asset_directory, "sprite_sheet.png")
icon_path = os.path.join(asset_directory, "deskmate_logo.svg")

# TODO: Implement YAML logic and something with the area picker
walk_animation = [(1, 1, 50, 50), (63, 1, 50, 50), (130, 1, 50, 50), (194, 3, 50, 50)]
# something


def app():
    """
    App which bundles everything like the sprites, mate and AppManager together in on place
    """
    sprite_sheet = SpriteSheet(sprite_sheet_path)
    mate = Mate(sprite_sheet, walk_animation)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(mate)
    constants.SCREEN.fill(constants.TRANSPARENT)
    all_sprites.draw(constants.SCREEN)
    app_manager = AppManager(all_sprites, icon_path)
    app_manager.run()
