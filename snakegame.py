from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


food=Food()
food.refresh()
snake=Snake()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")

game_is_on=True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    food.move_food()
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()
        scoreboard.update_scoreboard()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()
    if food.xcor()>270 or food.xcor()<-270 or food.ycor()>270 or food.ycor()<-270:
        food.refresh()
        food.add_escape()
        if food.escape_count==2:
            game_is_on=False
            scoreboard.food_escaped_game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()



screen.exitonclick()
