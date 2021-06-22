import pygame
import random
from pygame import mixer
import math

#xrwmata
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (24, 255, 0)

class Game(pygame.sprite.Sprite):
    
    def __init__(self,name,x,y):
       
        super().__init__()
 
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey(BLACK)
      
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        
        self.help_x = 0
        self.help_y = 0
        
        self.x_speed = 0
        self.y_speed = 0
        
        #benzinh
        self.curent_fuel = 400
        self.maximum_fuel = 400
        self.mikos_mparas = 400
        self.rithmos_katanaloshs = self.maximum_fuel / self.mikos_mparas
        
        self.over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        
        
        
    def speed(self, x, y):
        self.x_speed += x
        self.y_speed += y
        
    def update_pl(self):
        if self.rect.x >=170 and self.rect.x <=510:
            self.help_x = self.rect.x  
            self.rect.x += self.x_speed   
        else:
            self.rect.x = self.help_x
            
        if self.rect.y >=-10 and self.rect.y <=510:
            self.help_y = self.rect.y  
            self.rect.y += self.y_speed   
        else:
            self.rect.y = self.help_y
         
    def update(self):
      
        self.rect.y += level+1

        if self.rect.y > 560:
            self.reset_pos()
        
        self.mpara_benzinhs()
   
    def reset_pos(self):
        self.rect.y = random.randrange(-200, -20)
        self.rect.x = random.randrange(180, 500)   
        
    def katanalosh(self, posothta):
        if self.curent_fuel > 0:
            self.curent_fuel -= posothta
        if self.curent_fuel <= 0:
            self.curent_fuel = 0
            
    def bale_benzinh(self, posothta):
        if self.curent_fuel < self.maximum_fuel:
            self.curent_fuel += posothta
        if self.curent_fuel >= self.maximum_fuel:
            self.curent_fuel = self.maximum_fuel

    def mpara_benzinhs(self):
        pygame.draw.rect(screen, RED, (185, 530, self.curent_fuel / self.rithmos_katanaloshs, 25) )  
        pygame.draw.rect(screen, BLACK, (185, 530, self.mikos_mparas, 25), 4)              
    
    def game_over_text(self):
        screen.blit(self.over_text, (200, 250))

#functions 
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
     
def fire_bullet(x, y):
    global bullet_state
    bullet_state = False
    screen.blit(bulletImg, (x + 16, y +10))
    
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 20:
        return True
    else:
        return False

pygame.init()
over_font = pygame.font.Font('freesansbold.ttf', 64)

player_list = pygame.sprite.Group()
fuel_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#para8uro
screen_width = 800
screen_height = 560
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("kai kala atari river raid")
background_image = pygame.image.load("back1.png").convert()

#paixths
playerX = 370
playerY = 480   
player = Game("plane2.png",playerX,playerY)
player_list.add(player)

#benzinh
fuel = Game("fuel.png",15,15)
fuel.rect.x = random.randrange(245,310)
fuel.rect.y = random.randrange(screen_height)    
fuel_list.add(fuel)
all_sprites_list.add(fuel)



#ex8roi
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('heli.png'))
    enemyImg.append(pygame.image.load('boat.png'))
    enemyX.append(random.randint(190, 500))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(20)

#sfaires
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = True

