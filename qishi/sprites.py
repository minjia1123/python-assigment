import pygame as pg
from settings import *
from random import uniform,choice
import random
from Map_ import *
import math
from os import path
from itertools import chain
vec=pg.math.Vector2#维克托还是香啊

global PLAYER_HEALTH,PLAYER_SHIELD,PLAYER_ENERGY,HEALTH_POTION_RECOVER_AMOUNT,GUN_SPREAD,BULLET_RATE

def floder_music():
    pg.mixer.init()
    game_folder=path.dirname(__file__)
    music_folder=path.join(game_folder,'snd')
    SHOOT_KNIGHT = pg.mixer.Sound(path.join(music_folder, 'shoot_knight.wav'))
    return SHOOT_KNIGHT

def collide_with_walls(sprite,group,dir):
    #碰撞检测它lei了
    if dir=='x':
        hits=pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
        if hits:
            if hits[0].rect.centerx>sprite.hit_rect.centerx:
                sprite.pos.x=hits[0].rect.left-sprite.hit_rect.width/2
            if hits[0].rect.centerx<sprite.hit_rect.centerx:
                sprite.pos.x=hits[0].rect.right+sprite.hit_rect.width/2
            sprite.vel.x=0
            sprite.hit_rect.centerx=sprite.pos.x
    if dir=='y':
        hits=pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
        if hits:
            if hits[0].rect.centery>sprite.hit_rect.centery:
                sprite.pos.y=hits[0].rect.top-sprite.hit_rect.height/2
            if hits[0].rect.centery<sprite.hit_rect.centery:
                sprite.pos.y=hits[0].rect.bottom+sprite.hit_rect.height/2
            sprite.vel.y=0
            sprite.hit_rect.centery=sprite.pos.y


class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.players
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.player_img
        self.rect=self.image.get_rect()
        self.hit_rect=PLAYER_HIT_RECT
        self.hit_rect.center=self.rect.center
        self.vel=vec(0,0)
        #设置初始位置到所需点(当然实际在update里生成)
        self.pos=vec(x,y)*TILESIZE
        self.direction=True#1代表右，0代表左
        self.gunpos=(self.pos.x+10,self.pos.y+4)
        self.last_shot=0
        self.health=PLAYER_HEALTH
        self.max_health=PLAYER_HEALTH
        self.shield=PLAYER_SHIELD
        self.energy=PLAYER_ENERGY
        self.max_energy=PLAYER_ENERGY
        self.recover_health_amount=HEALTH_POTION_RECOVER_AMOUNT #生命药水专属
        self.dir_angle=0
        self.damaged=False
        self.invincible_time=-PLAYER_INVINCIBLE_TIME
        self.critical_strike_rate=PLAYER_CRITICAL_STRIKE_RATE
        self.attack_rate=BULLET_RATE
        self.attack_spread=GUN_SPREAD
      

    def get_keys(self):
        self.vel=vec(0,0)
        keys=pg.key.get_pressed()
        #移动按键的设置
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.vel.x=-PLAYER_SPEED
            self.direction=False
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.vel.x=PLAYER_SPEED
            self.direction=True
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.vel.y=-PLAYER_SPEED
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.vel.y=PLAYER_SPEED
        #你以为你两个按键一起按就能跑的更快了？
        if self.vel.x!=0 and self.vel.y!=0:
            self.vel*=0.7071

        #把鼠标事件也加入,shoot
        mos_pos = pg.mouse.get_pos() #返回鼠标的坐标
        pressed_mouse=pg.mouse.get_pressed()
        dplayer_pos=vec(self.pos.x+self.game.camera.camera.topleft[0],self.pos.y+self.game.camera.camera.topleft[1])
        self.dir_angle=(mos_pos-dplayer_pos).angle_to(vec(1,0))
        dir=vec(1,0).rotate(-self.dir_angle)
        if pressed_mouse[0]:
                now=pg.time.get_ticks()
                if now-self.last_shot>BULLET_RATE:
                    self.last_shot=now
                    if self.energy>0:
                        Bullet(self.game,self.gunpos,dir)
                        self.energy-=1
                    
    def hit(self):
        self.damaged= True
        self.damage_alpha=chain(DAMAGE_ALPHA*3)
        
    def update(self):
        self.get_keys()
        if not self.direction:
            self.image=pg.transform.flip(self.game.player_img,True,False)
        else:
            self.image=pg.transform.flip(self.game.player_img,False,False)            
        self.pos+=self.vel*self.game.dt
        self.hit_rect.centerx=self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.hit_rect.centery=self.pos.y
        collide_with_walls(self,self.game.walls,'y')
        self.rect.center=self.hit_rect.center
        if not self.direction:
            self.gunpos=(self.pos.x-10,self.pos.y+4)
        else:
            self.gunpos=(self.pos.x+10,self.pos.y+4)
        if self.damaged:
            try:
                self.image.fill((255,255,255,next(self.damage_alpha)),special_flags=pg.BLEND_RGBA_MULT)
            except:
                self.damaged=False
    

