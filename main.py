import customtkinter as ctk
import tkinter as tk
from datetime import date
window = ctk.CTk()
window.title("IntellectRPG")
window.geometry("500x500")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

xp = 0
level = 1

completed_quests = 0
achievement_window = None

study_streak = 0
last_study_date = None

achievements = {
    "First Quest": False,
    "Quest Grinder": False,
    "Getting Serious": False,
    "XP Hunter": False,
    "Level Up!": False
}

xp_label = ctk.CTkLabel(
    window,
    text="XP : 0",
    font=("Arial", 20, "bold")
)
xp_label.pack(pady=10)

level_label = ctk.CTkLabel(
    window,
    text="Level : 1",
    font=("Arial", 18, "bold")
)
level_label.pack(pady=10)

streak_label = ctk.CTkLabel(
    window,
    text="Streak : 0 ",
    font=("Arial", 16, "bold")
)
streak_label.pack(pady=5)

level_up_label = ctk.CTkLabel(
    window, 
    text="",
    font = ("Arial" , 18, "bold"),
)
level_up_label.pack(pady=5)

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

quest_type = ctk.StringVar(value="Main Quest")

quest_type_menu = ctk.CTkOptionMenu(
    window,
    variable=quest_type,
    values=["Main Quest", "Side Quest"]
)
quest_type_menu.pack(pady=5)

subject = ctk.StringVar(value="Select Subject")

subject_menu = ctk.CTkOptionMenu(
    window,
    variable=subject,
    values=[
        "Mathematics",
        "Statistics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Programming",
        "English",
        "Hindi",
        "Gujarati",
        "Social Science",
        "History",
        "Geography",
        "Economics",
        "Political Science",
        "Psychology",
        "Sociology",
        "Business",
        "Accounting",
        "Finance",
        "Law",
        "Medicine",
        "Engineering",
        "Art & Design",
        "Music",
        "Other"
    ]
)
subject_menu.pack(pady=5)

def filter_quests(selected_filter):
        for quest_card in quest_frame.winfo_children():

            quest_type_value = quest_card.quest_type_value
            subject_value = quest_card.subject_value

            if selected_filter == "All":
                quest_card.pack(fill="x", padx=10, pady=5)

            elif selected_filter == quest_type_value:
                quest_card.pack(fill="x", padx=10, pady=5)

            elif selected_filter == subject_value:
                quest_card.pack(fill="x", padx=10, pady=5)

            else:
                quest_card.pack_forget()

filter_choice = ctk.StringVar(value="All")

filter_menu = ctk.CTkOptionMenu(
    window,
    variable=filter_choice,
    values=[
        "All",
        "Main Quest",
        "Side Quest",
        "Mathematics",
        "Statistics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Programming",
        "English",
        "Hindi",
        "Gujarati",
        "Social Science",
        "History",
        "Geography",
        "Economics",
        "Political Science",
        "Psychology",
        "Sociology",
        "Business",
        "Accounting",
        "Finance",
        "Law",
        "Medicine",
        "Engineering",
        "Art & Design",
        "Music",
        "Other"
    ],
    command=filter_quests
)

filter_menu.pack(pady=5)

def delete_quest(quest_card):
    quest_card.destroy()

def xp_required_for_level(level):
    return 100 * level * (level - 1) // 2

def show_level_up(new_level):
    level_up_label.configure(
        text=f"🎉 LEVEL UP! You reached Level {new_level}! 🎉"
    )

    window.after(
        2500,
        lambda: level_up_label.configure(text="")
    )

def check_achievements():
    global completed_quests

    if completed_quests >= 1:
        achievements["First Quest"] = True

    if completed_quests >= 5:
        achievements["Quest Grinder"] = True

    if completed_quests >= 10:
        achievements["Getting Serious"] = True

    if xp >= 100:
        achievements["XP Hunter"] = True

    if level >= 2:
        achievements["Level Up!"] = True

def update_streak():
    global study_streak, last_study_date

    today = date.today()

    if last_study_date is None:
        study_streak = 1

    elif today == last_study_date:
        return

    elif( today - last_study_date).days == 1:
        study_streak += 1

    else:
        study_streak = 1

    last_study_date = today

    streak_label.configure(
    text=f"Streak : {study_streak} "
    )

