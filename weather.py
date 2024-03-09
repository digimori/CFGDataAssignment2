from tkinter import *
from tkinter import ttk

# Fetching the app call:
root = Tk()

# Basic UI pieces - Could maybe use resizable if we wanted to accomodate other sizes for geometry?
root.title("Weather App")
root.geometry('800x650')

# Allow user to input the city that they want to check the weather for:
# This generates a text box for user input
input_city = StringVar()

# Taking the input and the root defined above as parameters:
city_calc = Entry(root, textvariable=input_city)
city_calc.pack()

# This must be kept at the bottom to stop the GUI destroying itself every reset
root.mainloop()