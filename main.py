# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# main.py
# using classes and functions from other files, a game consisting of 2 levels are created

# input: key press and mouse press by the user
# output: displays the game on the screen and player score in the highscore.txt file

import pygame, pygame.mixer
import player
import bullet
import room
import constants as c
import collision
import level
import audio

# <editor-fold desc="initialize pygame library">
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Sewer Quest")
# </editor-fold>

# <editor-fold desc="start game variables">
#set screen with reference to the constants file
screen = pygame.display.set_mode((c.gamew, c.gameh))

clock = pygame.time.Clock()

#the persistent audio in this program
mainAudio = audio.Audio(c.mainAudio)

#the states of loops/screen in the running loop
running = True
startMenu = True
startScreen = True
gameScreen = True
gameoverScreen = True
highscoreScreen = True
# </editor-fold>

# <editor-fold desc="functions">

#checks if the mouse is over a surface (button)
def button(surfacePos, surfaceW, surfaceH):
    mousePos = pygame.mouse.get_pos()
    mask = pygame.Rect(surfacePos,(surfaceW,surfaceH))
    pressed = False

    if mask.collidepoint(mousePos[0],mousePos[1]):
        pressed = True

    return pressed

#returns the closest positive integer
def posInt(num):
    posInt = 0
    if num > 0:
        posInt = num

    return int(posInt)

#slowly displays a picture
def transitionIn(surface, posx = 0, posy = 0):
    for i in range(0, 255, 5):
        mainAudio.update(255)
        clock.tick(255)
        surface.set_alpha(i)
        screen.blit(surface, (posx, posy))
        pygame.display.update()

#pauses the game
def pause(score):
    global running,gameoverScreen,gameScreen,highscoreScreen,endScreen
    pause = True

    #creates title text of the screen and the score text
    scoretxt = c.font.render("SCORE: " + str(score),1,(255,255,255))

    while pause:
        #updates the position of the mainAudio if it is not muted
        if not mainAudio.muteState:mainAudio.update(15)
        clock.tick(15)

        #display all buttons and images on the screen
        screen.blit(c.menuBackground,(0,0))
        screen.blit(c.cat,(244, 157))
        screen.blit(c.continueButton,(240,356))
        screen.blit(c.menuButton,(215,422))
        screen.blit(c.exitButton,(331, 422))
        screen.blit(c.pausetxt,(212,64))
        screen.blit(scoretxt,(260,300))
        screen.blit(c.muteButton[mainAudio.muteState], (5,5))

        pygame.display.update()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()


            #if the player presses the:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if button((5,5),32,32): mainAudio.mute()

                #continue button/resume the game
                if button((240, 356),159,45):
                    transitionIn(c.transitionImg)
                    pause = False

                #menu button
                if button((215,422),94,45):
                    #turn everything off but does not escape the program
                    #this causes the game go back to the main menu
                    transitionIn(c.transitionImg)
                    gameoverScreen = False
                    gameScreen = False
                    highscoreScreen = False
                    pause = False

                #exit button
                if button((330,422),94,45):
                    #turns everything off, including the running loop
                    transitionIn(c.transitionImg)
                    gameoverScreen = False
                    gameScreen = False
                    highscoreScreen = False
                    running = False
                    pause = False
                    endScreen = False

            if ev.type == pygame.KEYDOWN:
                #escape button also resumes the game
                if ev.key == pygame.K_ESCAPE:
                    transitionIn(c.transitionImg)
                    pause = False

#the gameover/victory screen
def gameOver(state,score,fishesleft):
    global gameoverScreen, running, highscoreScreen,endScreen
    name = ""
    #the bonus text that will display if the player won

    #if the player won, a bonus score of 100 points will be rewarded
    if state == "VICTORY" and fishesleft == 0:bonusScore = 100
    else: bonusScore = 0

    quit = False

    while gameoverScreen:
        if not mainAudio.muteState: mainAudio.update(15)
        clock.tick(15)

        #title according to state, (victory or game over)
        titletxt = c.menuFont.render(state,1, (255, 255, 255))
        scoretxt = c.font.render("SCORE: " + str(score),1,(255,255,255))

        #changes the cat image according to whether player won or not
        if state == "GAME OVER":screen.blit(c.sadCat,(244, 157))
        else:screen.blit(c.cat,(244, 157))

        #updates the name
        nametxt = c.font.render("ENTER NAME: " + name,1,(255,255,255))

        #displays all images and text
        screen.blit(c.menuBackground,(0,0))
        screen.blit(c.cat,(244, 157))
        screen.blit(c.continueButton,(240,400))
        screen.blit(c.muteButton[mainAudio.muteState], (5,5))
        screen.blit(titletxt,(175,60))
        screen.blit(scoretxt,(250,300))
        screen.blit(nametxt, (250 - 7*len(name), 350))

        #shows the bonus score being added to score
        if bonusScore > 0:
            screen.blit(c.bonustxt,(380,300))
            score += 5
            bonusScore -= 5

        pygame.display.update()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                gameoverScreen = False
                running = False
                highscoreScreen = False
                endScreen = False
                quit = True

            #if the player presses:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if button((5,5),32,32): mainAudio.mute()

                #continue button and name is not blank
                if button((240,400),198,45) and name != "":
                    transitionIn(c.transitionImg)
                    gameoverScreen = False

            if ev.type == pygame.KEYDOWN and len(name) < 8:
                #if an alphabet is pressed
                if ev.unicode.isalpha():
                    #adds the capitalized version of it (for consistency) to the name
                    name += ev.unicode.upper()

                #adds space compatibility
                elif ev.key == pygame.K_SPACE:
                    name += " "

                #if the backspace button was pressed
                elif ev.key == pygame.K_BACKSPACE:
                    #delete the last letter in name
                    name = name[:-1]

                #return key also works as a continue button
                elif ev.key == pygame.K_RETURN and name != "":
                    transitionIn(c.transitionImg)
                    gameoverScreen = False

    if not quit:
        highscoreFile = open("highscore.txt","a")
        highscoreFile.write(name + ", " + str(score) + "\n")
        highscoreFile.close()

    return name

