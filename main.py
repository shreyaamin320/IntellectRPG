import customtkinter as ctk
import tkinter as tk
from datetime import date
import json
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

main_quests_completed = 0
side_quests_completed = 0
subject_counts = {}

quests = []

achievements = {
    "First Quest": False,
    "Quest Grinder": False,
    "Getting Serious": False,
    "XP Hunter": False,
    "Level Up!": False
}

def save_progress():
    data = {
        "xp" : xp,
        "level" : level,
        "completed_quests" : completed_quests,
        "main_quests_completed" : main_quests_completed,
        "side_quests_completed" : side_quests_completed,
        "subject_counts" : subject_counts,
        "study_streak" : study_streak,
        "last_study_date" : (
            last_study_date.isoformat()
            if last_study_date is not None 
            else None
        ),
        "achievements" : achievements,
        "quests" : quests,
    }

    with open("save_data.json" , "w") as file:
        json.dump(data, file, indent=4)

def load_progress():

    global xp, level
    global completed_quests
    global main_quests_completed, side_quests_completed
    global subject_counts
    global study_streak, last_study_date
    global achievements
    global quests

    try:

        with open("save_data.json", "r") as file:
            data = json.load(file)

        xp = data.get("xp", 0)
        level = data.get("level", 1)

        completed_quests = data.get( "completed_quests", 0)

        main_quests_completed = data.get("main_quests_completed", 0)

        side_quests_completed = data.get( "side_quests_completed", 0)

        subject_counts = data.get("subject_counts", {})

        quests = data.get("quests" , [])

        study_streak = data.get( "study_streak", 0)

        saved_date = data.get("last_study_date")

        if saved_date is not None:
            last_study_date = date.fromisoformat(saved_date)

            today = date.today()

            if( today - last_study_date).days > 1:
                study_streak = 0

        else:
            last_study_date = None

        saved_achievements = data.get("achievements", {})

        for achievement_name in achievements:

            if achievement_name in saved_achievements:
                achievements[achievement_name] = (saved_achievements[achievement_name])

    except FileNotFoundError:
        pass

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

def delete_quest(quest_card , quest_data):

    if quest_data in quests:
        quests.remove(quest_data)

    quest_card.destroy()

    save_progress()
    

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

def show_statistics():

    statistics_window = ctk.CTkToplevel(window)
    statistics_window.title("Statistics")
    statistics_window.geometry("500x600")

    statistics_frame = ctk.CTkScrollableFrame(
        statistics_window,
        width=450,
        height=520
    )
    statistics_frame.pack(
        padx=15,
        pady=10,
        fill="both",
        expand=True
    )

    title_label = ctk.CTkLabel(
        statistics_frame,
        text="Statistics",
        font=("Arial", 24, "bold")
    )
    title_label.pack(pady=15)

    total_quests_label = ctk.CTkLabel(
        statistics_frame,
        text=f"Total Quests Completed : {completed_quests}",
        font=("Arial", 16)
    )
    total_quests_label.pack(pady=8)

    total_xp_label = ctk.CTkLabel(
        statistics_frame,
        text=f"Total XP Earned : {xp}",
        font=("Arial", 16)
    )
    total_xp_label.pack(pady=8)

    level_stats_label = ctk.CTkLabel(
        statistics_frame,
        text=f"Current Level : {level}",
        font=("Arial", 16)
    )
    level_stats_label.pack(pady=8)

    streak_stats_label = ctk.CTkLabel(
        statistics_frame,
        text=f"Current Streak : {study_streak} days",
        font=("Arial", 16)
    )
    streak_stats_label.pack(pady=8)

    main_quest_label = ctk.CTkLabel(
        statistics_frame,
        text=f"Main Quests : {main_quests_completed}",
        font=("Arial", 16)
    )
    main_quest_label.pack(pady=8)

    side_quest_label = ctk.CTkLabel(
        statistics_frame,
        text=f"Side Quests : {side_quests_completed}",
        font=("Arial", 16)
    )
    side_quest_label.pack(pady=8)

    subject_title = ctk.CTkLabel(
        statistics_frame,
        text="Subject Activity",
        font=("Arial", 18, "bold")
    )
    subject_title.pack(pady=15)

    if subject_counts:

        for subject_name, count in subject_counts.items():

            subject_label = ctk.CTkLabel(
            statistics_frame,
            text=f"{subject_name} : {count} quests",
            font=("Arial", 14),
            )
            subject_label.pack(pady=3)

    else:
        no_subjects_label = ctk.CTkLabel(
            statistics_frame,
            text="No completed quests yet.",
            font=("Arial", 14),
        )
        no_subjects_label.pack(pady=5)

    if subject_counts:

        most_studied_subject = max(
            subject_counts,
            key=subject_counts.get,
        )   

    most_studied_count = subject_counts[most_studied_subject]

    most_studied_label = ctk.CTkLabel(
        statistics_frame,
        text=(
            f"Most Studied Subject : "
            f"{most_studied_subject} "
            f"({most_studied_count} quests)"
        ),
        font=("Arial", 16, "bold")
    )
    most_studied_label.pack(pady=15)

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
    selected_quest_type,
    selected_subject,
    quest_data,
 ):
    global xp, completed_quests
    global main_quests_completed, side_quests_completed
    global subject_counts

    quest_data["completed"] = True

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

    if selected_quest_type == "Main Quest":
        main_quests_completed += 1
    elif selected_quest_type == "Side Quest":
        side_quests_completed += 1

    if selected_subject not in subject_counts:
        subject_counts[selected_subject] = 0

    subject_counts[selected_subject] += 1

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

    save_progress()

