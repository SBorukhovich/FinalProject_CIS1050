import pygame 
import time
import random

pygame.init()  #initializes pygame

#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0) 
orange= (255,165,0)
blue = (0,0,255)

width, height = 600,400

game_display = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_size = 16
snake_speed= 10

message_font = pygame.font.SysFont('ubuntu',30)
score_font =  pygame.font.SysFont('ubuntu',20)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0,0])
    
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, blue, [pixel[0],pixel[1], snake_size, snake_size])

def run_game():        
    game_over = False
    game_close = False
    x = width/2
    y = height/2
    x_speed= 0
    y_speed= 0
    snake_pixels = []
    snake_length = 1
    food_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0


    while not game_over:
        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            game_over_message2 = message_font.render("Press 1 to Exit or 2 to Restart", True, red)
            game_display.blit(game_over_message2, [width / 4, height /2])
            print_score(snake_length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: #When user press 1 game ends
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2: #When user press 2 game restarts
                        run_game()
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_speed
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_speed
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_speed
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_speed
        if x>= width or x< 0 or y >= height or y<0:
            game_close = True
        x += x_speed
        y += y_speed
        
        game_display.fill(black) 
        pygame.draw.rect(game_display, orange, [food_x, food_y,snake_size, snake_size])
        
        snake_pixels.append([x,y])
        
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]  #delets the last pixel when the snake moves so it satys consistent
        for pixel in snake_pixels[:-1]: 
            if pixel == [x,y]:  #if the snake crushes into itself the game stops
                game_close = True
                
        draw_snake(snake_size,snake_pixels)
        print_score(snake_length-1)
        
        pygame.display.update()
        
        if x == food_x and y == food_y: #when snake gets food
            food_x = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
            snake_length +=1 
        clock.tick(snake_speed)
    pygame.quit()
    quit()
run_game()