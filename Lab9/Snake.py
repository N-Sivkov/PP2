import pygame
import random

pygame.init()

#game variables
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
done = False
score = 0
level = 1
record = 0 # a variable for keeping the count of the score collected and progressing in levels

#head variable

coor_head = [100,100]

#body variable

coor_body = [
    [30,100],
    [40,100],
    [50,100],
    [60,100],
    [70,100],
    [80,100],
    [90,100],
    [100,100]
]

#apple
eaten = False
coor_apple = [0, 0]
value = 0
COLOR = {1: (0, 255, 0), 2: (0, 0, 255), 3: (255, 0, 0)} # the apple's color now depends on its weight
def generate_apple():
    #appearance close to the walls and on top of the snake excluded
    global eaten 
    global width
    global height
    global coor_apple
    global value
    apple_width, apple_height = random.randrange(1,width//10)*10, random.randrange(1,height//10)*10
    if apple_width in [0, 800, coor_body[0], coor_head[0]]:
        if apple_width >= 3:
            apple_width -= 2
        else:
            apple_width += 1
    if apple_height in [0, 600, coor_body[1], coor_head[1]]:
        if apple_height >= 3:
            apple_height -= 2
        else:
            apple_height += 2
    coor_apple = [apple_width, apple_height]
    value = random.randint(1, 3) # randomly assigned weight of the apple
    eaten = False


generate_apple()

APPLE = pygame.USEREVENT + 1 # a gimmick event to be used in the timer below
timer = pygame.time.set_timer(APPLE, int(48000 / (value + level))) # apple's disappearance timer

#direction
next_dir = "r" #right direction
direc = "r" #right direction

def score_update(font, size, color):
    global score
    score_font = pygame.font.SysFont(font,size)
    score_render = score_font.render("Score: "+str(score),True,color)
    score_rect = score_render.get_rect()
    #level update included
    level_render = score_font.render("Level: "+str(level),True,color)
    level_rect = pygame.Rect(width - size * 5 - 1, 0, width - 1, size)


    screen.blit(score_render,score_rect)
    screen.blit(level_render, level_rect)

    pygame.display.update()

def game_over_message(font, size, color):
    global score
    global done
    game_over_font = pygame.font.SysFont(font,size)
    game_over_surface1 = game_over_font.render("Game Over, your final score: "+str(score)+";",True,color)
    game_over_surface2 = game_over_font.render("You reached level "+str(level),True,color)
    game_over_rect1, game_over_rect2 = pygame.Rect(100,100,200,200), pygame.Rect(100,200,400,400)
    screen.blit(game_over_surface1,game_over_rect1)
    screen.blit(game_over_surface2,game_over_rect2)
    pygame.display.update()
    pygame.time.delay(3000)
    done = True
    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_dir = "r"
            if event.key == pygame.K_LEFT:
                next_dir = "l"
            if event.key == pygame.K_UP:
                next_dir = "u"
            if event.key == pygame.K_DOWN:
                next_dir = "d"
        if event.type == APPLE:
            eaten = True
    for seg in coor_body[:-1]:
        if coor_head[0] == seg[0] and coor_head[1] == seg[1]:
            game_over_message("times new roman",44,(255,0,0))
    
    #additional check for the walls
    if coor_head[0] == 0 or coor_head[0] == 800 or coor_head[1] == 0 or coor_head[1] == 600:
        game_over_message("times new roman",44,(255,0,0))

    screen.fill((0,0,0))
    #logic
    if next_dir == "r" and direc != "l":
        direc = "r"
    if next_dir == "l" and direc != "r":
        direc = "l"
    if next_dir == "u" and direc != "d":
        direc = "u"
    if next_dir == "d" and direc != "u":
        direc = "d"



    if direc == "r":
        coor_head[0] += 10
    if direc == "l":
        coor_head[0] -= 10
    if direc == "u":
        coor_head[1] -= 10
    if direc == "d":
        coor_head[1] += 10

    new_coor = [coor_head[0],coor_head[1]]
    coor_body.append(new_coor)
    coor_body.pop(0)

    if coor_head[0] == coor_apple[0] and coor_head[1] == coor_apple[1]:
        eaten = True
        score += value * 10
        if score - record >= 30: 
            level += 1
            record = score
    
    if eaten:
        generate_apple()
        timer = pygame.time.set_timer(APPLE, int(48000 / (value + level)))
        

    # drawing section
    if not eaten:
        pygame.draw.rect(screen,COLOR[value],pygame.Rect(coor_apple[0],coor_apple[1],10,10))

    for el in coor_body:
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(el[0],el[1],10,10))
    
    pygame.draw.rect(screen,(128,128,128),pygame.Rect(coor_head[0],coor_head[1],10,10))

    score_update("times new roman",20,(128,128,128))

    #tweaked the delay so that the game's speed increases along with the progression in levels
    pygame.time.delay(int(300 / level))

    pygame.display.flip()

pygame.quit()