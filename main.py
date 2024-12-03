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
    if data is None:
        result += "No valid data in the appropriate folder!"
        result += "\nPress any key to continue..."
        showinfo("Invalid Data", result)
        return
    title = "Day " + str(number) + " Results"
    match number:
        case 1:
            day_function = Day01.main
        case 2:
            day_function = Day02.main
        case 3:
            day_function = Day03.main
        case 4:
            day_function = Day04.main
        case 5:
            day_function = Day05.main
        case 6:
            day_function = Day06.main
        case 7:
            day_function = Day07.main
        case 8:
            day_function = Day08.main
        case 9:
            day_function = Day09.main
        case 10:
            day_function = Day10.main
        case 11:
            day_function = Day11.main
        case 12:
            day_function = Day12.main
        case 13:
            day_function = Day13.main
        case 14:
            day_function = Day14.main
        case 15:
            day_function = Day15.main
        case 16:
            day_function = Day16.main
        case 17:
            day_function = Day17.main
        case 18:
            day_function = Day18.main
        case 19:
            day_function = Day19.main
        case 20:
            day_function = Day20.main
        case 21:
            day_function = Day21.main
        case 22:
            day_function = Day22.main
        case 23:
            day_function = Day23.main
        case 24:
            day_function = Day24.main
        case 25:
            day_function = Day25.main
    start = time.time()
    result += day_function(data)
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
