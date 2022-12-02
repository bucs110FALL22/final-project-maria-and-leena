#Call your mainloop

###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/


import pygame
import random
import time
import sys

#import your controller
pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake Game')
#Create Screen
surface = pygame.display.set_mode()
color = (95, 158, 160, 255)
surface.fill(color)
pygame.display.flip()

#Window Size
window_x=720
windiw_y=480
x,y=screen.get_size()

font_style = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("Arial", 35)

#Allow player to choose color of snake
red: (255, 0, 0)
yellow: (255, 255, 0)
blue: (0, 0, 255)
green: (0, 128, 0)

color_snake = input("Please input the color you would like your snake to be (red, yellow, blue green): ")

#Allow player to choose shape of food
food_pos= [
    random.randrange(1, (frame_size_x // 5)) * 5,
    random.randrange(1, (frame_size_y // 5)) * 5
    ]
food_spawn = True

square: pygame.draw.rect(dis, "red", [200, 150, 10, 10])
circle: pygame.draw.circle(dis, "red", food_pos, 10)

shape_food = input("Please input the shape you would like your food to be (square or circle: ")

#Create Snake
snake = False
while not snake:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snake = True
    pygame.draw.rect(dis, color_snake, [200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()

#Food

food = False
while not food:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        food= True
    pygame.draw.shape_food(dis,"red", food_pos)
    pygame.display.update()
pygame.quit()
quit()

#Buttons for Snake to move around
snake_pos= [100,50]
snake_bod = [[100,50],
             [90,50],
             [80,50],
             [70,50]
            ]
class Snake:

    def __init__(self):
        pass
#Snake movement

    def move(self, direction):
        if direction == 'UP':
            snake_pos[1]-=10
        if direction == 'DOWN':
            snake_pos[1] +=10
        if direction == 'RIGHT':
            snake_pos[0]+= 10
        if direction == 'LEFT':
            snake_pos[0]-= 10
         
    def change_color(self, color_snake):
        if color_snake == "red":
          snake.color = "red"
        elif color_snake == "green":
          snake.color = "green"
        elif color_snake == "blue":
          snake.color = "blue"
        elif color_snake == "yellow":
          snake.color = "yellow"
        else:
          snake.color = "white"
        pygame.display.update()

    def change_shape(self, shape_food):
      if shape_food == "square":
        food.shape = "square"
      elif shape_food == "circle":
        food.shape = "circle"
      else:
        shape_food == "triangle"
        food.shape = "triangle"
      pygame.display.update()
    
          
#Scoreboard
    def Your_score(score):
      value = score_font.render("Your Score: " + str(score), True, "yellow")
      dis.blit(value, [0, 0])

#Snake eats food + grows bigger  
      snake_bod.insert(0, list(snake_pos))
      if snake_pos[0] == food_pos[0] and snake_pos[0] == food_pos[1]:
        score +=10
        fruit_spawn = False
      else: 
        snake_body.pop()
      if not fruit_spawn:
        fruit_pos= [random.randrange(1, (window_x//10))*10, random.randrange (1, (window_y//10))*10]
      fruit_spawn= True
      surface.fill(black)

      for i in snake_bod:
        pygame.draw.rect(surface, blue, pygame.Rect(i[0],i[1],10,10))
        pygame.draw.rect(surface, white, pygame.Rect(fruit_pos[0],fruit_pos[1],10,10)
