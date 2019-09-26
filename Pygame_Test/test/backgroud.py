# # coding=utf-8
# import  pygame
#
# pygame.init()
# # 创建一个屏幕
# screen = pygame.display.set_mode((480,700),)
# # 显示背景图片
# # 1.加载背景图片（返回一个图片对象）
# bg = pygame.image.load("E:/pyCharm/Pygame_Test/images/background.png")
# # 2.在屏幕上绘制图片
# screen.blit(bg,(0,0))
# # 3.更新屏幕的显示
# pygame.display.update()
#
#
#
# print bg
#
#
# while True:
#      pass
#
# pygame.quit()
#
#
# # load_images("./images/background.png",screen)
# # def  load_images(url,screen,position = (0,0)):
# #      bg = pygame.image.load(url)
# #      screen.blit(bg,position)
# #      pygame.display.update()


for i in range(0,3):
     for j in range(0,2):
          print "a"
     print i
     i+=1