from tkinter import Toplevel, Label, Button
from datetime import datetime



favorite_cities = []

def save_favorite(city):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    
    favorite_cities.append(f"{current_date} {current_time} - {city}")


def show_favorite_list():
    favorite_window = Toplevel()
    favorite_window.title("Favorites")

    for index, city in enumerate(favorite_cities):
        label = Label(favorite_window, text=f"{index + 1}. {city}")
        label.pack()



class SaveFavoriteGUI(Toplevel):
    def __init__(self, master, city):
        super().__init__(master)
        self.title("Add to Favorites")
        self.geometry("400x300")
        self.city = city
        self.setup_gui()

    def setup_gui(self):
        self.favorite_label = Label(self, text="Add to favorites: " + self.city, font=("Arial", 12))
        self.favorite_label.pack(pady=10)

        self.save_button = Button(self, text="Save", command=self.save_favorite_action)
        self.save_button.pack(pady=10)
        
        self.show_favorite_button = Button(self, text="Show Favorites", command=show_favorite_list)
        self.show_favorite_button.pack(pady=10)

    def save_favorite_action(self):
        save_favorite(self.city)
        self.destroy()
