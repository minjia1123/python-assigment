from math import *
import numpy as np
import os
import random
import pygame
import sys
from pygame.locals import *
import time
#全局变量（图形学表现）
REC_SIZE = 50
CHESS_RADIUS = REC_SIZE//2 - 2
CHESS_LEN = 15 #15X15 五子棋盘
MAP_WIDTH = CHESS_LEN * REC_SIZE
MAP_HEIGHT = CHESS_LEN * REC_SIZE
INFO_WIDTH = 200
SCREEN_WIDTH = MAP_WIDTH + INFO_WIDTH
SCREEN_HEIGHT = MAP_HEIGHT

#map类用来保存五子棋的数据和提供绘制五子棋的函数，self.map 初始化为15 * 15的二维数组，表示棋盘， 数组中的值：0表示为空， 1为黑子下的棋， 2为白子下的棋。 
    
class Map:
    def __init__(self,width,height):
        self.width=width#这个是具体的值
        self.height=height#这个是具体的值
        self.map=[[0 for x in range(self.width)]for y in range(self.height)]
    
    def reset(self):#清空棋盘，把坐标值置为0（重新开始？）
        for y in range(self.height):
            for x in range(self.width):
                self.map[y][x]=0
        self.steps=[]
        
    def MapPosToIndex(self, map_x, map_y):#计算棋盘坐标
        if (map_x%REC_SIZE)<REC_SIZE/5 or (map_x%REC_SIZE)>REC_SIZE*4/5 or (map_y%REC_SIZE)<REC_SIZE/5 or (map_y%REC_SIZE)>REC_SIZE*4/5:
            return
        else:
            x=map_x//REC_SIZE
            y=map_y//REC_SIZE
            if 0<=x<=14 and 0<=y<=14:
                return (x,y)
            else: return    

