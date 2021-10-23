import pygame
from random import randint

# ........................................................GLOBAL VARIABLES...........................................................
IMAGE_DIR = 'C:/Users/juden/Desktop/python/python pygame/assets/images'
pygame.display.set_caption('First Python Game')
WIDTH_W,HEIGHT_W = 900,500
WINDOW = pygame.display.set_mode((WIDTH_W,HEIGHT_W))
BORDER = pygame.Rect(WIDTH_W // 2 ,0 , 5, HEIGHT_W)
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
VEL = 6
BULLET_VEL = 7
MAX_BULL = 5
BACK_COLOR = (225, 244, 243)
FPS = 60
WIDTH,HEIGHT = 50,50
YELLOW_SHIP = pygame.image.load(f'{IMAGE_DIR}/yellowship.png')
RED_SHIP = pygame.image.load(f'{IMAGE_DIR}/redship.png')
YELLOW_SHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SHIP, (WIDTH,HEIGHT)) , 90)
RED_SHIP = pygame.transform.rotate(pygame.transform.scale(RED_SHIP, (WIDTH,HEIGHT)) ,270)
#.....................................................IMportant Methods .......................................................................
def draw_window(red,yellow,yellow_list,red_list):
    WINDOW.fill(BACK_COLOR)
    pygame.draw.rect(WINDOW,(213,213,213),BORDER)
    WINDOW.blit(YELLOW_SHIP,(yellow.x,yellow.y))
    WINDOW.blit(RED_SHIP,(red.x,red.y))
    for bullet in yellow_list:
        pygame.draw.rect(WINDOW, (255,255,0),bullet)
    for bullet in red_list:
        pygame.draw.rect(WINDOW, (255,0,0), bullet)
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

def handle_bullets(yel_list ,red_list , yellow,red):
    for bullet in yel_list:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            if len(yel_list) > 1:
                yel_list.remove(bullet)
        elif bullet.x < 0 :
            print(True)
            yel_list.remove(bullet)

        # elif bullet.x 

    for bullet in red_list:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            if len(red_list) > 1:
                red_list.remove(bullet)
        elif bullet.x > WIDTH_W :
            red_list.remove(bullet)


# ..........................................................................................................................
def main():
    red = pygame.Rect(100,100, WIDTH,HEIGHT)
    yellow = pygame.Rect(700,100,WIDTH,HEIGHT)
    clock = pygame.time.Clock()
    bullets_red = []
    bullets_yellow = []
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                # print(yellow.x) 700
                # print(red.x) 100
                if event.key == pygame.K_LCTRL and len(bullets_red) < MAX_BULL:
                    bullet  = pygame.Rect(red.x , red.y + red.width // 2,10,5)
                    bullets_red.append(bullet)
                if event.key == pygame.K_RCTRL and len(bullets_yellow) < MAX_BULL:
                    bullet  = pygame.Rect(yellow.x, yellow.y + yellow.width // 2 ,10,5)
                    bullets_yellow.append(bullet)

            
        check_press(red,1)
        check_press(yellow,2)   
        handle_bullets(bullets_yellow,bullets_red,yellow,red) 
        draw_window(red,yellow,bullets_yellow,bullets_red)
    pygame.quit()


if __name__ == '__main__':
    main()