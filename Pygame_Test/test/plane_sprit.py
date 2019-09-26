# coding=utf-8
# 使用pygame的精灵类创建敌机和我机

from image_util import *


pygame.init()
# 创建一个游戏窗口
screen = pygame.display.set_mode((480,700))
# 显示背景图
back = pygame.image.load("E:/pyCharm/Pygame_Test/images/background.png")
# 2.在屏幕上绘制图片
screen.blit(back,(0,0))


# 显示飞机图片
# 1.加载飞机图片（返回一个图片对象）
fly = pygame.image.load("E:/pyCharm/Pygame_Test/images/me1.png")
# 2.在屏幕上绘制图片，
screen.blit(fly,(180,500))
# 3.更新屏幕的显示，在screen执行完所有的blit（）方法后，统一执行一次
pygame.display.update()

clock = pygame.time.Clock()
# 加载图片
plan1 = GameSprite("E:/pyCharm/Pygame_Test/images/enemy1.png")
# 指定图片的初始位置
plan1.rect.x = 100
plan_group = pygame.sprite.Group(plan1)


while True:
    # 控制循环体一秒钟执行的次数
    clock.tick(60)

    # 为了避免出现残影，在每一次绘制飞机之前要重新绘制一个一下屏幕背景
    screen.blit(back, (0, 0))
    screen.blit(fly, (180, 500))
   #  只是更新图片的位置，不是更新屏幕的显示
    plan_group.update()
    plan_group.draw(screen)  # 相当于screen.blit(fly,(180,500)) 绘制图片

    # 更新屏幕的显示
    pygame.display.update()


pygame.quit()

