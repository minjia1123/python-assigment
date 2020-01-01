import pygame as pg
import sys
from settings import *
from sprites import *
from os import path
from Map_ import *
from random import sample
import random

def draw_player_health(surf,x,y,pct):
    if pct<0:
        pct=0
    BAR_LENGTH=115
    BAR_HEIGHT=15
    fill=pct*BAR_LENGTH
    outline_rect=pg.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect=pg.Rect(x,y,fill,BAR_HEIGHT)
    col=RED
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,BROWN,outline_rect,1)

def draw_player_shield(surf,x,y,pct): #护盾系统它Lei了！
    if pct<0:
        pct=0
    BAR_LENGTH=115
    BAR_HEIGHT=15
    fill=pct*BAR_LENGTH
    outline_rect=pg.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect=pg.Rect(x,y,fill,BAR_HEIGHT)
    col=SHIELD_CLO
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,BROWN,outline_rect,1)
 
def draw_player_energy(surf,x,y,pct): #蓝条
    if pct<0:
        pct=0
    BAR_LENGTH=115
    BAR_HEIGHT=15
    fill=pct*BAR_LENGTH
    outline_rect=pg.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect=pg.Rect(x,y,fill,BAR_HEIGHT)
    col=ENERGY_CLO
    pg.draw.rect(surf,col,fill_rect)
    pg.draw.rect(surf,BROWN,outline_rect,1)

def shield_recover(sprite):
    if sprite.shield<PLAYER_SHIELD:
            sprite.shield+=1

           
def player_get_damage(sprite,damage,music):#玩家受伤害系统,先扣盾，再掉血
    if pg.time.get_ticks()-sprite.invincible_time>=PLAYER_INVINCIBLE_TIME:
        sprite.hit()
        sprite.invincible_time=pg.time.get_ticks()
        music.play()
        if sprite.shield>0:
            sprite.shield -=damage
        if sprite.shield<0:
            sprite.shield=0
            return #防止破盾时承受二次伤害
        if sprite.shield==0:
            sprite.health -=damage
    
    
