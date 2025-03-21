# Imports
import argparse
from tkinter import font
from tkinter.colorchooser import askcolor
import tkfontchooser
import xlsxwriter
from Spreadsheet import *

HELP_TEXT = ("Welcome to Itay's spreadsheet app!\n "
             "this app can help you manage and control data!\n"
             "you can insert text and integers into the cells.\n"
             "this app supports multiple spreadsheets, each in a separate tab.\n"
             "each cell has a specific id that you can use in the formulas options.\n"
             "Cell ID = (tab_num, column, row). F.E(1a0)\n"
             "if you start a cell with the = mark you can use the one of the following:\n"
             "1)=SUM gets the sum of all values in given cells. F.E =sum(1a0 1a2 3a4)\n"
             "2)=AVG gets the average value of the given cells. F.E =avg(1a0 1a2 3a4)\n"
             "3)=MIN gets the minimum value of the given cells. F.E =min(1a0 1a2 3a4)\n"
             "4)=MAX gets the maximus value of the given cells. F.E =max(1a0 1a2 3a4)\n"
             "this app also has a change color feature.You can customize your text color by clicking the CHANGE FONT COLOR BUTTON\n"
             "this app also has a change font feature.You can customize your text font by clicking the CHANGE FONT BUTTON")
XAXIS = string.ascii_lowercase[0:8]
YAXIS = range(0, 26)
CELLS: dict[str, list] = {}
try:
    ROOT = Tk()
    TITLE = "Spreadsheet App"
    ROOT.title(TITLE)
    NOTEBOOK = ttk.Notebook(ROOT)
    TAB1 = ttk.Frame(NOTEBOOK)
    NOTEBOOK.add(TAB1, text='Tab1')
    NOTEBOOK.grid()
    TABS = [TAB1]
except TclError:
    print("no display")