#alles metablhtes
done = False
lost = False
level = 1
score = 0
font = pygame.font.SysFont('Calibri', 30, True, False)
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done: 
    screen.fill(BLACK)
    screen.blit(background_image, [2, 0])
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
            
           #kinhsh paixth
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                player.speed(-3,0)
            elif event.key == pygame.K_RIGHT:
                player.speed(3, 0)
            elif event.key == pygame.K_UP:
                player.speed(0, -2)
            elif event.key == pygame.K_DOWN:
                player.speed(0, 2)
            #pirobolismos
            if event.key == pygame.K_SPACE:
                if bullet_state is True:
                    bulletSound = mixer.Sound("laser5.ogg")
                    bulletSound.play()
                    bulletX = player.rect.x
                    bulletY = player.rect.y
                    fire_bullet(bulletX, bulletY)
        
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.speed(-3, 0)
            elif event.key == pygame.K_UP:
                player.speed(0, 2)
            elif event.key == pygame.K_DOWN:
                player.speed(0, -2)
                
    #o paixths xanei an pesei stis ox8es            
    if player.rect.x <= 170:
        player.rect.x = 170
        game_over_text()
        gameoverSound = mixer.Sound("fail.ogg")
        gameoverSound.play()    
    
        
    elif player.rect.x >= 510:
        player.rect.x = 510
        game_over_text() 
        gameoverSound = mixer.Sound("fail.ogg")
        gameoverSound.play()    
        
    #gia na mhn bgenei o paixths panw h katw apo to potami    
    elif player.rect.y >= 515:
        player.rect.y = 515
    elif player.rect.y <= -10:
        player.rect.y = -10
    
    #gia na xtipaei o paixths tis benzines
    fuel_hit_list = pygame.sprite.spritecollide(player, fuel_list, False)
    
    #ti ginetai an petuxei tis benzines
    for fuel in fuel_hit_list:
           fuel.reset_pos()
           fuelSound = mixer.Sound("fuel_up.ogg")
           fuelSound.play()  
           #poso fuel anaplhrwnei 
           fuel.curent_fuel += 50
    all_sprites_list.update() 
    
    #meiwnei thn mpara benzinhs se ka8e frame
    fuel.curent_fuel -= 0.3
    #gia na mhn bgenei to xroma ektos mparas
    if fuel.curent_fuel >= 400:
        fuel.curent_fuel = 400
    if fuel.curent_fuel <= 0:
        fuel.curent_fuel = 0
       
    #pws kinountai oi ex8roi
    for i in range(num_of_enemies):
        #xanei an oi ex8roi perasoun ena sugkekrimeno y
        if enemyY[i] > 460:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        #xanei an teleiwsei h benzinh
        elif(fuel.curent_fuel <= 0):
            game_over_text()
            
        #kinhsh ex8rwn
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 190:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 500:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
            
        #xtuphma ex8rwn me sfaira   
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        #ti ginetai an xtuphsoun 
        if collision:
            explosionSound = mixer.Sound("explosion.ogg")
            explosionSound.play()  
            bulletY = 350
            bullet_state = True
            score += 1
            enemyX[i] = random.randint(190, 500)
            enemyY[i] = random.randint(50, 150)
            #pws orizontai ta levels
            if score < 10:
               level = 1
               
            if score == 10:
                 level = 2
                 levelupSound = mixer.Sound("levelup.ogg")
                 levelupSound.play()
        #level 2
        if level == 2:
            if enemyY[i] > 460:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                    game_over_text()
            elif(fuel.curent_fuel <= 0):
                game_over_text()
                break
            #oi ex8roi pane pio grhgora
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 190:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] > 500:
                 enemyX_change[i] = -2
                 enemyY[i] += enemyY_change[i]    
                 enemy(enemyX[i], enemyY[i], i)
        #emfanizontai sthn o8onh oi ex8roi
        enemy(enemyX[i], enemyY[i], i)
      
  

    # pws kinhte h sfaira
    if bulletY <= 0:
        bulletY = 480
        bullet_state = True

    if bullet_state is False:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change    
    #emfanizontai paixths kai benzines
    player.update_pl()  
    all_sprites_list.draw(screen)
    player_list.draw(screen)
    
    #boh8itika texts
    text2 = font.render("Score:"+str(score), True, WHITE)
    screen.blit(text2, [0, 0]) 
    text3 = font.render("level:"+str(level), True, WHITE)
    screen.blit(text3,[0,25])
    text4 = font.render("0                      FUEL                 400", True, BLACK)
    screen.blit(text4,[188,530])
      
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()

