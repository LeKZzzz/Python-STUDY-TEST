# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/7/25

import sys
import pygame
import random


class Bird(object):
    def __init__(self):
        self.birdrect = pygame.Rect(124, 50, 48, 48)  # 创建鸟的矩形
        self.birdstatus = [pygame.image.load(r'flappybird\bird0_0.png'),
                           pygame.image.load(r'flappybird\bird0_1.png'),
                           pygame.image.load(r'flappybird\bird0_2.png'),
                           pygame.image.load(r'flappybird/medals_0.png')]  # 鸟不同状态读取的图片
        self.status = 1  # 鸟的状态，默认为0
        self.birdY = 236  # 鸟的Y坐标
        self.jump = False  # 鸟是否跳跃，默认为降落
        self.jumpspeed = 10  # 初始化鸟跳跃的高度
        self.gravity = 5  # 初始化重力
        self.dead = False  # 鸟的生命状态，默认为活着

    def birdupdate(self):  # 鸟的位置
        if self.jump and self.jumpspeed >= 0:
            self.jumpspeed -= 1  # 设置鸟向上的速度，速度为递减的等差数列
            self.birdY -= self.jumpspeed  # 设置鸟的Y轴坐标，总移动距离为等差数列和
        else:
            self.gravity += 0.2  # 设置鸟向下的速度，速度为递增的等差数列
            self.birdY += self.gravity  # 设置鸟的Y轴坐标，总移动距离为等差数列和
            self.jump = False

        self.birdrect[1] = self.birdY  # 设置鸟的矩形Y轴坐标


class Pipeline(object):
    def __init__(self):
        self.wallx = 300  # 设置管道起始位置
        self.basis = random.randint(-320, 0)
        self.upwally = self.basis
        self.distance = random.randint(150, 192)
        self.downwally = self.upwally + 320 + self.distance
        self.pineup = pygame.image.load(r'flappybird\pipe_down.png')
        self.pinedown = pygame.image.load(r'flappybird\pipe_up.png')
        self.uprect = pygame.Rect(self.wallx, self.upwally,
                                  self.pineup.get_width() - 10,
                                  self.pinedown.get_height())  # 设置上管道矩形
        self.downrect = pygame.Rect(self.wallx, self.downwally,
                                    self.pinedown.get_width() - 10,
                                    self.pinedown.get_height())  # 设置下管道矩形

    def updatePipeline(self):
        global score
        self.wallx -= 5  # 将管道X坐标向左移动
        self.upwally = self.basis
        self.downwally = self.upwally + 320 + self.distance
        self.uprect = pygame.Rect(self.wallx, self.upwally,
                                  self.pineup.get_width() - 10,
                                  self.pinedown.get_height())
        self.downrect = pygame.Rect(self.wallx, self.downwally,
                                    self.pinedown.get_width() - 10,
                                    self.pinedown.get_height())
        if self.wallx < -80:
            self.wallx = 300  # 重置管道X坐标
            self.basis = random.randint(-320, 0)
            self.distance = random.randint(150, 192)
        if self.wallx == -80:
            score += 1  # 设置得分点


def CreateMap(color, background):  # 绘制整体图像
    screen.fill(color)  # 屏幕填充颜色
    screen.blit(background, (0, 0))  # 屏幕填充背景图片

    if Bird.dead:  # 鸟死亡的状态
        Bird.status = 3
    elif Bird.jump:  # 鸟跳跃的状态
        Bird.status = 2
    else:
        Bird.status = 0  # 鸟降落的状态
    screen.blit(Bird.birdstatus[Bird.status], (124, Bird.birdY))  # 在鸟的位置放置鸟的图像
    Bird.birdupdate()  # 更新下一次屏幕刷新时鸟的位置

    screen.blit(Pipeline.pineup, (Pipeline.wallx, Pipeline.upwally))  # 在管道的位置放置管道的图像
    screen.blit(Pipeline.pinedown, (Pipeline.wallx, Pipeline.downwally))
    Pipeline.updatePipeline()  # 更新下一次刷新屏幕时管道的位置

    pygame.display.update()  # 更新显示


def checkdead():
    # 判断鸟与管道的碰撞
    if Pipeline.uprect.colliderect(Bird.birdrect) or Pipeline.downrect.colliderect(Bird.birdrect):
        Bird.dead = True
    # 判断鸟与屏幕的碰撞
    if 0 < Bird.birdrect[1] < height:  # 判断鸟的矩形是否在屏幕内
        return False
    else:
        Bird.dead = True
        return True


def getresult():
    final_text1 = 'GAME OVER'
    final_text2 = 'YOUR FINAL SCORE IS:  ' + str(score)
    ft1_font = pygame.font.SysFont('Arial', 30)  # 设置字体
    ft1_surf = ft1_font.render(final_text1, 1, (242, 3, 36))  # 设置颜色
    ft2_font = pygame.font.SysFont('Arial', 20)
    ft2_surf = ft2_font.render(final_text2, 1, (253, 177, 6))

    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])

    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()

    size = width, height = 288, 512
    screen = pygame.display.set_mode(size)  # 设置屏幕尺寸
    clock = pygame.time.Clock()
    Bird = Bird()
    Pipeline = Pipeline()
    score = 0

    color = (255, 255, 255)
    background = pygame.image.load(r'flappybird\bg_day.png')

    while True:
        clock.tick(60)  # 设置每秒循环的次数
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                # 设置鸟的状态为跳跃，重置向上跳跃的高度和重力的初值
                Bird.jump = True
                Bird.gravity = 5  # 重置重力
                Bird.jumpspeed = 10  # 重置跳跃高度
        if checkdead():  # 满足与屏幕边缘或管道碰撞且鸟的矩形与屏幕边缘碰撞
            getresult()  # 显示得分界面且在该画面一直停留
        else:
            CreateMap(color, background)  # display画面，传入背景颜色和背景图片

    pygame.quit()
