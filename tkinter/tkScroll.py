import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollbar Demo")
root.resizable(0, 0)

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

v_scrollbar = ttk.Scrollbar(frame)
v_scrollbar.pack(side="right", fill="y")

text = tk.Text(frame, height=8)
text.pack(side="left", expand=True, fill="both")

text["yscrollcommand"]=v_scrollbar.set
v_scrollbar.config(command=text.yview)

text.insert(tk.END, "\n" * 20)

root.mainloop()