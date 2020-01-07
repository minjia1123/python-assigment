import pygame
import sys
import random
# from plane_sprites import *
# import time
from math import *

pygame.init()

golds = 0
# global golds

SIZE = WIDTH, HEIGHT = 1600, 900
BLACK = 0, 0, 0
angle = 1
judge = 0

screen = pygame.display.set_mode(SIZE)
leaf = pygame.image.load("arrow.png")
background = pygame.image.load("back.png").convert()

turtle = pygame.image.load('gold 1.png')

turtle1 = pygame.image.load('gold 2.png')
turtle2 = pygame.image.load('gold 3.png')
turtle3 = pygame.image.load('gold 4.png')
turtle4 = pygame.image.load('gold 5.png')
turtle5 = pygame.image.load('gold 6.png')
turtle6 = pygame.image.load('gold 7.png')
turtle7 = pygame.image.load('gold 8.png')
turtle8 = pygame.image.load('gold 9.png')
turtle9 = pygame.image.load('gold 10.png')
turtle10 = pygame.image.load('gold 11.png')
turtle11 = pygame.image.load('gold 12.png')
turtle12 = pygame.image.load('gold 13.png')
turtle13 = pygame.image.load('gold 14.png')
turtle14 = pygame.image.load('gold 15.png')

leafRect = leaf.get_rect()
leafRect = leafRect.move((WIDTH - leafRect.width) / 2, 50 - leafRect.height)

x0, y0 = leafRect.x, leafRect.y
x1, y1 = leafRect.x, leafRect.y

turtleRect = turtle.get_rect()
turtleRect = turtleRect.move(350, 550)
t0, u0 = turtleRect.x, turtleRect.y

height = leaf.get_height()
width = leaf.get_width()

velocity = 800  # 速度
time = 1 / 120  # 每个时间片的长度
clock = pygame.time.Clock()

tip = 0
j1 = True
j2 = True
j3 = True
j4 = True
j5 = True
j6 = True
j7 = True
j8 = True
j9 = True
j10 = True
j11 = True
j12 = True
j13 = True
j14 = True
j15 = True

g = 0

def enemy():
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    global n8
    global n9
    global n10
    global n11
    global n12
    global n13
    global n14
    global n15
    global g

    global Lx
    global Ly
    global tip

    g = 1
    n1 = turtle1.get_rect()
    n2 = turtle2.get_rect()
    n3 = turtle3.get_rect()
    n4 = turtle4.get_rect()
    n5 = turtle5.get_rect()
    n6 = turtle6.get_rect()
    n7 = turtle7.get_rect()
    n8 = turtle8.get_rect()
    n9 = turtle9.get_rect()
    n10 = turtle10.get_rect()
    n11 = turtle11.get_rect()
    n12 = turtle12.get_rect()
    n13 = turtle13.get_rect()
    n14 = turtle14.get_rect()

    Lx = []
    Ly = []
    i1 = 0
    i2 = 0
    while i1 < 14 or i2 < 14:
        g4 = random.randint(0, 1400)
        g5 = random.randint(200, 800)

        if g4 not in Lx and i1 != 14:
            Lx.append(g4)
            i1 += 1
        if g5 not in Ly and i2 != 14:
            Ly.append(g5)
            i2 += 1

    print(Lx, Ly)

    n1 = n1.move(Lx[0], Ly[0])
    n2 = n2.move(Lx[1], Ly[1])
    n3 = n3.move(Lx[2], Ly[2])
    n4 = n4.move(Lx[3], Ly[3])
    n5 = n5.move(Lx[4], Ly[4])
    n6 = n6.move(Lx[5], Ly[5])
    n7 = n7.move(Lx[6], Ly[6])
    n8 = n8.move(Lx[7], Ly[7])
    n9 = n9.move(Lx[8], Ly[8])
    n10 = n10.move(Lx[9], Ly[9])
    n11 = n11.move(Lx[10], Ly[10])
    n12 = n12.move(Lx[11], Ly[11])
    n13 = n13.move(Lx[12], Ly[12])
    n14 = n14.move(Lx[13], Ly[13])

    screen.blit(turtle1, n1)
    screen.blit(turtle2, n2)
    screen.blit(turtle3, n3)
    screen.blit(turtle4, n4)
    screen.blit(turtle5, n5)
    screen.blit(turtle6, n6)
    screen.blit(turtle7, n7)
    screen.blit(turtle8, n8)
    screen.blit(turtle9, n9)
    screen.blit(turtle10, n10)
    screen.blit(turtle11, n11)
    screen.blit(turtle12, n12)
    screen.blit(turtle13, n13)
    screen.blit(turtle14, n14)

    return


