###TODO:The Grid needs to be changed so that the buttons appear in a grid.###
###TODO:Each button needs to be assigned a value and then that value needs to be used to evaluate if it is a bomb or not###

import tkinter as tk
import math
from tkinter import ttk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        window = tk.Tk()
        ttk.Label(window, text='Minefield')
        window.title('Minefield')

        window_width = 800
        window_height = 600

# get the screen dimension
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

# find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
        window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        def button_clicked():
            print('button clicked')

        def create_GameBoard_Array(size):
            incrementor = 0
            col = 0
            while size != incrementor:
                if(col == size-1):
                        ttk.Button(window, text=incrementor+1).grid(row=incrementor, column=col)
                        col = 0
                        incrementor = incrementor+1
                else:
                        ttk.Button(window, width=10, command=()).grid(row=incrementor, column=col)
                        col = col+1
        # ttk.Button(window, text='click me', command=button_clicked).pack()
        # ttk.Button(window, text='click me', state = "disabled", command=button_clicked ).pack()
        create_GameBoard_Array(9)
if __name__ == "__main__":
    app = Gui()
    app.mainloop()