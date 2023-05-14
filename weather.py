from tkinter import *
import requests
from tkinter import messagebox

API_KEY = open('api_key','r').read().strip()


url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

def get_weather(city):
    result = requests.get(url.format(city, API_KEY))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15)*9/5+32
        weather = json['weather'][0]['main']
        final = (city,country,temp_kelvin,temp_celcius,temp_fahrenheit,weather)
        return final
    else:
        None

win = Tk()
win.title("Weather")
win.geometry('500x250')

city_txt = StringVar()
city_entry = Entry(win, textvariable=city_txt)
city_entry.pack()

def search_weather():
    city = city_txt.get()
    weather = get_weather(city)
    if weather:
        location_lbl.config(text=f"{weather[0]}, {weather[1]}")
        temp_lbl.config(text=f"{weather[3]:.2f} \u00B0C / {weather[4]:.2f} \u00B0F")
        weather_lbl.config(text=weather[5])
    else:
        messagebox.showerror('Error','City not found')

search_btn = Button(win, text='Search', width=12, command=search_weather)
search_btn.pack()

location_lbl  = Label(win, text='City', font=('bold', 20))
location_lbl.pack()

temp_lbl = Label(win, text='Temperature', font=('bold', 30))
temp_lbl.pack()

weather_lbl = Label(win, text='Weather', font=(10))
weather_lbl.pack()

win.mainloop()
