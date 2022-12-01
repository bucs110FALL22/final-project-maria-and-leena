import src.snake

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.state = "Game"
    self.snake = snake.Snake()
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

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
          if event.key == pgame.K_SPACE:
            color = self.getcolorfromuser()
            self.snake.change_color(color)

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
