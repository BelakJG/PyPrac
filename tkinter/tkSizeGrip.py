import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(True, True)

# create a sizegrip and place it at
# the bottom-right corner of the window
sizegrip = ttk.Sizegrip(root)
sizegrip.place(relx=1, rely=1, anchor=tk.SE)

root.mainloop()