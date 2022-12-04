import src.Snake
import pygame
import random
import sys

class Snake:        #controller 
#Snake movement
    def __init__(self): 
    #setup pygame data
      self.state = "Menu"
      self.snake = snake.Snake()
    
    def mainloop(self):
    #select state loop
      snake.move
      while True: 
        if (self.state == "Menu"):
          self.menuloop()
        elif (self.state == "GAME"):
          self.gameloop()
        elif(self.state == "Gameover"):
          self.gameover()
    mainloop()
  
  ### below are some sample loop states ###

def menuloop(self):
      pygame.init()
      dis = pygame.display.set_mode((400, 300))
      pygame.display.set_caption('Snake Game')
#Create Screen
      surface = pygame.display.set_mode()
      color = (95, 158, 160, 255)
      surface.fill(color)
      pygame.display.flip()
      screen= pygame.display.set_mode()
      x,y= screen.get_size()
      print (x,y)
      font_style = pygame.font.SysFont("Arial", 25)
      score_font = pygame.font.SysFont("Arial", 35)
#Allow player to choose color of snake
      red: (255, 0, 0)
      yellow: (255, 255, 0)
      blue: (0, 0, 255)
      green: (0, 128, 0)      
      food_spawn = True
      square: pygame.draw.rect(dis, "red", [200, 150, 10, 10])
      circle: pygame.draw.circle(dis, "red", food_pos, 10)
menuloop()  

shape_food = input("Please input the shape you would like your food to be (square or circle: ")
      #event loop
    
snake = False
color_snake = input("Please input the color you would like your snake to be (red, yellow, blue, green): ")
dis = pygame.display.set_mode((400, 300))
while not snake:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          snake = True   
          pygame.draw.rect(dis, color_snake, [200, 150, 10, 10])
    pygame.display.update()
pygame.display.flip()
food = False
window_x= 800
window_y= 600
food_pos= [

      random.randrange(1, (window_x // 5)) * 5,
      random.randrange(1, (window_y // 5)) * 5
      ]
while not food:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        food= True
    pygame.draw.shape_food(dis,"red", food_pos)
    pygame.display.update()
      #update data


      #redraw
      
def gameloop(self):
      while self.state == "GAME":
      #event loop
        for event in pygame.event.get(): 
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: 
              self.snake.move("DOWN")
            if event.key == pygame.K_UP: 
              self.snake.move('UP')
            if event.key == pygame.K_RIGHT:
              self.snake.move('RIGHT')
            if event.key == pygame.K_LEFT: 
              self.snake.move('LEFT')
            if event.key == pygame.K_SPACE:
              color = self.getcolorfromuser()
              self.snake.change_color(color)
          pygame.font.SysFont("Arial", 65)
          if snake_pos[0] < 0 or snake_pos > window_x-10:
            gameloop()
            self.state = "Gameover"
          if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            gameloop()
            self.state = "Gameover"


def move(self, direction):
  if direction == 'UP':
    snake_pos[1]-=10
  if direction == 'DOWN':
    snake_pos[1] +=10
  if direction == 'RIGHT':
    snake_pos[0]+= 10
  if direction == 'LEFT':
    snake_pos[0]-= 10
  snake.move  
move()

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
change_color()

def change_shape(self, shape_food):
      if shape_food == "square":
        food.shape = "square"
      elif shape_food == "circle":
        food.shape = "circle"
      else:
        shape_food == "triangle"
        food.shape = "triangle"
      pygame.display.update()      
snake_pos= [100,50]
snake_bod = [[100,50],
             [90,50],
             [80,50],
             [70,50]
            ]
change_shape()

snake_bod.insert(0, list(snake_pos))
if snake_pos[0] == food_pos[0] and snake_pos[0] == food_pos[1]:
  score +=10
  fruit_spawn = False
else: 
    snake_bod.pop()
if not fruit_spawn:
  fruit_pos= [random.randrange(1,(window_x//10))*10, random.randrange (1, (window_y//10))*10]
  fruit_spawn= True
  surf= pygame.surface.fill("black")
for pos in snake_bod:
  pygame.draw.rect(surf, "green",
  pygame.Rect(pos[0], pos[1], 10, 10))
  pygame.draw.rect(surf, "white", pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

def Your_score(score):
  score = score.render("Score: " + str(score), True, "yellow")
  dis.blit(score, [0, 0])
  pygame.display.update()
      #update data
Your_score()     
    #redraw
    
def gameoverloop(self):
  while self.state == "Gameover": 
    font= pygame.font.SysFont("Arial", 65)
    gameover_screen= font.render("Your Score:" + str(score), True, "red")
    gameover_rect= gameover_screen.get_rect()
    gameover_rect.midtop= (window_x/2,window_y/4)
    dis.blit_window(gameover_screen, gameover_rect)
  
pygame.display.flip()
gameoverloop()
      #update data
  
      #redraw
