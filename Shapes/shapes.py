#################################################################
# FILE : shapes.py
# WRITER : Itay Turniansky , itayturni , 322690397
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: A program that calculates the area of different sizes based on user input
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES:
#################################################################
import math


def triangle_area(line):
    """returns the area of a triangle with a given line"""
    return (math.sqrt(3)*(line**2))/4


def rectangle_area(line1, line2):
    """returns the area of a rectangle with given lines"""
    return line1 * line2


def circle_area(radius):
    """returns the area of a circle with a given radius"""
    return radius**2 * math.pi


def shape_area():
    """A function that calculates the area of shapes based on the user's input"""
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if shape == "1":
        radius = float(input())
        return circle_area(radius)
    elif shape == "2":
        line1 = float(input())
        line2 = float(input())
        return rectangle_area(line1, line2)
    elif shape == "3":
        line = float(input())
        return triangle_area(line)


