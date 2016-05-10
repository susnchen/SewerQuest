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

doorPos = [(288,0),(320,0),(639,224),(639,256),(320,480),(288,480),(0,224),(0,256)]

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

muteButton = [
    pygame.image.load("assets\\images\\muteButton0.png"),
    pygame.image.load("assets\\images\\muteButton1.png")
]

muteButton[0].set_alpha(175)
muteButton[1].set_alpha(175)

#level setting is the speed of the mouse
fishPlacements = {
    0:[(240,320), False, False,(96,280),(240,320), False, (500,96),False,False,(500,96)],
    1:[(240,320), False, False,(96,280),(32,32),False,False,(500,96),False,False,(32,32),False,(32,32),(96,280),False,False],
}

roomImgs = {
            0 : [
        pygame.image.load("assets\\images\\rooms\\room000.png"),
        pygame.image.load("assets\\images\\rooms\\room001.png"),
        pygame.image.load("assets\\images\\rooms\\room002.png"),
        pygame.image.load("assets\\images\\rooms\\room003.png"),
        pygame.image.load("assets\\images\\rooms\\room004.png"),
        pygame.image.load("assets\\images\\rooms\\room005.png"),
        pygame.image.load("assets\\images\\rooms\\room006.png"),
        pygame.image.load("assets\\images\\rooms\\room007.png"),
        pygame.image.load("assets\\images\\rooms\\room008.png"),
        pygame.image.load("assets\\images\\rooms\\room009.png"),
        pygame.image.load("assets\\images\\rooms\\room010.png"),
    ],
            1 : [
        pygame.image.load("assets\\images\\rooms\\room100.png"),
        pygame.image.load("assets\\images\\rooms\\room101.png"),
        pygame.image.load("assets\\images\\rooms\\room102.png"),
        pygame.image.load("assets\\images\\rooms\\room103.png"),
        pygame.image.load("assets\\images\\rooms\\room104.png"),
        pygame.image.load("assets\\images\\rooms\\room105.png"),
        pygame.image.load("assets\\images\\rooms\\room106.png"),
        pygame.image.load("assets\\images\\rooms\\room107.png"),
        pygame.image.load("assets\\images\\rooms\\room108.png"),
        pygame.image.load("assets\\images\\rooms\\room109.png"),
        pygame.image.load("assets\\images\\rooms\\room110.png"),
        pygame.image.load("assets\\images\\rooms\\room111.png"),
        pygame.image.load("assets\\images\\rooms\\room112.png"),
        pygame.image.load("assets\\images\\rooms\\room113.png"),
        pygame.image.load("assets\\images\\rooms\\room114.png"),
        pygame.image.load("assets\\images\\rooms\\room115.png")
    ]
}

roomDoorDict ={
    0: [
            # index of this list is the room number
            # where the 0th index of each item correspond to door 0 (top door)
            # where the 1st index of each item correspond to door 1 (right door)
            # where the 2nd index of each item correspond to door 2 (bottom door)
            # where the 4rd index of each item correspond to door 3 (left door)
            # the number in each index of the item represents the room the door leads to
            # for example, room 0's door 1 leads to room 1
            # room -1 does not exist so it leads to no where
            (1,-1,-1,-1),
            (-1,3,0,2),
            (-1,1,-1,-1),
            (4,-1,-1,1),
            (6,5,3,-1),
            (-1,-1,-1,4),
            (-1,7,4,-1),
            (8,-1,-1,6),
            (-1,-1,7,9),
            (10,8,-1,-1),
            (-1,-1,9,-1)
    ],
    1: [
            (1,-1,-1,-1),
            (-1,2,0,3),
            (-1,-1,-1,1),
            (5,1,-1,4),
            (-1,3,-1,-1),
            (-1,6,3,-1),
            (-1,7,-1,5),
            (9,8,-1,6),
            (-1,-1,-1,7),
            (-1,-1,7,10),
            (11,9,-1,-1),
            (-1,12,10,11),
            (-1,13,-1,11),
            (14,-1,-1,12),
            (-1,15,13,-1),
            (14,-1,-1,-1)
    ]
}

mainAudio = pygame.mixer.Sound("assets\\audio\\camel.wav")
mainAudio.set_volume(0.1)
onHit = pygame.mixer.Sound("assets\\audio\\onHit.wav")
shoot = pygame.mixer.Sound("assets\\audio\\shoot.wav")
shoot.set_volume(0.1)


roomList = []