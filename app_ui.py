import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

# Dummy data to represent search results
documents = [
    {"title": "Document 1", "snippet": "This is the first document.", "url": "http://example.com/doc1"},
    {"title": "Document 2", "snippet": "This is the second document.", "url": "http://example.com/doc2"},
    {"title": "Document 3", "snippet": "This is the third document.", "url": "http://example.com/doc3"},
]

# Function to perform the search
def perform_search(query):
    # Here you would integrate your search engine logic.
    # For now, we'll just return the dummy documents.
    return documents

# Function to handle the search button click
def on_search():
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Empty Query", "Please enter a search query.")
        return
    
    results = perform_search(query)
    display_results(results)

# Function to display search results
def display_results(results):
    # Clear the search frame
    for widget in search_frame.winfo_children():
        widget.destroy()

    # Display results
    for doc in results:
        title_label = ttk.Label(search_frame, text=doc['title'], font=("Helvetica", 14, "bold"), cursor="hand2")
        snippet_label = ttk.Label(search_frame, text=doc['snippet'])
        read_more_link = ttk.Label(search_frame, text="Read More", foreground="blue", cursor="hand2")
        
        def open_url(url=doc['url']):
            webbrowser.open(url)
        
        title_label.bind("<Button-1>", lambda e: open_url(doc['url']))
        read_more_link.bind("<Button-1>", lambda e: open_url(doc['url']))
        
        title_label.pack(anchor='w', pady=(10, 0))
        snippet_label.pack(anchor='w', padx=(20, 0))
        read_more_link.pack(anchor='w', padx=(20, 0), pady=(0, 10))

# Initialize the main application window
root = tk.Tk()
root.title("Search Engine")
root.geometry("800x600")

# Create the logo image (replace with your actual logo file)
logo = tk.PhotoImage(file="logo.png")
logo_label = ttk.Label(root, image=logo)
logo_label.pack(pady=20)

# Create the search entry and button
search_entry = ttk.Entry(root, width=50, font=("Helvetica", 16))
search_entry.pack(pady=10)

search_button = ttk.Button(root, text="Search", command=on_search)
search_button.pack()

# Create a frame to hold the search results
search_frame = ttk.Frame(root)
search_frame.pack(fill='both', expand=True, pady=20)

root.mainloop()




# https://nazmul-ahsan.medium.com/how-to-organize-multi-frame-tkinter-application-with-mvc-pattern-79247efbb02b