def create_quest_card(
    quest_text,
    selected_difficulty,
    selected_quest_type,
    selected_subject,
    completed=False,
    quest_data = None,
):

    quest_card = ctk.CTkFrame(
        quest_frame
    )

    quest_card.quest_type_value = selected_quest_type
    quest_card.subject_value = selected_subject

    quest_card.pack(
        fill="x",
        padx=10,
        pady=5
    )

    quest_label = ctk.CTkLabel(
        quest_card,
        text=(
            f"{quest_text}  "
            f"[{selected_quest_type}]  "
            f"[{selected_difficulty}]  "
            f"[{selected_subject}]"
        )
    )
    quest_label.pack(
        side="left",
        padx=10,
        pady=10
    )

    delete_button = ctk.CTkButton(
        quest_card,
        text="✕",
        width=40,
        command = lambda: delete_quest(quest_card, quest_data),
    )
    delete_button.pack(
        side="right",
        padx=5,
        pady=10
    )

    complete_button = ctk.CTkButton(
        quest_card,
        text="✓ Complete"
    )
    complete_button.pack(
        side="right",
        padx=10,
        pady=10
    )

    if completed:

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

    else:

        complete_button.configure(
            command=lambda: complete_quest(
                quest_label,
                complete_button,
                delete_button,
                selected_difficulty,
                selected_quest_type,
                selected_subject,
                quest_data,
            )
        )

        delete_button.configure(
            command=lambda: delete_quest(quest_card, quest_data)
        )

    return quest_card

def add_quest():

    quest_text = quest_entry.get()
    selected_difficulty = difficulty.get()
    selected_quest_type = quest_type.get()
    selected_subject = subject.get()

    quest_data = {
        "text": quest_text,
        "difficulty": selected_difficulty,
        "quest_type": selected_quest_type,
        "subject": selected_subject,
        "completed": False
    }

    quests.append(quest_data)

    create_quest_card(
        quest_text,
        selected_difficulty,
        selected_quest_type,
        selected_subject,
        quest_data = quest_data
    )

    quest_entry.delete(
        0,
        tk.END
    )

    save_progress()

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

statistics_button = ctk.CTkButton(
    window,
    text="Statistics",
    command=show_statistics,
)
statistics_button.pack(pady=5)

save_button = ctk.CTkButton(
    window,
    text="Save Progress",
    command=save_progress
)
save_button.pack(pady=5)

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

load_progress()

xp_label.configure(
    text=f"XP : {xp}"
)

level_label.configure(
    text=f"Level : {level}"
)

streak_label.configure(
    text=f"Streak : {study_streak}"
)

update_level()

for quest_data in quests:

    create_quest_card(
        quest_data["text"],
        quest_data["difficulty"],
        quest_data["quest_type"],
        quest_data["subject"],
        quest_data["completed"],
        quest_data
    )

window.mainloop()
