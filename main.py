# import pygame.examples.aliens
#
# pygame.examples.aliens.main()


import pygame

from model import initalize_board, initalize_snake, set_new_position
from view import draw

step = 20
width = 800
height = 600
dimension = (width, height)

pygame.init()
screen = pygame.display.set_mode(dimension)
pygame.display.set_caption("codebrainers-snake")
clock = pygame.time.Clock()


head_direction = 0
def turn(direction):
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN]:
        return 2
    if pressed_key[pygame.K_UP]:
        return 0
    if pressed_key[pygame.K_LEFT]:
        return 3
    if pressed_key[pygame.K_RIGHT]:
        return 1
    return direction


head_direction = 0
board = initalize_board()
snake = initalize_snake(board)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)
    head_direction = turn(head_direction)
    set_new_position(head_direction, snake, board)
    screen.fill((225, 225, 225))

    draw(board, screen)


    pygame.display.flip()
    clock.tick(12)
