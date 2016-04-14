import pygame,player,bullet,enemy,room,constants as c

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480))
background =  pygame.image.load("assets\\images\\map.png")
font = pygame.font.SysFont("None",20)


pygame.display.flip()

clock = pygame.time.Clock()

running = True
playerObj = player.Player(1)
enemyList = [enemy.Enemy(1,1,c.u*8,c.u*7)]
roomObj = room.Room()

timeBetweenBullet = 0
timeBetweenEnemy = 0
timeBetweenDamage = 0
bulletlist = []

while running:
    if enemyList == []:
        enemyList = [enemy.Enemy(1,1,c.u*8,c.u*7)]

    clock.tick(60)

    playerHP = font.render(str(playerObj.health),0,(255,255,255))
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
    timeBetweenEnemy += 1
    timeBetweenDamage += 1

    playerObj.move()
    roomObj.transition(playerpos)


    screen.blit(background, (0,0))

    for i in enemyList:
        print(timeBetweenDamage)
        print(i.playerCollision(playerpos))
        if i.playerCollision(playerpos) and timeBetweenDamage >= 25:
            print("a")
            timeBetweenDamage = 0
            playerObj.health -= 1

    for i in bulletlist:
        if i.collide() == True:
            del bulletlist[bulletlist.index(i)]
            continue
        screen.blit(i.bulletimg,(i.x,i.y))
        i.movement()

    for i in enemyList:
        if timeBetweenEnemy >= 2:
            timeBetweenEnemy = 0
            i.movement(playerpos)

        enemydeath = i.deathCollision(bulletlist)
        if enemydeath[0]:
            del bulletlist[bulletlist.index(enemydeath[1])]
            del enemyList[enemyList.index(i)]

        screen.blit(i.img,(i.x,i.y))

    screen.blit(playerObj.img,playerpos)
    screen.blit(playerHP,(60,60))

    pygame.display.flip()