import tkinter as tk
window = tk.Tk()
window.title("IntellectRPG")
window.geometry("500x500")

quest_entry = tk.Entry(
    window,
    width=50,
)
quest_entry.pack()

def add_quest():
    quest = quest_entry.get()
    quest_list.insert(tk.END, quest)
    quest_entry.delete(0, tk.END)

add_button = tk.Button(
    window,
    text= "Add Quest",
    command=add_quest,
)
add_button.pack()

quest_list = tk.Listbox(
    window,
    width=40,
    height=10,
)
quest_list.pack()

window.mainloop()
