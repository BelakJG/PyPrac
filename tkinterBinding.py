import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Return key pressed")

def log(event):
    print(event)

root = tk.Tk()
root.geometry("800x600")

btn = tk.Button(root, text = "Save")
btn.bind("<Return>", return_pressed)
btn.bind("<Return>", log, add="+")

btn.focus()
btn.pack(expand=True)

root.mainloop()