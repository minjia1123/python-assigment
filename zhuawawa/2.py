import pygame
import sys
import time
import datetime
import  random
from math import *

pygame.init()
ck = pygame.display.set_mode((1600,900))
pygame.display.set_caption("抓娃娃机")    
# clock = pygame.time.Clock()                         #  游戏刷新速度
start_ck = pygame.Surface(ck.get_size())#   充当开始界面的画布
start_ck1 = pygame.Surface(ck.get_size())
start_ck11 = pygame.Surface(ck.get_size())
start_ck2 = pygame.Surface(ck.get_size())  #  设置的画布界面
start_ck = start_ck.convert()
start_ck1 = start_ck1.convert()
start_ck11 = start_ck1.convert()
start_ck2 = start_ck2.convert()
start_ck.fill((255,230,229))  # 白色画布（开始界面）
start_ck1.fill((255,230,229))
start_ck11.fill((255,230,229))
start_ck2.fill((255,230,229))
SIZE = WIDTH, HEIGHT = 1600, 900
BLACK = 0, 0, 0
angle = 1
judge =0
golds = 0
g = 0

my_font = pygame.font.Font(None,60)                   #字体
line_height = my_font.get_linesize()                  #行高



screen = pygame.display.set_mode(SIZE)
leaf = pygame.image.load("arrow.png")
background = pygame.image.load("back.png").convert()

turtle = pygame.image.load('gold 1.png')
turtle1 = pygame.image.load('gold 2.png')
turtle2 = pygame.image.load('gold 3.png')
turtle3 = pygame.image.load('gold 4.png')
turtle4 = pygame.image.load('gold 4.png')
turtle5 = pygame.image.load('gold 4.png')
turtle6 = pygame.image.load('gold 4.png')
turtle7 = pygame.image.load('gold 4.png')
turtle8 = pygame.image.load('gold 4.png')
turtle9 = pygame.image.load('gold 2.png')
turtle10 = pygame.image.load('gold 2.png')
turtle11 = pygame.image.load('gold 2.png')
turtle12 = pygame.image.load('gold 2.png')
turtle13 = pygame.image.load('gold 3.png')
turtle14 = pygame.image.load('gold 3.png')

leafRect = leaf.get_rect()
leafRect = leafRect.move((WIDTH - leafRect.width) / 2, 50-leafRect.height)

x0, y0 = leafRect.x , leafRect.y
x1, y1 = leafRect.x , leafRect.y

turtleRect = turtle.get_rect()
turtleRect = turtleRect.move(350,550)
t0 , u0 = turtleRect.x, turtleRect.y


height = leaf.get_height()
width = leaf.get_width()

velocity = 800  # 速度
time = 1 / 120  # 每个时间片的长度
clock = pygame.time.Clock()

tip=0

G=[0,500,1100,1700,2400,3100,3900,4800,5800]

i1 = pygame.image.load("start2.png")           #开始及设置界面按钮图片
i1.convert()
i11 = pygame.image.load("start1.png")
i11.convert()


i2 = pygame.image.load("end2.png")
i2.convert()
i21 = pygame.image.load("end1.png")
i21.convert()

i3 = pygame.image.load("set2.png")
i3.convert()
i31 = pygame.image.load("set1.png")
i31.convert()

r1 = pygame.image.load("return2.png")
r1.convert()
r11 = pygame.image.load("return1.png")
r11.convert()

s1 = pygame.image.load("open1.png")
s1.convert()
s11 = pygame.image.load("open2.png")
s11.convert()

s2 = pygame.image.load("close1.png")
s2.convert()
s21 = pygame.image.load("close2.png")
s21.convert()

p1 = pygame.image.load("restart.png")
p1.convert()

p2 = pygame.image.load("unpasue2.png")
p2.convert()
p21 = pygame.image.load("unpasue1.png")
p21.convert()

a1,a11=s1,s11
b1,b11=s1,s11
a2,a21=s2,s21
b2,b21=s2,s21

#startbg=pygame.image.load("startbg1.png")
#startbg.convert()

setbutton=pygame.image.load("setbutton1.png")
setbutton.convert()

pasuebutton=pygame.image.load("pasue.png")
pasuebutton.convert()

setbg=pygame.image.load("setbackgound1.png")
setbg.convert()

pasue = pygame.image.load('pasuemenu.png')
pasue.convert()

winning = pygame.image.load('winning.png')
winning.convert()

gameover = pygame.image.load('gameover.png')
gameover.convert()

bg = pygame.image.load('back.png')
bg.convert()


