import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#places label to root window
tk.Label(root, text = "Classic Label").pack()
ttk.Label(root, text = "Themed Label").pack()

root.title("Hello, World!")

window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

try:
    photo = tk.PhotoImage(file="./assets/pythontutorial-1.png")
    root.iconphoto(False, photo)
except tk.TclError:
    print("Icon not found, using default.")

root.mainloop()