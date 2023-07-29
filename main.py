import turtle as turt
from turtle import Screen

random_turtle = turt.Turtle()
screen = Screen()
screen.title("Welcome to Etch-A-Sketch!")

random_turtle.pensize(2)


def move_forward():
    """Moves the turtle forward."""
    random_turtle.forward(10)


def move_backward():
    """Moves the turtle backward."""
    random_turtle.backward(10)


def counter_clockwise():
    """Moves the turtle counter-clockwise."""
    random_turtle.left(10)


def clockwise():
    """Moves the turtle clockwise."""
    random_turtle.right(10)


def clear_screen():
    """Clears the screen and reset the turtle."""
    random_turtle.clear()
    random_turtle.penup()
    random_turtle.home()
    random_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
