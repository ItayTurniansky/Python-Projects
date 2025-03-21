#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Itay Turniansky , itayturni , 322690397
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: A program that calculates mathematical expressions
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES:
#################################################################

def calculate_mathematical_expression(num1, num2, action):
    """"this function gets two numbers and a mathematical action and return the result of the mathematical action
    between the two numbers"""

    if action == "+":
        return float(num1) + float(num2)
    elif action == "-":
        return float(num1) - float(num2)
    elif action == "*":
        return float(num1) * float(num2)
    elif action == ":":
        if float(num2) == 0:
            return None
        else:
            return float(num1) / float(num2)


def calculate_from_string(string):
    """this function receives a string of a mathematical equation and returns its result"""
    split_string = string.split(" ")
    return calculate_mathematical_expression(split_string[0], split_string[2], split_string[1])



