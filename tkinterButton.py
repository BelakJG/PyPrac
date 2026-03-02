import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Exit button Demo")

exit_button = ttk.Button(
    root,
    text = "Exit",
    command = lambda: root.quit()
)
exit_button.pack(
    ipadx = 5,
    ipady = 5,
    expand = True
)

def handle_click():
    showinfo(
        title = "Information",
        message = "Download button clicked!"
    )
download_icon = tk.PhotoImage(file = "./assets/download.png")
download_button = ttk.Button(
    root,
    image = download_icon,
    text = "Download",
    compound = "left",
    command = handle_click
)
download_button.pack(
    ipadx = 5,
    ipady = 5,
    expand = True
)

root.mainloop()