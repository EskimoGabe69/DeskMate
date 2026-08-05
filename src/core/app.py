from utils.file_importer import file_importer
from components.appmanager import AppManager
from utils.yaml_dumper import yaml_dumper
from utils.sprite import SpriteSheet
from components.mate import Mate
from core import constants
import pygame


pygame.init()
sprite_sheet_path = file_importer(constants.ASSET_DIR, "sprite_sheet.png")
icon_path = file_importer(constants.ASSET_DIR, "deskmate_logo.svg")
walk_animation = yaml_dumper()


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
