#################################################################
# FILE : math_print.py
# WRITER : Itay Turniansky , itayturni , 322690397
# EXERCISE : intro2cs ex1 2024
# DESCRIPTION: A program that calculates stuff with the math module
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES:
#################################################################
import math


def golden_ratio():
    """function that returns the golden ration"""
    print((1+math.sqrt(5))/2)


def six_squared():
    """function that returns six squared"""
    print(math.pow(6, 2))


def hypotenuse():
    """function that returns the size of the third side of a triangle with a side sized 5 and another side sized 12"""
    print(math.sqrt(math.pow(5, 2)+math.pow(12, 2)))


def pi():
    """a function that returns constant pi"""
    print(math.pi)


def e():
    """a function that returns the constant e"""
    print(math.e)


def squares_area():
    """a function that returns the area of all the squares with sides sizes from 1-10"""
    print(1*1, 2*2, 3*3, 4*4, 5*5, 6*6, 7*7, 8*8, 9*9, 10*10)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
    print(7//2)

