import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Place Demo")
root.geometry("600x400")

label1 = tk.Label(root, text="Place", bg="red", fg="white")
label1.place(relx=.5, rely=.5, width=100, height=50, anchor="center")

root.mainloop()