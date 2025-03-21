# ################################################################
# FILE : ex7.py WRITER : Itay Turniansky ,itayturni , 322690397
# EXERCISE : intro2cs ex7 2024 DESCRIPTION: ex7
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: google, chatgpt
# NOTES: None
# ################################################################
from typing import *
from ex7_helper import *


def mult(x: N, y: int) -> N:
    """a function that calculates multiplication with restrictions, and O(n) runtime"""
    if y == 0:
        return 0
    return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
    """a function that returns if a number is even"""
    if n == 0:
        return True
    if n == 1:
        return False
    if is_even(subtract_1(n)):
        return False
    else:
        return True


def log_mult(x: N, y: int) -> N:
    """a function that calculates multiplication with restrictions, and O(log(n)) runtime"""
    if x == 0:
        return 0
    if not is_odd(int(x)):
        return log_mult(divide_by_2(int(x)), add(y, y))
    else:
        return add(log_mult(divide_by_2(int(x)), add(y, y)), y)


def is_power(b: int, x: int) -> bool:
    """a function that returns True if there is a natural n that solves b^n == x"""
    return is_power_helper(b, x, b)


def is_power_helper(b: int, x: int, b_p: int) -> bool:
    """a help function to the is_power function"""
    if b_p == x:
        return True
    if b_p > x:
        return False
    return is_power_helper(b, x, log_mult(b, b_p))


def reverse(s: str) -> str:
    """a function that reverses a string"""
    if len(s) <= 1:
        return s
    else:
        return append_to_end(reverse(s[1:]), s[0])


def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any) -> None:
    """a function that plays the hanoi tower game and solves it with recursion"""
    if n > 0:
        play_hanoi(hanoi, n-1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n-1, temp, dest, src)


def number_of_ones_helper(n: int) -> int:
    """a help function the numer of ones function that returns each number's number of ones"""
    total_1 = 0
    if n % 10 == 1:
        total_1 += 1
    if n == 0:
        return 0
    return total_1 + number_of_ones_helper(n // 10)


def number_of_ones(n: int) -> int:
    """a function that returns the number of total ones in all numbers from the input to 1"""
    total_1 = 0
    if n == 0:
        return 0
    else:
        total_1 += number_of_ones_helper(n)
    return total_1 + number_of_ones(n-1)


def compare_lists_cells(l1: List[int], l2: List[int]) -> bool:
    """a help function for the compare_2d_lists function that compares each 2 individual cells"""
    tmp_bool = False
    if len(l1) != len(l2):
        return False
    elif len(l1) == len(l2) == 0:
        return True
    if l1[0] == l2[0]:
        tmp_bool = True
    return tmp_bool and compare_lists_cells(l1[1:], l2[1:])


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    """a function that compares two ,2dimensional lists"""
    tmp_bool = False
    if len(l1) != len(l2):
        return False
    elif len(l1) == len(l2) == 0:
        return True
    if compare_lists_cells(l1[0], l2[0]):
        tmp_bool = True
    return tmp_bool and compare_2d_lists(l1[1:], l2[1:])


def magic_list(n: int) -> List[str]:
    """a function that returns a list with the specifications required in the question"""
    tmp_list = []
    if n == 0:
        return []
    tmp_list = magic_list(n-1)
    tmp_list.append(str(magic_list(n-1)))
    return tmp_list