# </editor-fold>

while running:

    # <editor-fold desc="initialize start game variables">
    #reset all game variables
    startMenu = True
    startScreen = True
    gameScreen = True
    gameoverScreen = True
    highscoreScreen = True
    levelSelect = False
    endScreen = True
    levelNum = 0
    time = 180
    timecount = 0
    timeBetweenBullet = 0
    timeBetweenDamage = 0
    nextRoom = 0
    bulletlist = []
    score = time
    name = ""
    victory = False
    # </editor-fold>

    # <editor-fold desc="start screen">
    #the introduction screen
    while startScreen:
        if not mainAudio.muteState: mainAudio.update(15)
        clock.tick(15)

        screen.blit(c.menuBackground, (0, 0))
        screen.blit(c.cat, (244, 157))
        screen.blit(c.titletxt,(135,60))
        screen.blit(c.continuetxt,(150,450))

        for i in range(0, len(c.introtxt)):
            screen.blit(c.introtxt[i], (125, 300 + i * 30))

        pygame.display.update()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                startScreen = False
                startMenu = False
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False

            if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                transitionIn(c.transitionImg)
                startScreen = False

    # </editor-fold>

    # <editor-fold desc = "start menu">
    #the start menu
    while startMenu:
        if not mainAudio.muteState:mainAudio.update(15)
        clock.tick(15)

        screen.blit(c.menuBackground,(0,0))
        screen.blit(c.cat,(244, 157))
        if levelSelect:
            screen.blit(c.level1Button,(182,296))
            screen.blit(c.level2Button,(330,296))
        else:screen.blit(c.startButton,(264,296))
        screen.blit(c.highscoresButton,(221,357))
        if button((5,5),32,32): screen.blit(c.muteButton[int(not(bool(mainAudio.muteState)))], (5,5))
        else: screen.blit(c.muteButton[mainAudio.muteState], (5,5))
        screen.blit(c.exitButton,(273, 418))
        screen.blit(c.titletxt,(135,60))

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                startMenu = False
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if button((5,5),32,32): mainAudio.mute()

                #level1 and level2 buttons for level select
                if levelSelect:
                    if button((182,296),128,45):
                        startMenu = False
                        transitionIn(c.transitionImg)
                        levelNum = 0

                    if button((330,296),128,45):
                        startMenu = False
                        transitionIn(c.transitionImg)
                        levelNum = 1

                #start button, if pressed, will show level select buttons
                if button((264,296),111,45) and levelSelect == False:
                    levelSelect = True

                #highscores button
                if button((221,357),198,45):
                    transitionIn(c.transitionImg)
                    startMenu = False
                    gameScreen = False
                    gameoverScreen = False

                #exit button
                if button((273,418),94,45):
                    transitionIn(c.transitionImg)
                    startMenu = False
                    gameScreen = False
                    gameoverScreen = False
                    running = False
                    endScreen = False
                    highscoreScreen = False

        pygame.display.update()

    levelObj = level.Level(levelNum)
    curRoomNum = 8
    curRoom = levelObj.roomList[curRoomNum]
    curRoom.visited = True
    background = curRoom.roomImg

    # </editor-fold>

    playerObj = player.Player()

    # <editor-fold desc="game screen">

    while gameScreen:
        if not mainAudio.muteState:mainAudio.update(25)
        clock.tick(25)

        #timer counting down each second
        timecount += 1
        if timecount == 25:
            timecount = 0
            score -= 1
            time -= 1

        timeBetweenBullet += 1
        timeBetweenDamage += 1

        #timer text
        timetxt = c.font.render("TIME: " + str(time), 1, (255, 255, 255))

        #update current room and player position
        playerpos = (playerObj.x, playerObj.y)

        #check if player is collided with the portal to other rooms
        door = collision.checkTransition(playerpos)

        if door != -1:
            nextRoom = room.transition(door, curRoomNum, levelNum)
            curRoomNum = nextRoom[0]
            print(curRoomNum)
            if curRoomNum == "win":
                victory = True

            else:
                bulletlist = []

                curRoom = levelObj.roomList[curRoomNum]
                curRoom.visited = True

                if nextRoom[1] == 0:
                    playerObj.x = 320
                    playerObj.y = 40

                elif nextRoom[1] == 1:
                    playerObj.x = 600
                    playerObj.y = 224

                elif nextRoom[1] == 2:
                    playerObj.x = 288
                    playerObj.y = 440

                elif nextRoom[1] == 3:
                    playerObj.x = 8
                    playerObj.y = 224

        #check if player is collided with a fish
        if curRoom.fishPlacement != False and collision.spritesCollision(playerpos, curRoom.fishPlacement):
            levelObj.fishLeft -= 1
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
            if i.playerCollision(playerpos) and timeBetweenDamage >= 25:
                timeBetweenDamage = 0
                playerObj.health -= 1
                playerObj.damaged = True

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

        for i in range(0, levelObj.fishNums):
            screen.blit(c.fishImg[0], (576 - i * 32, 480))

        for i in range(0, levelObj.fishNums - levelObj.fishLeft):
            screen.blit(c.fishImg[1], (576 - i * 32, 480))

        screen.blit(timetxt, (100, 3))
        screen.blit(c.pauseButton, (6, 3))

        pygame.display.update()

        # </editor-fold>

        for ev in pygame.event.get():
            #if player tries to quit
            if ev.type == pygame.QUIT:
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                #if you pressed the pause button
                if button((0,0),64,32):
                    pause(score)

                # if you shoot
                elif timeBetweenBullet > 12:
                    timeBetweenBullet = 0
                    bulletlist += [bullet.Bullet(playerpos, pygame.mouse.get_pos())]
                    c.shoot.play()

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    pause(score)

        if playerObj.health == 0 or levelObj.fishLeft == 0 or time <= 0 or victory:
            gameScreen = False

    # </editor-fold>
    outrotxtNum = 0
    if time <= 0 or playerObj.health <= 0:
        outrotxtNum = 2
    elif levelObj.fishLeft > 0:
        outrotxtNum = 1

    while endScreen:
        if not mainAudio.muteState: mainAudio.update(15)
        clock.tick(15)

        screen.blit(c.menuBackground, (0, 0))
        screen.blit(c.cat, (244, 157))
        screen.blit(c.titletxt,(135,60))
        screen.blit(c.continuetxt,(150,450))

        for i in range(0, len(c.outrotxt[outrotxtNum])):
            screen.blit(c.outrotxt[outrotxtNum][i], (150, 300 + i * 30))

        pygame.display.update()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                endScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False

            if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                transitionIn(c.transitionImg)
                endScreen = False

    # </editor-fold>

    if (playerObj.health > 0 and time > 0 and gameoverScreen):
        name = gameOver("VICTORY", score, levelObj.fishLeft)

    elif gameoverScreen:
        name = gameOver("GAME OVER", score, levelObj.fishLeft)

    # <editor-fold desc="highscore file indexing">
    highscoreFile = open("highscore.txt","r")

    if highscoreScreen:
        lines = highscoreFile.readlines()
        highscoreRange = posInt(len(lines) - 9)
        highscoreDict = {}

        for i in range(highscoreRange,len(lines)):
            line = lines[i].split(",")
            if line[0][0] != "#":
                highscoreDict[c.font.render(line[0],1,(255,255,255))] = c.font.render(line[1][:-1],1,(255,255,255))

        highscoreRange = posInt(len(highscoreDict) - 9)

        highscoreFile.close()
    # </editor-fold>

    # <editor-fold desc="highscore screen">
    while highscoreScreen:
        if not mainAudio.muteState:mainAudio.update(15)
        clock.tick(15)

        screen.blit(c.menuBackground, (0, 0))
        screen.blit(c.highscoretxt, (150, 60))
        screen.blit(c.menuButton,(215,422))
        screen.blit(c.exitButton,(331, 422))
        screen.blit(c.muteButton[mainAudio.muteState], (5,5))

        lineNum = 0
        for key,value in highscoreDict.items():
            screen.blit(key,(175, 135 + (lineNum - highscoreRange)*30))
            screen.blit(value,(410, 135 + (lineNum - highscoreRange)*30))
            lineNum += 1

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
                endScreen = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if button((5,5),32,32): mainAudio.mute()

                #menu button
                if button((215, 422), 94, 45):
                    transitionIn(c.transitionImg)
                    highscoreScreen = False

                #exit button
                if button((331, 422), 94, 45):
                    transitionIn(c.transitionImg)
                    running = False
                    endScreen = False
                    gameoverScreen = False
                    highscoreScreen = False

        pygame.display.update()
        # </editor-fold>