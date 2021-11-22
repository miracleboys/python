"""
作者：lrmy
日期：2021年10月28日
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen

        #在（0，0）处创建一个表示子弹的矩形,再设置正确的位置
        se

