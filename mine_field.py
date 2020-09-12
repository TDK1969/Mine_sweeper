import random
import pygame


class MineField:
    def __init__(self, settings, screen):
        """初始化场地"""
        self.settings = settings
        self.row = settings.row
        self.col = settings.column
        self.screen = screen
        self.field = []
        self.set_field()

    def set_field(self):
        """初始化场地，铺设边界和地雷"""
        # 初始化场地，默认为非地雷
        for row in range(self.row):
            self.field.append([])
            for column in range(self.col):
                self.field[row].append("Init")

        # 设定边界
        for row in range(self.row):
            self.field[row][0] = "Board"
            self.field[row][self.col-1] = "Board"
        for column in range(self.col):
            self.field[0][column] = "Board"
            self.field[self.row-1][column] = "Board"

        # 设置地雷
        mine_count = 0
        while mine_count < self.settings.mine_number:
            x = random.randint(1, 7)
            y = random.randint(1, 7)
            if self.field[x][y] != "Mine":
                self.field[x][y] = "Mine"
                mine_count += 1

    def print_block(self, block_content, pos_x, pos_y):
        """在屏幕上打印一个方格"""
        image = pygame.image.load("images/icons/mineInit.png")

        if block_content != "Init" or block_content != "Mine":
            if block_content == "markCorrect" or block_content == "markWrong":
                image = pygame.image.load("images/icons/mark.png")
            else:
                image_path = "images/icons/{}.png".format(block_content)
                image = pygame.image.load(image_path)

        rect = image.get_rect()
        rect.x = pos_x
        rect.y = pos_y

        self.screen.blit(image, rect)





