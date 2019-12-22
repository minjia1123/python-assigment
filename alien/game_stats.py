class GameStats():
    """统计外星人飞船"""
    
    def __init__(self, ai_settings):
        """初始化信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 游戏开始时，飞船处于静止状态
        self.game_active = False
        
        # 不重置最高分
        self.high_score = 0
        
    def reset_stats(self):
        """信息初始化，随游戏进程改变"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
