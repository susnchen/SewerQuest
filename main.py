import pygame, pygame.mixer
import player
import bullet
import room
import constants as c
import collision
import level

# <editor-fold desc="initialize pygame library">
pygame.init()
pygame.font.init()
pygame.mixer.init()
# </editor-fold>

# <editor-fold desc="start game variables">
screen = pygame.display.set_mode((c.gamew, c.gameh))
font = pygame.font.Font("assets\\font.ttf",12)
menuFont = pygame.font.Font("assets\\font.ttf",32)

clock = pygame.time.Clock()

running = True
gameoverScreen = False
gameScreen = False
startScreen = False
startMenu = False
# </editor-fold>

c.mainAudio.play()

# <editor-fold desc="functions">

def button(surfacePos, surfaceW, surfaceH):
    mousePos = pygame.mouse.get_pos()
    mask = pygame.Rect(surfacePos,(surfaceW,surfaceH))
    pressed = False

    if mask.collidepoint(mousePos[0],mousePos[1]):
        pressed = True

    return pressed

def posInt(int):
    posInt = 0
    if int > 0:
        posInt = int

    return posInt

def transistionIn(img, posx = 0, posy = 0):
    for i in range(0, 255, 5):
        img.set_alpha(i)
        screen.blit(img, (posx, posy))
        pygame.display.update()

def pause(score):
    global running,gameoverScreen,gameScreen,highscoreScreen
    clock.tick(15)
    pause = True

    while pause:
        titletxt = menuFont.render("PAUSED",1, (255, 255, 255))
        scoretxt = font.render("SCORE: " + str(score),1,(255,255,255))

        screen.blit(c.menuBackground,(0,0))
        screen.blit(c.cat,(244, 157))
        screen.blit(c.continueButton,(240,356))
        screen.blit(c.menuButton,(215,422))
        screen.blit(c.exitButton,(331, 422))
        screen.blit(titletxt,(212,64))
        screen.blit(scoretxt,(260,300))

        pygame.display.update()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:

                #continue button
                if button((240, 356),159,45):
                    transistionIn(c.transistionImg)
                    pause = False

                #menu button
                if button((215,422),94,45):
                    transistionIn(c.transistionImg)
                    gameoverScreen = False
                    gameScreen = False
                    highscoreScreen = False
                    pause = False

                #exit button
                if button((330,422),94,45):
                    transistionIn(c.transistionImg)
                    gameoverScreen = False
                    gameScreen = False
                    highscoreScreen = False
                    running = False
                    pause = False

def gameOver(state,score):
    global gameoverScreen, running, highscoreScreen
    name = ""
    while gameoverScreen:
            clock.tick(15)
            titletxt = menuFont.render(state,1, (255, 255, 255))
            scoretxt = font.render("SCORE: " + str(score),1,(255,255,255))

            if state == "GAME OVER":screen.blit(c.sadCat,(244, 157))
            else:screen.blit(c.cat,(244, 157))

            nametxt = font.render("ENTER NAME: " + name,1,(255,255,255))

            screen.blit(c.menuBackground,(0,0))
            screen.blit(c.cat,(244, 157))
            screen.blit(c.continueButton,(240,400))
            screen.blit(titletxt,(175,60))
            screen.blit(scoretxt,(250,300))
            screen.blit(nametxt, (250 - 7*len(name), 350))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    gameoverScreen = False
                    running = False
                    highscoreScreen = False

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if button((240,400),198,45):
                        transistionIn(c.transistionImg)
                        gameoverScreen = False

                if ev.type == pygame.KEYDOWN:
                    if ev.unicode.isalpha():
                        name += ev.unicode.upper()

                    elif ev.key == pygame.K_SPACE:
                        name += " "

                    elif ev.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    elif ev.key == pygame.K_RETURN:
                        transistionIn(c.transistionImg)
                        gameoverScreen = False


            pygame.display.update()

    highscoreFile = open("highscore.txt","a")
    highscoreFile.write(name + ", " + str(score) + "\n")
    highscoreFile.close()

    return name

# </editor-fold>

