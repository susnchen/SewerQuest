
# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# main.py
# using classes and functions from other files, a game consisting of 2 levels was created

# input: key press and mouse press by the user
# output: displays the game on the screen and player score in the highscore.txt file

import pygame, pygame.mixer
from operator import itemgetter
import player
import bullet
import room
import constants as c
import collision
import level
import audio

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Sewer Quest")
clock = pygame.time.Clock()

#set screen with reference to the constants file
screen = pygame.display.set_mode((c.gamew, c.gameh))

#the audio in this program
mainAudio = audio.Audio(c.mainAudio)
gameoverAudio = audio.Audio(c.playerLose)
victoryAudio = audio.Audio(c.playerWin)
outroMusic = victoryAudio

#the states of loops/screen in the running loop
running = True
startMenu = True
startScreen = True
gameScreen = True
gameoverScreen = True
highscoreScreen = True
endingScreen = True

#checks if the mouse is over a surface (button)
def mouseHover(surfacePos, surfaceW, surfaceH):
    #creates a mask Rect for the button
    mousePos = pygame.mouse.get_pos()
    mask = pygame.Rect(surfacePos,(surfaceW,surfaceH))
    hover = False

    #if the mouse collide with the mask Rect, returns True, else, False
    if mask.collidepoint(mousePos[0],mousePos[1]):
        hover = True

    return hover

#returns the closest positive integer
def posInt(num):
    posInt = 0
    if num > 0:
        posInt = num

    return int(posInt)

#slowly displays a picture
def transitionIn(surface, posx = 0, posy = 0):
    #using a loop and the alpha values of a surface, the surface slowly appears
    for i in range(0, 255, 51):
        mainAudio.update(15)
        clock.tick(15)
        surface.set_alpha(i)
        screen.blit(surface, (posx, posy))
        pygame.display.update()

#pauses the game
def pause(score):
    #global variables that controlls every loop after the gameScreen loop and the main running loop
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
            #exits the game, turn off all loops
            if ev.type == pygame.QUIT:
                gameoverScreen = False
                gameScreen = False
                highscoreScreen = False
                running = False
                pause = False
                endScreen = False
                pygame.quit()

            #if the player presses the:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if mouseHover((5,5),32,32):
                    c.click.play()
                    mainAudio.mute()

                #continue button/resume the game, just brings you back to the gameScreen
                if mouseHover((240, 356),159,45):
                    c.click.play()
                    transitionIn(c.transitionImg)
                    pause = False

                #menu button
                if mouseHover((215,422),94,45):
                    #plays the click sound
                    #turn everything off but does not escape the program
                    #this causes the game go back to the main menu
                    c.click.play()
                    transitionIn(c.transitionImg)
                    gameoverScreen = False
                    gameScreen = False
                    highscoreScreen = False
                    pause = False
                    endScreen = False

                #exit button
                if mouseHover((330,422),94,45):
                    #turns everything off, including the running loop
                    c.click.play()
                    transitionIn(c.transitionImg)
                    gameoverScreen = False
                    gameScreen = False
                    highscoreScreen = False
                    running = False
                    pause = False
                    endScreen = False
                    pygame.quit()

            if ev.type == pygame.KEYDOWN:
                #escape button also resumes the game
                if ev.key == pygame.K_ESCAPE:
                    c.click.play()
                    transitionIn(c.transitionImg)
                    pause = False

