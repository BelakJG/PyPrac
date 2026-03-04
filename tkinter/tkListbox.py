import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x180")
root.title("Listbox Demo")

languages = ('Java', 'C', 'C++', 'C#', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')
list_variable = tk.Variable(value=languages)

label = ttk.Label(
    root,
    text = "Select your favorite programming languages:"
)
label.pack(padx=10, pady=0, side="top", fill="x")

listbox = tk.Listbox(
    root,
    listvariable=list_variable,
    height=6
)

listbox.pack(
    padx=10, pady=10,
    expand=True, fill="both",
    side="left"
)

root.mainloop()