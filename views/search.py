from tkinter import Frame, Label, Entry, Button, PhotoImage
import os


class SearchView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        logo_path = os.path.join(os.path.dirname(__file__), '..', 'logo.png')
        logo = PhotoImage(file="logo.png")


        self.logo_label = Label(self, image=logo)
        self.logo_label.pack(pady=20)

        # Create the search entry and button
        self.search_entry = Entry(self, width=50, font=("Helvetica", 16))
        self.search_entry.pack(pady=10)

        self.search_btn = Button(self, text="Search")
        self.search_btn.pack()