#the gameover/victory screen
def gameOver(state,score,fishesleft):
    #global variables for all loops after the gameScreen loop
    global gameoverScreen, running, highscoreScreen,endScreen
    name = ""

    #if the player won, a bonus score of 100 points will be rewarded
    if state == "VICTORY" and fishesleft == 0:bonusScore = 100
    else: bonusScore = 0

    #a quit variable is used to ensure that the program does not append a highscore if the player quits without submitting their score
    quit = False

    while gameoverScreen:
        if not outroMusic.muteState: outroMusic.update(15)
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
        screen.blit(c.muteButton[outroMusic.muteState], (5,5))
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
            #shuts off all other loops and quits the program
            if ev.type == pygame.QUIT:
                gameoverScreen = False
                running = False
                highscoreScreen = False
                endScreen = False
                quit = True
                pygame.quit()

            #if the player presses:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if mouseHover((5,5),32,32):
                    c.click.play()
                    outroMusic.mute()

                #continue button and name is not blank
                if mouseHover((240,400),198,45) and name != "":
                    c.click.play()
                    transitionIn(c.transitionImg)
                    gameoverScreen = False

            #we have set a limit of 10 characters for the name the character can type
            #if player presses:
            if ev.type == pygame.KEYDOWN and len(name) < 11:
                #an alphabet on the keyboard and there are less than 10 characters
                if ev.unicode.isalpha() and len(name) < 10:
                    #adds the capitalized version of it (for consistency) to the name
                    name += ev.unicode.upper()

                #the space button
                elif ev.key == pygame.K_SPACE and len(name) < 10:
                    name += " "

                #the backspace button, no restriction on this statement, because the player should be able to backspace even if they are at the maximum character mark
                elif ev.key == pygame.K_BACKSPACE:
                    #delete the last letter in name
                    name = name[:-1]

                #the return key, which also works as the continue button, but makes sure the name isn't blank
                elif ev.key == pygame.K_RETURN and name != "":
                    transitionIn(c.transitionImg)
                    gameoverScreen = False

    #if the player has not quit before submitting their score, we append their name and score into the highscore.txt file
    if not quit:
        highscoreFile = open("highscore.txt","a")
        highscoreFile.write(name + "," + str(score) + "\n")
        #the format for the submission on each line is:
        #name,score
        highscoreFile.close()

    return name

