import os
import time
import ctypes
import tkinter as tk
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


def button_click(number):
    display_console()
    data = get_day_data(number)
    if data == None:
        print("\nNo valid data in the appropriate folder!")
        input("\nPress any key to continue...")
        return
    start = time.time()
    match number:
        case 1:
            Day01.main(data)
        case 2:
            Day02.main(data)
        case 3:
            Day03.main(data)
        case 4:
            Day04.main(data)
        case 5:
            Day05.main(data)
        case 6:
            Day06.main(data)
        case 7:
            Day07.main(data)
        case 8:
            Day08.main(data)
        case 9:
            Day09.main(data)
        case 10:
            Day10.main(data)
        case 11:
            Day11.main(data)
        case 12:
            Day12.main(data)
        case 13:
            Day13.main(data)
        case 14:
            Day14.main(data)
        case 15:
            Day15.main(data)
        case 16:
            Day16.main(data)
        case 17:
            Day17.main(data)
        case 18:
            Day18.main(data)
        case 19:
            Day19.main(data)
        case _:
            print("Day " + str(number) + " is not yet implemented!")
    execution_time = time.time() - start
    if execution_time < 1:
        print("\nExecuted in " + str(round(execution_time * 1000, 5)) + "ms")
    else:
        print("\nExecuted in " + str(round(execution_time, 2)) + " seconds")
    _ = input("\nPress any key to continue...")
    hide_console()


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
root.title("Archipelago 2023")

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