#主界面五子棋棋盘使用pygame来实现界面，主要有两个函数，一个是绘制棋盘，一个是绘制棋子。 drawBackground **函数分别绘制15条水平和竖直的线，正中两条线加粗，然后在5个点上加上小正方形。
    def drawBackground(self,screen,flag): #这个函数确定了没问题
        backgroundcolor=(247, 238, 214) #浅黄色背景
        color=(0,0,0) #用黑线来画棋盘
        pygame.draw.rect(screen, backgroundcolor, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        for y in range(self.height):
            #画垂线
            start_pos,end_pos=(REC_SIZE//2,REC_SIZE//2+REC_SIZE*y),(MAP_WIDTH-REC_SIZE//2,REC_SIZE//2+REC_SIZE*y)
            if y==(self.height)//2: #棋盘二分之一处为粗线
                width=2
            else:
                width=1
            pygame.draw.line(screen,color,start_pos,end_pos,width)
        
        for x in range(self.width):
            #画水平线
            start_pos,end_pos=(REC_SIZE//2 + REC_SIZE * x, REC_SIZE//2), (REC_SIZE//2 + REC_SIZE * x, MAP_HEIGHT - REC_SIZE//2)
            if x==(self.width)//2:
                width=2
            else:
                width=1
            pygame.draw.line(screen,color,start_pos,end_pos,width)
            
            rec_size=8
            pos=[(3,3),(11,3),(3,11),(11,11),(7,7)]
        for (x,y) in pos:
            pygame.draw.rect(screen,color,(REC_SIZE//2+x*REC_SIZE-rec_size//2,REC_SIZE//2+y*REC_SIZE-rec_size//2,rec_size,rec_size))#在五个点上加上小正方形      
        
        
        
        
         #(158, 217, 157)
        
        def showbutton(screen, text, location_x, locaiton_y, height,x=158,y=217,z=157):#展示按钮上面的字符
                    font = pygame.font.SysFont(None, height)
                    font_image = font.render(text, True, (255, 255, 255), (x, y,z))
                    font_image_rect = font_image.get_rect()
                    font_image_rect.x = location_x
                    font_image_rect.y = locaiton_y
                    screen.blit(font_image, font_image_rect)
        
                        
        if flag==0:
            colorbutton=(158, 217, 157)
            rec_size_x=150
            rec_size_y=50
            pos=[(15,1),(15,3),(15,5),(15,7)]
            for (x,y) in pos:
                pygame.draw.rect(screen,colorbutton,(REC_SIZE//2+x*REC_SIZE-rec_size//2,REC_SIZE//2+y*REC_SIZE-rec_size//2,rec_size_x,rec_size_y))#画出按钮      
            
            str1="ONE PLAYER"
            str2="TWO PLAYERS"
            str3="GIVE UP"
            str4="RESTART"
            showbutton(screen, str1, MAP_WIDTH + 32, SCREEN_HEIGHT-662, 30)       #调整了下字符串的位置，使其看上去更加对齐
            showbutton(screen, str2, MAP_WIDTH + 24, SCREEN_HEIGHT-562, 30)
            showbutton(screen, str3, MAP_WIDTH + 55, SCREEN_HEIGHT-462, 30)
            showbutton(screen, str4, MAP_WIDTH + 51, SCREEN_HEIGHT-362, 30)
        else:
            colorbutton1=(64, 67, 230)
            colorbutton2=(230, 67, 64)
            colorbutton3=(158, 217, 157)
            rec_size_x=150
            rec_size_y=50
            pos=[(15,1)]
            for (x,y) in pos:
                pygame.draw.rect(screen,colorbutton1,(REC_SIZE//2+x*REC_SIZE-rec_size//2,REC_SIZE//2+y*REC_SIZE-rec_size//2,rec_size_x,rec_size_y))#画出按钮   
            pos=[(15,3)]
            for (x,y) in pos:
                pygame.draw.rect(screen,colorbutton2,(REC_SIZE//2+x*REC_SIZE-rec_size//2,REC_SIZE//2+y*REC_SIZE-rec_size//2,rec_size_x,rec_size_y))#画出按钮   
            pos=[(15,5),(15,7)]
            for (x,y) in pos:
                pygame.draw.rect(screen,colorbutton3,(REC_SIZE//2+x*REC_SIZE-rec_size//2,REC_SIZE//2+y*REC_SIZE-rec_size//2,rec_size_x,rec_size_y))#画出按钮    
            str1="NORMAL"
            str2="HARD"
            str3="GIVE UP"
            str4="RESTART"
            showbutton(screen, str1, MAP_WIDTH + 56, SCREEN_HEIGHT-662, 30,64, 67, 230)       #调整了下字符串的位置，使其看上去更加对齐
            showbutton(screen, str2, MAP_WIDTH + 66, SCREEN_HEIGHT-562, 30,230, 67, 64)
            showbutton(screen, str3, MAP_WIDTH + 55, SCREEN_HEIGHT-462, 30)
            showbutton(screen, str4, MAP_WIDTH + 51, SCREEN_HEIGHT-362, 30)

        

    def drawChess(self, screen, color,chepos): #在下的位置画出棋子
        player_one = (88, 87, 86)
        player_two = (255, 251, 240)
        if color==1: #(当传入的参数为1时，代表黑色)
            drawcolor=player_one
        else: #白色
            drawcolor=player_two
        map_x, map_y= chepos[0],chepos[1]
        truex=(REC_SIZE//2+map_x*REC_SIZE)
        truey=(REC_SIZE//2+map_y*REC_SIZE)
        pos=(truex,truey)
        radius= CHESS_RADIUS
        pygame.draw.circle(screen, drawcolor, pos, radius)
        return
class maingame: #chessboard变量用map替换？
    
    def __init__(self): #把游戏的初始化放在主程序部分进行
        self.mousepos = []
        self.chesspos = () #先设置转换后的坐标这一变量
        self.chessboard = Map(CHESS_LEN, CHESS_LEN)#调用Map，为了避免和Map里面的变量重名，我把maingame里面的改叫chessboard
               

    def blackmove(self): #我们在这里设定玩家的棋子是黑色，而电脑执白子,图形表现放在主函数中完成
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    os._exit(0)
                if event.type == MOUSEBUTTONDOWN: #在这里判断，如果玩家落下鼠标，则认为是下棋）
                    self.mousepos = pygame.mouse.get_pos()
                    self.chesspos = self.chessboard.MapPosToIndex(self.mousepos[0],self.mousepos[1])
                    if 771 <= self.mousepos[0] <= 921 and 271 <= self.mousepos[1] <= 321:
                        os._exit(0)
                    elif 771 <= self.mousepos[0] <= 921 and 371 <= self.mousepos[1] <= 421:
                        return True
                    if self.chesspos != None:
                        if self.chessboard.map[self.chesspos[0]][self.chesspos[1]] == 0:
                            self.chessboard.map[self.chesspos[0]][self.chesspos[1]] = 1
                            return 
                        else:
                            continue
                    else:
                        continue
    def whitemove_ai_normal(self):  #预留给电脑ai的函数接口
        t_score=[None]*10
        t_score[0]=7                #没有子
        t_score[1]=35				#一个己方子
        t_score[2]=800				#两个己方子
        t_score[3]=15000			#三个己方子
        t_score[4]=800000			#四个己方子
        t_score[5]=15				#一个对方子
        t_score[6]=400				#两个对方子
        t_score[7]=8000				#三个对方子
        t_score[8]=100000			#四个对方子
        t_score[9]=0				#五五开

		#打分表
        def chess_t_score(black_num,white_num):
            if black_num==0 and white_num==0: 
                pos_t_score=t_score[0]
            elif black_num > white_num: 	
                pos_t_score=t_score[black_num - white_num + 4]
            elif black_num < white_num: 	
                pos_t_score=t_score[white_num - black_num]
            else:                             	
                if black_num != 0:			
                    pos_t_score=t_score[black_num+4]
                if white_num != 0:			
                    pos_t_score=t_score[white_num]		
            return pos_t_score

		#计算一个空位的分数
        def chess_score(self,chess_pos):
            pos_score=0	
            x=chess_pos[0]
            y=chess_pos[1]
            black_num=0
            white_num=0	
			#横列
            for i in range(5):#统计所有五元组的得分总和
                for j in range(5):
                    if x>14 or y-j+i>14 or x<0 or y-j+i<0:
                        continue
                    if self.chessboard.map[x][y-j+i]==1: 
                        black_num+=1
                    elif self.chessboard.map[x][y-j+i]==2: 
                        white_num+=1
                pos_score=pos_score+chess_t_score(black_num, white_num)#计算一个元组
                white_num=0
                black_num=0
			#右斜
            for i in range(5):
                for j in range(5):
                    if x-j+i>14 or y-j+i>14 or x-j+i<0 or y-j+i<0:
                        continue
                    if self.chessboard.map[x-j+i][y-j+i]==1: 
                        black_num+=1
                    elif self.chessboard.map[x-j+i][y-j+i]==2: 
                        white_num+=1	
                pos_score=pos_score+chess_t_score(black_num, white_num)
                white_num=0
                black_num=0
			#左斜
            for i in range(5):
                for j in range(5):
                    if x+j-i>14 or y-j+i>14 or x+j-i<0 or y-j+i<0:
                        continue
                    if self.chessboard.map[x+j-i][y-j+i]==1: 
                        black_num+=1
                    elif self.chessboard.map[x][y-j+i]==2: 
                        white_num+=1	
                pos_score=pos_score+chess_t_score(black_num, white_num)
                white_num=0
                black_num=0
			#竖列	
            for i in range(5):
                for j in range(5):
                    if x-j+i>14 or y>14 or x-j+i<0 or y<0:
                        continue
                    if self.chessboard.map[x-j+i][y]==1: 
                        black_num+=1
                    elif self.chessboard.map[x-j+i][y]==2: 
                        white_num+=1	
                pos_score=pos_score+chess_t_score(black_num, white_num)
                white_num=0
                black_num=0
            return pos_score

        def find_maxscore(self):
            chess_score_board=[]
            for row in range(15):
                for col in range(15):
                    chess_pos = [row,col]
                    if self.chessboard.map[row][col]==0:
                        pos_score=chess_score(self,chess_pos)
                        chess_score_board.append([pos_score, row, col])
            chess_score_board.sort(reverse=True)		
			#随机落子
            if chess_score_board[0][0]-chess_score_board[2][0]<50:	
                choose_pos=random.randint(0,2)		
            elif chess_score_board[0][0]-chess_score_board[1][0]<100:	
                choose_pos=random.randint(0,1)
            else :	
                choose_pos=0
            pc_pressed_x=chess_score_board[choose_pos][1]
            pc_pressed_y=chess_score_board[choose_pos][2]
            self.chessboard.map[pc_pressed_x][pc_pressed_y]=2
            self.chesspos=(pc_pressed_x,pc_pressed_y)
            return 
        find_maxscore(self)		
        
    def whitemove_ai_hard(self):  #预留给电脑ai的函数接口
        list1 = []  # AI
        list2 = []  # human
        list3 = []  # 已经搜索过的集合
        list_all = []  # 整个棋盘的点

        for row in range(15):
            for col in range(15):
                chess_pos = (row,col)
                list_all.append(chess_pos)
                if self.chessboard.map[chess_pos[0]][chess_pos[1]]==1:
                    list2.append(chess_pos)
                    list3.append(chess_pos)
                if self.chessboard.map[chess_pos[0]][chess_pos[1]]==2:
                    list1.append(chess_pos)
                    list3.append(chess_pos)

        next_point = [0, 0]  # 初始化AI下一步最应该下的位置
        #棋型的评估分数
        shape_score = [(50, (0, 1, 1, 0, 0)),
                       (50, (0, 0, 1, 1, 0)),
                       (200, (1, 1, 0, 1, 0)),
                       (500, (0, 0, 1, 1, 1)),
                       (500, (1, 1, 1, 0, 0)),
                       (5000, (0, 1, 1, 1, 0)),
                       (5000, (0, 1, 0, 1, 1, 0)),
                       (5000, (0, 1, 1, 0, 1, 0)),
                       (5000, (1, 1, 1, 0, 1)),
                       (5000, (1, 1, 0, 1, 1)),
                       (5000, (1, 0, 1, 1, 1)),
                       (5000, (1, 1, 1, 1, 0)),
                       (5000, (0, 1, 1, 1, 1)),
                       (50000, (0, 1, 1, 1, 1, 0)),
                       (99999999, (1, 1, 1, 1, 1))]

        def ai(self):
            search(True, 3, -99999999, 99999999)
            self.chessboard.map[next_point[0]][next_point[1]] = 2
            self.chesspos = (next_point[0],next_point[1])
            return

        #极大极小值搜索 alpha + beta剪枝，white用True和False表示当前位于最大层还是最小层
        def search(white, depth, alpha, beta):
        #递归深度是否到达边界
            if  depth == 0:
                return evaluation(white)
            blank_list = list(set(list_all).difference(set(list3)))		#深度优先
            order(blank_list)
	    #遍历每一个候选步
            for next_step in blank_list:
                if not has_neighbor(next_step):
                    continue
                if white:
                    list1.append(next_step)
                else:
                    list2.append(next_step)
                list3.append(next_step)
		#获取当前节点的值value
                value = -search(not white, depth - 1, -beta, -alpha)
                if white:
                    list1.remove(next_step)
                else:
                    list2.remove(next_step)
                list3.remove(next_step)
		#α值是该层节点当前最有利的评分，β值是父节点当前的α值
                if value > alpha:
                    #print(str(value) + "alpha:" + str(alpha) + "beta:" + str(beta))
                    #print(list3)
                    if depth == 3:						#第一层
                        next_point[0] = next_step[0]
                        next_point[1] = next_step[1]
        # alpha + beta剪枝点,对于敌人层选择最小值，自己层选择最大值
                    if value >= beta:return beta
                    alpha = value
            return alpha

        def evaluation(white):
            total_score = 0
            if white:
                my_list = list1
                enemy_list = list2
            else:
                my_list = list2
                enemy_list = list1
    #算自己的得分
            score_all_arr = []  
            my_score = 0
            for pt in my_list:
                m = pt[0]
                n = pt[1]
                my_score += cal_score(m, n, 0, 1, enemy_list, my_list, score_all_arr)
                my_score += cal_score(m, n, 1, 0, enemy_list, my_list, score_all_arr)
                my_score += cal_score(m, n, 1, 1, enemy_list, my_list, score_all_arr)
                my_score += cal_score(m, n, -1, 1, enemy_list, my_list, score_all_arr)

    #算敌人的得分
            score_all_arr_enemy = []
            enemy_score = 0
            for pt in enemy_list:
                m = pt[0]
                n = pt[1]
                enemy_score += cal_score(m, n, 0, 1, my_list, enemy_list, score_all_arr_enemy)
                enemy_score += cal_score(m, n, 1, 0, my_list, enemy_list, score_all_arr_enemy)
                enemy_score += cal_score(m, n, 1, 1, my_list, enemy_list, score_all_arr_enemy)
                enemy_score += cal_score(m, n, -1, 1, my_list, enemy_list, score_all_arr_enemy)
            total_score = my_score - enemy_score*0.1
            return total_score

        def order(blank_list):
            last_pt = list3[-1]
            for item in blank_list:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if (last_pt[0] + i, last_pt[1] + j) in blank_list:
                            blank_list.remove((last_pt[0] + i, last_pt[1] + j))
                            blank_list.insert(0, (last_pt[0] + i, last_pt[1] + j))

        def has_neighbor(pt):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if pt[0] + i>14 or pt[0] + i<0 or pt[1]+j>14 or pt[1]+j<0:
                        continue
                    if (pt[0] + i, pt[1]+j) in list3:
                        return True
            return False

    #每个方向上的分值计算
        def cal_score(m, n, xdimen, ydimen, enemy_list, my_list, score_all_arr):
            add_score = 0  # 加分项
    #在一个方向上，只取最大的得分项
            max_score_shape = (0, None)

    #如果此方向上，该点已经有得分形状，不重复计算
            for item in score_all_arr:
                for pt in item[1]:
                    if m == pt[0] and n == pt[1] and xdimen == item[2][0] and ydimen == item[2][1]:
                        return 0

            #在落子点四个方向上循环查找得分形状
            for offset in range(-5, 1):
                # offset = -2
                pos = []
                for i in range(0, 6):
                    if (m + (i + offset) * xdimen, n + (i + offset) * ydimen) in enemy_list:
                        pos.append(2)
                    elif (m + (i + offset) * xdimen, n + (i + offset) * ydimen) in my_list:
                        pos.append(1)
                    else:
                        pos.append(0)
                tmp_shap5 = (pos[0], pos[1], pos[2], pos[3], pos[4])
                tmp_shap6 = (pos[0], pos[1], pos[2], pos[3], pos[4], pos[5])
                for (score, shape) in shape_score:
                    if tmp_shap5 == shape or tmp_shap6 == shape:
                        if score > max_score_shape[0]:
                            max_score_shape = (score, ((m + (0+offset) * xdimen, n + (0+offset) * ydimen),
                                                       (m + (1+offset) * xdimen, n + (1+offset) * ydimen),
                                                       (m + (2+offset) * xdimen, n + (2+offset) * ydimen),
                                                       (m + (3+offset) * xdimen, n + (3+offset) * ydimen),
                                                       (m + (4+offset) * xdimen, n + (4+offset) * ydimen)), (xdimen, ydimen))

            # 计算多个形状相交
            if max_score_shape[1] is not None:
                for item in score_all_arr:
                    for pt1 in item[1]:
                        for pt2 in max_score_shape[1]:
                            if pt1 == pt2 and max_score_shape[0] > 10 and item[0] > 10:
                                add_score += item[0] + max_score_shape[0]

                score_all_arr.append(max_score_shape)

            return add_score + max_score_shape[0]

        ai(self)

    def whitemove_player(self): #若选择双人对战模式，预留给另一个玩家
         flag = True  #先设立一个死循环，直到玩家能下出正确的棋就终止
         while flag:
            for event in pygame.event.get():
                if event.type == QUIT:
                    os._exit(0)
                if event.type == MOUSEBUTTONDOWN: #在这里判断，如果玩家落下鼠标，则认为是下棋，但也有可能是误触（这部分先不写，等lzy的部分）
                    self.mousepos = pygame.mouse.get_pos()
                    self.chesspos = self.chessboard.MapPosToIndex(self.mousepos[0],self.mousepos[1]) 
                    if 771 <= self.mousepos[0] <= 921 and 271 <= self.mousepos[1] <= 321:
                        os._exit(0)
                    elif 771 <= self.mousepos[0] <= 921 and 371 <= self.mousepos[1] <= 421:
                        return True
                    if self.chesspos != None:
                        if self.chessboard.map[self.chesspos[0]][self.chesspos[1]] == 0:
                            self.chessboard.map[self.chesspos[0]][self.chesspos[1]] = 2
                            return
                        else:
                            continue


    def gameresult(self): #设立游戏结束条件
        #return 1黑子胜利 return 2白子胜利 return 3平局  return 0游戏继续
        if self.chessboard.map[self.chesspos[0]][self.chesspos[1]]==1:
            i=1
            count=1
            while (self.chesspos[1]+i)<=14 and self.chessboard.map[self.chesspos[0]][self.chesspos[1]+i]==1:
                count+=1
                i+=1
            i=1
            while 0<=(self.chesspos[1]-i) and self.chessboard.map[self.chesspos[0]][self.chesspos[1]-i]==1:
                count+=1
                i+=1
            if count>=5:
                return 1   #判断黑子在横向是否连成5子(如果不行可以考虑加特判)
            count=1
            i=1
            while (self.chesspos[0]+i)<=14 and self.chessboard.map[self.chesspos[0]+i][self.chesspos[1]]==1:
                count+=1
                i+=1
            i=1
            while 0<=(self.chesspos[0]-i) and self.chessboard.map[self.chesspos[0]-i][self.chesspos[1]]==1:
                count+=1
                i+=1
            if count>=5:
                return 1  #判断黑子在纵向是否连成5子（可以考虑加特判）


        #设立斜向胜利标准(慎思),可以在最后落子的上面考虑。

        #先设立右斜方
            count=1
            i=1
            while 0<=(self.chesspos[0]-i) and (self.chesspos[1]+i)<=14 and self.chessboard.map[self.chesspos[0]-i][self.chesspos[1]+i]==1:
                count+=1
                i+=1
            i=1
            while (self.chesspos[0]+i)<=14 and 0<=(self.chesspos[1]-i) and self.chessboard.map[self.chesspos[0]+i][self.chesspos[1]-i]==1:
                count+=1
                i+=1
            if count>=5:
                return 1
        #再设立左斜方
            count=1
            i=1
            while 0<=(self.chesspos[0]-i) and 0<=(self.chesspos[1]-i) and self.chessboard.map[self.chesspos[0]-i][self.chesspos[1]-i]==1:
                count+=1
                i+=1
            while (self.chesspos[0]+i)<=14 and (self.chesspos[1]+i)<=14 and self.chessboard.map[self.chesspos[0]+i][self.chesspos[1]+i]==1:
                count+=1
                i+=1
            if count>=5:
                return 1
        else:  #白子胜利条件（基本上和黑子一样，只是把所有的1改成2）
            i=1
            count=1
            while (self.chesspos[1]+i)<=14 and self.chessboard.map[self.chesspos[0]][self.chesspos[1]+i]==2:
                count+=1
                i+=1
            i=1
            while 0<=(self.chesspos[1]-i) and self.chessboard.map[self.chesspos[0]][self.chesspos[1]-i]==2:
                count+=1
                i+=1
            if count>=5:
                return 2   #判断白子在横向是否连成5子(如果不行可以考虑加特判)
            count=1
            i=1
            while (self.chesspos[0]+i)<=14 and self.chessboard.map[self.chesspos[0]+i][self.chesspos[1]]==2:
                count+=1
                i+=1
            i=1
            while 0<=(self.chesspos[0]-i) and self.chessboard.map[self.chesspos[0]-i][self.chesspos[1]]==2:
                count+=1
                i+=1
            if count>=5:
                return 2  #判断白子在纵向是否连成5子（可以考虑加特判）

        #设立斜向胜利标准(慎思)
        #先设立右斜方
            count=1
            i=1
            while 0<=(self.chesspos[0]-i) and (self.chesspos[1]+i)<=14 and self.chessboard.map[self.chesspos[0]-i][self.chesspos[1]+i]==2:
                count+=1
                i+=1
            i=1
            while (self.chesspos[0]+i)<=14 and 0<=(self.chesspos[1]-i) and self.chessboard.map[self.chesspos[0]+i][self.chesspos[1]-i]==2:
                count+=1
                i+=1
            if count>=5:
                return 2
        #再设立左斜方
            count=1
            i=1
            while 0<=(self.chesspos[0]-i) and 0<=(self.chesspos[1]-i) and self.chessboard.map[self.chesspos[0]-i][self.chesspos[1]-i]==2:
                count+=1
                i+=1
            while (self.chesspos[0]+i)<=14 and (self.chesspos[1]+i)<=14 and self.chessboard.map[self.chesspos[0]+i][self.chesspos[1]+i]==2:
                count+=1
                i+=1
            if count>=5:
                return 2
        #设立平局条件
        for x in range(15):
            if 0 in self.chessboard.map[x]:
                return 0
        return 3
  

    def showresult(self,result,screen):  #显示游戏结果
         def showFont(screen, text, location_x, locaiton_y, height):
            font = pygame.font.SysFont(None, height)
            font_image = font.render(text, True, (0, 0, 255), (247, 238, 214))
            font_image_rect = font_image.get_rect()
            font_image_rect.x = location_x
            font_image_rect.y = locaiton_y
            screen.blit(font_image, font_image_rect)
         if result==1:
            str = 'Winner is Black'
         elif result==2:
            str = 'Winner is White'
         else:
            str = 'Draw' #平局用Draw表示
         showFont(screen, str, MAP_WIDTH + 18, SCREEN_HEIGHT - 250, 30) #调整了一下最终显示的位置
   


def main():
    def againstai(flag): #与ai对战
        while True:
            suddenstop=game1.blackmove()
            if suddenstop==True:
                return "restart" #如果用户中途选择重开
            game1.chessboard.drawChess(screen,1,game1.chesspos)
            window.blit(screen,(0,0))
            pygame.display.flip()
            if game1.gameresult()!=0:
                game1.showresult(game1.gameresult(),screen)
                window.blit(screen,(0,0)) #刷新到屏幕上
                pygame.display.flip()
                time.sleep(2)
                return
            if flag==1:
                game1.whitemove_ai_normal()
            if flag==2:
                game1.whitemove_ai_hard()
            game1.chessboard.drawChess(screen,2,game1.chesspos)
            window.blit(screen,(0,0))
            pygame.display.flip()
            if game1.gameresult()!=0:
                game1.showresult(game1.gameresult(),screen)
                window.blit(screen,(0,0))  #刷新到屏幕上
                pygame.display.flip()
                time.sleep(2)
                return
        
    def againstpeople(): #与人对战
        while True:
            suddenstop=game1.blackmove()
            if suddenstop==True:
                return "restart" #如果用户中途选择重开
            game1.chessboard.drawChess(screen,1,game1.chesspos)
            window.blit(screen,(0,0))
            pygame.display.flip()
            if game1.gameresult()!=0:
                game1.showresult(game1.gameresult(),screen)
                window.blit(screen,(0,0)) #刷新到屏幕上
                pygame.display.flip()
                time.sleep(2)
                return
            suddenstop=game1.whitemove_player()
            if suddenstop==True:
                return "restart" #如果用户中途选择重开
            game1.chessboard.drawChess(screen,2,game1.chesspos)
            window.blit(screen,(0,0))
            pygame.display.flip()
            if game1.gameresult()!=0:
                game1.showresult(game1.gameresult(),screen)
                window.blit(screen,(0,0))  #刷新到屏幕上
                pygame.display.flip()
                time.sleep(2)
                return
    def quitzera():
        os._exit(0) #直接退出
    def remake(): #当一局游戏结束后，玩家可以选择give up 或者再来一盘
        while True:
            for event in pygame.event.get():
                if event.type== QUIT:
                    os._exit(0)
                elif event.type==MOUSEBUTTONDOWN:
                    mainpos=pygame.mouse.get_pos()
                    if 771<=mainpos[0]<=921 and 271<=mainpos[1]<=321: #放弃
                        return 0 
                    elif 771<=mainpos[0]<=921 and 371<=mainpos[1]<=421: #再来一盘，清零，回到modechose()函数，重新进行模式选择
                        game1.chessboard.reset()
                        screen.fill((0,0,0))
                        game1.chessboard.drawBackground(screen,0)
                        window.blit(screen,(0,0))
                        pygame.display.flip()
                        return 1
    def whenplayrestart():  #在游戏中途选择restart
        game1.chessboard.reset()
        screen.fill((0,0,0))
        game1.chessboard.drawBackground(screen,0)
        window.blit(screen,(0,0))
        pygame.display.flip()
        return


           
    def modechose():
        while True:  #第一个循环完成模式选择
            for event in pygame.event.get():
                if event.type== QUIT:
                    quitzera()
                elif event.type==MOUSEBUTTONDOWN:
                    mainpos=pygame.mouse.get_pos()
                    if 771<=mainpos[0]<=921 and 71<=mainpos[1]<=121: #第一个按钮的坐标
                        return 1
                    elif 771<=mainpos[0]<=921 and 171<=mainpos[1]<=221: #第二个按钮
                        return 2
                    elif 771<=mainpos[0]<=921 and 271<=mainpos[1]<=321: #第三个按钮
                        quitzera()  #直接退出游戏
    pygame.init()
    window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    screen=pygame.Surface([SCREEN_WIDTH,SCREEN_HEIGHT])
    game1=maingame()
    game1.chessboard.drawBackground(screen,0)
    window.blit(screen,(0,0))
    pygame.display.flip()
    while True:
        modevalue=modechose()
        if modevalue==1:
            game1.chessboard.drawBackground(screen,modevalue)
            window.blit(screen,(0,0))
            pygame.display.flip()
            modevalue=modechose()
            #再获取一次modelvalue，1则normal，2则hard
            
            whetherrestart=againstai(modevalue)
            if whetherrestart=="restart":
                whenplayrestart()
                continue
        else:
            whetherrestart=againstpeople()
            if whetherrestart=="restart":
                whenplayrestart()
                continue
        modevalue=remake()
        if modevalue==0:
            quitzera() #退出游戏
        else:
            continue  #重新开始

main()

 












