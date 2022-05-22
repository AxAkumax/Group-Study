import tkinter as tk
window = tk.Tk()

window.geometry("240x100")

box1 = tk.Label(
    window,
    text="Box 1",
    bg="green",
    fg="white"
)
box2 = tk.Label(
    window,
    text="Box 1",
    bg="green",
    fg="white"
)

box1.grid(
    column=0, 
    row=1,
    ipadx=10,
    ipady=10
)
box2.grid(
    column=1, 
    row=1,
    ipadx=10,
    ipady=10
)

window.mainloop()