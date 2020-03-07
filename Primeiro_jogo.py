import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Primeiro jogo - Israel Alves Lucena Gomes')

x = 50
y = 350
width = 40
height = 60
vel = 5

jumping = False
jump_height = 11
impulse = jump_height

run = True
while run:
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= vel
    if keys[pygame.K_RIGHT]:
        if x + width < SCREEN_WIDTH:
            x += vel
    if not jumping:
        if keys[pygame.K_UP]:
            if y > 0:
                y -= vel
        if keys[pygame.K_DOWN]:
            if y + height < SCREEN_HEIGHT:
                y += vel
        if keys[pygame.K_SPACE]:
            jumping = True
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

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()


