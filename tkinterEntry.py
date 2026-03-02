import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("tkinter Entry widger demo")

name_label = ttk.Label(root, text="Name: ")
name_label.pack(pady=2)

name_entry = ttk.Entry(root)
name_entry.pack(
    pady=5
)
name_entry.focus()


email_label = ttk.Label(root, text = "Email: ")
email_label.pack(pady=2)

email_entry = ttk.Entry(root)
email_entry.pack(
    pady=5
)


pass_label = ttk.Label(root, text = "Password: ")
pass_label.pack(pady=2)

pass_entry = ttk.Entry(root, show="*")
pass_entry.pack(pady=5)

root.mainloop()