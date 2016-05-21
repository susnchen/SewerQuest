import pygame
import platform

#checks the operating system
system = platform.system()

#the directory names is defined based on the operating system
guiDir = ""
assetsDir = ""
playerSpritesDir = ""
enemySpritesDir = ""
audioDir = ""
imageDir = ""
roomDir = ""

#linux operating system
if system == "Linux":
    guiDir = "assets/images/gui/"
    assetsDir = "assets/"
    playerSpritesDir = "assets/images/playersprites/"
    enemySpritesDir = "assets/images/enemysprites/"
    audioDir = "assets/audio/"
    imageDir = "assets/images/"
    roomDir = "assets/images/rooms/"


#windows operating system
elif system == "Windows":
    guiDir = "assets\\images\\gui\\"
    assetsDir = "assets\\"
    playerSpritesDir = "assets\\images\\playersprites\\"
    enemySpritesDir = "assets\\images\\enemysprites\\"
    audioDir = "assets\\audio\\"
    imageDir = "assets\\images\\"
    roomDir = "assets\\images\\rooms\\"

#mac operating system
elif system == "Darwin":
    guiDir = "~assets/images/gui/"
    assetsDir = "~assets/"
    playerSpritesDir = "~assets/images/playersprites/"
    enemySpritesDir = "~assets/images/enemysprites/"
    audioDir = "~assets/audio/"
    imageDir = "~assets/images/"
    roomDir = "~assets/images/rooms/"

else:
    print("ERROR: invalid operating system")
    quit()

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.font.init()

gamew = 640
gameh = 512

#establish the 2 fonts that will be used in this program
font = pygame.font.Font(assetsDir + "font.ttf",12)
menuFont = pygame.font.Font(assetsDir + "font.ttf",32)

#change the game title and icon
pygame.display.set_caption("Sewer Quest")
pygame.display.set_icon(pygame.image.load(guiDir + "cat.png"))

#display a loading Screen because audio takes a while to load, especially on slow computers
screen = pygame.display.set_mode((gamew, gameh))
background = pygame.Surface(screen.get_size()).convert()
background.fill((0,0,0))

text = font.render("Loading...", 1, (255, 255, 255))

background.blit(text,(0,0))
screen.blit(background, (0,0))

pygame.display.flip()

#the bullet image
bullet = pygame.image.load(imageDir + "bullet.png")

#the player sprites, which keys corresponding to each state and values corresponding to the pygame surfaces the game will loop through
playerSprites = {
    "left": [None]*3,
    "right": [None]*3,
    "up": [None]*3,
    "down":[None]*3,
    "idlel": [None]*3,
    "idled": [None]*3,
    "idleu": [None]*3,
    "idler": [None]*3
}

#adds all sprite according to their sprite
for state in playerSprites:
    #all sprites have 3 images
    for i in range(0,3):
        playerSprites[state][i] = pygame.image.load(playerSpritesDir + state + str(i) + ".png")

#same with the enemySprites
enemySprites = {
    "left": [None]*3,
    "right": [None]*3,
    "up": [None]*3,
    "down":[None]*3
}

for state in enemySprites:
    #all sprites have 3 images
    for i in range(0,3):
        enemySprites[state][i] = pygame.image.load(enemySpritesDir + state + str(i) + ".png")


#a list of all the door positions, each door has 2 positions
doorPos = [(288,0),(320,0),(639,224),(639,256),(320,480),(288,480),(0,224),(0,256)]

#all gui images such as buttons, screens, and icons
transitionImg = pygame.image.load(guiDir + "blackScreen.png")
startButton = pygame.image.load(guiDir + "startButton.png")
highscoresButton = pygame.image.load(guiDir + "highscoresButton.png")
exitButton = pygame.image.load(guiDir + "exitButton.png")
continueButton = pygame.image.load(guiDir + "continueButton.png")
menuButton = pygame.image.load(guiDir + "menuButton.png")
menuBackground = pygame.image.load(guiDir + "bg.png")
cat = pygame.image.load(guiDir + "cat.png")
sadCat = pygame.image.load(guiDir + "sadCat.png")
level1Button = pygame.image.load(guiDir + "level1Button.png")
level2Button = pygame.image.load(guiDir + "level2Button.png")