pygame.mixer.init()                                #音乐相关
soundsta=pygame.mixer.Sound("start.wav")
#soundend=pygame.mixer.Sound("end.wav")
soundsuc=pygame.mixer.Sound("success(2).wav")
soundwin=pygame.mixer.Sound("success(2).wav")
soundfail=pygame.mixer.Sound("fail(1).wav")
soundsuc.set_volume(100)


music2=1
sound=[]
f=["%d.flac"%x for x in range(1,8)]
for x in f:
    sound.append(pygame.mixer.Sound(x))
soundl=[0,0,4,4,5,5,4,3,3,2,2,1,1,0,4,4,3,3,2,2,1,3,3,2,2,1,1,0]
psum=0

music1=1
soundsta.play()
time1=datetime.datetime.now()
while (datetime.datetime.now()-time1).seconds <=2:
    clock.tick(30)
    ck.blit(start_ck,(0,0))
    pygame.display.update()
    
pygame.mixer.music.load("bgm.flac")
pygame.mixer.music.play(-1)

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

def enemy():
    global j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15
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
        g4 = random.randint(0, 1500)
        g5 = random.randint(200, 800)

        if g4 not in Lx and i1 != 14:
            Lx.append(g4)
            i1 += 1
        if g5 not in Ly and i2 != 14:
            Ly.append(g5)
            i2 += 1

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

    if random.randint(1,5)== 2:
        j2 = 0
    else:
        screen.blit(turtle1, n1)
    if random.randint(1,5)== 2:
        j3 = 0
    else:
        screen.blit(turtle2, n2)
    if random.randint(1,3)== 2:
        j4 = 0
    else:
        screen.blit(turtle3, n3)
    if random.randint(1,3)== 2:
        j5 = 0
    else:
        screen.blit(turtle4, n4)

    if random.randint(1,3)== 2:
        j6 = 0
    else:
        screen.blit(turtle5, n5)

    if random.randint(1,3)== 2:
        j7 = 0
    else:
        screen.blit(turtle6, n6)

    if random.randint(1,3)== 2:
        j8 = 0
    else:
        screen.blit(turtle7, n7)

    if random.randint(1,4)== 2:
        j9 = 0
    else:
        screen.blit(turtle8, n8)

    if random.randint(1,4)== 2:
        j10 = 0
    else:
        screen.blit(turtle9, n9)

    if random.randint(1,4)== 2:
        j11 = 0
    else:
        screen.blit(turtle10, n10)

    if random.randint(1,4)== 2:
        j12 = 0
    else:
        screen.blit(turtle11, n11)

    if random.randint(1,4)== 2:
        j13 = 0
    else:
        screen.blit(turtle12, n12)

    if random.randint(1,3)== 2:
        j14 = 0
    else:
        screen.blit(turtle13, n13)

    if random.randint(1,3)== 2:
        j15 = 0
    else:
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



def winend():
    global psum,number0,golds
    while True:
        button0 = pygame.mouse.get_pressed()
        x3, y3= pygame.mouse.get_pos()
        clock.tick(30)
        start_ck1.blit(winning,(600,100))
        start_ck1.blit(p1,(700,502))
        start_ck1.blit(p2,(900,500))
        start_ck1.blit(my_font.render(str(number0),True,(207,169,114)),(835,310))
        start_ck1.blit(my_font.render(ch2,True,(207,169,114)),(820,394))

        if x3>=690 and x3<=790 and y3>=507 and y3<=597:
            start_ck1.blit(p1,(699,503))
            if button0[0]:
                golds = 0
                number0 = 1
                return 1

        elif x3>=890 and x3<=990 and y3>=510 and y3<=600:
            start_ck1.blit(p21,(900,500))
            if button0[0]:
                number0+=1
                return 1
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出QAQ")
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and music2:
                n=soundl[psum]
                sound[n].play()
                psum=(psum+1)%28

        #start_ck2.blit(winning,(600,100))
        #start_ck2.blit(p1,(700,502))
        #start_ck2.blit(p2,(900,500))

        ck.blit(start_ck1,(0,0))
        pygame.display.update()


