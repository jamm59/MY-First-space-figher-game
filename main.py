import pygame
from random import randint
pygame.font.init()

# ........................................................GLOBAL VARIABLES...........................................................
IMAGE_DIR = 'C:/Users/juden/Desktop/python/python pygame/assets/images'
pygame.display.set_caption('First Python Game')
HEALTH_FONT = pygame.font.SysFont('calibri', 35)
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
WINNER = pygame.font.SysFont('ebrima', 50)
#.....................................................IMportant Methods .......................................................................
def draw_window(red,yellow,yellow_list,red_list,yellow_health,red_health,text):
    WINDOW.fill(BACK_COLOR)
    pygame.draw.rect(WINDOW,(213,213,213),BORDER)

    yellow_health_text = HEALTH_FONT.render(f'Health: {red_health}', 1,(73, 84, 100))
    red_health_text = HEALTH_FONT.render(f'Health: {yellow_health}', 1,(73, 84, 100))
    WINDOW.blit(yellow_health_text , (WIDTH_W-180, 10))
    WINDOW.blit(red_health_text , (10,10))

    WINDOW.blit(YELLOW_SHIP,(yellow.x,yellow.y))
    WINDOW.blit(RED_SHIP,(red.x,red.y))

    for bullet in yellow_list:
        pygame.draw.rect(WINDOW, (255,255,0),bullet)
    for bullet in red_list:
        pygame.draw.rect(WINDOW, (255,0,0), bullet)

    if text == '':
        pass
    else:
        new_text =WINNER.render(f'{text}',1,(0,0,0))
        WINDOW.blit(new_text, (WIDTH_W // 2 - 100 ,HEIGHT_W // 2))

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

def handle_bullets(yel_list ,red_list ,yellow,red):
    for bullet in yel_list:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            yel_list.remove(bullet)
        elif bullet.x < 0 :
            yel_list.remove(bullet)

        # elif bullet.x 

    for bullet in red_list:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
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
    red_health = 10
    yellow_health = 10
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(bullets_red) < MAX_BULL:
                    bullet  = pygame.Rect(red.x , red.y + red.width // 2,10,5)
                    bullets_red.append(bullet)
                if event.key == pygame.K_RCTRL and len(bullets_yellow) < MAX_BULL:
                    bullet  = pygame.Rect(yellow.x, yellow.y + yellow.width // 2 ,10,5)
                    bullets_yellow.append(bullet)


            if event.type == RED_HIT:
                red_health -= 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                
        winner_text = ''
        if red_health <= 0:
            winner_text = 'Yellow wins'
        if yellow_health <= 0:
            winner_text = 'Red Wins'
            
        check_press(red,1)
        check_press(yellow,2)   
        handle_bullets(bullets_yellow,bullets_red,yellow,red) 
        draw_window(red,yellow,bullets_yellow,bullets_red,yellow_health,red_health,winner_text)
        if winner_text != '':
            pygame.time.delay(1000)
            run  = False
        

    print(winner_text)
    pygame.quit()


if __name__ == '__main__':
    main()