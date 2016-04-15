import pygame

u = 32 #one unit in the game is 32 pixels
solidv = (32,15*32)
solidh = (20*32,32)
obstacleList = [((u,u),u,0),(solidh,4*u,0),(solidh,0,14*u),(solidv,0,0),(solidv,19*u,0),((7*u,u),u,4*u),((7*u,u),11*u,6*u),((3*u,u),4*u,9*u)]

bulletl = pygame.image.load("assets\\images\\bullet.png")
bulletd = pygame.transform.rotate(bulletl,90)
bulletr = pygame.transform.rotate(bulletd,90)
bulletu = pygame.transform.rotate(bulletr,90)

playerdown = [pygame.image.load("assets\\images\\down1.png"),pygame.image.load("assets\\images\\down2.png"),pygame.image.load("assets\\images\\down3.png"),pygame.image.load("assets\\images\\down4.png"),pygame.image.load("assets\\images\\down5.png"),pygame.image.load("assets\\images\\down6.png")]

playerup = [pygame.image.load("assets\\images\\up1.png"),pygame.image.load("assets\\images\\up1.png"),pygame.image.load("assets\\images\\up1.png"),pygame.image.load("assets\\images\\up2.png"),pygame.image.load("assets\\images\\up3.png"),pygame.image.load("assets\\images\\up4.png"),pygame.image.load("assets\\images\\up5.png"),pygame.image.load("assets\\images\\up6.png")]

playerleft = [pygame.image.load("assets\\images\\left1.png"),pygame.image.load("assets\\images\\left2.png"),pygame.image.load("assets\\images\\left3.png"),pygame.image.load("assets\\images\\left4.png"),pygame.image.load("assets\\images\\left5.png"),pygame.image.load("assets\\images\\left6.png")]

playerright = [pygame.image.load("assets\\images\\right1.png"),pygame.image.load("assets\\images\\right2.png"),pygame.image.load("assets\\images\\right3.png"),pygame.image.load("assets\\images\\right4.png"),pygame.image.load("assets\\images\\right5.png"),pygame.image.load("assets\\images\\right6.png")]

enemyimg = pygame.image.load("assets\\images\\enemy.png")