def failend():
    global psum,number0,golds
    pygame.mixer.music.pause()
    if music2:
       soundfail.play()
    start_ck11.blit(gameover,(600,100))
    while True:
        button0 = pygame.mouse.get_pressed()
        x3, y3= pygame.mouse.get_pos()
        clock.tick(30)
        start_ck11.blit(gameover,(600,100))
        start_ck11.blit(p1,(800,502))
        start_ck11.blit(my_font.render(str(number0),True,(207,169,114)),(833,310))
        start_ck11.blit(my_font.render(ch2,True,(207,169,114)),(780,380))

        if x3>=790 and x3<=890 and y3>=507 and y3<=597:
            start_ck11.blit(p1,(799,503))
            if button0[0]:
                golds=0
                number0=1
                pygame.mixer.music.unpause()
                return 1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出QAQ")
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and music2:
                n=soundl[psum]
                sound[n].play()
                psum=(psum+1)%28

        ck.blit(start_ck11,(0,0))
        pygame.display.update()
        
    
def pasuemenu():
    global psum,number0,golds
    while True:
        button0 = pygame.mouse.get_pressed()
        x3, y3= pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(pasue,(510,300))
        screen.blit(p1,(590,395))
        screen.blit(p2,(760,390))
        screen.blit(setbutton,(940,393))

        if x3>=580 and x3<=680 and y3>=400 and y3<=490:
           screen.blit(p1, (589,396))
           if button0[0]:
               velocity = 800
               tip = 0
               golds=0
               number0=1
               return 1
           
        elif x3>=750 and x3<=850 and y3>=400 and y3<=490:
           screen.blit(p21, (760,390))
           if button0[0]:return 0

        elif x3>=930 and x3<=1030 and y3>=400 and y3<=490:
           screen.blit(setbutton, (939,394))
           if button0[0]:setmenu()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出QAQ")
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and music2:
                n=soundl[psum]
                sound[n].play()
                psum=(psum+1)%28

        pygame.display.update()

                    
def setmenu():                                #设置界面
    global psum,a1,a11,b1,b11,a2,a21,b2,b21,music1,music2
    n3=True
    start_ck2.blit(setbg,(0,-20))
    while n3:
        clock.tick(30)
        start_ck2.blit(setbg,(0,-20))
        button0 = pygame.mouse.get_pressed()
        x3, y3= pygame.mouse.get_pos()   

        if x3>=1256 and x3<=1335 and y3>=70 and y3<=160:
           start_ck2.blit(r11, (1238,65))
           if button0[0]:
               n3=False

        elif x3 >= 1010 and x3 <= 1225 and y3>= 288 and y3 <=347:
            start_ck2.blit(a11, (991,283))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("游戏退出QAQ")
                    pygame.quit()
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a1,a2=a2,a1
                    a11,a21=a21,a11
                    if music2:
                        n=soundl[psum]
                        sound[n].play()
                        psum=(psum+1)%28
                    if music1:
                        pygame.mixer.music.pause()
                        music1=0
                    else:
                        pygame.mixer.music.unpause()
                        music1=1
                                           

        elif x3 >= 1010 and x3 <= 1225 and y3>= 468 and y3 <=527:
            start_ck2.blit(b11, (991,463))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("游戏退出QAQ")
                    pygame.quit()
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if music2:
                        n=soundl[psum]
                        sound[n].play()
                        psum=(psum+1)%28
                        music21=1
                    b1,b2=b2,b1
                    b11,b21=b21,b11
                    if music2:music2=0
                    else:music2=1
                    

        start_ck2.blit(r1, (1240,65))
        start_ck2.blit(a1, (1000,285))
        start_ck2.blit(b1, (1000,465))
              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出QAQ")
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and music2:
                n=soundl[psum]
                sound[n].play()
                psum=(psum+1)%28


        ck.blit(start_ck2,(0,0))
        pygame.display.update()    
    



n1 = True
while n1:                                       #开始界面
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x2, y2 = pygame.mouse.get_pos()
    
    if x2 >= 680 and x2 <= 920 and y2 >= 305 and y2 <=360:
        start_ck.blit(i11, (680, 300))
        if buttons[0]:
            n1 = False
            n2 = True
            
    elif x2 >= 680 and x2 <= 920 and y2 >= 405 and y2 <=460:
        start_ck.blit(i21, (680, 400))
        if buttons[0]:
            print("游戏退出QAQ")
            pygame.quit()
            exit()
            
    elif x2 >= 680 and x2 <= 920 and y2 >= 505 and y2 <=560:
        start_ck.blit(i31, (680, 500))
        if buttons[0]:
            setmenu()
            ck.blit(start_ck,(0,0))
            pygame.display.update()

            
    else:
        #start_ck.blit(startbg, (0, 0))
        start_ck.blit(i1, (680, 300))
        start_ck.blit(i2, (680, 400))
        start_ck.blit(i3, (680, 500))

        
    ck.blit(start_ck,(0,0))
    pygame.display.update()

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("游戏退出QAQ")
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and music2:
            n=soundl[psum]
            sound[n].play()
            psum=(psum+1)%28


