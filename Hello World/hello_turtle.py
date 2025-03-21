#################################################################
# FILE : hello_turtle.py
# WRITER : Itay Turniansky , itayturni , 322690397
# EXERCISE : intro2cs ex1 2024
# DESCRIPTION: A program that draws stuff with the turtle
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES:
#################################################################
import turtle


def draw_edge_and_turn():
    """a function that makes the turtle move forward 45 steps then turn right 120 steps"""
    turtle.forward(45)
    turtle.right(120)


def draw_triangle():
    """this function draws a triangle"""
    draw_edge_and_turn()
    draw_edge_and_turn()
    draw_edge_and_turn()


def draw_sail():
    """this function draws a sail"""
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    draw_triangle()
    turtle.right(30)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)


def forward_and_draw_sail():
    """a function that moves the turtle forward 50 steps then draws a sail"""
    turtle.forward(50)
    draw_sail()


def draw_ship():
    """this function draws a ship"""
    forward_and_draw_sail()
    forward_and_draw_sail()
    forward_and_draw_sail()
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(180)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(30)


def draw_fleet():
    """this function draws two ships next to each other"""
    draw_ship()
    turtle.left(90)
    turtle.up()
    turtle.forward(300)
    turtle.down()
    turtle.right(180)
    draw_ship()
    turtle.up()
    turtle.right(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.down()


if __name__ == "__main__":
    # draw_triangle()
    # draw_sail()
    # draw_ship()
    draw_fleet()
    turtle.done()




