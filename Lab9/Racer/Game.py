#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0
RECORD = 0 # a variable for keeping the count of the coin harvest and adjusting speed according to it

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self, value=1):
        super().__init__()
        self.value = value # this parameter defines the amount of points added to the counter when collected and the image used
        self.image = pygame.image.load("Coin_C.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
    
    #The object's re-appearance on the stage's upper margin made into a separate method for further convenience
    def respawn(self):
        self.value = random.randint(1, 3) # reassign value and change the sprite accordingly
        if self.value == 1:
            self.image = pygame.image.load("Coin_C.png")
        elif self.value == 2:
            self.image = pygame.image.load("Coin_S.png")
        elif self.value == 3:
            self.image = pygame.image.load("Coin_G.png")
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0,SPEED // 2)
        if (self.rect.bottom > 600):
            self.respawn()
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(E1)


#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:

    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #Coin counter added to the top-right corner
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_count = font_small.render(str(COIN), True, BLUE)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_count, (SCREEN_WIDTH - 20,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        

    #Player colliding with a coin   
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound("jingle.mp3").play()
        for coin in coins:
            if coin.rect.colliderect(P1.rect): 
                COIN += coin.value
                if COIN - RECORD >= 10: # if >= 10 coins have been collected since the last record
                    SPEED += 0.5
                    RECORD = COIN
                coin.respawn()
                break

    pygame.display.update()
    FramePerSec.tick(FPS)
