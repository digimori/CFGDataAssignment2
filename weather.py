from tkinter import *

# Fetching the app call:
root = Tk()

# Basic UI pieces - Could maybe use resizable if we wanted to accomodate other sizes for geometry?
root.title("Weather App")
root.geometry('800x650')



# This must be kept at the bottom to stop the GUI destroying itself every reset
root.mainloop()