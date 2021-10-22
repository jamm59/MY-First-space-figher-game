import pygame
from random import randint

pygame.display.set_caption('First Python Game')
IMAGE_DIR = 'C:/Users/juden/Desktop/python/python pygame/assets/images'
WIDTH_W,HEIGHT_W = 900,500
WINDOW = pygame.display.set_mode((WIDTH_W,HEIGHT_W))
BORDER = pygame.Rect(WIDTH_W / 2 ,0 , 5, HEIGHT_W)
VEL = 6
BACK_COLOR = (255,255,255)
FPS = 60
WIDTH,HEIGHT = 50,50
YELLOW_SHIP = pygame.image.load(f'{IMAGE_DIR}/yellowship.png')
RED_SHIP = pygame.image.load(f'{IMAGE_DIR}/redship.png')

YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP, (WIDTH,HEIGHT)) , 90)
RED_SHIP = pygame.transform.rotate(pygame.transform.scale(RED_SHIP, (WIDTH,HEIGHT)) ,270)

def draw_window(red,yellow):
    WINDOW.fill(BACK_COLOR)
    pygame.draw.rect(WINDOW,(0,0,0),BORDER)
    WINDOW.blit(YELLOW_SHIP,(yellow.x,yellow.y))
    WINDOW.blit(RED_SHIP,(red.x,red.y))
    pygame.display.update()

def check_press(type,num):
    keys_pressed = pygame.key.get_pressed()
    right = [pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]
    left = [pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a]
    if num == 1:
        other = left
    else :
        other = right

    if keys_pressed[other[2]]: # RIGHT
        if WIDTH_W / 2 < type.x < WIDTH_W - 60 :
            type.x += VEL
        if WIDTH_W / 2 - 60> type.x: # check for collision with Border
            type.x += VEL
    if keys_pressed[other[3]]: # LEFT
        if WIDTH_W / 2 > type.x and type.x - VEL > 0:
            type.x -= VEL
        if type.x > WIDTH_W / 2 + 5:
            type.x -= VEL
    if keys_pressed[other[0]] and type.y - VEL > 0: # UP
        type.y -= VEL
    if keys_pressed[other[1]] and type.y + VEL < HEIGHT_W - 60: # DOWN
        type.y += VEL

def main():
    red = pygame.Rect(100,100, WIDTH,HEIGHT)
    yellow = pygame.Rect(700,100,WIDTH,HEIGHT)
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        check_press(red,1)
        check_press(yellow,2)
            
        draw_window(red,yellow)
    pygame.quit()


if __name__ == '__main__':
    main()