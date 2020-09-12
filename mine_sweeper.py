import pygame
from mine_field import MineField
from settings import Settings


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Mine Sweeper")
    # 创建场地
    mine_field = MineField(settings, screen)





run_game()