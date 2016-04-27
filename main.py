import pygame, pygame.mixer
import player
import bullet
import room
import constants as c
import collision
import level

pygame.init()
pygame.font.init()
pygame.mixer.init()

levelNum = int(input("level: "))
level = level.Level(levelNum)

curRoomNum = 0
curRoom = level.roomList[curRoomNum]
time = 1200
timecount = 0

screen = pygame.display.set_mode((c.gamew, c.gameh))
background = curRoom.roomImg
font = pygame.font.SysFont("None",20)


pygame.display.flip()

clock = pygame.time.Clock()

running = True
playerObj = player.Player(1)

timeBetweenBullet = 0
timeBetweenDamage = 0
nextRoom = 0
bulletlist = []


c.mainAudio.play()

while running:
    clock.tick(60)

    #if player tries to quit
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    #timer counting down each second
    timecount += 1
    if timecount == 60:
        timecount = 0
        time -= 1

    timeBetweenBullet += 1
    timeBetweenDamage += 1

    #timer text
    timetxt = font.render("time: " + str(time), 1, (255, 255, 255))

    #update current room and player position
    playerpos = (playerObj.x, playerObj.y)
    curRoom = level.roomList[curRoomNum]

    #if you shoot
    if pygame.mouse.get_pressed()[0] and timeBetweenBullet > 20:
        timeBetweenBullet = 0
        bulletlist += [bullet.Bullet(playerpos, pygame.mouse.get_pos())]
        c.shoot.play()

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
        level.fishesLeft -= 1
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
            c.onHit.play()

    #display all items
    # <editor-fold desc="display">
    screen.blit(playerObj.img,(playerObj.x,playerObj.y))
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

    for i in range(0, c.levelSettings[levelNum] - level.fishesLeft):
        screen.blit(c.fishImg[1], (576 - i * 32, 480))

    screen.blit(timetxt, (32, 12))
    # </editor-fold>

    pygame.display.flip()


