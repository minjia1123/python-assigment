import pygame as pg
vec=pg.math.Vector2
#颜色面板
WHITE=(255,255,255)
BLACK=(0,0,0)
DARKGREY=(40,40,40)
LIGHTGREY=(100,100,100)
GREEN=(0,255,0)
RED=(255,0,0)
YELLOW=(255,255,0)
BROWN=(106,55,5)
LIGHTBLUE=(137, 207, 240)
SHIELD_CLO=(129,129,129)
ENERGY_CLO=(31,114,196)
BOSS_BARCLO=(243,53,61)
PAUSED_CLO=(33,34,36)

#游戏界面
START_IMG1="start_img1.png"
START_IMG2="start_img2.png"

#音乐

START_MUSIC="start_music.mp3"
BACKGROUND_MUSIC = "background.mp3"
FINISH_MUSIC="finish_music.mp3"
HIT_MUSIC='hit.wav'
SHOOT_ENEMY='shoot_enemy.wav'
SHOOT_KNIGHT='shoot_knight.wav'
SHOT_KNIGHT='shot_knight.wav' 
JUMP_BOSS='jump.wav'


#游戏基本设置
WIDTH=1024#16*64 or 32*32
HEIGHT=768#16*48 or 32*24
FPS=60
TITLE="SOUL KNIGHT"
BGCOLOR=BLACK

TILESIZE=36
GRIWIDTH=WIDTH/TILESIZE
GRIHEIGHT=HEIGHT/TILESIZE

HEALTH_BAR_IMG="PLAYER_HEALTH_BAR.png"

#角色设置
PLAYER_HEALTH=6
PLAYER_SHIELD=5
PLAYER_ENERGY=350
SHIELD_RECOVERSPEED=1500
SHIELD_CANRECOVER=3000
PLAYER_SPEED=300
PLAYER_ROT_SPEED=250
PLAYER_IMG1='knight1.png'
PLAYER_IMG2='knight2.png'
PLAYER_HIT_RECT=pg.Rect(0,0,35,35)
PLAYER_INVINCIBLE_TIME=1000
PLAYER_CRITICAL_STRIKE_RATE=0

#墙的设置
WALL_IMG="wall2.png"

###################################### 
#Mob_Pig设置
MOBPIG_IMG="mobpig.png"
MOBPIG_SPEED=150
MOB_HIT_RECT=pg.Rect(0,0,30,30)
MOBPIG_DAMAGE=3
MOBPIG_HEALTH=10
MOBPIG_KNOCKBACK=20
AVOID_RADIUS=75#

#Mob_Miner设置
MINER_IMG="mob_miner.png"
MINER_SPEED=125
MINERATTACK_RATE=3000

#射子弹，所以不设置伤害了
MINER_HEALTH=15
AVOID_RADIUS=50#
AVOID_PLAYER_RADIUS=125

#Mob_Blueflower设置
MOBFLOWER_IMG="mob_blueflower.png"
MOBBULLET_IMG="mobflower_bullet.png"
MOBFLOWER_HEALTH=18
MOBBULLET_SPEED=100
MOBBULLET_DAMAGE=4
MOBBULLET_LIFETIME=8000
MOBATTACK_RATE=3000

#boss设置
BOSS_HEALTH=500
BOSS_IMG1="boss3.png"
BOSS_IMG2="boss2.png"
BOSSBULLET_IMG={'boss_bullet1':'boss_bullet1.png',
                'boss_bullet2':'boss_bullet2.png',
                'boss_bullet3':'boss_bullet3.png',
                'boss_bullet4':'boss_bullet4.png'}
BOSS_DAMAGE=3
BOSSATTACK_RATE=6000
BOSSATTACK_RATE1=500
BOSSATTACK_RATE2=5000
BOSSATTACK_RATE3=10000
BOSSATTACK_RATE3_1=750
BOSSBULLET_LIFETIME=7000
BOSSBULLET_SPEED={'boss_bullet1':150,
                  'boss_bullet2':300,
                  'boss_bullet3':300,
                  'boss_bullet4':400}

BOSS_HEALTH_BAR_IMG="boss_health_bar.png"


#####################################
#射击设置
BULLET_IMG="bullet1.png"
BULLET_SPEED=500
BULLET_LIFETIME=3000
BULLET_RATE=150
KICKBACK=200 #后座力，或许会有用呢，暂时用不上(太烦了)。。。
GUN_SPREAD=5#稍微降低武器准度
BULLET_DAMAGE=3

#地板
FLOOR_IMG1="floor1.png"
FLOOR_IMG2="floor2.png"
FLOOR_IMG3="floor3.png"
FLOOR_IMG4="floor4.png"
FLOOR_IMG5="floor5.png"
FLOOR_IMG6="floor6.png"

#枪械设置
GUN_IMG="oldgun.png"

#传送门
GATE_IMG="GATE1.png"
STONE_IMG="STONE.png"

#地图


#可捡拾物品
ITEM_IMAGES={'health':'health_potion.png','energy':'energy_potion.png'}
HEALTH_POTION_RECOVER_AMOUNT=2
ENERGY_POTION_RECOVER_AMOUNT=80

#文本设置
FONT_NAME='arial'

#升级选项
UPGRADE_IMG={"HP_up":["HP_up.png","max HP+2"],
             "SHIELD_up":["SHIELD_up.png","max shield+1"],
             "ENERGY_up":["ENERGY_up.png","max energy+100"],
             "HEALTHPOTION_up":["healthpotion_up.png","health potion could recover more HP"],
             "ACCURACY_up":["crtical strike and accurate shoot .png","improve your shooting accracy and also a rate of crtical strike"],
             "ATTACKRATE_up":["attackrate_up.png","faster shooting speed"]
            }

#其他奇怪的东西
RED_IMG="red.png"
GREY_IMG="grey.png"
BLUE_IMG="blue.png"
NEWGAME1_IMG="newgame1.PNG"
NEWGAME2_IMG="newgame2.PNG"
FINISH_IMG="finish.png"
DAMAGE_ALPHA=[i for i in range(0,255,25)]

KNIGHT_HEAD_IMG="knight_head.png"
SUREBUTTON1_IMG="sure_button1.png"
SUREBUTTON2_IMG="sure_button2.png"

DEAD_IMG="dead.png"
YES_IMG1="Yes1.png"
YES_IMG2="Yes2.png"
OFCOURSE_IMG1="OfCourse1.png"
OFCOURSE_IMG2="OfCourse2.png"