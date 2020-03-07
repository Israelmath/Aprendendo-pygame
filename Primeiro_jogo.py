import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Primeiro jogo - Israel Alves Lucena Gomes')

clock = pygame.time.Clock()

x = 50
y = 350
width = 64
height = 64
vel = 5

jumping = False
jump_height = 10
impulse = jump_height
step_counts = 0

walkcount = 0

walking = [pygame.image.load('Sprites/Run1.png'),
           pygame.image.load('Sprites/Run2.png'),
           pygame.image.load('Sprites/Run3.png'),
           pygame.image.load('Sprites/Run4.png'),
           pygame.image.load('Sprites/Run5.png'),
           pygame.image.load('Sprites/Run6.png'),
           pygame.image.load('Sprites/Run7.png'),
           pygame.image.load('Sprites/Run8.png'),
           pygame.image.load('Sprites/Run9.png')]

char = pygame.image.load('Sprites/Idle1.png')
bg = pygame.image.load('Sprites/BG.png')
bg = pygame.transform.scale(bg, (1280, 732))


def redraw_game_window():
    global step_counts

    screen.blit(bg, (0, 0))

    if step_counts + 1 >= 27:
        step_counts = 0

    if RIGHT:
        screen.blit(walking[step_counts//3], (x, y))
        step_counts += 1
    else:
        screen.blit(char, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= vel
            LEFT = True
            RIGHT = False
    elif keys[pygame.K_RIGHT]:
        if x + width < SCREEN_WIDTH:
            x += vel
            LEFT = False
            RIGHT = True
    else:
        RIGHT = False
        LEFT = False
        step_counts = 0

    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            LEFT = False
            RIGHT = False
            step_counts = 0
    else:
        if impulse >= -jump_height:
            movment_aux = 1
            if impulse < 0:
                movment_aux = -1
            y -= (impulse ** 2) * 0.5 * movment_aux
            impulse -= 1
        else:
            jumping = False
            impulse = jump_height

    redraw_game_window()


pygame.quit()


