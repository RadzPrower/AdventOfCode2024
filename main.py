import os
import time
import ctypes
import tkinter as tk
from tkinter.messagebox import showinfo

import Day01
import Day02
import Day04
import Day03
import Day05
import Day06
import Day07
import Day08
import Day09
import Day10
import Day11
import Day12
import Day13
import Day14
import Day15
import Day16
import Day17
import Day18
import Day19
import Day20
import Day21
import Day22
import Day23
import Day24
import Day25


def button_click(number):
    data = get_day_data(number)
    result = ""
    if data == None:
        result += "No valid data in the appropriate folder!"
        result += "\nPress any key to continue..."
        showinfo("Invalid Data", result)
        return
    title = "Day " + str(number) + " Results"
    start = time.time()
    match number:
        case 1:
            result += Day01.main(data)
        case 2:
            result += Day02.main(data)
        case 3:
            result += Day03.main(data)
        case 4:
            result += Day04.main(data)
        case 5:
            result += Day05.main(data)
        case 6:
            result += Day06.main(data)
        case 7:
            result += Day07.main(data)
        case 8:
            result += Day08.main(data)
        case 9:
            result += Day09.main(data)
        case 10:
            result += Day10.main(data)
        case 11:
            result += Day11.main(data)
        case 12:
            result += Day12.main(data)
        case 13:
            result += Day13.main(data)
        case 14:
            result += Day14.main(data)
        case 15:
            result += Day15.main(data)
        case 16:
            result += Day16.main(data)
        case 17:
            result += Day17.main(data)
        case 18:
            result += Day18.main(data)
        case 19:
            result += Day19.main(data)
        case 20:
            result += Day20.main(data)
        case 21:
            result += Day21.main(data)
        case 22:
            result += Day22.main(data)
        case 23:
            result += Day23.main(data)
        case 24:
            result += Day24.main(data)
        case 25:
            result += Day25.main(data)
        case _:
            title = "Not Yet Implemented"
            result += "Day " + str(number) + " is not yet implemented!"
    execution_time = time.time() - start
    if execution_time < 1:
        result += "\n\nExecuted in " + str(round(execution_time * 1000, 5)) + "ms"
    else:
        result += "\n\nExecuted in " + str(round(execution_time, 2)) + " seconds"
    showinfo(title, result)


def create_buttons(frame, start, end):
    for i in range(start, end + 1):
        button = tk.Button(frame, text=str(i), width=5, height=2, command=lambda i=i: button_click(i))
        button.grid(row=(i - start) // 5, column=(i - start) % 5, padx=5, pady=5)


def create_checkbox(frame):
    checkbox = tk.Checkbutton(frame, text="Testing", variable=testing, onvalue=True, offvalue=False)
    checkbox.pack(padx=10, pady=5)


def display_console():
    os.system('cls||clear')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)


def hide_console():
    os.system('cls||clear')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def get_day_data(day):
    if testing.get():
        source = './test/'
    else:
        source = './input/'

    try:
        data = open(source + str(day) + '.txt').read().splitlines()
    except:
        data = None
    return data


# Create the main window
hide_console()
root = tk.Tk()
root.title("Advent of Code 2024")

# Create a frame for the buttons
button_frame = tk.Frame(root)

# Create buttons from 1 to 25
create_buttons(button_frame, 1, 25)

# Pack the frame containing buttons
button_frame.pack(padx=10, pady=10)

# Add testing checkbox
testing = tk.BooleanVar()
create_checkbox(root)

# Start the GUI event loop
root.mainloop()
