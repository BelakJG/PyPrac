import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")
root.title("Tkinter Label Demo")

label = ttk.Label(
    root,
    text = "This is a label",
    font = ("Helvetica", 14)
)
label.pack()

photo = tk.PhotoImage(file ="../assets/python.png")
photo_label = ttk.Label(
    root,
    image = photo,
    padding = 5,
    text = "Python",
    compound = "top"
)
photo_label.pack()

root.mainloop()