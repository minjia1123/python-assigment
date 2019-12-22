import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #设置尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (178,34,34)
        self.text_color = (245, 245, 245)
        self.font = pygame.font.SysFont(None, 48)
        
        #设置按钮的rect属性,居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message only needs to be prepped once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """绘制一个用颜色填充的按钮，再绘制文本."""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #创建一个空按钮
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
