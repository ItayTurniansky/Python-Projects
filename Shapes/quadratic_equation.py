#################################################################
# FILE : quadratic_equation.py
# WRITER : Itay Turniansky , itayturni , 322690397
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: A program that solves quadratic equation based on user's input
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES:
#################################################################
import math


def quadratic_equation(a, b, c):
    """A function that gets three numbers and returns the solution to their quadratic equation"""
    root = b * b - 4 * a * c
    if root > 0:
        return (-b + math.sqrt(root)) / (a * 2), (-b - math.sqrt(root)) / (a * 2)
    elif root == 0:
        return (-b + math.sqrt(root)) / (a * 2), None
    else:
        return None, None


def quadratic_equation_user_input():
    """A function that receives 3 numbers from the user and returns their quadratic equation solutions"""
    answer = input("Insert coefficients a, b, and c: ")
    coefficients = answer.split(" ")
    if coefficients[0] == '0':
        print("The parameter 'a' may not equal 0")
    else:
        solution1, solution2 = quadratic_equation(float(coefficients[0]), float(coefficients[1]), float(coefficients[2]))
        if solution2 == None:
            if solution1 == None:
                print("The equation has no solutions")
            else:
                print("The equation has 1 solution: " + str(solution1))
        else:
            print("The equation has 2 solutions: " + str(solution1) + " and " +str(solution2))


