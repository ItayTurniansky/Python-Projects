import json
from tkinter import *
import string
import sys
import csv
from tkinter import ttk
from typing import Union


MAX_VALUE = 9999999.0
MIN_VALUE = -9999999.0


class Spreadsheet:
    def __init__(self, rows: str, columns: range, cells: dict, tab: ttk.Frame):
        """Spreadsheet class - contains ows and columns numbers and strings, a dictionary of cells and the tab connected to the spreadsheet"""
        self.rows = rows
        self.columns = columns
        self.cells = cells
        self.tab = tab

    def sum_func(self, split_content: list) -> Union[float, str, list]:
        """return the sum of entered cells"""
        final_sum = 0.0
        tester = 0.0
        split_content[1] = split_content[1].replace("sum", "")
        split_content[1] = split_content[1].replace("(", "")
        split_content[1] = split_content[1].replace(")", "")
        split_content[1] = split_content[1].replace("\n", "")
        cell_list = split_content[1].split(" ")
        for possible_cell in cell_list:
            for cell in self.cells:
                if cell == possible_cell:
                    try:
                        target_label = self.cells[cell][1]["text"]
                        final_sum += float(target_label)
                    except:
                        content = 'No number in the referenced cell'
                        return content
            if tester == final_sum:
                content = 'Not a cell name'
                return content
        return final_sum

    def avg_func(self, split_content: list) -> Union[float, str, list]:
        """returns the average of given cells"""
        final_sum = 0.0
        tester = 0.0
        counter = 0.0
        split_content[1] = split_content[1].replace("avg", "")
        split_content[1] = split_content[1].replace("(", "")
        split_content[1] = split_content[1].replace(")", "")
        split_content[1] = split_content[1].replace("\n", "")
        cell_list = split_content[1].split(" ")
        for possible_cell in cell_list:
            for cell in self.cells:
                if cell == possible_cell:
                    try:
                        target_label = self.cells[cell][1]["text"]
                        final_sum += float(target_label)
                        counter += 1
                    except:
                        content = 'No number in the referenced cell'
                        return content
            if tester == final_sum:
                 content = 'Not a cell name'
                 return content
        return round(final_sum / counter, 2)

    def max_func(self, split_content: list) -> Union[float, str, list]:
        """returns the maximum value of given cells"""
        tester = MIN_VALUE
        tmp_max = MIN_VALUE
        split_content[1] = split_content[1].replace("max", "")
        split_content[1] = split_content[1].replace("(", "")
        split_content[1] = split_content[1].replace(")", "")
        split_content[1] = split_content[1].replace("\n", "")
        cell_list = split_content[1].split(" ")
        for possible_cell in cell_list:
            for cell in self.cells:
                if cell == possible_cell:
                    try:
                        target_label = float(self.cells[cell][1]["text"])
                        if target_label > tmp_max:
                            tmp_max = target_label
                            tester = tmp_max
                    except:
                        content = 'No number in the referenced cell'
                        return content
        if tester == MIN_VALUE:
            content = 'Not a cell name'
            return content
        return tmp_max

    def min_func(self, split_content: list) -> Union[float, str, list]:
        """return the minimum value in the given cells"""
        tester = MAX_VALUE
        tmp_min = MAX_VALUE
        split_content[1] = split_content[1].replace("min", "")
        split_content[1] = split_content[1].replace("(", "")
        split_content[1] = split_content[1].replace(")", "")
        split_content[1] = split_content[1].replace("\n", "")
        cell_list = split_content[1].split(" ")
        for possible_cell in cell_list:
            for cell in self.cells:
                if cell == possible_cell:
                    try:
                        target_label = float(self.cells[cell][1]["text"])
                        if target_label <= tmp_min:
                            tmp_min = target_label
                            tester = tmp_min
                    except:
                        content = 'No number in the referenced cell'
                        return content
        if tester == MAX_VALUE:
             content = 'Not a cell name'
             return content
        return tmp_min

    def evaluateCell(self, cell__content: str, label: Label) -> Union[float, str, list]:
        """a functions that handles a cells input based on formulas and cell pointers"""
        # Get the content from the string var
        # and make it lowercase
        content = cell__content
        content = content.lower()
        error_content = "nan"
        # get the reference to the label
        label = label
        # if the cell starts with a = it is evaluated
        if content.startswith('='):
            split_content = content.split("=")
            if split_content[1].startswith("sum"):
                tmp_sum = self.sum_func(split_content)
                if tmp_sum != label['text']:
                    label['text'] = tmp_sum
            elif split_content[1].startswith("avg"):
                tmp_avg = self.avg_func(split_content)
                if tmp_avg != label['text']:
                    label['text'] = tmp_avg
            elif split_content[1].startswith("max"):
                tmp_max = self.max_func(split_content)
                if tmp_max != label['text']:
                    label['text'] = tmp_max
            elif split_content[1].startswith("min"):
                tmp_min = self.min_func(split_content)
                if tmp_min != label['text']:
                    label['text'] = tmp_min
            # Loop through all cells ...
            else:
                for cell in self.cells:
                    # ... and see if their name appears in this cell
                    if cell in content.lower():
                        # if it is then replace the name occurences
                        # with the evaluated content from there.
                        content = content.replace(cell, str(self.evaluateCell(str(self.cells[cell][1]["text"]), self.cells[cell][1])))
                        # Get the content without the = and try to evaluate it
                content = content[1:]
                try:
                    content = eval(content)
                except:
                    return error_content
                label['text'] = content
                return content
        else:
            label['text'] = content
            return content
        return content

    def generate_json(self) -> None:
        """function that generates a JSON file based on the spreadsheet values"""
        header = self.rows
        json_data = {}
        for key, value in self.cells.items():
            json_data[key] = [value[0].get(), value[1]['text']]
        counter = 0
        print(json_data)
        file = open('data.json', 'w', encoding='UTF8', newline='')
        file.write(json.dumps(json_data, indent=4))
        file.close()

    def generate_csv(self) -> None:
        """function that generates a CSV file based on the spreadsheet values"""
        header = self.rows
        csv_data = []
        for key, value in self.cells.items():
            csv_data.append(value[0].get())
        counter = 0
        main_array = []
        for y in self.columns:
            inner_array = []
            for x in self.rows:
                inner_array.append(csv_data[counter])
                counter += 1
            main_array.append(inner_array)
        print(main_array)

        file = open('data.csv', 'w', encoding='UTF8', newline='')
        writer = csv.writer(file)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(main_array)
        file.close()

    def get_rows(self) -> str:
        return self.rows

    def get_columns(self) -> range:
        return self.columns

    def get_cells(self) -> dict:
        return self.cells

    def set_rows(self, rows) -> None:
        self.rows = rows

    def set_columns(self, columns) -> None:
        self.columns = columns

    def set_cells(self, cells) -> None:
        self.cells = cells
