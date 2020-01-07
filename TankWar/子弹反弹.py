import pygame
import sys
from pygame.locals import *

# 初始化pygame
pygame.init()

size = width, height = 600, 400
speed = [-2, 1]

# 背景设置，全白
bg = (255, 255, 255)

# 创建指定大小的窗口 Surface对象
screen = pygame.display.set_mode(size)
# 设置窗口标题
pygame.display.set_caption("子弹反弹")

# 加载图片
gamemaster = pygame.image.load("炮弹.png")
# 获得图像的位置矩形
position = gamemaster.get_rect()

l_head = gamemaster
r_head = pygame.transform.flip(gamemaster, True, False)

# 事件，终止事件
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                gamemaster = l_head
                speed = [-2, 1]

            if event.key == K_RIGHT:
                gamemaster = r_head
                speed = [2, -1]

            if event.key == K_UP:
                speed = [1, -2]

            if event.key == K_DOWN:
                speed = [-1, 2]


        elif event.type == KEYUP:
            # speed =[-2,1]
            pass

    # 移动图像
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # 图像翻转 gamemaster,True,False 左右翻转 上下不翻转
        gamemaster = pygame.transform.flip(gamemaster, True, False)
        # 反方向移动
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        # 反方向移动
        speed[1] = -speed[1]

    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(gamemaster, position)
    # 更新界面
    pygame.display.flip()
    # 延时10ms
    pygame.time.delay(10)
