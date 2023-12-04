from tkinter import Toplevel, Label, Text, Button, Scrollbar, BOTH, END, Y
from datetime import datetime


notes_list = []

def save_notes(city, notes):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
 
    notes_list.append(f"{current_date} {current_time} - {city}: {notes}")

def show_notes_list():
    notes_window = Toplevel()
    notes_window.title("Notes")
    
    scrollbar = Scrollbar(notes_window)
    scrollbar.pack(side="right", fill="y")
    
    notes_text = Text(notes_window, wrap="word", yscrollcommand=scrollbar.set)
    
    for note in notes_list:
        notes_text.insert(END, note + "\n")
    
    notes_text.pack(expand=True, fill=BOTH)
    scrollbar.config(command=notes_text.yview)


class SaveNotesGUI(Toplevel):
    def __init__(self, master, city):
        super().__init__(master)
        self.title("Add Notes")
        self.geometry("400x300")
        self.city = city
        self.setup_gui()

    def setup_gui(self):
        self.notes_label = Label(self, text="Add notes for " + self.city, font=("Arial", 12))
        self.notes_label.pack(pady=10)

        self.notes_entry = Text(self, height=5, width=30)
        self.notes_entry.pack(pady=10)

        self.save_button = Button(self, text="Save", command=self.save_notes_action)
        self.save_button.pack(pady=10)
        
        self.show_notes_button = Button(self, text="Show Notes", command=show_notes_list)
        self.show_notes_button.pack(pady=10)

    def save_notes_action(self):
        notes_text = self.notes_entry.get("1.0", "end-1c")
        save_notes(self.city, notes_text)
        self.destroy()
