import pygame
import random
#import your controller
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake game')
#Create Screen
surface = pygame.display.set_mode((400,300))
color = (95, 158, 160, 255)
surface.fill(color)
pygame.display.flip()

#Allow player to choose color and shape of snake
red:(255,0,0)
yellow:(255,255,0)
blue:(0,0,255)
green:(0,128,0)

color_snake="Please input the color you would like your snake to be (Red, Yellow, Blue Green): "

#Create Snake
snake=False
while not snake:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            snake=True
    pygame.draw.rect(dis,color_snake,[200,150,10,10])
    if color_snake=="red":
        snake.color="red"
    elif color_snake=="green":
        snake.color="green"
    elif color_snake=="blue":
        snake.color="blue"
    elif color_snake=="yellow":
      snake.color="yellow"
      pygame.display.update()
pygame.quit()
quit()
 
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######


# https://codefather.tech/blog/if-name-main-python/


#Food (Random Coord)