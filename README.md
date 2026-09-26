# IntellectRPG

A gamified study tracker built with Python, CustomTkinter and Tkinter.

## Project Status

**Completed.**

IntellectRPG was built from scratch as part of the FirstCommit hackathon.

## Goal

IntellectRPG aims to turn studying and productivity into an RPG-style experience.

Users can create quests, complete them, earn XP, level up, unlock achievements, maintain study streaks, and track their progress — while being accompanied by a supportive orange cat who is there for the treats.

The goal is to make studying feel more rewarding, motivating, and fun.

## Built With

- Python
- Tkinter
- CustomTkinter

## How to Run

### Requirements

- Python 3
- CustomTkinter

### Setup

1. Clone or download this repository.
2. Open the project folder in VS Code or another Python-compatible code editor.
3. Install CustomTkinter by running:

    pip install customtkinter

4. Run the application:

    python main.py

The IntellectRPG desktop application will open in a new window.

## Screenshots

### Main Dashboard
![Main Dashboard](screenshots/main_screen.png)

### Statistics
![Statistics](screenshots/statistics.png)

### Achievements
![Achievements](screenshots/achievement.png)

## Save Data

IntellectRPG automatically saves user progress in `save_data.json`.

The saved data includes:

- XP
- Level
- Completed quests
- Main Quest and Side Quest progress
- Subject activity
- Study streak
- Achievements
- Last study date

Each user running the project on their own computer will have their own local progress.

## Features

### Quest System

- Create study quests
- Choose between Main Quest and Side Quest
- Select quest difficulty
- Receive different XP rewards based on quest type and difficulty
- Complete and delete quests
- Filter quests by type and subject

### RPG Progression

- Earn XP by completing quests
- Level up as XP increases
- Track current progress toward the next level
- Receive level-up feedback

### Study Tracking

- Organize quests by subject
- Track subject activity
- Maintain a study streak
- View overall study statistics

### Achievement System

IntellectRPG includes achievements that unlock as the user progresses, including achievements for:

- Completing quests
- Reaching XP milestones
- Reaching new levels

### Statistics Dashboard

The statistics section provides information such as:

- Total quests completed
- Total XP
- Current level
- Study streak
- Main Quest and Side Quest activity
- Subject activity
- Most studied subject

### Cat Companion — Crookshanks

A orange cat companion accompanies the user throughout the application.

Crookshanks reacts to the user's progress and provides an additional playful element to the study experience.

## Current Progress

The core project is complete.

- Quest creation and management
- Main Quest and Side Quest system
- Difficulty-based XP rewards
- XP and level progression
- Progress tracking
- Subject-based study tracking
- Study streak system
- Statistics dashboard
- Achievement system
- Save and load progress
- Quest filtering
- Level-up feedback
- Cat companion
- RPG-inspired UI
- Local progress storage

## Future Improvements

Possible future improvements include:

- More cat companion reactions
- Additional achievements
- More RPG progression elements
- Additional visual customization
- More detailed study analytics

## Hackathon

IntellectRPG was created as a project for the **FirstCommit Hackathon**.

The project was developed from scratch during the hackathon period.
