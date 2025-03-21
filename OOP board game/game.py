# ################################################################
# FILE : game.py WRITER : Itay Turniansky ,itayturni , 322690397
# EXERCISE : intro2cs ex9 2024 DESCRIPTION: ex9
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: google
# NOTES: None
# ################################################################
import sys

import helper
from board import Board
from helper import *
from car import Car


def validate_input(user_input: str) -> bool:
    if "," not in user_input:
        return False
    car_name = user_input.split(",")[0]
    direction = user_input.split(",")[1]
    if car_name not in ("Y", "B", "O", "G", "W", "R"):
        return False
    if direction not in ("u", "d", "l", "r"):
        return False
    return True


def validate_car_for_game(car):
    if car.name not in ("Y", "B", "O", "G", "W", "R"):
        return False
    return True


class Game:
    """
    A game class to run a full game of "rush hour"
    """

    def __init__(self, board: Board) -> None:
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        # You may assume board follows the API
        self.board = board

    def __single_turn(self, player_input: str, board: Board):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code and erase the "pass"
        while not validate_input(player_input):
            player_input = input("Invalid Input")
        tmp_car_name = player_input.split(",")[0]
        tmp_direction = player_input.split(",")[1]
        tmp_possible_moves = self.board.possible_moves()
        var = 0
        while var == 0:
            for move in tmp_possible_moves:
                if move[0] == tmp_car_name and move[1] == tmp_direction:
                    self.board.move_car(tmp_car_name, tmp_direction)
                    var += 1
            if var == 0:
                print("Invalid Move, try one of the following:")
                player_input = input(tmp_possible_moves)
                while not validate_input(player_input):
                    player_input = input("Invalid Input")
                tmp_car_name = player_input.split(",")[0]
                tmp_direction = player_input.split(",")[1]
                tmp_possible_moves = self.board.possible_moves()

    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        for item in car_dict.keys():
            if int(car_dict[item][0]) > 0 and car_dict[item][2] in (0, 1) and int(car_dict[item][1][0]) >= 0 and int(
                    car_dict[item][1][1]) >= 0:
                tmp_car = Car(item, car_dict[item][0], car_dict[item][1], car_dict[item][2])
                if validate_car_for_game(tmp_car):
                    self.board.add_car(tmp_car)
        print(self.board)
        while self.board.cell_content(self.board.target_location()) is None:
            player_input = input("please enter your next move!")
            if player_input == "!":
                break
            self.__single_turn(player_input, self.board)
            print(self.board)
        print("Game Over!")


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    board_1 = Board()
    if len(sys.argv) > 1:
        car_dict = helper.load_json(sys.argv[1])
    else:
        car_dict = helper.load_json("car_config.json")
    game_1 = Game(board_1)
    game_1.play()
