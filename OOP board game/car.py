# ################################################################
# FILE : car.py WRITER : Itay Turniansky ,itayturni , 322690397
# EXERCISE : intro2cs ex9 2024 DESCRIPTION: ex9
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: google
# NOTES: None
# ################################################################
from typing import Tuple, List, Dict
Coordinates = Tuple[int, int]


class Car:
    """
    Car class
    """

    def __init__(self, name: str, length: int, location: Coordinates,
                 orientation: int) -> None:
        """
        A constructor for a Car object.
        :param name: A string representing the car's name.
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head location (row,col).
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL).
        """
        # Note that this function is required in your Car implementation.
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self) -> List[Coordinates]:
        """
        :return: A list of coordinates the car is in.
        """
        car_coord = []
        for i in range(self.length):
            if self.orientation == 0:
                car_coord.append((self.location[0]+i, self.location[1]))
            elif self.orientation == 1:
                car_coord.append((self.location[0], self.location[1]+i))
        return car_coord

    def possible_moves(self) -> Dict[str, str]:
        """
        :return: A dictionary of strings describing possible movements 
                 permitted by this car.
        """
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings to describe each movements.
        # For example: a car that supports the commands 'f', 'd', 'a' may return
        # the following dictionary:
        # {'f': "cause the car to fly and reach the Moon",
        #  'd': "cause the car to dig and reach the core of Earth",
        #  'a': "another unknown action"}
        #
        return_dict = {}
        if self.orientation == 0:
            return_dict["u"] = (self.location[0]-1, self.location[1])
            return_dict["d"] = (self.location[0]+1, self.location[1])
        elif self.orientation == 1:
            return_dict["l"] = (self.location[0], self.location[1]-1)
            return_dict["r"] = (self.location[0], self.location[1]+1)
        return return_dict

    def movement_requirements(self, move_key: str) -> List[Coordinates]:
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for 
                 this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        return_list = []
        if move_key == "d":
            if self.orientation == 0:
                return_list.append(self.length + self.location[0]+1, self.location[1])
        elif move_key == "u":
            if self.orientation == 0:
                return_list.append(self.location[0] - 1, self.location[1])
        elif move_key == "l":
            if self.orientation == 1:
                return_list.append(self.location[0], self.location[1]-1)
        elif move_key == "r":
            if self.orientation == 1:
                return_list.append(self.location[0], self.location[1]+self.length + 1)
        return return_list

    def move(self, move_key: str) -> bool:
        """
        This function moves the car.
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if move_key == "d":
            if self.orientation == "0":
                self.location = self.location[0]+1, self.location[1]
                return True
        elif move_key == "u":
            if self.orientation == "0":
                self.location = self.location[0]-1, self.location[1]
                return True
        elif move_key == "l":
            if self.orientation == "1":
                self.location = self.location[0], self.location[1]-1
                return True
        elif move_key == "r":
            if self.orientation == "1":
                self.location = self.location[0]+1, self.location[1]+1
                return True
        return False

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.name
