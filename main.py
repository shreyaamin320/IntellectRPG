import customtkinter as ctk
import tkinter as tk
window = ctk.CTk()
window.title("IntellectRPG")
window.geometry("500x500")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

quest_entry = ctk.CTkEntry(
    window,
    width=400,
)
quest_entry.pack()

def add_quest():
    quest = quest_entry.get()

    quest_card = ctk.CTkFrame(quest_frame)
    quest_card.pack(fill="x", padx=10, pady=5)

    quest_label = ctk.CTkLabel(
        quest_card,
        text=quest,
    )
    quest_label.pack(side="left", padx=10, pady=10)

    complete_button = ctk.CTkButton(
        quest_card,
        text="✓ Complete",
    )
    complete_button.pack(side="right", padx=10, pady=10)

    quest_entry.delete(0, tk.END)

add_button = ctk.CTkButton(
    window,
    text= "Add Quest",
    command=add_quest,
)
add_button.pack()

quest_frame = ctk.CTkFrame(window)
quest_frame.pack()

def complete_quest():
    selected = quest_frame.curselection()

    if selected:
        index = selected[0]
        quest_frame.delete(index)

complete_button = ctk.CTkButton(
    window,
    text= "Completed",
    command= complete_quest,
)
complete_button.pack()

window.mainloop()
