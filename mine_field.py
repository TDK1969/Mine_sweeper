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
        # 图像默认为init图像
        image = pygame.image.load("images/icons/mineInit.png")

        if block_content != "Init" or block_content != "Mine":
            # 标志方块
            if block_content == "markCorrect" or block_content == "markWrong":
                image = pygame.image.load("images/icons/mark.png")
            elif block_content == "markUnknown" or block_content == "markUnknown_Mine":
                image = pygame.image.load("images/icons/markUnknown.png")
            else:
                # 数字方块
                image_path = "images/icons/{}.png".format(block_content)
                image = pygame.image.load(image_path)

        # 设置图像打印的位置
        rect = image.get_rect()
        rect.x = pos_x
        rect.y = pos_y

        # 打印图像
        self.screen.blit(image, rect)

    def count_mine(self, x, y):
        """统计数字方格周围的地雷数"""
        nearby = [-1, 0, 1]
        mine_count = 0
        for nearby_x in nearby:
            for nearby_y in nearby:
                if self.field[x + nearby_x][y + nearby_y] == "Mine" or \
                   self.field[x + nearby_x][y + nearby_y] == "markCorrect" or \
                   self.field[x + nearby_x][y + nearby_y] == "markUnknown_Mine":
                    mine_count += 1

        # 返回地雷数
        return mine_count

    def click(self, x, y):
        """点击格子，如果是数字则打开，如果是地雷则爆炸，游戏结束"""
        if self.field[x][y] == "Init":
            mine_count = self.count_mine(x, y)
            self.field[x][y] = str(mine_count)

            if mine_count == 0:
                self.sweep_zero(x, y)
        elif self.field[x][y] == "Mine":
            self.field[x][y] = "mineBoom"
            self.game_lose()

    def sweep_zero(self, x, y):
        """点开0的时候扫出一片范围"""
        stack = []
        top = -1
        visited = []

        stack.append((x, y))
        visited.append((x, y))
        top += 1

        while stack:
            temp_x, temp_y = stack.pop()
            top -= 1


            mine_count = -1

            if self.field[temp_x][temp_y] == "Init":
                mine_count = self.count_mine(x, y)
                self.field[x][y] = str(mine_count)

            if mine_count == 0:
                nextx = [0, 1, 0, -1]
                nexty = [-1, 0, 1, 0]

                for i in range(4):
                    stack.append((temp_x + nextx[i], temp_y + nexty[i]))
                    top += 1





    def mark(self, x, y):
        """标雷一个格子，当已被标记时标记改为问号，再标记则改为正常"""
        pass

    def game_win(self):
        """游戏胜利，打印全图并祝贺"""
        pass

    def game_lose(self):
        """游戏失败，打印全图并标记处错误的地方"""
        pass

    def print_field_win(self):
        """打印胜利时的全图"""
        pass



