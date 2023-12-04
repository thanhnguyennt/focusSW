from tkinter import *
from timezonefinder import TimezoneFinder
from datetime import datetime
from geopy.geocoders import ArcGIS
import requests
import pytz
import threading
from voice_input import voice_command
from welcome import init_assistance
from tkinter import ttk, messagebox

assistance = init_assistance()

def activate_microphone():
    thread = threading.Thread(target=voice_command, args=(assistance, None))
    thread.start()

def get_weather(city, clock, name, t, c, w, h, d, p):
    try:
        geolocator = ArcGIS()
        location = geolocator.geocode(city)

        # Get timezone
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Get weather data
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7a2cf28ff543bc7246652ebe4ecc767b&units=metric"
       
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update labels with weather data
        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°C"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry")