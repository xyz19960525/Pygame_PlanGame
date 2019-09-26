# coding=utf-8
import random
import pygame

# 定义屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_url, speed=1):
        super(GameSprite, self).__init__()
        self.image = pygame.image.load(image_url)
        self.rect = self.image.get_rect()
        self.speed = speed

    # 更新图像的位置
    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):

    def __init__(self,is_First = True):
        #  简化主程序中创建背景图片的代码（背景图片都相同）
        super(BackGround, self).__init__("./images/background.png")
        if is_First is False:
            self.rect.y = -self.rect.height

    def update(self):
        super(BackGround, self).update()

        if self.rect.y >= SCREEN_RECT.height :
            self.rect.y = - self.rect.height



class Enemy(GameSprite):
    # 如果在这里创建 ，以后创建的所有敌机对象的速度都是相同的（这行代码只会执行一次）
    # enemy_speed = random.randint(1, 5)
    def __init__(self):

        self.enemy_speed = random.randint(1, 5)
        # 1. 指定敌人的图片路径
        super(Enemy, self).__init__("./images/enemy1.png",self.enemy_speed)

        # 从屏幕上方缓缓的进入效果
        self.rect.y = -self.rect.height
        max_position = SCREEN_RECT.width - self.rect.width
        # # 2. 随机指定敌人的水平距离
        self.rect.x = random.randint(0, max_position)
        # self.died_photo = pygame.image.load("./images/enemy1_down3.png")
        # 爆炸图片的列表
        self.enemy_list = []
        self.get_boom()

    def update(self):

        super(Enemy, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            # print ("移除屏幕")
            self.kill()

    def get_boom(self):

        self.enemy_list.append(pygame.image.load("./images/enemy1_down1.png"))
        self.enemy_list.append(pygame.image.load("./images/enemy1_down2.png"))
        self.enemy_list.append(pygame.image.load("./images/enemy1_down3.png"))
        self.enemy_list.append(pygame.image.load("./images/enemy1_down4.png"))



class Plan(GameSprite):
    def __init__(self):
        super(Plan, self).__init__("./images/me1.png",0)
        # 飞机的初始位置 位置屏幕的中间
        self.rect.centerx = SCREEN_RECT.centerx

        # 飞机的垂直位置 位于bottom=120
        self.rect.bottom = SCREEN_RECT.height - 80

        self.bellet_group = pygame.sprite.Group()

        self.died_list = []
        self.died_boom()

    def update(self):

         self.rect.x += self.speed
         # 限制飞机不能滑出屏幕
         if self.rect.x <= 0:
             self.rect.x = 0
         #  设置速度等于0此方法不行 因为当用户再次点击键盘向左时，speed还是会被修改为-2
         # self.speed = 0

         elif self.rect.right >= SCREEN_RECT.width:
               self.rect.right = SCREEN_RECT.width

    def died_boom(self):
        self.died_list.append(pygame.image.load("./images/me_destroy_1.png"))
        self.died_list.append(pygame.image.load("./images/me_destroy_2.png"))
        self.died_list.append(pygame.image.load("./images/me_destroy_3.png"))
        self.died_list.append(pygame.image.load("./images/me_destroy_4.png"))


    def  fire(self):
        # print ("发射子弹。。。")

        # 每次发射三个子弹
        for i in (0,1,2):
            # 创建子弹对象
            bullet = Bullet()
            # 设置子弹的初始位置
            bullet.rect.bottom = self.rect.y - i*15
            bullet.rect.centerx = self.rect.centerx
            # 精灵组中添加子弹
            self.bellet_group.add(bullet)



class Bullet(GameSprite):

     def __init__(self):
         # 子弹向上移动
         super(Bullet, self).__init__("./images/bullet1.png",-6)

     def update(self):
         super(Bullet, self).update()

         # 如果子弹移除屏幕，则自动销毁，从精灵组中删除
         if self.rect.y <= 0:
             self.kill()