#ck.blit(start_ck2,(0,0))
#pygame.display.update()

resta=0
timehead=datetime.datetime.now()
subtime=60
#  以下可以写游戏的代码了
number0=1
soundplay=1
while n2:
    if resta:
        j1=1
        j2=1
        j3=1
        j4=1
        j5= 1
        j6=1
        j7=1
        j8=1
        j9=1
        j10=1
        j11=1
        j12=1
        j13=1
        j14=1
        j15=1
        velocity=800
        subtime=60
        g=0
        angle=1
        judge=0
        tip=0
        timehead=datetime.datetime.now()
        resta=0
    buttons = pygame.mouse.get_pressed()
    x2, y2 = pygame.mouse.get_pos()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏结束了")
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if music2:
                n=soundl[psum]
                sound[n].play()
                psum=(psum+1)%28
            if k == 1:
                x1, y1 = newRect.x, newRect.y  # 初始发射位置
                tip =1

    keys = pygame.key.get_pressed()

    newLeaf = pygame.transform.rotate(leaf, angle)
    # 旋转图片(注意：这里要搞一个新变量，存储旋转后的图片）

    newRect = newLeaf.get_rect(center=leafRect.center)
    #这里矫正中心点 新的中心点 center=leafRect.center 意义让新的图像到旧规定的地方

    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    screen.blit(pasuebutton, (1400, 60))

    # pygame.draw.rect(screen, (255, 0, 0), leafRect, 1)
    # pygame.draw.rect(screen, (0, 255, 0), newRect, 1)

    if g == 0:
        enemy()

    if tip == 0:  # 转动
        k = 1
        bli()
        if angle == 1:
            judge = 0
        if angle == 179:
            judge = 1

        if judge == 0:
            angle += 2
        else:
            angle -= 2
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

    if tip == 2.1:  # 抓到
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
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
            soundplay=1
            
    if tip == 2.2:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
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
            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.3:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
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
            soundplay=1
            
    if tip == 2.4:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j4 = False
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

            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.5:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j5 = False
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
            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.6:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j6 = False
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
            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.7:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j7 = False
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

            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.8:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j8 = False
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

            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.9:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j9 = False
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

            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.11:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
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

            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1
            
    if tip == 2.12:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j11 = False

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
            golds += 75
            screen.blit(newLeaf, (x1, y1))
            tip = 0
            soundplay=1            

    if tip == 2.13:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j12 = False
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
            soundplay=1
            soundplay=1
            
    if tip == 2.14:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j13 = False
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
            soundplay=1
            
    if tip == 2.15:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j14 = False
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
            soundplay=1
            
    if tip == 2.16:
        if soundplay and music2:
            soundsuc.play()
        soundplay=0
        j15 = False
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
            soundplay=1

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
            velocity = 800
            screen.blit(newLeaf, (x1, y1))
            tip = 0

    if x2 >= 1390 and x2 <= 1500 and y2 >= 50 and y2 <=150:
        screen.blit(pasuebutton, (1399, 59))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏退出QAQ")
                pygame.quit()
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music2:
                    n=soundl[psum]
                    sound[n].play()
                    psum=(psum+1)%28
                resta=pasuemenu()
                pygame.display.update()

    ch1=str(subtime)
    ch2=str(golds)
    ch3=str(G[number0])
    screen.blit(my_font.render('Time:'+ch1,True,(250,230,230)),(300,80))
    screen.blit(my_font.render('Golds:'+ch2,True,(250,230,230)),(1000,80))
    screen.blit(my_font.render('Goal:'+ch3,True,(250,230,230)),(0,0))
    timetail=datetime.datetime.now()
    if (timetail-timehead).seconds>=1:
        timehead=timetail
        subtime-=1
    pygame.display.flip()

    if j1 ==0 and j2== 0and j3 ==0 and j4 == 0and j5 == 0 and j7 == 0 and j8 == 0 and j9 == 0 and j10 ==0 and j11==0 and j12==0 and j13 ==0 and j14==0 and j15==0:
        resta = winend()

    if subtime==0:
        velocity= 800
        tip = 0
        angle=1
        judge=0
        if number0==8:
            resta = failend()        
        elif golds >= G[number0]:
            resta = winend()
        else:
            resta=failend()
    
    pygame.display.update()
    clock.tick(120)
