from parse import parse
import pygame
from pygame.locals import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
MUSIC_OFFSET=450
ACCELERATE=0.0000063
TOTAL_TIME=500
GREAT_TIME=150
PERFECT_TIME=70

V0=(1-ACCELERATE*0.5*TOTAL_TIME*TOTAL_TIME)/TOTAL_TIME
class SngButton():
    def __init__(self,sngbuttonimg,typeofbutton,clicktime):
        self.ori=sngbuttonimg
        self.pos=(0,0)
        self.img=self.ori
        self.typeofbutton=typeofbutton
        self.clicktime=clicktime
    def update(self,nowtime):
        x=V0*(TOTAL_TIME-self.clicktime+nowtime)+0.5*ACCELERATE*((TOTAL_TIME-self.clicktime+nowtime)**2)
        if self.typeofbutton==1:
            toppos=(370,0)
            buttompos=(16,465) 
            #213*68
            self.pos=(toppos[0]+(buttompos[0]-toppos[0])*x,toppos[1]+(buttompos[1]-toppos[1])*x)
            self.img=pygame.transform.scale(self.ori,(int(213*0.2629+(213*1.0147-213*0.2629)*x),int(68*0.2629+(68*1.0147-68*0.2629)*x)))
        elif self.typeofbutton==2:
            toppos=(434,0)
            buttompos=(261,465) 
            #196*68
            self.pos=(toppos[0]+(buttompos[0]-toppos[0])*x,toppos[1]+(buttompos[1]-toppos[1])*x)
            self.img=pygame.transform.scale(self.ori,(int(196*0.2194+(196*1.0147-196*0.2194)*x),int(68*0.2194+(68*1.0147-68*0.2194)*x)))
        elif self.typeofbutton==3:
            toppos=(483,0)
            buttompos=(498,465) 
            #203*66
            self.pos=(toppos[0]+(buttompos[0]-toppos[0])*x,toppos[1]+(buttompos[1]-toppos[1])*x)
            self.img=pygame.transform.scale(self.ori,(int(203*0.202+(203*1.0147-203*0.202)*x),int(66*0.202+(66*1.0147-66*0.202)*x)))
        elif self.typeofbutton==4:
            toppos=(533,0)
            buttompos=(729,465) 
            #212*67
            self.pos=(toppos[0]+(buttompos[0]-toppos[0])*x,toppos[1]+(buttompos[1]-toppos[1])*x)
            self.img=pygame.transform.scale(self.ori,(int(212*0.2406+(212*1.0147-212*0.2406)*x),int(67*0.2406+(67*1.0147-67*0.2406)*x)))



