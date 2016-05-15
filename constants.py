import pygame
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.font.init()

gamew = 640
gameh = 512

#change the game title and icon
pygame.display.set_caption("Sewer Quest")
pygame.display.set_icon(pygame.image.load("assets\\images\\gui\\cat.png"))

#Loading Screen because audio takes a while to load
screen = pygame.display.set_mode((gamew, gameh))
background = pygame.Surface(screen.get_size())
font = pygame.font.Font(None, 36)
text = font.render("Loading...", 1, (255, 255, 255))
background.blit(text, (0,0))

pygame.display.flip()

#the bullet image
bullet = pygame.image.load("assets\\images\\bullet.png")

#the enemy sprites
enemyimg = pygame.image.load("assets\\images\\enemy.png")

#the player sprites, which keys corresponding to each state and values corresponding to the pygame surfaces the game will loop through
playerSprites = {
    "left": [None]*4,
    "right": [None]*4,
    "idlel": [None]*4,
    "idler": [None]*4
}

#adds all sprite according to their sprite
for state in playerSprites:
    #all sprites have 4 images
    for i in range(0,4):
        playerSprites[state][i] = pygame.image.load("assets\\images\\playersprites\\" + state + str(i) + ".png")

#a list of all the door positions, each door has 2 positions
doorPos = [(288,0),(320,0),(639,224),(639,256),(320,480),(288,480),(0,224),(0,256)]

#all gui images such as buttons, screens, and icons
startScreenImg = pygame.image.load("assets\\images\\gui\\startScreen.png")
transistionImg = pygame.image.load("assets\\images\\gui\\blackScreen.png")

startButton = pygame.image.load("assets\\images\\gui\\startButton.png")
highscoresButton = pygame.image.load("assets\\images\\gui\\highscoresButton.png")
exitButton = pygame.image.load("assets\\images\\gui\\exitButton.png")
continueButton = pygame.image.load("assets\\images\\gui\\continueButton.png")
menuButton = pygame.image.load("assets\\images\\gui\\menuButton.png")
menuBackground = pygame.image.load("assets\\images\\gui\\bg.png")
cat = pygame.image.load("assets\\images\\gui\\cat.png")
sadCat = pygame.image.load("assets\\images\\gui\\sadCat.png")
level1Button = pygame.image.load("assets\\images\\gui\\level1Button.png")
level2Button = pygame.image.load("assets\\images\\gui\\level2Button.png")

#heart and fish images
heartImg = pygame.image.load("assets\\images\\gui\\heart.png")

fishImg = [
    pygame.image.load("assets\\images\\gui\\fish0.png"),
    pygame.image.load("assets\\images\\gui\\fish1.png")
]

#mute button icons
muteButton = [
    pygame.image.load("assets\\images\\gui\\muteButton0.png"),
    pygame.image.load("assets\\images\\gui\\muteButton1.png")
]

#the enemy speed in level 1 and level 2
enemySpeedSetting = [4,8]

#fish placements for each level
fishPlacements = {
    0:[(240,320), False, False,(96,280),(240,320), False, (500,96),False,False,(500,96)],
    1:[(240,320), False, False,(96,280),(32,32),False,False,(500,96),False,False,(32,32),False,(32,32),(96,280),False,False],
}

#the image for each room
roomImgs = {
    #level 1
    0 : [None]*10,
    #level 2
    1 : [None]*15
}

#use loops to put each image for each room on each level into the roomImgs dictionary for level 1
for i in range(0,10):
    doorNum = str(i)

    #make all numbers 2 characters long, so "0" turns into "00" and "1" turns into "01"
    if i < 10:
        doorNum = "0" + str(i)

    #set the room i of level 1 in the roomImg dictionary according to their room number
    roomImgs[0][i] = pygame.image.load("assets\\images\\rooms\\room0" + doorNum + ".png")

#same with level 2
for i in range(0,15):
    doorNum = str(i)

    if i < 10:
        doorNum = "0" + str(i)

    roomImgs[1][i] = pygame.image.load("assets\\images\\rooms\\room1" + doorNum + ".png")

#a dictionary containing which each door of each room leads to
roomDoorDict = {
    #level 1
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
    #level 2
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
            (-1,12,10,-1),
            (-1,13,-1,11),
            (14,-1,-1,12),
            (-1,15,13,-1),
            (14,-1,-1,-1)
    ]
}

#loads each audio file, and set their volume to be close to each other
mainAudio = pygame.mixer.Sound("assets\\audio\\camel.wav")
mainAudio.set_volume(0.1)
onHit = pygame.mixer.Sound("assets\\audio\\onHit.wav")
shoot = pygame.mixer.Sound("assets\\audio\\shoot.wav")
shoot.set_volume(0.1)