#heart and fish images
heartImg = pygame.image.load(guiDir + "heart.png")

fishImg = [
    pygame.image.load(guiDir + "fish0.png"),
    pygame.image.load(guiDir + "fish1.png")
]

#mute button icons
muteButton = [
    pygame.image.load(guiDir + "muteButton0.png"),
    pygame.image.load(guiDir + "muteButton1.png")
]

#the enemy speed in level 1 and level 2
enemySpeedSetting = [4,8]

#fish placements for each level
fishPlacements = {
    #the key corresponds to the level number 0 equals level 1 and 1 equals level2
    #the items of the list in the value corresponds to the position of the fishes in each room
    #the index of that item corresponds to the room number
    #if the value is False, it means there are no fishes
    0:[(240,320), False, False,(96,280),(240,320), False, (500,96),False,False,(500,96),(500,96)],
    1:[(240,320), False, False,(96,280),(32,32),False,False,(500,96),False,False,(32,32),False,(32,32),(96,280),False,False],
}

#the image for each room
roomImgs = {
    #level 1
    0 : [None]*11,
    #level 2
    1 : [None]*16
}

#use loops to put each image for each room on each level into the roomImgs dictionary for level 1
for i in range(0,11):
    doorNum = str(i)

    #make all numbers 2 characters long, so "0" turns into "00" and "1" turns into "01"
    if i < 10:
        doorNum = "0" + str(i)

    #set the room i of level 1 in the roomImg dictionary according to their room number
    roomImgs[0][i] = pygame.image.load(roomDir + "room0" + doorNum + ".png")

#same with level 2
for i in range(0,16):
    doorNum = str(i)

    if i < 10:
        doorNum = "0" + str(i)

    roomImgs[1][i] = pygame.image.load(roomDir + "room1" + doorNum + ".png")

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
            ("win",-1,9,-1)
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
            (14,-1,"win",-1)
    ]
}

#loads each audio file, and set their volume to be close to each other
mainAudio = pygame.mixer.Sound(audioDir + "camel.wav")
mainAudio.set_volume(0.1)
onHit = pygame.mixer.Sound(audioDir + "onHit.wav")
shoot = pygame.mixer.Sound(audioDir + "shoot.wav")
shoot.set_volume(0.1)

#text that will display during certain parts of the game such as outro and intro
introtxt = ["OH NO I GOTTA GET ALL MY FISHES.", "IM HUNGRY. BUT WOW THOSE DARN RATS!", "I\'M SO HUNGRY I BETTER GET GOING!"]
for i in range (0,len(introtxt)):
    introtxt[i] = font.render(introtxt[i],1, (255, 255, 255))
outrotxt = {
    0:["YES!!! I GOT ALL MY FISHES!", "THAT WAS GREAT. I LOVE MY fISH.", "AHAH SCREW THOSE RATS!!11!!!!"],
    1:["oh no!"],
    2:["imbad!","alkjfal;kdjf"]
}
for list in range(0,len(outrotxt)):
    for i in range (0,len(outrotxt[list])):
        outrotxt[list][i] = font.render(outrotxt[list][i],1, (255, 255, 255))

pausetxt = menuFont.render("PAUSED",1, (255, 255, 255))
bonustxt = font.render(" + BONUS!", 1,(255,255,255))
titletxt = menuFont.render("SEWER QUEST",1, (255, 255, 255))
highscoretxt = menuFont.render("HIGH SCORE", 1, (255, 255, 255))
continuetxt = font.render("PRESS ANYTHING TO CONTINUE", 1,(255,255,255))
pauseButton = font.render("PAUSE", 1,(255,255,255))