class Mob_Pig(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.mobpigs,game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.mobpig_img.copy()#注意！copy!
        self.rect=self.image.get_rect()
        self.hit_rect=MOB_HIT_RECT.copy()
        self.hit_rect.center=self.rect.center
        self.pos=vec(x,y)*TILESIZE
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.rect.center=self.pos
        self.rot=0
        self.health=MOBPIG_HEALTH
        
    def avoid_mobs(self):
        for mob in self.game.mobpigs:
            if mob!=self:
                dist=self.pos-mob.pos
                if 0<dist.length()<AVOID_RADIUS:
                    self.acc+=dist.normalize()
    
    def update(self):
        self.rect=self.image.get_rect()
        self.rect.center=self.pos
        self.image=pg.transform.rotate(self.game.mobpig_img,0)#如果不加这一句的话，血条会重叠覆盖
        if self.chase():
            self.rot=(self.game.player.pos-self.pos).angle_to(vec(1,0))
            self.acc=vec(1,0).rotate(-self.rot)
            self.avoid_mobs()
            self.acc.scale_to_length(MOBPIG_SPEED)
            self.acc+=self.vel*(-1)
            self.vel+=self.acc*self.game.dt
            self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2
        self.hit_rect.centerx=self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.hit_rect.centery=self.pos.y
        collide_with_walls(self,self.game.walls,'y')
        if self.game.player.pos.x<self.pos.x:
            self.image=pg.transform.flip(self.game.mobpig_img,True,False)
        else:
            self.image=pg.transform.flip(self.game.mobpig_img,False,False)
        self.rect.center=self.hit_rect.center
        if self.health<=0:
            self.kill()
            
    def draw_health(self):#血条
            if self.health>MOBPIG_HEALTH*0.6:
                col=GREEN
            elif self.health>MOBPIG_HEALTH*0.3:
                col=YELLOW
            else:
                col=RED
            width1=int(self.rect.width*self.health/MOBPIG_HEALTH)
            self.health_bar=pg.Rect(0,0,width1,2)
            if self.health<MOBPIG_HEALTH:
                pg.draw.rect(self.image,col,self.health_bar)

    def chase(self):
        m,n=self.pos+self.game.camera.camera.topleft
        if 0<m<WIDTH and 0<n<HEIGHT:
            return True

class Mob_Miner(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.mobminers,game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.mobminer_img.copy()#注意！copy!
        self.rect=self.image.get_rect()
        self.hit_rect=MOB_HIT_RECT.copy()
        self.hit_rect.center=self.rect.center
        self.pos=vec(x,y)*TILESIZE
        self.health=MINER_HEALTH
        self.attacktiming=pg.time.get_ticks()
        self.movtiming=pg.time.get_ticks()
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.rand=random.randint(5,15)
        self.rot1=random.randint(0,360)
        if self.rot1==90 or self.rot1==270:
            self.rot1+=1
    
    def avoid_mobs(self):
        for mob in self.game.mobminers:
            if mob!=self:
                dist=self.pos-mob.pos
                if 0<dist.length()<AVOID_RADIUS :
                    self.acc+=dist.normalize()
        dist=self.pos-self.game.player.pos
        if 0<dist.length()<AVOID_PLAYER_RADIUS:
                    self.acc+=dist.normalize()
        
        

    def update(self):
        self.rect=self.image.get_rect()
        self.rect.center=self.pos
        self.image=pg.transform.rotate(self.game.mobminer_img,0)#如果不加这一句的话，血条会重叠覆盖
        self.rot=(self.game.player.pos-self.pos).angle_to(vec(1,0))
        self.acc=vec(1,0).rotate(-self.rot1)
        self.avoid_mobs()
        self.acc.scale_to_length(MINER_SPEED)
        if pg.time.get_ticks()-self.movtiming>=4000:
            self.rot1=random.randint(0,360)
            self.rand=random.randint(5,15)
            self.movetiming=pg.time.get_ticks()
        if self.fire():
            self.acc.scale_to_length(MINER_SPEED)
            self.acc+=self.vel*(-1)
            self.vel+=self.acc*self.game.dt*self.rand
            self.movetiming=pg.time.get_ticks
            self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2
           
        self.hit_rect.centerx=self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.hit_rect.centery=self.pos.y
        collide_with_walls(self,self.game.walls,'y')
        if self.game.player.pos.x<self.pos.x:
            self.image=pg.transform.flip(self.game.mobminer_img,True,False)
        else:
            self.image=pg.transform.flip(self.game.mobminer_img,False,False)
        if pg.time.get_ticks()-self.attacktiming>=MINERATTACK_RATE and self.fire():
            self.attacktiming=pg.time.get_ticks()
            Flower_Bullet(self.game,self.pos,vec(1,0).rotate(-self.rot))#嗯，小花的子弹(我就是懒得找素材)
            
        self.rect.center=self.hit_rect.center
        if self.health<=0:
            self.kill()

    def draw_health(self):#血条
        if self.health>MINER_HEALTH*0.6:
            col=GREEN
        elif self.health>MINER_HEALTH*0.3:
            col=YELLOW
        else:
            col=RED
        width1=int(self.rect.width*self.health/MINER_HEALTH)
        self.health_bar=pg.Rect(0,0,width1,2)
        if self.health<MINER_HEALTH:
            pg.draw.rect(self.image,col,self.health_bar)

    def fire(self):
        m,n=self.pos+self.game.camera.camera.topleft
        if 0<m<WIDTH and 0<n<HEIGHT:
            return True


class Mob_Blueflower(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.mobflowers,game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.mobflower_img.copy()#注意！copy!
        self.rect=self.image.get_rect()
        self.pos=vec(x,y)*TILESIZE
        self.health=MOBFLOWER_HEALTH
        self.attacktiming=pg.time.get_ticks()
        
        


    def update(self):
        self.rect=self.image.get_rect()
        self.rect.center=self.pos
        self.image=pg.transform.rotate(self.game.mobflower_img,0)#如果不加这一句的话，血条会重叠覆盖
        if pg.time.get_ticks()-self.attacktiming>=MOBATTACK_RATE and self.fire():
            self.attacktiming=pg.time.get_ticks()
            for i in range(1,13):
                Flower_Bullet(self.game,self.pos,vec(1,0).rotate(30*(i-1)))

        if self.health<=0:
            self.kill()

    def draw_health(self):#血条
            if self.health>MOBFLOWER_HEALTH*0.6:
                col=GREEN
            elif self.health>MOBFLOWER_HEALTH*0.3:
                col=YELLOW
            else:
                col=RED
            width1=int(self.rect.width*self.health/MOBFLOWER_HEALTH)
            self.health_bar=pg.Rect(0,0,width1,2)
            if self.health<MOBFLOWER_HEALTH:
                pg.draw.rect(self.image,col,self.health_bar)

    def fire(self):
        m,n=self.pos+self.game.camera.camera.topleft
        if 0<m<WIDTH and 0<n<HEIGHT:
            return True

class Boss(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.boss,game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.boss_img.copy()#注意！copy!
        self.rect=self.image.get_rect()
        self.direction=True
        self.pos=vec(x,y)*TILESIZE
        self.vel=vec(0,0)
        self.health=BOSS_HEALTH
        self.attacktiming1=pg.time.get_ticks()
        self.attacktiming1_1=pg.time.get_ticks()
        self.attackflag1=False
        self.attackflag2=False
        self.flag1=0
        self.flag2=0
        self.attacktiming2=pg.time.get_ticks()
        self.attacktiming3=pg.time.get_ticks()
        self.attacktiming3_1=pg.time.get_ticks()
        self.damaged=False
                        
    def update(self):
        if not self.direction:
            self.image=pg.transform.flip(self.game.boss_img,True,False)
        else:
            self.image=pg.transform.flip(self.game.boss_img,False,False)
        self.pos+=self.vel*self.game.dt
        self.rect=self.image.get_rect()
        self.rect.center=self.pos
        if self.health<0:
            self.kill()
        if self.health<=BOSS_HEALTH:
            if pg.time.get_ticks()-self.attacktiming1>=BOSSATTACK_RATE:
                self.attacktiming1=pg.time.get_ticks()
                self.attackflag1=True
            if self.attackflag1:
                if pg.time.get_ticks()-self.attacktiming1_1>=BOSSATTACK_RATE1:
                    self.attacktiming1_1=pg.time.get_ticks()
                    self.flag1+=1
                    for i in range(4):
                        for j in range(1,11):
                            Boss_Bullet(self.game,self.pos,'boss_bullet1',vec(1,0).rotate(80*i+9*j),80*i+9*j)
                    if self.flag1==5:
                        self.flag1=0
                        self.attackflag1=False
                        
        if self.health<=BOSS_HEALTH*0.8:
            if pg.time.get_ticks()-self.attacktiming2>=BOSSATTACK_RATE2:
                self.attacktiming2=pg.time.get_ticks()
                for i in range(1,11):
                    Boss_Bullet(self.game,self.pos,'boss_bullet4',vec(1,0).rotate(30*i),30*i)

        if self.health<=BOSS_HEALTH*0.6:
            if pg.time.get_ticks()-self.attacktiming3>=BOSSATTACK_RATE3:
                self.attacktiming3=pg.time.get_ticks()
                self.attackflag2=True
            if self.attackflag2:
                if pg.time.get_ticks()-self.attacktiming3_1>=BOSSATTACK_RATE3_1:
                    self.attacktiming3_1=pg.time.get_ticks()
                    self.flag2+=1
                    for i in range(1,11):
                        for j in range(8):
                          Boss_Bullet(self.game,self.pos,'boss_bullet2',vec(1,0).rotate(36*(i-1)+4*j),36*(i-1)+4*j)
                    if self.flag2==6:
                        self.flag2=0
                        self.attackflag2=False
                    
        
        if self.health<=BOSS_HEALTH*0.4:
            if pg.time.get_ticks()-self.attacktiming3>=BOSSATTACK_RATE*0.05:
                self.attacktiming3=pg.time.get_ticks()
                for i in range(1,21):
                        Boss_Bullet(self.game,self.pos,'boss_bullet3',vec(1,0).rotate(20*(i-1)),20*(i-1))
                   
        
    def draw_health(self):
        self.game.screen.blit(self.game.boss_health_bar_img,(200,30))
        pct=self.health/BOSS_HEALTH
        if pct<0:
            pct=0
        BAR_LENGTH=600
        BAR_HEIGHT=24
        fill=pct*BAR_LENGTH
        outline_rect=pg.Rect(200,36,BAR_LENGTH,BAR_HEIGHT)
        fill_rect=pg.Rect(200,36,fill,BAR_HEIGHT)
        col=BOSS_BARCLO
        pg.draw.rect(self.game.screen,col,fill_rect)
        pg.draw.rect(self.game.screen,BLACK,outline_rect,1)

            
        
class Boss_Bullet(pg.sprite.Sprite):
    def __init__(self,game,pos,type,dir,angle):
        self.groups=game.all_sprites,game.bossbullets,game.mobbullets
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.type=type
        self.angle=angle
        self.dir=dir
        self.image=pg.transform.rotate(game.bossbullet_imgs[type],-angle)
        self.rect=self.image.get_rect()
        self.pos=vec(pos)
        self.rect.center=pos
        self.vel=dir * BOSSBULLET_SPEED[type]
        self.spawn_time=pg.time.get_ticks()
        self.timing=pg.time.get_ticks()
        
    def update(self):
        if self.type=='boss_bullet1':
            self.pos+=self.vel*self.game.dt
            
        if self.type=='boss_bullet2':
            self.pos+=self.vel*self.game.dt
            if pg.time.get_ticks()-self.timing>=3000:
                self.rot=(self.vel).angle_to(vec(1,0))+100
                self.acc=vec(1,0).rotate(-self.rot)
                self.acc.scale_to_length(BOSSBULLET_SPEED[self.type])
                self.vel+=self.acc*self.game.dt
                self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2
        
        if self.type=='boss_bullet3':
            self.rot=(self.vel).angle_to(vec(1,0))+100
            self.acc=vec(1,0).rotate(-self.rot)
            self.acc.scale_to_length(BOSSBULLET_SPEED[self.type]*0.5)
            self.vel+=self.acc*self.game.dt
            self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2

        if self.type=='boss_bullet4':
            self.rot=(self.game.player.pos-self.pos).angle_to(vec(1,0))
            self.acc=vec(1,0).rotate(-self.rot)
            self.image=pg.transform.rotate(self.game.bossbullet_imgs[self.type],self.rot)
            self.acc.scale_to_length(BOSSBULLET_SPEED[self.type])
            self.acc+=self.vel*(-1)
            self.vel+=self.acc*self.game.dt
            self.pos+=self.vel*self.game.dt+0.5*self.acc*self.game.dt**2


        
        
        self.rect.center=self.pos
        if pg.sprite.spritecollideany(self,self.game.walls):#这样子弹就不穿墙啦
            self.kill()
        if pg.time.get_ticks()-self.spawn_time>BOSSBULLET_LIFETIME:#子弹寿命当然有限
            self.kill()
                
class Flower_Bullet(pg.sprite.Sprite):
    def __init__(self,game,pos,dir):
        self.groups=game.all_sprites,game.mobbullets
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.mobbullet_img.copy()
        self.rect=self.image.get_rect()
        self.pos=vec(pos)
        self.rect.center=pos
        self.vel=dir.rotate(0) * MOBBULLET_SPEED
        self.spawn_time=pg.time.get_ticks()

    def update(self):
        self.pos+=self.vel*self.game.dt
        self.rect.center=self.pos
        if pg.sprite.spritecollideany(self,self.game.walls):#这样子弹就不穿墙啦
            self.kill()
        if pg.time.get_ticks()-self.spawn_time>MOBBULLET_LIFETIME:#子弹寿命当然有限
            self.kill()

class Wall(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites,game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.wall_img
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x=self.x*TILESIZE
        self.rect.y=self.y*TILESIZE

SHOOT_KNIGHT=floder_music()
class Bullet(pg.sprite.Sprite):

    def __init__(self,game,pos,dir):
        SHOOT_KNIGHT.play()
        self.groups=game.all_sprites,game.bullets
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.bullet_img
        self.rect=self.image.get_rect()
        self.pos=vec(pos)
        self.rect.center=pos
        spread=uniform(-self.game.player.attack_spread,self.game.player.attack_spread)
        self.vel=dir.rotate(spread) * BULLET_SPEED
        self.spawn_time=pg.time.get_ticks()


    def update(self):
        self.pos+=self.vel*self.game.dt
        self.rect.center=self.pos
        if pg.sprite.spritecollideany(self,self.game.walls):#这样子弹就不穿墙啦
            self.kill()
        if pg.time.get_ticks()-self.spawn_time>BULLET_LIFETIME:#子弹寿命当然有限
            self.kill()

class Floor(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.floors
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        i=random.randint(1,6)
        if i==1:
            self.image=game.floor_img1
        elif i==2:
            self.image=game.floor_img2
        elif i==3:
            self.image=game.floor_img3
        elif i==4:
            self.image=game.floor_img4
        elif i==5:
            self.image=game.floor_img5
        elif i==6:
            self.image=game.floor_img6
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x=self.x*TILESIZE
        self.rect.y=self.y*TILESIZE

class OLDGUN(pg.sprite.Sprite):
    def __init__(self,game,sprite):
        self.groups=game.guns
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.sprite=sprite
        self.image=game.gun_img
        self.rect=self.image.get_rect()
        self.pos=sprite.pos

    def update(self):
        self.pos=self.sprite.gunpos
        self.rect=self.image.get_rect()
        self.rect.center=self.pos
        if not self.sprite.direction:
            self.image=pg.transform.flip(self.game.gun_img,True,False)
        else:
            self.image=pg.transform.flip(self.game.gun_img,False,False)      
        self.image=pg.transform.rotate(self.game.gun_img,self.sprite.dir_angle)

class Gate(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.gate_img
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x=self.x*TILESIZE
        self.rect.y=self.y*TILESIZE
        self.pos=vec(self.rect.x,self.rect.y)

class Stone(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.stone_img
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x=self.x*TILESIZE
        self.rect.y=self.y*TILESIZE
        self.pos=vec(self.rect.x,self.rect.y)

class Item(pg.sprite.Sprite):
    def __init__(self,game,pos,type):
        self.groups=game.all_sprites,game.items
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.item_images[type]
        self.rect=self.image.get_rect()
        self.type=type
        self.rect.x=pos.x*TILESIZE
        self.rect.y=pos.y*TILESIZE
        self.recover_health=self.game.player.recover_health_amount #生命药水专属
        self.recover_energy=ENERGY_POTION_RECOVER_AMOUNT #能量药水专属

    def update(self):
        hits=pg.sprite.collide_rect(self.game.player,self)
        if hits:
            keys=pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                if self.type=="health":
                    if self.game.player.health+self.recover_health<=self.game.player.max_health:
                        self.game.player.health+=self.recover_health
                    else:
                        self.game.player.health=self.game.player.max_health
                elif self.type=="energy":
                    if self.game.player.energy+self.recover_energy<=self.game.player.max_energy:
                        self.game.player.energy+=self.recover_energy
                    else:
                        self.game.player.energy=self.game.player.max_energy

                self.kill()
            
            
