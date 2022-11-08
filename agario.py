import pygame
import random

pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 1024
fps = 60
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Agar.io")

white = [255, 255, 255]
black = [0, 0, 0]
lightgreen = [0, 255, 0]
green = [0, 200, 0]
blue = [0, 0, 128]
lightblue = [0, 0, 255]
darkred = [200, 0, 0]
red = [255, 100, 100]
yellow = [255, 200, 0]
orange = [255, 100, 10]
purple = [102, 0, 102]
lightpurple = [153, 0, 153]

x = random.randint(1, 1280)
y = random.randint(1, 1024)
r = random.randint(5, 50)
x_pos = x
y_pos = y
speed = 25

clock = pygame.time.Clock()
quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_pos = x_pos + speed
                pygame.draw.circle(window, red, (x_pos, y_pos), 20)
            elif event.key == pygame.K_LEFT:
                x_pos = x_pos - speed
                pygame.draw.circle(window, red, (x_pos, y_pos), 20)
            elif event.key == pygame.K_UP:
                y_pos = y_pos - speed
                pygame.draw.circle(window, red, (x_pos, y_pos), 20)
            elif event.key == pygame.K_DOWN:
                y_pos = y_pos + speed
                pygame.draw.circle(window, red, (x_pos, y_pos), 20)

    window.fill(white)
    pygame.draw.circle(window, red, (x_pos, y_pos), 20)
    colours = [lightgreen, green, blue, lightblue, darkred, yellow, orange, purple, lightpurple, black]
    colour = random.choice(colours)

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
