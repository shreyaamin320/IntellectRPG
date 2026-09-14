import customtkinter as ctk
import tkinter as tk
window = ctk.CTk()
window.title("IntellectRPG")
window.geometry("500x500")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

xp = 0
level = 1

xp_label = ctk.CTkLabel(
    window,
    text="⭐ XP : 0",
    font=("Arial", 20, "bold")
)
xp_label.pack(pady=10)

level_label = ctk.CTkLabel(
    window,
    text="🏆 Level : 1",
    font=("Arial", 18, "bold")
)
level_label.pack()

quest_entry = ctk.CTkEntry(
    window,
    width=400,
)
quest_entry.pack()

difficulty = ctk.StringVar(value="Medium")

difficulty_menu = ctk.CTkOptionMenu(
    window,
    variable=difficulty,
    values=["Easy", "Medium", "Hard"]
)
difficulty_menu.pack(pady=5)

def delete_quest(quest_card):
    quest_card.destroy()

def complete_quest(quest_label, complete_button, delete_button, selected_difficulty):
    global xp, level

    if selected_difficulty == "Easy":
        xp += 10

    elif selected_difficulty == "Medium":
        xp += 25

    elif selected_difficulty == "Hard":
        xp += 50

    if xp >= level * 100:
        level += 1

    xp_label.configure(
        text=f"⭐ XP : {xp}"
    )

    level_label.configure(
        text=f"🏆 Level : {level}"
    )

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
    selected_difficulty = difficulty.get()

    quest_card = ctk.CTkFrame(quest_frame)
    quest_card.pack(fill="x", padx=10, pady=5)

    quest_label = ctk.CTkLabel(
        quest_card,
        text=f"{quest} [{selected_difficulty}]",
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
            delete_button,
            selected_difficulty,
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
