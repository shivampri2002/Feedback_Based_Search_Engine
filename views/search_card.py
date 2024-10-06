from tkinter import Frame, Label

class SearchCard(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.configure(bd=1, relief="solid")
        self.pack(pady=10)

        self.title_label = Label(self, text="", font=("Helvetica", 14, "bold"), cursor="hand2")
        self.title_label.pack(pady=5)

        self.description_label = Label(self, text="")
        self.description_label.pack(pady=5)

        self.read_more_link = Label(self, text="Read More", foreground="blue", cursor="hand2")
        self.read_more_link.pack(pady=5)