def start(filename):
    score=0
    comble=0
    maxcomble=0
    sgn, log = parse(filename+".xml")
    print(sgn)
    pygame.init()
    pygame.mixer.init()  
    pygame.mixer.music.load(filename+".mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    
    
    screen = pygame.display.set_mode((961, 579))#flags=pygame.HWSURFACE|pygame.FULLSCREEN
    pygame.display.set_caption('PyJam')
    img_gamepad = pygame.image.load('bg2.png').convert_alpha()
    gamepad = pygame.transform.scale(img_gamepad, (961, 579))
    topbar = pygame.image.load('topbar.png').convert_alpha()
    img_background = pygame.image.load(filename+'.png').convert()
    background = pygame.transform.scale(img_background, (961, 579))
    back1=pygame.image.load("back1.png")
    back1.convert()
    back2=pygame.image.load("back2.png")
    back2.convert()
    quit1=pygame.image.load("quit1.png")
    quit1.convert()
    quit2=pygame.image.load("quit2.png")
    quit2.convert()
    perfect = pygame.image.load('perfect.png').convert_alpha()
    great = pygame.image.load('great.png').convert_alpha()
    miss = pygame.image.load('miss.png').convert_alpha()

    perfect_display_status=0
    great_display_status=0
    miss_display_status=0

    grade_display_pattern=[0, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.8, 0.6, 0.4]
    perfect_pattern=[None]
    great_pattern=[None]
    miss_pattern=[None]

    for i in range(1, len(grade_display_pattern)):
        perfect_pattern.append(pygame.transform.scale(perfect, (int(perfect.get_width()*grade_display_pattern[i]), int(perfect.get_height()*grade_display_pattern[i]))))
    for i in range(1, len(grade_display_pattern)):
        great_pattern.append(pygame.transform.scale(great, (int(great.get_width()*grade_display_pattern[i]), int(great.get_height()*grade_display_pattern[i]))))
    for i in range(1, len(grade_display_pattern)):
        miss_pattern.append(pygame.transform.scale(miss, (int(miss.get_width()*grade_display_pattern[i]), int(miss.get_height()*grade_display_pattern[i]))))


    click_animation_combined = pygame.image.load("click.png").convert_alpha()
    click_animation=[click_animation_combined.subsurface((0,0,256,256))]
    click_animation+=[click_animation_combined.subsurface((256,0,256,256))]
    click_animation+=[click_animation_combined.subsurface((512,0,256,256))]
    click_animation+=[click_animation_combined.subsurface((768,0,256,256))]
    click_animation+=[click_animation_combined.subsurface((0,256,256,256))]
    click_animation+=[click_animation_combined.subsurface((256,256,256,256))]
    click_animation+=[click_animation_combined.subsurface((512,256,256,256))]
    click_animation+=[click_animation_combined.subsurface((768,256,256,256))]
    
    clock = pygame.time.Clock()

    screen.blit(background, (0, 0))

    single_pointer = 0
    long_pointer = 0
    single_in_progress = []
    long_in_progress = []

    single_button_img=[0]
    for i in range(1,5):
        single_button_img.append(pygame.image.load('single'+str(i)+'.png'))

    click_animation_status=[0 for i in range(4)]


    while(True):
        myscore = pygame.font.SysFont("微软雅黑", 80)
        mycomble = pygame.font.SysFont("微软雅黑", 80)
        mymaxcomble=pygame.font.SysFont("微软雅黑",40)
        scoreImage = myscore.render("%d"%score, True, (255, 255, 255))
        combleImage = mycomble.render("%d"%comble, True, (255, 255, 255))
        maxcombleImage=mymaxcomble.render("%d"%maxcomble,True,(255,255,255))
        current_time=pygame.mixer.music.get_pos()-MUSIC_OFFSET
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                maxcomble=max(comble,maxcomble)
                print("你的得分是 %d 分"%score)
                print("最多连击次数 %d 次"%maxcomble)
                pygame.quit()
                exit()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    #print(current_time)
                    for i in range(len(single_in_progress)):
                        if single_in_progress[i].typeofbutton==1 and abs(current_time-single_in_progress[i].clicktime)<=GREAT_TIME:
                            if single_in_progress[i].typeofbutton==1 and abs(current_time-single_in_progress[i].clicktime)<=PERFECT_TIME:
                                score+=100+comble//10
                                comble+=1
                                #print("perfect","score:",score,"comble:",comble)
                                perfect_display_status=1
                                great_display_status=0
                                miss_display_status=0
                            else:
                                score+=50+comble//20
                                comble+=1
                                #print("great","score:",score,"comble:",comble)
                                perfect_display_status=0
                                great_display_status=1
                                miss_display_status=0
                            single_in_progress.remove(single_in_progress[i])
                            click_animation_status[0]=1
                            break
                elif event.key==pygame.K_f:
                    #print(current_time)
                    for i in range(len(single_in_progress)):
                        if single_in_progress[i].typeofbutton==2 and abs(current_time-single_in_progress[i].clicktime)<=GREAT_TIME:
                            if single_in_progress[i].typeofbutton==2 and abs(current_time-single_in_progress[i].clicktime)<=PERFECT_TIME:
                                score+=100+comble//10
                                comble+=1
                                #print("perfect","score:",score,"combo:",comble)
                                perfect_display_status=1
                                great_display_status=0
                                miss_display_status=0
                            else:
                                score+=50+comble//20
                                comble+=1
                                #print("great","score:",score,"combo:",comble)
                                perfect_display_status=0
                                great_display_status=1
                                miss_display_status=0
                            single_in_progress.remove(single_in_progress[i])
                            click_animation_status[1]=1
                            break
                elif event.key==pygame.K_j:
                    #print(current_time)
                    for i in range(len(single_in_progress)):
                        if single_in_progress[i].typeofbutton==3 and abs(current_time-single_in_progress[i].clicktime)<=GREAT_TIME:
                            if single_in_progress[i].typeofbutton==3 and abs(current_time-single_in_progress[i].clicktime)<=PERFECT_TIME:
                                score+=100+comble//10
                                comble+=1
                                #print("perfect","score:",score,"combo:",comble)
                                perfect_display_status=1
                                great_display_status=0
                                miss_display_status=0
                            else:
                                score+=50+comble//20
                                comble+=1
                                #print("great","score:",score,"combo:",comble)
                                perfect_display_status=0
                                great_display_status=1
                                miss_display_status=0
                            single_in_progress.remove(single_in_progress[i])
                            click_animation_status[2]=1
                            break
                elif event.key==pygame.K_k:
                    #print(current_time)
                    for i in range(len(single_in_progress)):
                        if single_in_progress[i].typeofbutton==4 and abs(current_time-single_in_progress[i].clicktime)<=GREAT_TIME:
                            if single_in_progress[i].typeofbutton==4 and abs(current_time-single_in_progress[i].clicktime)<=PERFECT_TIME:
                                score+=100+comble//10
                                comble+=1
                                #print("perfect","score:",score,"combo:",comble)
                                perfect_display_status=1
                                great_display_status=0
                                miss_display_status=0
                            else:
                                score+=50+comble//20
                                comble+=1
                                #print("great","score:",score,"combo:",comble)
                                perfect_display_status=0
                                great_display_status=1
                                miss_display_status=0
                            single_in_progress.remove(single_in_progress[i])
                            click_animation_status[3]=1
                            break

        screen.blit(background, (0, 0))
        screen.blit(gamepad, (0, 0))
        #击键动画
        if (click_animation_status[0]>0):
            screen.blit(click_animation[click_animation_status[0]//5],(0,372))
            click_animation_status[0]+=1
            if click_animation_status[0]==40: click_animation_status[0]=0
        if (click_animation_status[1]>0):
            screen.blit(click_animation[click_animation_status[1]//5],(235,372))
            click_animation_status[1]+=1
            if click_animation_status[1]==40: click_animation_status[1]=0
        if (click_animation_status[2]>0):
            screen.blit(click_animation[click_animation_status[2]//5],(470,372))
            click_animation_status[2]+=1
            if click_animation_status[2]==40: click_animation_status[2]=0
        if (click_animation_status[3]>0):
            screen.blit(click_animation[click_animation_status[3]//5],(700,372))
            click_animation_status[3]+=1
            if click_animation_status[3]==40: click_animation_status[3]=0


        

        #看有没有新的键需要渲染
        while (single_pointer<=len(sgn)-1 and sgn[single_pointer][0]-TOTAL_TIME<current_time):
            single_in_progress.append(SngButton(single_button_img[sgn[single_pointer][1]],sgn[single_pointer][1],sgn[single_pointer][0]))
            single_pointer+=1

        #更新已经被渲染的键，
        for note in single_in_progress:
            note.update(current_time)
            if note.pos[1]>850:
                single_in_progress.remove(note)
                score+=comble*10
                #print("miss",score)
                perfect_display_status=0
                great_display_status=0
                miss_display_status=1
                maxcomble=max(comble,maxcomble)
                comble=0
            screen.blit(note.img,note.pos)
        
        if(perfect_display_status>0):
            screen.blit(perfect_pattern[perfect_display_status], perfect_pattern[perfect_display_status].get_rect(center=(480,80)))
            perfect_display_status+=1
            screen.blit(combleImage, (450, 118))
            if (perfect_display_status==len(grade_display_pattern)):
                perfect_display_status=0
        if(great_display_status>0):
            screen.blit(great_pattern[great_display_status], great_pattern[great_display_status].get_rect(center=(480,80)))
            great_display_status+=1
            screen.blit(combleImage,(450, 118))
            if (great_display_status==len(grade_display_pattern)):
                great_display_status=0
        if(miss_display_status>0):
            screen.blit(miss_pattern[miss_display_status], miss_pattern[miss_display_status].get_rect(center=(480,80)))
            miss_display_status+=1
            if (miss_display_status==len(grade_display_pattern)):
                miss_display_status=0
        screen.blit(topbar, (0, 0))
        screen.blit(scoreImage, (690, 18))
        screen.blit(maxcombleImage,(825,80))
        #screen.blit(back1,(361,190))
        #screen.blit(back2,(361,190))
        #screen.blit(quit1,(361,300))
        #screen.blit(quit2,(361,300))
        pygame.display.update()
        clock.tick(120)
        flag1=True
        if not pygame.mixer.music.get_busy():
            maxcomble=max(comble,maxcomble)
            maxcombleImage=mymaxcomble.render("%d"%maxcomble,True,(255,255,255))
            while True:
                x3,y3=pygame.mouse.get_pos()
                buttons2 = pygame.mouse.get_pressed()
                if 387<=x3<=621 and 200<=y3<=254:
                    screen.blit(background, (0, 0))
                    screen.blit(gamepad, (0, 0))
                    screen.blit(topbar, (0, 0))
                    screen.blit(back2,(361,190))
                    screen.blit(quit1,(361,300))
                    screen.blit(scoreImage, (690, 18))
                    screen.blit(maxcombleImage,(825,80))
                    if buttons2[0]:
                        flag1=False
                        break
                elif 361<=x3<=596 and 300<=y3<=357:
                    
                    screen.blit(background, (0, 0))
                    screen.blit(gamepad, (0, 0))
                    screen.blit(topbar, (0, 0))
                    screen.blit(quit2,(361,300))
                    screen.blit(back1,(361,190))
                    screen.blit(scoreImage, (690, 18))
                    screen.blit(maxcombleImage,(825,80))
                    if buttons2[0]:
                        pygame.quit()
                        exit()
                else:    
                    screen.blit(background, (0, 0))
                    screen.blit(gamepad, (0, 0))                
                    screen.blit(topbar, (0, 0))
                    screen.blit(back1,(361,190))
                    screen.blit(quit1,(361,300)) 
                    screen.blit(scoreImage, (690, 18))
                    screen.blit(maxcombleImage,(825,80))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                pygame.display.update()
            if flag1==False:
                break
            
        

pygame.init()
ck = pygame.display.set_mode((800,600))
bgr=pygame.image.load("bgr.png")
bgr=pygame.transform.scale(bgr, (900, 700))
bgr.convert_alpha()  
pygame.display.set_caption("节奏带师")    
clock = pygame.time.Clock()                        
start_ck = pygame.Surface(ck.get_size())      
start_ck = start_ck.convert()
start_ck.fill((255,255,255))  

i0=pygame.image.load("节奏带师1.png")
i0.convert()

i1 = pygame.image.load("开始游戏1.png")
i1.convert()
i11 = pygame.image.load("开始游戏2.png")
i11.convert()

i2 = pygame.image.load("结束游戏1.png")
i2.convert()
i21 = pygame.image.load("结束游戏2.png")
i21.convert()


while True:
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= 227 and x1 <= 555 and y1 >= 261 and y1 <=327:
        start_ck.blit(bgr,(0,0))
        start_ck.blit(i0, (175, 50))
        start_ck.blit(i11, (200, 240))
        start_ck.blit(i2, (200, 360))
        if buttons[0]:
            pygame.init()
            catbgr=pygame.image.load("catbgr.png")
            catbgr=pygame.transform.scale(catbgr,(961,579))  
            catbgr.convert()
            catalog_bg_ = pygame.display.set_mode((961,579))  
            pygame.display.set_caption("节奏带师")
            clock1=pygame.time.Clock()
            catalog_bg = pygame.Surface(catalog_bg_.get_size())
            catalog_bg = catalog_bg.convert()
            catalog_bg.fill((255,255,255)) 
            white=pygame.image.load("white.png")
            white.convert()
            rapsody0=pygame.image.load("rapsody.png")
            rapsody0.convert()
            rapsody1=pygame.image.load("克罗地亚狂想曲1.png")
            rapsody1.convert()
            rapsody2=pygame.image.load("克罗地亚狂想曲2.png")
            rapsody2.convert()
            rapsody3=pygame.image.load("克罗地亚狂想曲3.png")
            rapsody3.convert()
            flowerdance0=pygame.image.load("flowerdance.png")
            flowerdance0.convert()
            flowerdance1=pygame.image.load("花之舞1.png")
            flowerdance1.convert()
            flowerdance2=pygame.image.load("花之舞2.png")
            flowerdance2.convert()
            flowerdance3=pygame.image.load("花之舞3.png")
            flowerdance3.convert()
            drama0=pygame.image.load("drama.png")
            drama0.convert()
            drama1=pygame.image.load("drama1.png")
            drama1.convert()
            drama2=pygame.image.load("drama2.png")
            drama2.convert()
            drama3=pygame.image.load("drama3.png")
            drama3.convert()
            luvletter0=pygame.image.load("luvletter.png")
            luvletter0.convert()
            luvletter1=pygame.image.load("luvletter1.png")
            luvletter1.convert()
            luvletter2=pygame.image.load("luvletter2.png")
            luvletter2.convert()
            luvletter3=pygame.image.load("drama3.png")
            luvletter3.convert()
            bee0=pygame.image.load("yefengfeiwu.png")
            bee0.convert()
            bee1=pygame.image.load("野蜂飞舞1.png")
            bee1.convert()
            bee2=pygame.image.load("野蜂飞舞2.png")
            bee2.convert()
            bee3=pygame.image.load("野蜂飞舞3.png")
            bee3.convert()
            redsign0=pygame.image.load("redsign.png")
            redsign0.convert()
            redsign1=pygame.image.load("redsign1.png")
            redsign1.convert()
            redsign2=pygame.image.load("redsign2.png")
            redsign2.convert()
            redsign3=pygame.image.load("redsign3.png")
            redsign3.convert()

            while True:
                clock1.tick(60)
                catalog_bg.blit(catbgr,(0,0))
                buttons1=pygame.mouse.get_pressed()
                x2,y2=pygame.mouse.get_pos()
                if 42<=x2<=368 and 47<=y2<=98:
                    catalog_bg.blit(rapsody2,(39,48))
                    catalog_bg.blit(rapsody0,(450,145))
                    catalog_bg.blit(rapsody3,(630,91))
                    catalog_bg.blit(flowerdance1,(40,115))
                    catalog_bg.blit(drama1,(41,188))
                    catalog_bg.blit(luvletter1,(40,254))
                    catalog_bg.blit(bee1,(38,322))
                    catalog_bg.blit(redsign1,(36,392))
                    if buttons1[0]:
                        start("rapsody")
                elif 40<=x2<=180 and 115<=y2<=168:
                    catalog_bg.blit(flowerdance2,(39,117))
                    catalog_bg.blit(flowerdance0,(450,145))
                    catalog_bg.blit(flowerdance3,(630,88))
                    catalog_bg.blit(rapsody1,(40,45))
                    catalog_bg.blit(drama1,(41,188))
                    catalog_bg.blit(luvletter1,(40,254))
                    catalog_bg.blit(bee1,(38,322))
                    catalog_bg.blit(redsign1,(36,392))
                    if buttons1[0]:
                        start("flowerdance")
                elif 40<=x2<=180 and 182<=y2<=228:
                    catalog_bg.blit(drama2,(40,191))
                    catalog_bg.blit(drama0,(450,145))
                    catalog_bg.blit(drama3,(630,91))
                    catalog_bg.blit(rapsody1,(40,45))
                    catalog_bg.blit(flowerdance1,(40,115))
                    catalog_bg.blit(luvletter1,(40,254))
                    catalog_bg.blit(bee1,(38,322))
                    catalog_bg.blit(redsign1,(36,392))
                    if buttons1[0]:
                        start("drama")
                elif 40<=x2<=260 and 252<=y2<=295:
                    catalog_bg.blit(luvletter2,(39,256))
                    catalog_bg.blit(luvletter0,(450,145))
                    catalog_bg.blit(luvletter3,(630,91))
                    catalog_bg.blit(rapsody1,(40,45))
                    catalog_bg.blit(flowerdance1,(40,115))
                    catalog_bg.blit(drama1,(41,188))
                    catalog_bg.blit(bee1,(38,322))
                    catalog_bg.blit(redsign1,(36,392))
                    if buttons1[0]:
                        start("luvletter")
                elif 40<=x2<=224 and 324<=y2<=372:
                    catalog_bg.blit(bee2,(37,324))
                    catalog_bg.blit(bee0,(450,145))
                    catalog_bg.blit(bee3,(630,91))
                    catalog_bg.blit(rapsody1,(40,45))
                    catalog_bg.blit(flowerdance1,(40,115))
                    catalog_bg.blit(drama1,(41,188))
                    catalog_bg.blit(luvletter1,(40,254))
                    catalog_bg.blit(redsign1,(36,392))
                    if buttons1[0]:
                        start("yefengfeiwu")
                elif 38<=x2<=180 and 393<=y2<=439:
                    catalog_bg.blit(redsign2,(35,394))
                    catalog_bg.blit(redsign0,(450,145))
                    catalog_bg.blit(redsign3,(625,96))
                    catalog_bg.blit(rapsody1,(40,45))
                    catalog_bg.blit(flowerdance1,(40,115))
                    catalog_bg.blit(drama1,(41,188))
                    catalog_bg.blit(luvletter1,(40,254))
                    catalog_bg.blit(bee1,(38,322))
                    if buttons1[0]:
                        start("redsign")
    
                else:
                    catalog_bg.blit(rapsody1,(40,45))
                    catalog_bg.blit(flowerdance1,(40,115))
                    catalog_bg.blit(drama1,(41,188))
                    catalog_bg.blit(luvletter1,(40,254))
                    catalog_bg.blit(bee1,(38,322))
                    catalog_bg.blit(redsign1,(36,392))
                    catalog_bg.blit(white,(291,0))
                catalog_bg_.blit(catalog_bg,(0,0))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        exit()

    elif x1 >= 227 and x1 <= 555 and y1 >= 381 and y1 <=447:
        start_ck.blit(bgr,(0,0))
        start_ck.blit(i0, (175, 50))
        start_ck.blit(i21, (200, 360))
        start_ck.blit(i1, (200, 240))
        if buttons[0]:
            pygame.quit()
            exit()

    else:
        start_ck.blit(bgr,(0,0))
        start_ck.blit(i0, (175, 50))
        start_ck.blit(i1, (200, 240))
        start_ck.blit(i2, (200, 360))


    ck.blit(start_ck,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
ck.blit(bgr,(0,0))
pygame.display.update()




#克罗地亚狂想曲 rapsody 6级
#花之舞 flowerdance 7级
#Drama drama 8级
#Luv Letter luvletter 8级
#野蜂飞舞 yefengfeiwu 9级
#赤信号 redsign 10级