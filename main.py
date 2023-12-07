import os
import ctypes
import tkinter as tk
import Day01
import Day02
import Day05
import Day06
import Day07


def button_click(number):
    display_console()
    data = get_day_data(number)
    match number:
        case 1:
            Day01.main(data)
        case 2:
            Day02.main(data)
        case 5:
            Day05.main(data)
        case 6:
            Day06.main(data)
        case 7:
            Day07.main(data)
        case _:
            print("Day " + str(number) + " is not yet implemented!")
    _ = input("\nPress any key to continue...")
    hide_console()


def create_buttons(frame, start, end):
    for i in range(start, end + 1):
        button = tk.Button(frame, text=str(i), width=5, height=2, command=lambda i=i: button_click(i))
        button.grid(row=(i - start) // 5, column=(i - start) % 5, padx=5, pady=5)


def display_console():
    os.system('cls||clear')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)


def hide_console():
    os.system('cls||clear')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)


def get_day_data(day):
    try:
        data = open('./input/' + str(day) + '.txt').read().splitlines()
    except:
        try:
            data = open('./test/' + str(day) + '.txt').read().splitlines()
        except:
            data = ""
    finally:
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

# Start the GUI event loop
root.mainloop()
