import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("tkinter Entry widger demo")

name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack()
name_entry.focus()

output_label = ttk.Label(root)
output_label.pack()

name_var.trace_add("write", lambda *args: output_label.config(text=name_var.get().upper()))

root.mainloop()