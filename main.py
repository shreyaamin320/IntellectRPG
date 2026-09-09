import tkinter as tk
window = tk.Tk()
window.title("IntellectRPG")
window.geometry("500x500")

quest_entry = tk.Entry(
    window,
    width=50,
)
quest_entry.pack()

window.mainloop()
