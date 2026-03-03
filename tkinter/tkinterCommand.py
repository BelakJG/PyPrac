import tkinter as tk
from tkinter import ttk

def button_clicked():
    print("Button Clicked")

def callback_function(args):
    print(args)

root = tk.Tk()
root.geometry("800x600")

button = ttk.Button(root, text = "Click Me", command = button_clicked)
button.pack()

button2 = ttk.Button(
    root,
    text = "callback button",
    command = lambda: callback_function("Callback Button")
)
button2.pack()

root.mainloop()