#the main game loop
while running:

    #reset all game variables, this includes loop bools, delay ints, score and name at the beginning
    startMenu = True
    startScreen = True
    gameScreen = True
    gameoverScreen = True
    highscoreScreen = True
    levelSelect = False
    endScreen = True
    victory = False
    levelNum = 0
    time = 180
    timecount = 0
    timeBetweenBullet = 0
    timeBetweenDamage = 0
    outroDelay = 15
    nextRoom = 0
    bulletlist = []
    score = time
    name = ""
    outrotxtNum = 0
    outroMusic = victoryAudio
    fromStart = False

    #the introduction screen, displays the introductory paragraph of the story
    while startScreen:
        #updates audio and clock
        if not mainAudio.muteState: mainAudio.update(15)
        clock.tick(15)

        #displays all items, like background and title
        screen.blit(c.menuBackground, (0, 0))
        screen.blit(c.cat, (244, 157))
        screen.blit(c.titletxt,(135,60))
        screen.blit(c.continuetxt,(150,450))

        #displays the text
        for i in range(0, len(c.introtxt)):
            screen.blit(c.introtxt[i], (125, 300 + i * 30))

        pygame.display.update()

        for ev in pygame.event.get():
            #quits the program
            if ev.type == pygame.QUIT:
                startScreen = False
                startMenu = False
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False
                pygame.quit()

            #if the player presses anything, we leave this screen
            if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
                transitionIn(c.transitionImg)
                startScreen = False

    #the start menu, allows player to select the level and go to the highscore screen
    while startMenu:
        #updates audio and clock
        if not mainAudio.muteState:mainAudio.update(15)
        clock.tick(15)

        #displays background and buttons
        screen.blit(c.menuBackground,(0,0))
        screen.blit(c.cat,(244, 157))
        screen.blit(c.highscoresButton,(221,357))
        screen.blit(c.muteButton[mainAudio.muteState], (5,5))
        screen.blit(c.exitButton,(273, 418))
        screen.blit(c.titletxt,(135,60))

        #checks if the player pressed the start button, if they did, we display the level select button instead of the start button
        if levelSelect:
            screen.blit(c.level1Button, (182, 296))
            screen.blit(c.level2Button, (330, 296))
        else:
            screen.blit(c.startButton, (264, 296))

        pygame.display.update()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                startMenu = False
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False
                pygame.quit()

            #if the player presses:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if mouseHover((5,5),32,32):
                    c.click.play()
                    mainAudio.mute()

                #level1 and level2 buttons for level select
                if levelSelect:
                    #level 1
                    if mouseHover((182,296),128,45):
                        c.click.play()
                        startMenu = False
                        transitionIn(c.transitionImg)
                        levelNum = 0

                    #level 2
                    if mouseHover((330,296),128,45):
                        c.click.play()
                        startMenu = False
                        transitionIn(c.transitionImg)
                        levelNum = 1

                #start button, if pressed, will show level select buttons
                if mouseHover((264,296),111,45) and levelSelect == False:
                    c.click.play()
                    levelSelect = True

                #highscores button
                if mouseHover((221,357),198,45):
                    c.click.play()
                    transitionIn(c.transitionImg)
                    fromStart = True
                    startMenu = False
                    gameScreen = False
                    gameoverScreen = False
                    endScreen = False

                #exit button
                if mouseHover((273,418),94,45):
                    c.click.play()
                    transitionIn(c.transitionImg)
                    startMenu = False
                    gameScreen = False
                    gameoverScreen = False
                    running = False
                    endScreen = False
                    highscoreScreen = False
                    pygame.quit()

    #initializes the level and all the rooms, starting room, and room images according to which level the player selected
    levelObj = level.Level(levelNum)
    curRoomNum = 0
    curRoom = levelObj.roomList[curRoomNum]
    curRoom.visited = True
    background = curRoom.roomImg

    #creates the player object
    playerObj = player.Player()

    #the gameScreen loop, this loop contains the part of the program where the player plays the game
    while gameScreen:
        #updates clock and audio
        if not mainAudio.muteState:mainAudio.update(25)
        clock.tick(25)

        #timer counting down each second
        timecount += 1
        if timecount == 25:
            timecount = 0
            score -= 1
            time -= 1

        #updates the time varibles that controls delay between the enemies ability to damage the player and the player's ability to shoot bullets
        timeBetweenBullet += 1
        timeBetweenDamage += 1

        #timer text and score text, updates every second
        timetxt = c.font.render("TIME: " + str(time), 1, (255, 255, 255))
        scoretxt = c.font.render("SCORE: " + str(score), 1, (255, 255, 255))

        #update current room and player position
        playerpos = (playerObj.x, playerObj.y)

        #check if player is collided with the portal to other rooms
        door = collision.checkTransition(playerpos)

        #the player collides with a door if the checkTransition function returns something that is not -1
        if door != -1:
            #nextRoom variable depends the arrangement of doors and rooms
            nextRoom = room.transition(door, curRoomNum, levelNum)


            #if that door is a "win" door, it means the player has reached to last room, if this is true, we do not update any further
            if nextRoom[0] == "win":
                victory = True

            else:
                #clear the bullet list as you enter a new room
                bulletlist = []

                #updates the current room according to the next room, this depends on the door number and room configuration located in the constants.py file
                curRoomNum = nextRoom[0]
                curRoom = levelObj.roomList[curRoomNum]
                curRoom.visited = True

                #updates the coordinates of the player according the which door the player entered
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
            #the player is given 5 points as an award
            score += 5

            #we will update how many fishes is left in the level
            levelObj.fishLeft -= 1

            #the fishPlacement variable of this room is also turned off, to make sure that fish no longers shows up
            curRoom.fishPlacement = False

            #play the audio when you pick up a fish
            c.getFish.play()

        #move the player
        playerObj.movement(curRoom)

        #move all bullets
        for bulletObj in bulletlist:
            #if the bullet collides with walls in the room
            if bulletObj.collide(curRoom) == True:
                #we find and delete that bullet
                del bulletlist[bulletlist.index(bulletObj)]

            bulletObj.movement()

        #move all enemy
        for enemy in curRoom.enemyList:
            #the timeBetweenEnemy variable is used to make sure collision still works while having a lower speed
            enemy.timeBetweenEnemy += 1

            #checks if it collides with the player and the player is not invulnerable
            if enemy.playerCollision(playerpos) and timeBetweenDamage >= 25:
                #make the player invulnerable again for 1 second
                timeBetweenDamage = 0

                #depletes 1 health from the player object
                playerObj.health -= 1
                c.playerHit.play()

            #updates the enemy movement acoording to the timeBetweenEnemy delay variable
            if enemy.timeBetweenEnemy >= 2:
                enemy.timeBetweenEnemy = 0
                enemy.movement(playerpos, curRoom)

            #checks if the enemy got hit by any bullet in the bulletlist
            enemydeath = enemy.deathCollision(bulletlist)
            if enemydeath[0]:
                #finds and deletes both bullet and enemy from perspective lists
                del bulletlist[bulletlist.index(enemydeath[1])]
                del curRoom.enemyList[curRoom.enemyList.index(enemy)]

                #the player will be rewarded with 4 points for killing an enemy
                score += 4

                #plays the audio for hitting an enemy
                c.onHit.play()

        #display all items
        #displays the room image
        screen.blit(curRoom.roomImg, (-32, -32))

        #displays all the bullets and enemies in the room
        for i in bulletlist:
            screen.blit(i.bulletimg,(i.x,i.y))
        for i in curRoom.enemyList:
            screen.blit(i.img,(i.x,i.y))

        #displays the player
        screen.blit(playerObj.img, (playerObj.x,playerObj.y))

        #displays the fishes if there are any in the room
        if curRoom.fishPlacement != False:
            screen.blit(c.fishImg[1], curRoom.fishPlacement)

        #displays the player health depending on how many health points the player has
        for i in range(0, playerObj.health):
            screen.blit(c.heartImg, (512 + i * 32, 0))

        #displays the total fishes that is in the level
        for i in range(0, levelObj.fishNums):
            screen.blit(c.fishImg[0], (576 - i * 32, 480))

        #displays the fishes the player has collected in the level
        for i in range(0, levelObj.fishNums - levelObj.fishLeft):
            screen.blit(c.fishImg[1], (576 - i * 32, 480))

        #displays the time left, score, and pause button
        screen.blit(timetxt, (100, 3))
        screen.blit(scoretxt,(6,483))
        screen.blit(c.pauseButton, (6, 3))

        pygame.display.update()

        for ev in pygame.event.get():
            #if player tries to quit
            if ev.type == pygame.QUIT:
                gameScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False
                pygame.quit()

            #if the player presses:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #the pause button
                if mouseHover((0,0),64,32):
                    c.click.play()
                    pause(score)

                #anywhere else and they have the ability to shoot
                elif timeBetweenBullet > 12:
                    timeBetweenBullet = 0

                    #creates a bullet depending on the position of mouse and player
                    bulletlist += [bullet.Bullet(playerpos, pygame.mouse.get_pos())]

                    #plays the bullet shooting sound
                    c.shoot.play()

            #if the player presses:
            if ev.type == pygame.KEYDOWN:
                #the escape button, the game is paused
                if ev.key == pygame.K_ESCAPE:
                    pause(score)

        #if the player reaches 0 health, runs out of time, or exits the last room
        if playerObj.health == 0 or time <= 0 or victory:
            gameScreen = False

    #updates what text to display according to if the player collects all the fishes and is alive or not
    #also updates audio depending on the ending, if it's not a lose, the audio will remain the victoryAudio object

    #if the player loses (have 0 remaining health or time), we display the losing dialogue
    if time <= 0 or playerObj.health <= 0:
        outrotxtNum = 2
        outroMusic = gameoverAudio

    #if the player did not collect all the fishes, we display the sad dialogue
    elif levelObj.fishLeft > 0:
        outrotxtNum = 1

    #or else the outrotxtNum variable will remain 0, as initialized at the beginning of the running loop, which is the victory dialogue

    #if the main audio is muted, so will the outro music
    outroMusic.muteState = mainAudio.muteState

    #disable game audio
    if mainAudio.muteState == 0 and endScreen:
        mainAudio.mute()

    #the endScreen loop, similar to the startScreen loop, displays the outrotxt according to the ending the player got
    while endScreen:
        #updates the audio and clock
        if not outroMusic.muteState: outroMusic.update(15)
        clock.tick(15)

        #updates the delay variable to make sure the player does not accidently skip this screen too fast
        if outroDelay >= 0: outroDelay -= 1

        #displays all images on screen
        screen.blit(c.menuBackground, (0, 0))
        screen.blit(c.cat, (244, 157))
        screen.blit(c.titletxt,(135,60))
        screen.blit(c.continuetxt,(150,450))

        #displays the outrotxt
        for i in range(0, len(c.outrotxt[outrotxtNum])):
            screen.blit(c.outrotxt[outrotxtNum][i], (150, 300 + i * 30))

        pygame.display.update()

        for ev in pygame.event.get():
            #if player quits
            if ev.type == pygame.QUIT:
                endScreen = False
                running = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False
                pygame.quit()

            #makes sure the outroDelay variable is 0, and transistions to the next screen if the player presses anything
            if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN and outroDelay <= 0:
                transitionIn(c.transitionImg)
                endScreen = False

    #checks if the player is alive and there are still time left, and the player didn't exit the program
    if (playerObj.health > 0 and time > 0 and gameoverScreen):
        #the player wins the game, call the gameOver loop to record the score of the player
        name = gameOver("VICTORY", score, levelObj.fishLeft)

    #if the player didn't exit the program, but either is not alive or ran out of time
    elif gameoverScreen:
        #the player loses the game
        name = gameOver("GAME OVER", score, levelObj.fishLeft)

    #if the player did not exit the game, creates a list of highscore that will be displayed
    if highscoreScreen:
        #open and record the lines of the highscore.txt file
        highscoreFile = open("highscore.txt", "r")
        lines = highscoreFile.readlines()

        #initializes the highscoreRange variable, this is used to display only the latest 9 scores so it does not display out of the screen
        highscoreRange = posInt(len(lines) - 9)

        #initializes the list of highscore
        highscoreList = []

        #append the latest 9 scores to highscoreList
        for i in range(highscoreRange,len(lines)):
            line = lines[i].split(",")
            highscoreList += [(line[0],line[1][:-1])]

        #sort the highscoreList from highest score to lowest
        highscoreList.sort(key=itemgetter(1),reverse=True)
        highscoreRange = posInt(len(highscoreList) - 9)

        #converts all the text in highscoreList to pygame font objects
        for i in range (0,len(highscoreList)):
            highscoreList[i]= (c.font.render(highscoreList[i][0], 1,(255,255,255)),c.font.render(highscoreList[i][1], 1,(255,255,255)))

        #closes the file
        highscoreFile.close()

    #the highscoreScreen, displays all highscore
    while highscoreScreen:
        #updates audio according to whether or not the player came from the startMenu or not
        if fromStart:
            if not mainAudio.muteState:mainAudio.update(15)
        elif not outroMusic.muteState:outroMusic.update(15)
        clock.tick(15)

        #displays the images
        screen.blit(c.menuBackground, (0, 0))
        screen.blit(c.highscoretxt, (150, 60))
        screen.blit(c.menuButton,(215,422))
        screen.blit(c.exitButton,(331, 422))
        if fromStart:screen.blit(c.muteButton[mainAudio.muteState], (5,5))
        else: screen.blit(c.muteButton[outroMusic.muteState], (5,5))

        #displays the highscore with the list created previously
        for i in range(0,len(highscoreList)):
            screen.blit(highscoreList[i][0],(175, 135 + (i - highscoreRange)*30))
            screen.blit(highscoreList[i][1],(410, 135 + (i - highscoreRange)*30))

        pygame.display.update()

        for ev in pygame.event.get():
            #if the player quits
            if ev.type == pygame.QUIT:
                running = False
                endScreen = False
                gameoverScreen = False
                highscoreScreen = False
                endScreen = False
                pygame.quit()

            #if the player presses:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                #mute button
                if mouseHover((5,5),32,32):
                    c.click.play()
                    if fromStart:mainAudio.mute()
                    else: outroMusic.mute()

                #menu button
                if mouseHover((215, 422), 94, 45):
                    c.click.play()
                    transitionIn(c.transitionImg)
                    highscoreScreen = False
                    endScreen = False

                #exit button
                if mouseHover((331, 422), 94, 45):
                    c.click.play()
                    transitionIn(c.transitionImg)
                    running = False
                    endScreen = False
                    gameoverScreen = False
                    highscoreScreen = False
                    pygame.quit()

    #stop the outro music and play the main audio again
    if outroMusic.muteState == 0 and running:
        outroMusic.mute()
    if mainAudio.muteState == 1:
        mainAudio.mute()