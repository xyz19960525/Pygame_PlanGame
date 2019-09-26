# coding=utf-8
import  pygame

pygame.init()
# 创建一个屏幕
screen = pygame.display.set_mode((480,700))
# 显示背景图片
# 1.加载背景图片（返回一个图片对象）
bg = pygame.image.load("./images/background.png")
# 2.在屏幕上绘制图片
screen.blit(bg,(0,0))
# 3.更新屏幕的显示
# pygame.display.update()

# 显示飞机图片
# 1.加载飞机图片（返回一个图片对象）
fly = pygame.image.load("./images/me1.png")
# 2.在屏幕上绘制图片，
screen.blit(fly,(180,500))
# 3.更新屏幕的显示，在screen执行完所有的blit（）方法后，统一执行一次
pygame.display.update()


clock = pygame.time.Clock() # 限制一秒钟执行的次数

# 定义飞机的初始位置
fly_position = pygame.Rect(180,500,102,126)

fly_up = True

while True:
    # 控制循环体一秒钟执行的次数
     clock.tick(60)

    # TODO 飞机上下循环飞行
    #  if fly_up:
    #     if fly_position.y <= 130:
    #         fly_up = False
    #     fly_position.y -= 1
    #
    #  else:
    #      if fly_position.y >= 550:
    #          fly_up = True
    #      fly_position.y += 1


    # 获取用户的事件(关闭游戏）
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             print ("游戏退出！！！")

             pygame.quit()
             exit()




    # 如果飞机飞出屏幕，让飞机从底部飞出
     if fly_position.y == -126:

         fly_position.y = 700
    # 每循环一次，就让飞机向上1mm
     fly_position.y -= 1

    # 为了避免出现残影，在每一次绘制飞机之前要重新绘制一个一下屏幕背景
     screen.blit(bg, (0,0))
    # 重新再屏幕上绘制飞机
     screen.blit(fly, fly_position)

    # 刷新屏幕
     pygame.display.update()



pygame.quit()