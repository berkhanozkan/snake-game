import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("White Hunter")
window.tracer(0)

snake = Snake()
food = Food()
score = Score()

# Directions on keyboard
window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

is_game_active = True
while is_game_active:
    window.update()
    time.sleep(0.1)
    snake.move()

    # Eat Food :)
    if snake.head.distance(food) < 18:
        score.increase_score()
        snake.extend()
        food.refresh()

    # Pass wall
    for part in snake.parts:
        if part.xcor() > 280:
            part.goto(-280, part.ycor())
        elif part.xcor() < -280:
            part.goto(280, part.ycor())
        elif part.ycor() > 280:
            part.goto(part.xcor(), -280)
        elif part.ycor() < -280:
            part.goto(part.xcor(), 280)

    # Hit Tail
    for part in snake.parts[1:]:
        if snake.head.distance(part) < 10:
            is_game_active = False
            score.game_over()


window.exitonclick()
