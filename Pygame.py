# -*- coding: UTF-8 -*- 
# 创建者：LeK
# 创建日期：2022/7/24

import sys
import pygame

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口
screen = pygame.display.set_mode(size)  # 显示窗口，返回一个Surface对象
color = (0, 0, 0)  # 设置颜色

ball = pygame.image.load(r'ball.png')  # 加载图片，返回一个Surface对象
ballrect = ball.get_rect()  # 获取矩形区域，返回一个Rect对象

speed = [5, 5]  # 设置移动的X轴、Y轴距离
clock = pygame.time.Clock()

while True:
    clock.tick(60)  # 每秒执行60次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 获取点击pygame窗口退出事件
            sys.exit()

    ballrect = ballrect.move(speed)  # 移动小球
    # 碰撞检测
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]  # x轴上碰到边界，将运动方向转为相反方向
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]  # y轴上碰到边界，将运动方向转为相反方向

    screen.fill(color)  # 填充颜色
    screen.blit(ball, ballrect)  # 将图片划到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame
