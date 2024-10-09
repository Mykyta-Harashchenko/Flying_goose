import random
import os
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0 , 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

IMAGE_PATH = "GOOSE"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)


player_size=(170,80)
player = pygame.image.load('player.png').convert_alpha()
# player.fill(COLOR_BLACK)
player_rect = pygame.Rect(WIDTH/2, HEIGHT/2, *player_size)
player_move_down = [0,4]
player_move_right = [4,0]
player_move_up = [0,-4]
player_move_left = [-4,0]

def create_enemy():
   enemy_size = (140,70) 
   enemy = pygame.image.load('enemy.png').convert_alpha()
#    enemy.fill(COLOR_BLUE)
   enemy_rect = pygame.Rect(WIDTH, random.randint(30, HEIGHT-30), *enemy_size)
   enemy_move = [random.randint(-8, -4), 0]
   return [enemy, enemy_rect, enemy_move]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

enemies = []

def create_bonus():
   bonus_size = (160, 280) 
   bonus = pygame.image.load('bonus.png').convert_alpha()
#    bonus.fill(COLOR_RED)
   bonus_rect = pygame.Rect(random.randint(10, WIDTH-300), 0,  *bonus_size)
   bonus_move =  [0, random.randint(2, 4)]
   return [bonus, bonus_rect, bonus_move]

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)

bonuses = []

def create_bonus_2():
   bonus_2_size = (160, 280) 
   bonus_2 = pygame.image.load('bonus 2.png').convert_alpha()
#    bonus.fill(COLOR_RED)
   bonus_2_rect = pygame.Rect(random.randint(10, WIDTH-300), 0,  *bonus_2_size)
   bonus_2_move =  [0, random.randint(2, 4)]
   return [bonus_2, bonus_2_rect, bonus_2_move]

CREATE_BONUS_2 = pygame.USEREVENT + 3
pygame.time.set_timer(CREATE_BONUS_2, 5000)

bonuses_2 = []

score = 0

CHANGE_IMAGE=pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)
image_index = 0

playing = True

while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CREATE_BONUS_2:
            bonuses.append(create_bonus_2())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index +=  1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0
    
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()
    
    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()


    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
   
    if keys[K_RIGHT] and player_rect.right < WIDTH :
         player_rect = player_rect.move(player_move_right)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    if keys[K_UP] and player_rect.top > 0 :
         player_rect = player_rect.move(player_move_up) 

    for enemy in enemies :
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing = False

    for bonus in bonuses :
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus))
    
    for bonus_2 in bonuses_2 :
        bonus_2[1] = bonus_2[1].move(bonus_2[2])
        main_display.blit(bonus_2[0], bonus_2[1])

        if player_rect.colliderect(bonus_2[1]):
            score += 5
            bonuses_2.pop(bonuses_2.index(bonus_2))

    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))

    main_display.blit(player, player_rect)

   #  main_display.blit(enemy, enemy_rect)
    print(len(enemies))

    print(len(bonuses))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))


    for bonus in bonuses:
        if bonus[1].bottom < 0:
            bonus.pop(bonuses.index(bonus))


    for bonus_2 in bonuses_2:
        if bonus_2[1].bottom < 0:
            bonus_2.pop(bonuses_2.index(bonus_2))