class Game:
    def __init__(self):
        global pg
        pg.init()
        self.screen=pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock=pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.load_data()
        self.playing=True
        self.timing=True
        self.paused=False
        self.t=pg.time.get_ticks()
        self.player_tran=1
        self.i=0 #奇怪的变量，在update里有用(好吧就是懒的拉函数）
        self.level=1
        self.players=pg.sprite.Group()
        self.player=Player(self,-100,-100)
        self.font_name=pg.font.match_font(FONT_NAME)
        
    def load_data(self):
        game_folder=path.dirname(__file__)
        img_folder=path.join(game_folder,'img')
        
        music_folder=path.join(game_folder,'snd')
        
        #self.start_sound=pg.mixer.sound(path.join(music_folder,START_MUSIC))
        pg.mixer.music.load(path.join(music_folder,START_MUSIC))
        self.hit_music = pg.mixer.Sound(path.join(music_folder, HIT_MUSIC))
        self.shoot_enemy=pg.mixer.Sound(path.join(music_folder,SHOOT_ENEMY ))
        self.shoot_knight=pg.mixer.Sound(path.join(music_folder,SHOOT_KNIGHT ))
        self.shot_knight=pg.mixer.Sound(path.join(music_folder,SHOT_KNIGHT ))
        self.jump=pg.mixer.Sound(path.join(music_folder,JUMP_BOSS ))

        self.map1=Map(path.join(game_folder,'map1.txt'))
        self.map2=Map(path.join(game_folder,'map2.txt'))
        self.map3=Map(path.join(game_folder,'map3.txt'))
        self.map4=Map(path.join(game_folder,'map4.txt'))

        self.player_img1=pg.image.load(path.join(img_folder,PLAYER_IMG1)).convert_alpha()
        self.player_img2=pg.image.load(path.join(img_folder,PLAYER_IMG2)).convert_alpha()
        self.player_img=self.player_img1
        
        self.bullet_img=pg.image.load(path.join(img_folder,BULLET_IMG)).convert_alpha()
        self.mobbullet_img=pg.image.load(path.join(img_folder,MOBBULLET_IMG)).convert_alpha()

        self.gun_img=pg.image.load(path.join(img_folder,GUN_IMG)).convert_alpha()
        
        self.floor_img1=pg.image.load(path.join(img_folder,FLOOR_IMG1)).convert_alpha()
        self.floor_img1=pg.transform.scale(self.floor_img1,(TILESIZE,TILESIZE))
        self.floor_img2=pg.image.load(path.join(img_folder,FLOOR_IMG2)).convert_alpha()
        self.floor_img2=pg.transform.scale(self.floor_img2,(TILESIZE,TILESIZE))
        self.floor_img3=pg.image.load(path.join(img_folder,FLOOR_IMG3)).convert_alpha()
        self.floor_img3=pg.transform.scale(self.floor_img3,(TILESIZE,TILESIZE))
        self.floor_img4=pg.image.load(path.join(img_folder,FLOOR_IMG4)).convert_alpha()
        self.floor_img4=pg.transform.scale(self.floor_img4,(TILESIZE,TILESIZE))
        self.floor_img5=pg.image.load(path.join(img_folder,FLOOR_IMG5)).convert_alpha()
        self.floor_img5=pg.transform.scale(self.floor_img5,(TILESIZE,TILESIZE))
        self.floor_img6=pg.image.load(path.join(img_folder,FLOOR_IMG6)).convert_alpha()
        self.floor_img6=pg.transform.scale(self.floor_img6,(TILESIZE,TILESIZE))
        
        self.mobpig_img=pg.image.load(path.join(img_folder,MOBPIG_IMG)).convert_alpha()
        self.mobflower_img=pg.image.load(path.join(img_folder,MOBFLOWER_IMG)).convert_alpha()
        self.mobminer_img=pg.image.load(path.join(img_folder,MINER_IMG)).convert_alpha()
        self.boss_img1=pg.image.load(path.join(img_folder,BOSS_IMG1)).convert_alpha()
        self.boss_img2=pg.image.load(path.join(img_folder,BOSS_IMG2)).convert_alpha()
        self.boss_img=self.boss_img1

        self.wall_img=pg.image.load(path.join(img_folder,WALL_IMG)).convert_alpha()
        self.wall_img=pg.transform.scale(self.wall_img,(TILESIZE,TILESIZE))
        #self.mob_img=pg.image.load(path.join(img_folder,MOB_IMG)).convert_alpha()
        self.healthbar_img=pg.image.load(path.join(img_folder,HEALTH_BAR_IMG)).convert_alpha()
        self.boss_health_bar_img=pg.image.load(path.join(img_folder,BOSS_HEALTH_BAR_IMG)).convert_alpha()

        self.gate_img=pg.image.load(path.join(img_folder,GATE_IMG)).convert_alpha()
        self.stone_img=pg.image.load(path.join(img_folder,STONE_IMG)).convert_alpha()

        self.start_img1=pg.image.load(path.join(img_folder,START_IMG1)).convert_alpha()
        self.start_img2=pg.image.load(path.join(img_folder,START_IMG2)).convert_alpha()

        self.red_img=pg.image.load(path.join(img_folder,RED_IMG)).convert_alpha()
        self.grey_img=pg.image.load(path.join(img_folder,GREY_IMG)).convert_alpha()
        self.blue_img=pg.image.load(path.join(img_folder,BLUE_IMG)).convert_alpha()
        self.newgame1_img=pg.image.load(path.join(img_folder,NEWGAME1_IMG)).convert_alpha()
        self.newgame2_img=pg.image.load(path.join(img_folder,NEWGAME2_IMG)).convert_alpha()
        self.surebutton1_img=pg.image.load(path.join(img_folder,SUREBUTTON1_IMG)).convert_alpha()
        self.surebutton2_img=pg.image.load(path.join(img_folder,SUREBUTTON2_IMG)).convert_alpha()
        self.knight_head_img=pg.image.load(path.join(img_folder,KNIGHT_HEAD_IMG)).convert_alpha()        
        self.emptyarea_img=pg.image.load(path.join(img_folder,"emptyarea.png")).convert_alpha()

        self.dead_img=pg.image.load(path.join(img_folder,DEAD_IMG)).convert_alpha()
        self.yes_img1=pg.image.load(path.join(img_folder,YES_IMG1)).convert_alpha()
        self.yes_img2=pg.image.load(path.join(img_folder,YES_IMG2)).convert_alpha()
        self.ofcourse_img1=pg.image.load(path.join(img_folder,OFCOURSE_IMG1)).convert_alpha()
        self.ofcourse_img2=pg.image.load(path.join(img_folder,OFCOURSE_IMG2)).convert_alpha()

        self.finish_img=pg.image.load(path.join(img_folder,FINISH_IMG)).convert_alpha()

        self.item_images={}
        for item in ITEM_IMAGES:
            self.item_images[item]=pg.image.load(path.join(img_folder,ITEM_IMAGES[item])).convert_alpha()
        
        self.bossbullet_imgs={}
        for img in BOSSBULLET_IMG:
            self.bossbullet_imgs[img]=pg.image.load(path.join(img_folder,BOSSBULLET_IMG[img])).convert_alpha()

        self.upgrade_imgs={}
        for img in UPGRADE_IMG:
            self.upgrade_imgs[img]=pg.image.load(path.join(img_folder,UPGRADE_IMG[img][0])).convert_alpha()
        self.upgrade_list=[]
        for option in self.upgrade_imgs.keys():
            self.upgrade_list.append(option)

    def new(self):
        game_folder=path.dirname(__file__)
        music_folder=path.join(game_folder,'snd')
        pg.mixer.music.load(path.join(music_folder,BACKGROUND_MUSIC)) 
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(loops=-1)
        #
        if self.level==1:
            self.map=self.map1
        if self.level==2:
            self.map=self.map2
        if self.level==3:
            self.map=self.map3
        if self.level==4:
            self.map=self.map4
            
        #初始化变量，并完成在开始新游戏时需要的所有设置
        self.all_sprites=pg.sprite.Group()
        
        
        self.walls=pg.sprite.Group()
        
        self.bullets=pg.sprite.Group()
        self.mobbullets=pg.sprite.Group()
        self.bossbullets=pg.sprite.Group()

        self.floors=pg.sprite.Group()

        
        self.guns=pg.sprite.Group()
        
        self.mobs=pg.sprite.Group()
        self.mobpigs=pg.sprite.Group()
        self.mobflowers=pg.sprite.Group()
        self.mobminers=pg.sprite.Group()
        self.boss=pg.sprite.Group()

        self.items=pg.sprite.Group()
        #简易地图编辑器
        for row,tiles in enumerate(self.map.data):#enumerate可以同时得到列表索引和变量
            for col,tile in enumerate(tiles):
                if tile=='1':#wall
                    Wall(self,col,row)
                if tile=='M':#mobpig
                    Floor(self,col,row)
                    Mob_Pig(self,col,row)
                if tile=='P':#player
                    Floor(self,col,row)
                    self.player.pos=vec(col,row)*TILESIZE
                    OLDGUN(self,self.player)
                if tile=='B':#mobblueflower
                    Floor(self,col,row)
                    Mob_Blueflower(self,col,row)
                if tile=='-':#地板
                    Floor(self,col,row)
                if tile=="G":#gate
                    Floor(self,col,row)
                    self.gate=Gate(self,col,row)
                if tile=="N":#mobminer
                    Floor(self,col,row)
                    Mob_Miner(self,col,row)
                if tile=="H":#health_potion
                    Floor(self,col,row)
                    Item(self,vec(col,row),'health')
                if tile=="E":#energy_potion
                    Floor(self,col,row)
                    Item(self,vec(col,row),'energy')
                if tile=="S":#stone
                    Floor(self,col,row)
                    self.stone=Stone(self,col,row)
                if tile=="*":#boss
                    Floor(self,col,row)
                    Boss(self,col,row)

        self.camera=Camera(self.map.width,self.map.height)

        
    def run(self):
        #游戏的主循环
        self.playing=True
        while self.playing:
            self.dt=self.clock.tick(FPS)/1000
            self.events()
            if not self.paused:
                self.update()
            self.draw()
            
            
    def quit(self):
        pg.quit()
        sys.exit()

        
    def update(self):
        #做个小人和boss抖动
        self.i+=1
        if self.player_tran==1 and self.i==15:
            self.player_img=self.player_img2
        if self.player_tran==-1 and self.i==15:
            self.player_img=self.player_img1

        if self.player_tran==1 and self.i==40 and self.level==4:
            self.jump.play()
            self.boss_img=self.boss_img2
        if self.player_tran==-1 and self.i==40 and self.level==4:
            self.boss_img=self.boss_img1
        if self.i==40:
            self.player_tran=-self.player_tran
            self.i=0
        
        #更新游戏循环
        self.players.update()
        self.all_sprites.update()
        self.guns.update()
        self.camera.update(self.player)

        #当你被怪撞到
        hits=pg.sprite.spritecollide(self.player,self.mobpigs,False,collide_hit_rect)
  
        for hit in hits:
            player_get_damage(self.player,MOBPIG_DAMAGE,self.hit_music)
            hit.vel=vec(0,0)
            if self.player.health<=0:
                self.playing=False
                #由于game over没做，把血回复一下，以免太奇怪
                ######################
                self.player.health=PLAYER_HEALTH
                self.player.shield=PLAYER_SHIELD
                self.player.energy=PLAYER_ENERGY
                ######################
                self.dead()
        if hits:
            self.player.pos += vec(MOBPIG_KNOCKBACK,0).rotate(-hits[0].rot)
            self.t=pg.time.get_ticks()
        if pg.time.get_ticks()-self.t>=SHIELD_CANRECOVER:
            shield_recover(self.player)
            self.t=pg.time.get_ticks()-SHIELD_RECOVERSPEED

        #当你被射到
        hits=pg.sprite.groupcollide(self.players,self.mobbullets,False,True)
        for hit in hits: 
            player_get_damage(self.player,MOBBULLET_DAMAGE,self.shoot_enemy)
            hit.vel=vec(0,0)
            if self.player.health<=0:
                self.playing=False
                #由于game over没做，把血回复一下，以免太奇怪
                ######################
                self.player.health=PLAYER_HEALTH
                self.player.shield=PLAYER_SHIELD
                self.player.energy=PLAYER_ENERGY
                ######################
                self.dead()
        if hits:
            self.t=pg.time.get_ticks()
        if pg.time.get_ticks()-self.t>=SHIELD_CANRECOVER:
            shield_recover(self.player)
            self.t=pg.time.get_ticks()-SHIELD_RECOVERSPEED
        
        #子弹打到小怪
        hits=pg.sprite.groupcollide(self.mobs,self.bullets,False,True)
        for hit in hits:
            self.shot_knight.play()
            critical_attack=random.randint(0,100)
            if critical_attack<self.player.critical_strike_rate:
                hit.health -=BULLET_DAMAGE*2
            else:
                hit.health -=BULLET_DAMAGE
            hit.vel=vec(0,0)
        number=0
        for mob in self.mobs:
            number+=1
            break
        
        #下一关
        mkeys=pg.key.get_pressed()
        if mkeys[pg.K_SPACE] and ((abs(self.gate.pos.y-self.player.pos.y)<=TILESIZE and\
                                    abs(self.gate.pos.x-self.player.pos.x)<=TILESIZE ) or\
                                    (abs(self.stone.pos.y-self.player.pos.y)<=TILESIZE and\
                                    abs(self.stone.pos.x-self.player.pos.x)<=TILESIZE )):
            if number==0:
                self.level+=1
                if self.level<=4:
                    self.upgrade()
                    self.new()
                if self.level==5:
                    playing=False
                    self.show_finish_screen()
            else:
                self.draw_text("You should destroy all enemies",20,WHITE,500,730)
                pg.display.flip()
                self.wait_for_key()
            
    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(0,y),(WIDTH,y))

        
    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        #self.draw_grid() #画线，编辑地图时看得清楚点
        for sprite in self.floors:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        
        for sprite in self.all_sprites:
            if sprite in self.mobs:#怪血条
                sprite.draw_health()
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        
        self.screen.blit(self.player.image,self.camera.apply(self.player))
        
        for sprite in self.guns:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
        self.screen.blit(self.healthbar_img,(0,0))
    
        #画角色血条
        draw_player_health(self.screen,28,9,self.player.health/PLAYER_HEALTH)
        self.draw_text("{0}/{1}".format(self.player.health,PLAYER_HEALTH),15,WHITE,80,8)
        if self.player.health<=0.2*PLAYER_HEALTH:
             self.screen.blit(self.red_img,(160,8))
        #画角色护盾
        draw_player_shield(self.screen,28,29,self.player.shield/PLAYER_SHIELD)
        self.draw_text("{0}/{1}".format(self.player.shield,PLAYER_SHIELD),15,WHITE,80,28)
        if self.player.shield<=0.2*PLAYER_SHIELD:
             self.screen.blit(self.grey_img,(160,28))
        #画角色能量
        draw_player_energy(self.screen,28,49,self.player.energy/PLAYER_ENERGY)
        self.draw_text("{0}/{1}".format(self.player.energy,PLAYER_ENERGY),15,WHITE,80,48)
        if self.player.energy<0.5*PLAYER_ENERGY:
             self.screen.blit(self.blue_img,(160,48))
        
        pg.display.flip()

    def draw_text(self,text,size,color,x,y):
        font=pg.font.Font(self.font_name,size)
        text_surface=font.render(text,True,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface,text_rect)
    
    def events(self):
        #在该循环获取所有事件
        for event in pg.event.get():
            if event.type==pg.QUIT:
                self.quit()
            '''
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_p:
                    self.paused=not self.paused

            '''

    def dead(self):
        #啊我死了
        self.screen.blit(self.dead_img,(0,0))
        self.screen.blit(self.yes_img1,(250,550))
        self.screen.blit(self.ofcourse_img1,(550,550))
        begin=False
        while not begin:
            self.clock.tick(FPS)
            mos_pos = pg.mouse.get_pos() #返回鼠标的坐标
            pressed_mouse=pg.mouse.get_pressed()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
            if 250<=mos_pos[0]<=450 and 550<=mos_pos[1]<=645:
                self.screen.blit(self.yes_img2,(250,550))
                if pressed_mouse[0]:
                    begin=True
            else:
                self.screen.blit(self.yes_img1,(250,550))
            
            if 550<=mos_pos[0]<=750 and 550<=mos_pos[1]<=645:
                self.screen.blit(self.ofcourse_img2,(550,550))
                if pressed_mouse[0]:
                    begin=True
            else:
                self.screen.blit(self.ofcourse_img1,(550,550))

            pg.display.flip()

    def show_start_screen(self):
        #开始界面
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(loops=-1)
        self.screen.blit(self.start_img1,(0,0))
        #self.start_sound.play()
        self.draw_text("Press a key to play",20,WHITE,500,730)
        pg.display.flip()
        self.wait_for_key()
        self.screen.blit(self.start_img2,(0,0))
        self.screen.blit(self.newgame2_img,(400,630))
        begin=False
        while not begin:
            self.clock.tick(FPS)
            mos_pos = pg.mouse.get_pos() #返回鼠标的坐标
            pressed_mouse=pg.mouse.get_pressed()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
            if 400<=mos_pos[0]<=600 and 630<=mos_pos[1]<=725:
                self.screen.blit(self.newgame1_img,(400,630))
                if pressed_mouse[0]:
                    begin=True
            else:
                self.screen.blit(self.newgame2_img,(400,630))
            pg.display.flip()
                
        pg.mixer.music.stop()

    def show_finish_screen(self):
        global PLAYER_HEALTH,PLAYER_SHIELD,PLAYER_ENERGY,HEALTH_POTION_RECOVER_AMOUNT,GUN_SPREAD
        #结束界面
        game_folder=path.dirname(__file__)
        music_folder=path.join(game_folder,'snd')
        pg.mixer.music.load(path.join(music_folder,FINISH_MUSIC)) 
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(loops=-1)
        self.screen.blit(self.finish_img,(0,0))
        self.screen.blit(self.newgame2_img,(400,630))
        begin=False
        while not begin:
            self.clock.tick(FPS)
            mos_pos = pg.mouse.get_pos() #返回鼠标的坐标
            pressed_mouse=pg.mouse.get_pressed()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
            if 400<=mos_pos[0]<=600 and 630<=mos_pos[1]<=725:
                self.screen.blit(self.newgame1_img,(400,630))
                if pressed_mouse[0]:
                    self.level=1
                    PLAYER_HEALTH=6
                    PLAYER_SHIELD=5
                    PLAYER_ENERGY=350
                    PLAYER_CRITICAL_STRIKE_RATE=0
                    BULLET_RATE=150
                    self.player.health=PLAYER_HEALTH
                    self.player.max_health=PLAYER_HEALTH
                    self.player.shield=PLAYER_SHIELD
                    self.player.energy=PLAYER_ENERGY
                    self.player.max_energy=PLAYER_ENERGY
                    self.recover_health_amount=HEALTH_POTION_RECOVER_AMOUNT
                    self.attack_spread=GUN_SPREAD
                    self.player.attack_rate=BULLET_RATE
                    self.critical_strike_rate=PLAYER_CRITICAL_STRIKE_RATE
                    self.new()
                    begin=True
                    playing=True
            else:
                self.screen.blit(self.newgame2_img,(400,630))
            pg.display.flip()


    def show_go_screen(self):
        pass

    def wait_for_key(self):
        waiting=True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    waiting=False
                    pg.quit()

                if event.type==pg.KEYUP:
                    waiting=False

    def upgrade(self):
        self.paused=True
        self.screen.fill(PAUSED_CLO)
        options=sample(self.upgrade_list,3)
        self.screen.blit(self.knight_head_img,(0,0))
        self.draw_text("choose an ability",100,WHITE,500,150)
        pg.display.flip()
        finish=False
        choose=-1
        option_pos_list=[]
        while not finish:
            self.clock.tick(FPS)
            flag=0
            mos_pos = pg.mouse.get_pos() #返回鼠标的坐标
            pressed_mouse=pg.mouse.get_pressed()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
            for row in range(3):
                self.screen.blit(self.upgrade_imgs[options[row]],(180+300*row,580))
                option_pos_list.append([180+300*row,580])
            for i in range(3):
                if option_pos_list[i][0]<=mos_pos[0]<=option_pos_list[i][0]+75 and \
                   option_pos_list[i][1]<=mos_pos[1]<=option_pos_list[i][1]+75 and \
                   pressed_mouse[0]:
                    flag=1
                    index=i
                    self.draw_text(UPGRADE_IMG[options[index]][1],30,WHITE,500,520)
                    break
                
            while flag:
                global PLAYER_HEALTH,PLAYER_SHIELD,PLAYER_ENERGY,HEALTH_POTION_RECOVER_AMOUNT,GUN_SPREAD,BULLET_RATE
                self.clock.tick(FPS)
                mos_pos = pg.mouse.get_pos() #返回鼠标的坐标
                pressed_mouse=pg.mouse.get_pressed()
                for event in pg.event.get():
                    if event.type==pg.QUIT:
                        pg.quit()
                for i in range(3):
                    if option_pos_list[i][0]<=mos_pos[0]<=option_pos_list[i][0]+75 and \
                       option_pos_list[i][1]<=mos_pos[1]<=option_pos_list[i][1]+75 and \
                       pressed_mouse[0]:
                        flag=1
                        index=i
                        self.screen.blit(self.emptyarea_img,(0,480))
                        pg.display.flip()
                        self.draw_text(UPGRADE_IMG[options[index]][1],30,WHITE,500,520)
                        break

                self.screen.blit(self.surebutton1_img,(450,660))
                if 400<=mos_pos[0]<=450+120 and 660<=mos_pos[1]<=660+95:
                    self.screen.blit(self.surebutton2_img,(450,660))
                    
                    if pressed_mouse[0]:
                    #各项升级放入其中
                        if options[index]=="HP_up":
                            PLAYER_HEALTH+=2
                            self.player.health+=2
                            self.player.max_health+=2
                        elif options[index]=="SHIELD_up":
                            PLAYER_SHIELD+=1
                            self.player.shield+=1
                        elif options[index]=="ENERGY_up":
                            PLAYER_ENERGY+=100
                            self.player.energy+=100
                            self.player.max_energy+=100
                        elif options[index]=="HEALTHPOTION_up":
                            self.player.recover_health_amount+=2
                        elif options[index]=="ACCURACY_up":
                            self.player.attack_spread=2
                            self.player.critical_strike_rate+=10
                        elif options[index]=="ATTACKRATE_up":
                            self.player.attack_rate-=75
                        finish=True
                        flag=False
                        self.upgrade_list.remove(options[index])
                        self.paused=False
     
                else:
                    self.screen.blit(self.surebutton1_img,(450,660))
                pg.display.flip()
            
            pg.display.flip()
                    

#创建游戏
g=Game()
g.show_start_screen()
playing=True
while playing:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()