while running:

    # <editor-fold desc="initialize start game variables">
    levelNum = 0
    levelObj = level.Level(levelNum)
    curRoomNum = 0
    curRoom = levelObj.roomList[curRoomNum]
    time = 120
    timecount = 0
    startMenu = True
    startScreen = True
    gameScreen = True
    gameoverScreen = True
    highscoreScreen = True
    timeBetweenBullet = 0
    timeBetweenDamage = 0
    nextRoom = 0
    bulletlist = []
    background = curRoom.roomImg
    score = time
    name = ""
    # </editor-fold>

    # <editor-fold desc="start screen">

    while startScreen:
        screen.blit(c.startScreenImg,(0,0))

        clock.tick(15)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                startScreen = False
                startMenu = False
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False

            if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                transistionIn(c.transistionImg)
                startScreen = False

        pygame.display.update()

    # </editor-fold>

    # <editor-fold desc = "start menu">

    while startMenu:
        clock.tick(15)
        titletxt = menuFont.render("SEWER QUEST",1, (255, 255, 255))

        screen.blit(c.menuBackground,(0,0))
        screen.blit(c.cat,(244, 157))
        screen.blit(c.startButton,(264,296))
        screen.blit(c.highscoresButton,(221,357))
        screen.blit(c.exitButton,(273, 418))
        screen.blit(titletxt,(135,60))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                startMenu = False
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if button((264,296),111,45):
                    transistionIn(c.transistionImg)
                    startMenu = False

                #highscores button
                if button((221,357),198,45):
                    transistionIn(c.transistionImg)
                    startMenu = False
                    gameScreen = False
                    gameoverScreen = False

                #exit button
                if button((273,418),94,45):
                    transistionIn(c.transistionImg)
                    startMenu = False
                    gameScreen = False
                    gameoverScreen = False
                    running = False
                    highscoreScreen = False

        pygame.display.update()

    # </editor-fold>

    playerObj = player.Player()

    # <editor-fold desc="game screen">

    while gameScreen:
        clock.tick(60)

        #timer counting down each second
        timecount += 1
        if timecount == 60:
            timecount = 0
            score -= 1
            time -= 1

        timeBetweenBullet += 1
        timeBetweenDamage += 1

        #timer text
        timetxt = font.render("TIME: " + str(time), 1, (255, 255, 255))

        pausetxt = font.render("PAUSE", 1, (255, 255, 255))

        #update current room and player position
        playerpos = (playerObj.x, playerObj.y)
        curRoom = levelObj.roomList[curRoomNum]

        #check if player is collided with the portal to other rooms
        if collision.checkTransition(playerpos) != 4:
            bulletlist = []
            nextRoom = room.transition(collision.checkTransition(playerpos), curRoomNum)

            curRoomNum = nextRoom[0]

            if nextRoom[1] == 0:
                playerObj.move((320, 0), "down")

            elif nextRoom[1] == 1:
                playerObj.move((608, 224), "left")

            elif nextRoom[1] == 2:
                playerObj.move((288, 480), "up")

            elif nextRoom[1] == 3:
                playerObj.move((0, 224), "right")

        #check if player is collided with a fish
        if curRoom.fishPlacement != False and collision.objectCollider(playerpos, curRoom.fishPlacement):
            levelObj.fishesLeft -= 1
            score += 5
            curRoom.fishPlacement = False

        #move the player
        playerObj.movement(curRoom)

        #move all bullets
        for i in bulletlist:
            if i.collide(curRoom) == True:
                del bulletlist[bulletlist.index(i)]
                continue
            i.movement()

        #move all enemy
        for i in curRoom.enemyList:
            i.timeBetweenEnemy += 1
            if i.playerCollision(playerpos) and timeBetweenDamage >= 60:
                timeBetweenDamage = 0
                playerObj.health -= 1

            if i.timeBetweenEnemy >= 2:
                i.timeBetweenEnemy = 0
                i.movement(playerpos, curRoom)

            enemydeath = i.deathCollision(bulletlist)
            if enemydeath[0]:
                del bulletlist[bulletlist.index(enemydeath[1])]
                del curRoom.enemyList[curRoom.enemyList.index(i)]
                score += 4
                c.onHit.play()

        #display all items
        # <editor-fold desc="display">
        screen.blit(curRoom.roomImg, (-32, -32))

        for i in bulletlist:
            screen.blit(i.bulletimg,(i.x,i.y))
        for i in curRoom.enemyList:
            screen.blit(i.img,(i.x,i.y))

        screen.blit(playerObj.img, (playerObj.x,playerObj.y))

        if curRoom.fishPlacement != False:
            screen.blit(c.fishImg[1], curRoom.fishPlacement)

        for i in range(0, playerObj.health):
            screen.blit(c.heartImg, (512 + i * 32, 0))

        for i in range(0, c.levelSettings[levelNum]):
            screen.blit(c.fishImg[0], (576 - i * 32, 480))

        for i in range(0, c.levelSettings[levelNum] - levelObj.fishesLeft):
            screen.blit(c.fishImg[1], (576 - i * 32, 480))

        screen.blit(timetxt, (100, 3))
        screen.blit(pausetxt, (6, 3))

        pygame.display.update()

        # </editor-fold>

        for ev in pygame.event.get():
            #if player tries to quit
            if ev.type == pygame.QUIT:
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                #if you pressed the pause button
                if button((0,0),64,32):
                    pause(score)

                # if you shoot
                elif timeBetweenBullet > 20:
                    timeBetweenBullet = 0
                    bulletlist += [bullet.Bullet(playerpos, pygame.mouse.get_pos())]
                    c.shoot.play()

        if playerObj.health == 0 or levelObj.fishesLeft == 0:
            gameScreen = False

    # </editor-fold>

    if playerObj.health > 0 and gameoverScreen:
        name = gameOver("VICTORY", 2*score)

    elif gameoverScreen:
        name = gameOver("GAME OVER", score)

    # <editor-fold desc="highscore file indexing">
    highscoreFile = open("highscore.txt","r")

    if highscoreScreen:
        lines = highscoreFile.readlines()
        nameList = []
        scoreList = []

        for i in lines:
            line = i.split(",")
            if line[0][0] != "#":
                nameList += [font.render(line[0],1,(255,255,255))]
                scoreList += [font.render(line[1][:-1],1,(255,255,255))]

        highscoreRange1 = posInt(len(nameList) - 9)
        highscoreRange2 = len(nameList)

        highscoreFile.close()
    # </editor-fold>

    # <editor-fold desc="highscore screen">
    while highscoreScreen:
        clock.tick(15)
        titletxt = menuFont.render("HIGH SCORE", 1, (255, 255, 255))

        screen.blit(c.menuBackground, (0, 0))
        screen.blit(titletxt, (150, 60))
        screen.blit(c.menuButton,(215,422))
        screen.blit(c.exitButton,(331, 422))

        for i in range (highscoreRange1,highscoreRange2):
            screen.blit(nameList[i],(150, 135 + (i - highscoreRange1)*30))
            screen.blit(scoreList[i],(400, 135 + (i - highscoreRange1)*30))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
                highscoreScreen = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                #menu button
                if button((215, 422), 94, 45):
                    transistionIn(c.transistionImg)
                    highscoreScreen = False

                #exit button
                if button((331, 422), 94, 45):
                    transistionIn(c.transistionImg)
                    running = False
                    highscoreScreen = False

        pygame.display.update()
        # </editor-fold>