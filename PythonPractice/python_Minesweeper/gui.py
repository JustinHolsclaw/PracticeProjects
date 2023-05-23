import tkinter as tk
from tkinter import ttk

window = tk.Tk()
ttk.Label(window, text='Minefield').pack()
window.title('Minefield')

window_width = 600
window_height = 400

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

def create_GameBoard_Array(numberOfPieces):
    incrementor = 0
    while numberOfPieces != incrementor:
        ttk.Button(window, text="first").pack()
        incrementor = incrementor+1
ttk.Button(window, text='click me', command=button_clicked).pack()
ttk.Button(window, text='click me', state = "disabled", command=button_clicked ).pack()
create_GameBoard_Array(10)
window.mainloop()