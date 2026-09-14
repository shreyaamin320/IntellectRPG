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

def delete_quest(quest_card):
    quest_card.destroy()

def complete_quest(quest_label, complete_button, delete_button):
    quest_label.configure(
        text="✓ " + quest_label.cget("text"),
        font=("Arial", 14, "italic", "overstrike")
    )

    complete_button.configure(
        text="Completed!",
        state="disabled"
    )

    delete_button.configure(
        state="disabled"
    )

def add_quest():
    quest = quest_entry.get()

    quest_card = ctk.CTkFrame(quest_frame)
    quest_card.pack(fill="x", padx=10, pady=5)

    quest_label = ctk.CTkLabel(
        quest_card,
        text=quest,
    )
    quest_label.pack(side="left", padx=10, pady=10)

    delete_button = ctk.CTkButton(
        quest_card,
        text="✕",
        width=40,
        command=lambda: delete_quest(quest_card),
    )
    delete_button.pack(side="right" , padx=5, pady=10)

    complete_button = ctk.CTkButton(
        quest_card,
        text="✓ Complete",
        command=lambda: complete_quest(
            quest_label,
            complete_button,
            delete_button
    ),
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

window.mainloop()
