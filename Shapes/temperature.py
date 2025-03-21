#################################################################
# FILE : temperature.py
# WRITER : Itay Turniansky , itayturni , 322690397
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: A program that returns boolean values based on conditions of the past 3 days weather
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES:
#################################################################

def is_vormir_safe(min_temp, temp1, temp2, temp3):
    """Returns boolean value based on if 2 of the 3 last inputs are higher than the first input """
    if temp1 > min_temp:
        if temp2 > min_temp:
            return True
        elif temp3 > min_temp:
            return True
        else:
            return False
    elif temp2 > min_temp:
        if temp1 > min_temp:
            return True
        elif temp3 > min_temp:
            return True
        else:
            return False
    elif temp3 > min_temp:
        if temp2 > min_temp:
            return True
        elif temp1 > min_temp:
            return True
        else:
            return False
    else:
        return False
