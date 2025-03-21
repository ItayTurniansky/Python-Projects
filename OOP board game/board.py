# ################################################################
# FILE : board.py WRITER : Itay Turniansky ,itayturni , 322690397
# EXERCISE : intro2cs ex9 2024 DESCRIPTION: ex9
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: google
# NOTES: None
# ################################################################
from typing import Tuple, List, Optional
from car import Car

Coordinates = Tuple[int, int]
ROWS_NUM = 7
COL_NUM = 8
EXIT_LOC = (3, 7)


def create_loc_dict() -> dict:
    loc_dict = {}
    for row in range(ROWS_NUM):
        for col in range(COL_NUM):
            if col == COL_NUM-1 and row == EXIT_LOC[0]:
                loc_dict[(row, col)] = "E"
            elif col == COL_NUM-1 and row != EXIT_LOC[0]:
                loc_dict[(row, col)] = "*"
            else:
                loc_dict[(row, col)] = "_"
    return loc_dict


class Board:
    """
    Board class for "rush hour" game board
    """

    def __init__(self) -> None:
        """
        A constructor for a Board object.
        """
        # Note that this function is required in your Board implementation.
        self.row = ROWS_NUM
        self.col = COL_NUM
        self.target = EXIT_LOC
        self.loc_dict = create_loc_dict()
        self.car_dict = {}

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed.
        :return: A string representing the current status of the board.
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # implement your code and erase the "pass"
        return_string = ""
        for loc in self.loc_dict.keys():
            if loc[1] == self.col-1:
                return_string += (self.loc_dict[loc] + "\n")
            else:
                return_string += (self.loc_dict[loc] + " ")
        return return_string

    def cell_list(self) -> List[Coordinates]:
        """
        This function returns the coordinates of cells in this board.
        :return: list of coordinates.
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        return_list = []
        for loc in self.loc_dict.keys():
            if loc[1] != self.col-1:
                return_list.append(loc)
        return_list.append(EXIT_LOC)
        return return_list

    def possible_moves(self) -> List[Tuple[str, str, str]]:
        """ 
        This function returns the legal moves of all cars in this board.
        :return: list of tuples of the form (name, move_key, description)
                 representing legal moves. The description should briefly
                 explain what is the movement represented by move_key.
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"description"), ('R','r',"description"), ('O','u',"description")]
        return_list = []
        for car in self.car_dict.keys():
            if self.car_dict[car][2] == 0:
                if self.car_dict[car][1][0] - 1 >= 0:
                    if self.loc_dict[(self.car_dict[car][1][0] - 1, self.car_dict[car][1][1])] in ("_", "E"):
                        return_list.append((car, "u", "this car can go up one step"))
                if self.car_dict[car][1][0] + 1 + self.car_dict[car][0] <= self.row:
                    if self.loc_dict[(self.car_dict[car][1][0] + self.car_dict[car][0], self.car_dict[car][1][1])] in ("_", "E"):
                        return_list.append((car, "d", "this car can go down one step"))
            if self.car_dict[car][2] == 1:
                if self.car_dict[car][1][1] - 1 >= 0:
                    if self.loc_dict[(self.car_dict[car][1][0], self.car_dict[car][1][1]-1)] in ("_", "E"):
                        return_list.append((car, "l", "this car can go left one step"))
                if self.car_dict[car][1][1] + 1 + self.car_dict[car][0] <= self.col:
                    if self.loc_dict[(self.car_dict[car][1][0], self.car_dict[car][1][1] + self.car_dict[car][0])] in ("_", "E"):
                        return_list.append((car, "r", "this car can go right one step"))
        return return_list

    def target_location(self) -> Coordinates:
        """
        This function returns the coordinates of the location that should be 
        filled for victory.
        :return: (row, col) of the goal location.
        """
        # In this board, returns (3,7)
        return EXIT_LOC

    def cell_content(self, coordinates: Coordinates) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinates: tuple of (row, col) of the coordinates to check.
        :return: The name of the car in "coordinates", None if it's empty.
        """
        # implement your code and erase the "pass"
        for loc in self.loc_dict.keys():
            if coordinates == loc:
                if self.loc_dict[coordinates] in ("_", "E"):
                    return None
                else:
                    return self.loc_dict[coordinates]

    def add_car(self, car: Car) -> bool:
        """
        Adds a car to the game.
        :param car: car object to add.
        :return: True upon success, False if failed.
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        if tuple(car.location) in self.loc_dict.keys():
            if car.orientation == 0:
                for i in range(1, car.length):
                    if (car.location[0] + i, car.location[1]) not in self.loc_dict.keys() or self.loc_dict[
                        (car.location[0] + i, car.location[1])] not in ("_", "E"):
                        return False
                for i in range(0, car.length):
                    self.loc_dict[(car.location[0 + i], car.location[1])] = car.name
                self.car_dict[car.name] = [car.length, car.location, car.orientation]
                return True
            elif car.orientation == 1:
                for i in range(1, car.length):
                    if (car.location[0], car.location[1] + i) not in self.loc_dict.keys() or self.loc_dict[
                        (car.location[0], car.location[1] + i)] not in ("_", "E"):
                        return False
                for i in range(0, car.length):
                    self.loc_dict[(car.location[0], car.location[1]+i)] = car.name
                self.car_dict[car.name] = [car.length, car.location, car.orientation]
                return True
            return False

    def move_car(self, name: str, move_key: str) -> bool:
        """
        Moves car one step in a given direction.
        :param name: name of the car to move.
        :param move_key: the key of the required move.
        :return: True upon success, False otherwise.
        """
        # implement your code and erase the "pass"
        cell_list = []
        for loc in self.loc_dict.keys():
            if self.loc_dict[loc] == name:
                cell_list.append(loc)
        if len(cell_list) != 0:
            if move_key == "u":
                self.loc_dict[tuple(cell_list[-1])] = "_"
                self.loc_dict[(cell_list[0][0]-1, cell_list[0][1])] = name
                self.car_dict[name][1][0] -= 1
                return True
            if move_key == "d":
                self.loc_dict[tuple(cell_list[0])] = "_"
                self.loc_dict[(cell_list[-1][0] + 1, cell_list[0][1])] = name
                self.car_dict[name][1][0] += 1
                return True
            if move_key == "l":
                self.loc_dict[tuple(cell_list[-1])] = "_"
                self.loc_dict[(cell_list[0][0], cell_list[0][1]-1)] = name
                self.car_dict[name][1][1] -= 1
                return True
            if move_key == "r":
                self.loc_dict[tuple(cell_list[0])] = "_"
                self.loc_dict[(cell_list[-1][0], cell_list[-1][1]+1)] = name
                self.car_dict[name][1][1] += 1
                return True
        return False
