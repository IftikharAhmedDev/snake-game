from turtle import Turtle, Screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

positions = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []

for position in positions:
    new_body = Turtle(shape="square")
    new_body.color("Yellow")
    new_body.goto(position)
    snake_body.append(snake_body)

print(snake_body)












screen.exitonclick()