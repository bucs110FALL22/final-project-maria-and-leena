
class Snake:

    def __init__(self):
        pass
#Snake movement

    def move(self, direction):
        if direction == 'UP':
            snake_pos_y: -10
            snake_pos_x: 0
        if direction == 'DOWN':
            snake_pos_y: 10
            snake_pos_x: 0
        if direction == 'RIGHT':
            snake_pos_y: 0
            snake_pos_x: 10
        if direction == 'LEFT':
            snake_pos_y: 0
            snake_pos_x: -10
        pygame.display.update()
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