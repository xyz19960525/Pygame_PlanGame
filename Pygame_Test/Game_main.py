# coding=utf-8
import  pygame
import  time

from Pygame_Test.image_util import *


class Game_Plan(object):

     pygame.init()
     # pygame.mixer.init()
     # 定义屏幕的大小（常亮）
     SCREEN_RECR = pygame.Rect(0,0,480,700)
    # TODO 这只敌机创建的定时器事件
     ENEMY_EVENT = pygame.USEREVENT
    # TODO 创建飞机反射子弹的定时器时间（每隔0.5秒）
     HERO_FIRE = pygame.USEREVENT + 1

    # 播放背景音乐 （使用音乐播放器需调用 pygame.init()先初始化）
     pygame.mixer.music.load("./sound/game_music.wav")
     pygame.mixer.music.play(-1, 0.0)
     pygame.mixer.music.set_volume(0.1)


     """
        初始化方法中创建对象
          1,创建游戏窗口
          2.创建时钟对象（控制帧率）
          3.创建精灵和精灵组（需要显示图片对象）
     """
     def __init__(self):

         self.screen = pygame.display.set_mode(self.SCREEN_RECR.size)
         self.clock = pygame.time.Clock()
         self.__create_sprites()
         self.play_sound() # 播放游戏声音

         #  一秒创建一次敌机
         pygame.time.set_timer(self.ENEMY_EVENT,1000)
         # 设置一个每隔0.2秒发射一次子弹
         pygame.time.set_timer(self.HERO_FIRE,200)


     def play_sound(self):
         # 敌机销毁声音
         self.enemy_down_sound = pygame.mixer.Sound("./sound/enemy1_down.wav")
         self.game_over_sound = pygame.mixer.Sound("./sound/game_over.wav")
         self.enemy_down_sound.set_volume(0.3)
         self.game_over_sound.set_volume(0.3)
         # 游戏结束图片
         self.game_over = pygame.image.load("./images/gameover.png")


     def start_game(self):
         while True:

             # 1.设置帧率
             self.clock.tick(60)
             # 2.事件监听
             self.__event_check()
             # 3.碰撞检测
             self.__position_check()
             # 4.更新/设置精灵
             self.__update_sprites()
             # 5.更新屏幕的显示
             pygame.display.update()

     def __create_sprites(self):
         # 代码重复 过于冗杂
         # bg1 = BackGround("./images/background.png")
         # bg2 = BackGround("./images/background.png")

         bg1 = BackGround()
         bg2 = BackGround(False)
         self.plan = Plan()


         self.bg_group = pygame.sprite.Group(bg1,bg2)
         # TODO 创建敌机的精灵组
         self.enemy_group = pygame.sprite.Group()
         self.plan_group = pygame.sprite.Group(self.plan)

        # 创建一个所有被销毁的敌机的精灵组
         self.enemys_die = pygame.sprite.Group()



     def __update_sprites(self):
         # 背景
         self.bg_group.update()
         self.bg_group.draw(self.screen)
         # 敌机
         self.enemy_group.update()
         self.enemy_group.draw(self.screen)
        # 英雄飞机
         self.plan_group.update()
         self.plan_group.draw(self.screen)
        # 子弹
         self.plan.bellet_group.update()
         self.plan.bellet_group.draw(self.screen)

     # 在while循环中 每秒钟执行60次
     def __event_check(self):


         # 监听各种事件
         for event in pygame.event.get():
             #  监听关闭事件
             if event.type == pygame.QUIT:
                 self.__exit_game()
             # 监听创建敌机事件
             elif event.type == self.ENEMY_EVENT:
                 # TODO 创建敌机
                 enemy = Enemy()
                 #  TODO 在精灵组中添加精灵
                 self.enemy_group.add(enemy)

             # 监听发射子弹的事件
             elif event.type == self.HERO_FIRE:
                 self.plan.fire()

        #  获取用户键盘的操作
         key_press = pygame.key.get_pressed()
         if key_press[pygame.K_RIGHT] :
                 self.plan.speed = 4

                 # print ("向右")
         elif key_press[pygame.K_LEFT]:
                 self.plan.speed = -4
                 # print ("向左！！！")
         else:
                self.plan.speed = 0







     def __position_check(self):
         # 子弹装到敌机时 敌机被销毁
         enemy_down=  pygame.sprite.groupcollide(self.enemy_group,self.plan.bellet_group,True,True)
         for enemy in enemy_down:
             # 将销毁的敌机放在精灵组里
             self.enemys_die.add(enemy)



         for enemys in self.enemys_die:
             for i in range(0,4) :
               # self.screen.blit(enemys.died_photo,enemys.rect)
               self.screen.blit(enemys.enemy_list[i], enemys.rect)
               pygame.display.update()
            # 敌机撞毁的声音
             self.enemy_down_sound.play()
             # 控制不能立即更新
             time.sleep(0.04)
             self.enemys_die.remove(enemys)


         # 飞机装到敌机时，返回一个列表，包含所有和精灵碰撞的精灵组中的精灵
         enemy_sprites = pygame.sprite.spritecollide(self.plan,self.enemy_group,True)
         if  len(enemy_sprites)>0:
             # 飞机销毁动画
             for i in range(0,4) :
                 # print i
                 self.screen.blit(self.plan.died_list[i], self.plan.rect)
                 pygame.display.update()

             # 游戏over声音
             self.game_over_sound.play()
             # 结束游戏
             time.sleep(1)
             self.screen.blit(self.game_over,(0,0))
             pygame.display.update()
             pygame.mixer.music.stop() # 停止声音播放
             time.sleep(2)
             self.__exit_game()



     def __exit_game(self):
         pygame.quit()
         # exit()

if __name__ == "__main__":

     game = Game_Plan()
     game.start_game()



