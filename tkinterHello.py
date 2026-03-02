import tkinter as tk

root = tk.Tk()

#places label to root window
message = tk.Label(root, text = "Hello, World!")
message.pack()

root.mainloop()