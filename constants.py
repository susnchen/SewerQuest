import pygame
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.font.init()

gamew = 640
gameh = 512

#Loading Screen
screen = pygame.display.set_mode((gamew, gameh))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
font = pygame.font.Font(None, 36)
text = font.render("Loading...", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)
screen.blit(background, (0, 0))
pygame.display.set_caption("Sewer Quest")

pygame.display.flip()

clock = pygame.time.Clock()
clock.tick(60)

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
    pygame.image.load("assets\\images\\room1.png"),
    pygame.image.load("assets\\images\\room2.png"),
    pygame.image.load("assets\\images\\room3.png")
]

startScreenImg = pygame.image.load("assets\\images\\startScreen.png")
transistionImg = pygame.image.load("assets\\images\\blackScreen.png")

startButton = pygame.image.load("assets\\images\\startButton.png")
highscoresButton = pygame.image.load("assets\\images\\highscoresButton.png")
exitButton = pygame.image.load("assets\\images\\exitButton.png")
continueButton = pygame.image.load("assets\\images\\continueButton.png")
menuButton = pygame.image.load("assets\\images\\menuButton.png")
menuBackground = pygame.image.load("assets\\images\\bg.png")
cat = pygame.image.load("assets\\images\\cat.png")
sadCat = pygame.image.load("assets\\images\\sadCat.png")


heartImg = pygame.image.load("assets\\images\\heart.png")
fishImg = [
    pygame.image.load("assets\\images\\fish0.png"),
    pygame.image.load("assets\\images\\fish1.png")
]

levelSettings = [
    4,(5)
]
'''
mainAudio = pygame.mixer.Sound("assets\\audio\\camel.wav")
mainAudio.set_volume(0.1)'''
onHit = pygame.mixer.Sound("assets\\audio\\onHit.wav")
shoot = pygame.mixer.Sound("assets\\audio\\shoot.wav")
shoot.set_volume(0.1)


roomList = []