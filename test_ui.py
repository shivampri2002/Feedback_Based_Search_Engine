import tkinter as tk

root = tk.Tk()
root.title("Card List")


class Card(tk.Frame):
    def __init__(self, parent, title, text, button_text):
        super().__init__(parent)
        self.configure(bd=1, relief="solid")
        self.pack(pady=10)

        # Title
        title_label = tk.Label(self, text=title, font=("Arial", 14, "bold"))
        title_label.pack(pady=5)

        # Text
        text_label = tk.Label(self, text=text, wraplength=300, justify="left", width=20)
        text_label.pack(pady=5)

        # Button
        button = tk.Button(self, text=button_text, width=18)
        button.pack(pady=5)



# List of card data
card_data = [
    ("Card 1", "This is the first card.", "Click me!"),
    ("Card 2", "This is the second card.", "Click me too!"),
    ("Card 3", "This is the third card.", "Click me as well!"),
]

# Create the cards
for title, text, button_text in card_data:
    card = Card(root, title, text, button_text)


root.mainloop()