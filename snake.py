from turtle import Turtle

# Constants 
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.parts = []
        self.create_sneake()
        self.head = self.parts[0]

    def create_sneake(self):
        for pos in STARTING_POSITIONS:
            self.add_part(pos)

    def move(self):
        for seg_num in range(len(self.parts) - 1, 0, -1):
            coordinate_x = self.parts[seg_num - 1].xcor()
            coordinate_y = self.parts[seg_num - 1].ycor()
            self.parts[seg_num].goto(coordinate_x, coordinate_y)
        self.head.forward(MOVE_DISTANCE)

    def add_part(self, position):
        new_snake_part = Turtle("square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.parts.append(new_snake_part)

    def extend(self):  # adds new part to the end of snake.
        self.add_part(self.parts[-1].position())

    # Directions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
