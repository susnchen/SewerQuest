import pygame

u = 32 #one unit in the game is 32 pixels

bulletl = pygame.image.load("assets\\images\\bullet.png")
bulletd = pygame.transform.rotate(bulletl,90)
bulletr = pygame.transform.rotate(bulletd,90)
bulletu = pygame.transform.rotate(bulletr,90)

enemyimg = pygame.image.load("assets\\images\\enemy.png")

playerdown = [
    pygame.image.load("assets\\images\\down1.png"),
    pygame.image.load("assets\\images\\down2.png"),
    pygame.image.load("assets\\images\\down3.png"),
    pygame.image.load("assets\\images\\down4.png"),
    pygame.image.load("assets\\images\\down5.png"),
    pygame.image.load("assets\\images\\down6.png")
]

playerup = [
    pygame.image.load("assets\\images\\up1.png"),
    pygame.image.load("assets\\images\\up2.png"),
    pygame.image.load("assets\\images\\up3.png"),
    pygame.image.load("assets\\images\\up4.png"),
    pygame.image.load("assets\\images\\up5.png"),
    pygame.image.load("assets\\images\\up6.png")
]

playerleft = [
    pygame.image.load("assets\\images\\left1.png"),
    pygame.image.load("assets\\images\\left2.png"),
    pygame.image.load("assets\\images\\left3.png"),
    pygame.image.load("assets\\images\\left4.png"),
    pygame.image.load("assets\\images\\left5.png"),
    pygame.image.load("assets\\images\\left6.png")
]

playerright = [
    pygame.image.load("assets\\images\\right1.png"),
    pygame.image.load("assets\\images\\right2.png"),
    pygame.image.load("assets\\images\\right3.png"),
    pygame.image.load("assets\\images\\right4.png"),
    pygame.image.load("assets\\images\\right5.png"),
    pygame.image.load("assets\\images\\right6.png")
]

doorPos = [(288,-32),(320,-32),(640,224),(640,256),(320,512),(288,512),(-32,224),(-32,256)]

roomImg = [
    pygame.image.load("assets\\images\\room0.png"),
    pygame.image.load("assets\\images\\room1.png")
]

roomList = []