def bli():
    if j1:
        screen.blit(turtle, turtleRect)
    if j2:
        screen.blit(turtle1, n1)
    if j3:
        screen.blit(turtle2, n2)
    if j4:
        screen.blit(turtle3, n3)
    if j5:
        screen.blit(turtle4, n4)
    if j6:
        screen.blit(turtle5, n5)
    if j7:
        screen.blit(turtle6, n6)
    if j8:
        screen.blit(turtle7, n7)
    if j9:
        screen.blit(turtle8, n8)
    if j10:
        screen.blit(turtle9, n9)
    if j11:
        screen.blit(turtle10, n10)
    if j12:
        screen.blit(turtle11, n11)
    if j13:
        screen.blit(turtle12, n12)
    if j14:
        screen.blit(turtle13, n13)
    if j15:
        screen.blit(turtle14, n14)
    return


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15)
            if k == 1:
                x1, y1 = newRect.x, newRect.y  # 初始发射位置
                tip = 1

    keys = pygame.key.get_pressed()

    newLeaf = pygame.transform.rotate(leaf, angle)
    # 旋转图片(注意：这里要搞一个新变量，存储旋转后的图片）

    newRect = newLeaf.get_rect(center=leafRect.center)
    # 这里矫正中心点 新的中心点 center=leafRect.center 意义让新的图像到旧规定的地方

    screen.fill(BLACK)
    screen.blit(background, (0, 0))

    # pygame.draw.rect(screen, (255, 0, 0), leafRect, 1)
    # pygame.draw.rect(screen, (0, 255, 0), newRect, 1)
    if g == 0:
        enemy()

    if tip == 0:  # 转动
        k = 1
        bli()
        if angle == 0:
            judge = 0
        if angle == 180:
            judge = 1

        if judge == 0:
            angle += 1
        else:
            angle -= 1
        screen.blit(newLeaf, newRect)

    if tip == 1:  # 点鼠标

        k = 0
        bli()
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))

    if tip == 2.1:  # 抓到
        j1 = False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle, (x1, y1))

        bli()

        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.2:
        j2 = False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle1, (x1, y1))

        bli()

        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.3:
        j3 = False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值.
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle2, (x1, y1))

        bli()

        if y1 <= -50:
            velocity = 800

            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.4:
        j4 =False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle3, (x1, y1))

        bli()
        if y1 <= -50:
            velocity = 800

            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.5:
        j5 =False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle4, (x1, y1))
        bli()
        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.6:
        j6 =False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle5, (x1, y1))
        bli()

        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0



    if tip == 2.7:
        j7=False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle6, (x1, y1))

        bli()

        if y1 <= -50:
            velocity = 800

            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.8:
        j8=False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle7, (x1, y1))
        bli()

        if y1 <= -50:
            velocity = 800

            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.9:
        j9=False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle8, (x1, y1))
        bli()

        if y1 <= -50:
            velocity = 800

            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.11:
        j10 = False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle9, (x1, y1))

        bli()
        if y1 <= -50:
            velocity = 800

            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.12:
        j11=False

        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle10, (x1, y1))

        bli()

        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.13:
        j12= False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle11, (x1, y1))
        bli()

        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.14:
        j13 =False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle12, (x1, y1))
        bli()
        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.15:
        j14= False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle13, (x1, y1))
        bli()
        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 2.16:
        j15 =False
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))
        screen.blit(turtle14, (x1, y1))
        bli()
        if y1 <= -50:
            velocity = 800
            golds += 100
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if tip == 3:  # 出界
        bli()
        section = velocity * time  # 每个时间片需要移动的距离
        langle = radians(angle)  # 两点间线段的弧度值
        fangle = angle  # 弧度转角度
        sina = sin(langle)
        cosa = cos(langle)

        x1 = x1 - section * cosa
        y1 = y1 + section * sina

        screen.blit(newLeaf, (x1, y1))

        if y1 <= -50:
            print(golds)
            velocity = 800
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    # 判断抓取
    if j1:
        if t0 + 50 >= x1 >= t0 - 50 and u0 + 50 >= y1 >= u0 - 50:
            tip = 2.1
            velocity = -200
    if j2:
        if Lx[0] + 50 >= x1 >= Lx[0] - 50 and Ly[0] + 50 >= y1 >= Ly[0] - 50:
            tip = 2.2
            velocity = -200
    if j3:
        if Lx[1] + 50 >= x1 >= Lx[1] - 50 and Ly[1] + 50 >= y1 >= Ly[1] - 50:
            tip = 2.3
            velocity = -200
    if j4:
        if Lx[2] + 50 >= x1 >= Lx[2] - 50 and Ly[2] + 50 >= y1 >= Ly[2] - 50:
            tip = 2.4
            velocity = -200
    if j5:
        if Lx[3] + 50 >= x1 >= Lx[3] - 50 and Ly[3] + 50 >= y1 >= Ly[3] - 50:
            tip = 2.5
            velocity = -200
    if j6:
        if Lx[4] + 50 >= x1 >= Lx[4] - 50 and Ly[4] + 50 >= y1 >= Ly[4] - 50:
            tip = 2.6
            velocity = -200
    if j7:
        if Lx[5] + 50 >= x1 >= Lx[5] - 50 and Ly[5] + 50 >= y1 >= Ly[5] - 50:
            tip = 2.7
            velocity = -200
    if j8:
        if Lx[6] + 50 >= x1 >= Lx[6] - 50 and Ly[6] + 50 >= y1 >= Ly[6] - 50:
            tip = 2.8
            velocity = -200
    if j9:
        if Lx[7] + 50 >= x1 >= Lx[7] - 50 and Ly[7] + 50 >= y1 >= Ly[7] - 50:
            tip = 2.9
            velocity = -200
    if j10:
        if Lx[8] + 50 >= x1 >= Lx[8] - 50 and Ly[8] + 50 >= y1 >= Ly[8] - 50:
            tip = 2.11
            velocity = -200
    if j11:
        if Lx[9] + 50 >= x1 >= Lx[9] - 50 and Ly[9] + 50 >= y1 >= Ly[9] - 50:
            tip = 2.12
            velocity = -200
    if j12:
        if Lx[10] + 50 >= x1 >= Lx[10] - 50 and Ly[10] + 50 >= y1 >= Ly[10] - 50:
            tip = 2.13
            velocity = -200
    if j13:
        if Lx[11] + 50 >= x1 >= Lx[11] - 50 and Ly[11] + 50 >= y1 >= Ly[11] - 50:
            tip = 2.14
            velocity = -200
    if j14:
        if Lx[12] + 50 >= x1 >= Lx[12] - 50 and Ly[12] + 50 >= y1 >= Ly[12] - 50:
            tip = 2.15
            velocity = -200
    if j15:
        if Lx[13] + 50 >= x1 >= Lx[13] - 50 and Ly[13] + 50 >= y1 >= Ly[13] - 50:
            tip = 2.16
            velocity = -200

    if x1 >= 1700 or x1 <= -100 or y1 >= 900:
        velocity = -2000
        tip = 3

    pygame.display.update()
    clock.tick(120)

# leaf-02
