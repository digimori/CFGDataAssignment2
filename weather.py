from tkinter import *
from configparser import ConfigParser

api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={API key}'

# Parsing our API key from the text file - This will be in gitignore to protect it.
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']
def search():
    pass

# Fetching the app call:
root = Tk()

# Basic UI pieces - Could maybe use resizable if we wanted to accommodate other sizes for geometry?
root.title("Weather App")
root.geometry('500x800')
root.config(bg='black')

# Allow user to input the city that they want to check the weather for:
# This generates a text box for user input
input_city = StringVar()

# Taking the input and the root defined above as parameters:
city_calc = Entry(root, textvariable=input_city, width=25)
city_calc.pack()

# Search button
search_button = Button(root, text="Find Weather", width=20, command=search)

# Note: pack() is the method we are using to display these elements on the GUI
search_button.pack()

# Getting the locations:
location_label = Label(root, text='Location', font={'bold', 20})
location_label.pack()

# Images:
img = Label(root, bitmap='')
img.pack()

# Labels for displaying the weather, temperature etc
temperature_label = Label(root, text='Temperature')
temperature_label.pack()

weather_label = Label(root, text='Weather')
weather_label.pack()

previous_weather = Label(root, text='Previously Searched:')
previous_weather.pack()

# This must be kept at the bottom to stop the GUI destroying itself every reset
root.mainloop()
