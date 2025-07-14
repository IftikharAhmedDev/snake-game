from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_segments = []
snake = Turtle()
snake.shape("circle")
snake.color("Yellow")
snake1 = Turtle()
snake1.shape("circle")
snake1.color("Yellow")

snake_segments.append(snake)
print(snake_segments)












screen.exitonclick()