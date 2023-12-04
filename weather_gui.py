import tkinter as tk
from tkinter import Button, PhotoImage
from api import get_weather
from voice_input import speak, voice_command
from favorite import SaveFavoriteGUI
from notes import SaveNotesGUI
from welcome import init_assistance, speak

assistance = init_assistance()

class WeatherAppGUI:
    def __init__(self, master):
        self.master = master
        self.setup_gui()

    def get_weather(self):
        city = self.textfield.get()
        get_weather(city, self.clock_label, self.name_label, self.temp_label, self.condition_label,
                    self.wind_label, self.humidity_label, self.description_label, self.pressure_label)

    # Mở mic và bắt đầu thu âm
    def activate_microphone(self):
        speak(assistance, 'Please speak the name of the city you want to check the weather for.')
        query = voice_command(assistance, self.textfield)
        if query:
            # Đặt giá trị của textfield thành tên thành phố từ giọng nói
            self.textfield.delete(0, tk.END)
            self.textfield.insert(0, query)
            speak(assistance, f"I will check the weather for {query}. Please wait.")
            self.get_weather()

    def save_favorite(self):
        SaveFavoriteGUI(self.master, self.textfield.get())

    def save_notes_window(self):
        SaveNotesGUI(self.master, self.textfield.get())

    def setup_gui(self):
        # Search icon

        self.textfield = tk.Entry(self.master, justify="center", width=17, font=("poppins", 25, "bold"),
                                  bg="#404040", border=0, fg="white")
        self.textfield.place(x=50, y=40)
        self.textfield.focus()

        search_icon = PhotoImage(file="Image/search_icon.png")
        self.search_button = Button(self.master, image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=self.get_weather)
        self.search_button.image = search_icon
        self.search_button.place(x=400, y=44)

        microphone_icon = PhotoImage(file="Image/microphone_icon.png").subsample(1, 1)
        self.microphone_button = Button(self.master, image=microphone_icon, borderwidth=0, cursor="hand2", bg="#404040", command=self.activate_microphone)
        self.microphone_button.image = microphone_icon
        self.microphone_button.place(x=460, y=46)
    

        # Labels for weather information
        label1 = tk.Label(self.master, text="WIND", font=("Helvetica", 15, 'bold'), fg='green')
        label1.place(x=120, y=400)

        label2 = tk.Label(self.master, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg='green')
        label2.place(x=250, y=400)

        label3 = tk.Label(self.master, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg='green')
        label3.place(x=430, y=400)

        label4 = tk.Label(self.master, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg='green')
        label4.place(x=750, y=400)

        self.wind_label = tk.Label(self.master, text="...", font=("arial", 15, "bold"))
        self.wind_label.place(x=120, y=430)

        self.humidity_label = tk.Label(self.master, text="...", font=("arial", 15, "bold"))
        self.humidity_label.place(x=280, y=430)

        self.description_label = tk.Label(self.master, text="...", font=("arial", 15, "bold"))
        self.description_label.place(x=430, y=430)

        self.pressure_label = tk.Label(self.master, text="...", font=("arial", 15, "bold"))
        self.pressure_label.place(x=750, y=430)

        # Time
        self.name_label = tk.Label(self.master, font=("arial", 15, "bold"))
        self.name_label.place(x=50, y=150)

        self.clock_label = tk.Label(self.master, font=("Helvetica", 20))
        self.clock_label.place(x=50, y=189)

        self.temp_label = tk.Label(self.master, font=("arial", 40, "bold"), fg="#ee666d")
        self.temp_label.place(x=500, y=150)

        self.condition_label = tk.Label(self.master, font=("arial", 13, "bold"))
        self.condition_label.place(x=500, y=250)

        # Buttons for favorites
        favorite_image = PhotoImage(file="Image/favorite.png").subsample(5, 5)
        self.favorites_button = Button(self.master, image=favorite_image, command=self.save_favorite)
        self.favorites_button.image = favorite_image
        self.favorites_button.place(x=700, y=34)

        # Notes
        note_image = PhotoImage(file="Image/note.png").subsample(12, 12)
        self.notes_button = Button(self.master, image=note_image, command=self.save_notes_window)
        self.notes_button.image = note_image
        self.notes_button.place(x=770, y=34)