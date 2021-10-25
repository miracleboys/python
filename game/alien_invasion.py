"""
作者：lrmy
日期：2021年10月20日
"""
import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #每次循环重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #屏幕可见
        pygame.display.flip()

run_game()