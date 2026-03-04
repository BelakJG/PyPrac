import os
import tkinter as tk
from tkinter import ttk

def tk_shutdown():
    os.system("systemctl poweroff")

root = tk.Tk()
root.title("ShutDown")
root.geometry("200x200")
root.resizable(0,0)

shutdown_btn = ttk.Button(
    root,
    text="Shut Down",
    command=tk_shutdown
)
shutdown_btn.place(relx=.5, rely=.5, anchor="center")

root.mainloop()