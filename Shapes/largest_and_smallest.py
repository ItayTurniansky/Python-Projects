#################################################################
# FILE : largest_and_smallest.py
# WRITER : Itay Turniansky , itayturni , 322690397
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: A program that calculates the largest and smallest numbers of 3 numbers
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES:
#################################################################
# I chose the 2 last values in the check_largest_and_smallest function because the first one tests the function when
# all the numbers are equal and the second one test the function when two values are equal to zero and one is smaller.
# in my opinion these 2 cases are important to test
def largest_and_smallest(num1, num2, num3):
    """A function that receives three numbers and return the highest and lower number of the three"""
    if num1 >= num2:
        if num1 >= num3:
            if num3 >= num2:
                return num1, num2
            else:
                return num1, num3
    elif num2 >= num3:
        if num1 >= num3:
            return num2, num3
        else:
            return num2, num1
    if num3 >= num1:
        if num2 >= num1:
            return num3, num1
        else:
            return num3, num2


def check_largest_and_smallest():
    """verifies that the function larges_and_smallest works correctly"""
    if largest_and_smallest(17,1,6) == (17,1) :
        if largest_and_smallest(1, 17, 6) == (17, 1):
            if largest_and_smallest(1, 1, 2) == (2, 1):
                if largest_and_smallest(1, 1, 1) == (1, 1):
                    if largest_and_smallest(0, -5, 0) == (0, -5):
                        return True
    return False