class App:
    def __init__(self, spreadsheets: dict[int, Spreadsheet], tabs: list[ttk.Frame]) -> None:
        """app class - contains a spreadsheet dict and tabs list"""
        self.spreadsheets = spreadsheets
        self.tabs = tabs

    def generate_x_and_y_axis(self, x_axis: str, y_axis: range, tab: ttk.Frame) -> None:
        """this function generates the y-axis's and x-axis's labels"""
        for y in y_axis:
            label = ttk.Label(tab, text=y, width=5, background='white')
            label.grid(row=y + 1, column=0, padx=5)

        for i, x in enumerate(x_axis):
            label = ttk.Label(tab, text=x, width=22, background='white')
            label.grid(row=0, column=i + 1, sticky='n', pady=5)

    def update_all_cells(self, event) -> None:
        """the function updates all cells in the app according to inputs and formulas"""
        cells = {}
        for tab in range(1, len(self.tabs) + 1):
            for cell in self.spreadsheets[tab].cells:
                cells[cell] = self.spreadsheets[tab].cells[cell]
                self.spreadsheets[int(tab)].evaluateCell(self.spreadsheets[tab].cells[cell][0].get(),
                                                         self.spreadsheets[tab].cells[cell][1])
        tmp_spreadsheet = Spreadsheet(XAXIS, YAXIS, cells, TAB1)
        for cell in tmp_spreadsheet.cells:
            tmp_spreadsheet.evaluateCell(tmp_spreadsheet.cells[cell][0].get(), tmp_spreadsheet.cells[cell][1])

    def initiate_cells(self, Xaxis: str, Yaxis: range, tab: ttk.Frame, tab_num: int) -> None:
        """function that initiates the cells in each tab and creates a spreadsheet"""
        # checks if user gave a file to the terminal to open
        if len(sys.argv) > 1:
            try:
                # opens a json file as a spreadsheet
                if sys.argv[1].endswith(".json") and len(self.tabs) == 1:
                    f = open(sys.argv[1])
                    data = dict(json.load(f))
                    fix_data = {}
                    for i in data:
                        fix_data[i[1:]] = data[i]
                    for y in Yaxis:
                        for xcoor, x in enumerate(Xaxis):

                            id = f'{tab_num}{x}{y}'
                            if id[1:] in fix_data.keys():
                                var = StringVar(tab, fix_data[id[1:]][0], id)
                                label = ttk.Label(tab, text=fix_data[id[1:]][1], width=7, wraplength=80)
                            else:
                                var = StringVar(tab, '', id)
                                label = ttk.Label(tab, text='', width=7, wraplength=80)

                            e = ttk.Entry(tab, textvariable=var, width=14)
                            e.grid(row=y + 1, column=xcoor + 1, sticky="w", padx=2, pady=2)
                            label.grid(row=y + 1, column=xcoor + 1, sticky="e")

                            self.spreadsheets[tab_num].cells[id] = [var, label]
                            e.bind('<1>', self.update_all_cells)
                elif sys.argv[1].endswith(".csv") and len(self.tabs) == 1:
                    # opens a csv file as a spreadsheet
                    f = open(sys.argv[1])
                    data_list = f.read().split("\n")
                    data = {str: StringVar}
                    for i, layer in enumerate(data_list):
                        data[i] = layer.split(',')
                    for y in Yaxis:
                        for xcoor, x in enumerate(Xaxis):
                            id = f'{tab_num}{x}{y}'
                            var = StringVar(tab, '', id)
                            e = ttk.Entry(tab, textvariable=var, width=14)
                            e.grid(row=y + 1, column=xcoor + 1, sticky="w", padx=2, pady=2)
                            label = ttk.Label(tab, text='', width=7, wraplength=80)
                            label.grid(row=y + 1, column=xcoor + 1, sticky="e")
                            self.spreadsheets[tab_num].cells[id] = [var, label]
                            if data != '':
                                try:
                                    var.set(data[y + 1][xcoor])
                                except:
                                    pass
                            e.bind('<1>', self.update_all_cells)
                else:
                    # opens an extra tab if the original was opened with a file
                    for y in Yaxis:
                        for xcoor, x in enumerate(Xaxis):
                            id = f'{tab_num}{x}{y}'
                            var = StringVar(tab, '', id)
                            e = ttk.Entry(tab, textvariable=var, width=14)
                            e.grid(row=y + 1, column=xcoor + 1, sticky="w", padx=2, pady=2)
                            label = ttk.Label(tab, text='', width=7, wraplength=80)
                            label.grid(row=y + 1, column=xcoor + 1, sticky="e")

                            self.spreadsheets[int(tab_num)].cells[id] = [var, label]
                            e.bind('<1>', self.update_all_cells)
            except:
                for y in Yaxis:
                    for xcoor, x in enumerate(Xaxis):
                        id = f'{tab_num}{x}{y}'
                        var = StringVar(tab, '', id)
                        e = ttk.Entry(tab, textvariable=var, width=14)
                        e.grid(row=y + 1, column=xcoor + 1, sticky="w", padx=2, pady=2)
                        label = ttk.Label(tab, text='', width=7, wraplength=80)
                        label.grid(row=y + 1, column=xcoor + 1, sticky="e")

                        self.spreadsheets[int(tab_num)].cells[id] = [var, label]
                        e.bind('<1>', self.update_all_cells)

        else:
            # opens an empty spreadsheet if no file was given
            for y in Yaxis:
                for xcoor, x in enumerate(Xaxis):
                    id = f'{tab_num}{x}{y}'
                    var = StringVar(tab, '', id)
                    e = ttk.Entry(tab, textvariable=var, width=14)
                    e.grid(row=y + 1, column=xcoor + 1, sticky="w", padx=2, pady=2)
                    label = ttk.Label(tab, text='', width=7, wraplength=80)
                    label.grid(row=y + 1, column=xcoor + 1, sticky="e")

                    self.spreadsheets[int(tab_num)].cells[id] = [var, label]
                    e.bind('<1>', self.update_all_cells)

    def add_tab(self) -> None:
        """adds an extra spreadsheet tab"""
        tab = ttk.Frame(NOTEBOOK)
        self.tabs.append(tab)
        NOTEBOOK.add(tab, text=f'Tab{len(self.tabs)}')
        cells: dict[str, list] = {}
        s = Spreadsheet(XAXIS, YAXIS, cells, tab)
        self.spreadsheets[(len(self.tabs))] = s
        self.generate_x_and_y_axis(XAXIS, YAXIS, tab)
        self.initiate_cells(XAXIS, YAXIS, tab, int(len(self.tabs)))
        self.initiate_buttons_for_tab(tab, len(self.tabs))

    def initiate_buttons_for_tab(self, tab: ttk.Frame, tab_num: int) -> None:
        """ Generates the buttons for each tab"""
        generate_json_button = ttk.Button(tab, text="Generate JSON", command=self.spreadsheets[tab_num].generate_json,
                                          width=14)
        generate_json_button.grid(column=1, row=28, sticky="sw", pady=20)
        generate_csv_button = ttk.Button(tab, text="Generate CSV", command=self.spreadsheets[tab_num].generate_csv,
                                         width=14)
        generate_csv_button.grid(column=2, row=28, sticky="sw", pady=20)

    def generate_xl(self):
        """function that connects to the generate XL button and generates the xlsx workbook"""
        workbook = xlsxwriter.Workbook('data.xlsx')
        for s in spreadsheets.values():
            worksheet = workbook.add_worksheet()
            for key, value in s.cells.items():
                worksheet.write(str(key[1]).upper() + str(int(key[2:]) + 1), str(value[1]['text']))
        workbook.close()

    def initiate_add_tab_button(self) -> None:
        """function that generates the add tab button"""
        add_tab_button = Button(ROOT, text="Add Tab", command=self.add_tab)
        add_tab_button.grid(column=1, row=0, sticky="s", padx=20, pady=20)
        add_tab_button.config(width=10, height=0)

    def initiate_design_buttons(self) -> None:
        """function that generates the cell design buttons"""
        color_button = Button(ROOT, text="Change Font Color", command=self.change_font_color, wraplength=100,
                              justify='center', width=20, height=3)
        color_button.grid(column=1, row=0, sticky="ne", padx=20, pady=150)
        font_button = Button(ROOT, text="Change Font", command=self.change_font, wraplength=100, justify='center',
                             width=20, height=3)
        font_button.grid(row=0, column=1, padx=20, pady=20, sticky="n")
        generate_xl_button = Button(ROOT, text="Generate XL", command=self.generate_xl, width=20, height=3)
        generate_xl_button.grid(column=1, row=0, sticky="n", pady=400)

    def change_font_color(self) -> None:
        """change a cells text color"""
        selected_entry = ROOT.focus_get()
        if selected_entry:
            color = askcolor()[1]
            selected_entry.configure({"foreground": color})

    def change_font(self) -> None:
        """change a cells font and text design"""
        selected_entry = ROOT.focus_get()
        if selected_entry:
            selected_font = font.Font(family="Helvetica", size=10)  # Default font
            font_tuple = tkfontchooser.askfont()
            if font_tuple:
                selected_font = font.Font(**font_tuple)
                selected_entry.configure({"font": selected_font})


if __name__ == "__main__":
    """main function that creates an empty spreadsheet in one tab """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, epilog=HELP_TEXT,
                                     description="helping the user")
    parser.add_argument('--itay', type=int, default=42, help=HELP_TEXT)
    args, unknown = parser.parse_known_args()
    s = Spreadsheet(XAXIS, YAXIS, CELLS, TAB1)
    spreadsheets: dict[int, Spreadsheet] = {1: s}
    my_app = App(spreadsheets, TABS)
    ROOT.columnconfigure(0, weight=1)
    ROOT.columnconfigure(1, weight=1)
    screen_width = ROOT.winfo_screenwidth()
    screen_height = ROOT.winfo_screenheight()
    ROOT.geometry(f"{screen_width}x{screen_height}+0+0")
    my_app.generate_x_and_y_axis(XAXIS, YAXIS, TAB1)
    my_app.initiate_cells(XAXIS, YAXIS, TAB1, 1)
    my_app.initiate_buttons_for_tab(TAB1, 1)
    my_app.initiate_add_tab_button()
    my_app.initiate_design_buttons()
    ROOT.mainloop()