def show_achievements():
    global achievement_window

    check_achievements()

    achievement_window = ctk.CTkToplevel(window)
    achievement_window.title("Achievements")
    achievement_window.geometry("450x500")

    title = ctk.CTkLabel(
        achievement_window,
        text="ACHIEVEMENTS",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    achievement_frame = ctk.CTkScrollableFrame(
        achievement_window,
        width=400,
        height=400,
    )
    achievement_frame.pack(
        padx=15,
        pady=5,
        fill = "both",
        expand=True,
    )

    achievement_details = {
    "First Quest": {
        "badge": "🥉",
        "title": "Rookie Adventurer",
        "description": "Complete your first quest"
    },

    "Quest Grinder": {
        "badge": "🥈",
        "title": "Quest Grinder",
        "description": "Complete 5 quests"
    },

    "Getting Serious": {
        "badge": "🥇",
        "title": "Dedicated Adventurer",
        "description": "Complete 10 quests"
    },

    "XP Hunter": {
        "badge": "💎",
        "title": "XP Hunter",
        "description": "Earn 100 XP"
    },

    "Level Up!": {
        "badge": "🏆",
        "title": "Rising Hero",
        "description": "Reach Level 2"
    }
}

    for achievement, unlocked in achievements.items():

        badge = achievement_details [achievement] ["badge"]
        title = achievement_details [achievement] ["title"]
        description = achievement_details [achievement] ["description"]

        achievement_card = ctk.CTkFrame(
            achievement_frame
        )
        achievement_card.pack(
            fill="x",
            padx=20,
            pady=6
        )

        name_label = ctk.CTkLabel(
            achievement_card,
            text=f"{badge} {title}",
            font=("Arial", 16, "bold")
        )
        name_label.pack(
            anchor="w",
            padx=15,
            pady=(10, 2)
        )

        description_label = ctk.CTkLabel(
            achievement_card,
            text=description,
            font=("Arial", 12)
        )
        description_label.pack(
            anchor="w",
            padx=15
        )

        if unlocked:
            status_text = "✓ UNLOCKED"
        else:
            status_text = "🔒 LOCKED"

        status_label = ctk.CTkLabel(
            achievement_card,
            text=status_text,
            font=("Arial", 12, "bold")
        )
        status_label.pack(
            anchor="e",
            padx=15,
            pady=(2, 10)
        )

def update_level():
    global level

    old_level = level

    new_level = 1

    while xp >= xp_required_for_level(new_level + 1):
        new_level += 1

    level = new_level

    current_level_xp = xp_required_for_level(level)
    next_level_xp = xp_required_for_level(level + 1)

    xp_in_current_level = xp - current_level_xp
    xp_needed_for_level = next_level_xp - current_level_xp

    progress = xp_in_current_level / xp_needed_for_level

    xp_progress.set(progress)

    level_label.configure(
        text=f"Level : {level}"
    )

    if level > old_level:
        show_level_up(level)
    

def complete_quest(
    quest_label,
    complete_button,
    delete_button,
    selected_difficulty,
    selected_quest_type
 ):
    global xp, completed_quests

    if selected_quest_type == "Main Quest":

        if selected_difficulty == "Easy":
            xp += 20

        elif selected_difficulty == "Medium":
            xp += 30

        elif selected_difficulty == "Hard":
            xp += 40

    elif selected_quest_type == "Side Quest":

        if selected_difficulty == "Easy":
            xp += 10

        elif selected_difficulty == "Medium":
            xp += 15

        elif selected_difficulty == "Hard":
            xp += 20

    xp_label.configure(
        text=f"XP : {xp}"
    )

    update_level()

    completed_quests += 1

    update_streak()

    check_achievements()

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
    selected_quest_type = quest_type.get()
    selected_subject = subject.get()

    quest_card = ctk.CTkFrame(quest_frame)

    quest_card.quest_type_value = selected_quest_type
    quest_card.subject_value = selected_subject

    quest_card.pack(fill="x", padx=10, pady=5)

    quest_label = ctk.CTkLabel(
        quest_card,
        text=f"{quest}  [{selected_quest_type}]  [{selected_difficulty}]  [{selected_subject}]",
    )
    quest_label.pack(side="left", padx=10, pady=10)

    delete_button = ctk.CTkButton(
        quest_card,
        text="✕",
        width=40,
        command=lambda: delete_quest(quest_card),
    )
    delete_button.pack(side="right", padx=5, pady=10)

    complete_button = ctk.CTkButton(
        quest_card,
        text="✓ Complete",
        command=lambda: complete_quest(
            quest_label,
            complete_button,
            delete_button,
            selected_difficulty,
            selected_quest_type,
        ),
    )
    complete_button.pack(side="right", padx=10, pady=10)

    quest_entry.delete(0, tk.END)

xp_progress = ctk.CTkProgressBar(
        window,
        width=400,
        height=15,
        fg_color= "grey"
    )
xp_progress.pack(pady=10)
xp_progress.set(0)

add_button = ctk.CTkButton(
    window,
    text= "Add Quest",
    command=add_quest,
)
add_button.pack()

achievements_button = ctk.CTkButton(
    window, 
    text = "Achievements",
    command = show_achievements,
)
achievements_button.pack(pady=5)

quest_frame = ctk.CTkScrollableFrame(
    window,
    width = 450,
    height = 250,
)
quest_frame.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True,
)

window.mainloop()
