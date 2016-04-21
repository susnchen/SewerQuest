import pygame
import player
import bullet
import enemy
import room
import constants as c
import collision

pygame.init()
pygame.font.init()

curRoomNum = 2
curRoom = room.roomList[curRoomNum]

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

while running:
    '''if enemyList == []:
        enemyList = [enemy.Enemy(1,1,c.u*8,c.u*7)]'''

    clock.tick(60)

    curRoom = room.roomList[curRoomNum]

    playerHP = font.render("health: " + str(playerObj.health),0,(255,255,255))
    playerpos = (playerObj.x,playerObj.y)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_z] and timeBetweenBullet > 10:
        timeBetweenBullet = 0
        curBullet = bullet.Bullet(playerpos,playerObj.facing)
        curBullet.movement
        bulletlist += [bullet.Bullet(playerpos,playerObj.facing)]

    timeBetweenBullet += 1
    timeBetweenDamage += 1

    playerObj.movement(curRoom)
    if collision.checkTransition(playerpos) != 4:
        nextRoom = room.transition(collision.checkTransition(playerpos),curRoomNum)

        curRoomNum = nextRoom[0]
        curRoom = room.roomList[curRoomNum]

        if nextRoom[1] == 0:
            playerObj.move((320,0),"down")

        elif nextRoom[1]== 1:
            playerObj.move((608,224),"left")

        elif nextRoom[1]== 2:
            playerObj.move((288,480),"up")

        elif nextRoom[1]== 3:
            playerObj.move((0,224),"right")

    screen.blit(curRoom.roomImg, (-32,-32))

    for i in bulletlist:
        if i.collide(curRoom) == True:
            del bulletlist[bulletlist.index(i)]
            continue
        screen.blit(i.bulletimg,(i.x,i.y))
        i.movement()

    #print(playerpos)

    for i in curRoom.enemyList:
        i.timeBetweenEnemy += 1
        if i.playerCollision(playerpos) and timeBetweenDamage >= 60:
            timeBetweenDamage = 0
            playerObj.health -= 1

        if i.timeBetweenEnemy >= 2:
            i.timeBetweenEnemy = 0
            i.movement(playerpos,curRoom)

        enemydeath = i.deathCollision(bulletlist)
        if enemydeath[0]:
            del bulletlist[bulletlist.index(enemydeath[1])]
            del curRoom.enemyList[curRoom.enemyList.index(i)]

        screen.blit(i.img,(i.x,i.y))

    screen.blit(playerObj.img,playerpos)
    screen.blit(playerHP,(60,60))

    pygame.display.flip()