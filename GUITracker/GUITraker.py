"""
Program: GUITraker.py
Author: Adrian Valdez
Date: 5/12/24

The purpose of this GUI is to keep track of your habits.
Habit Tracker is a GUI application designed to help you track and maintain your daily habits.
With this application, add the habits you want to complete each day, easy to use and simple to understand. 

"""


import tkinter as tk
from PIL import Image, ImageTk

class Habit:
    def __init__(self, name, days_of_week):

        #Initializes a new instance of the Habit class with a name and a list of days of the week
        self.name = name
        self.days_of_week = days_of_week
        self.progress = [False] * len(days_of_week)

class HabitTracker:
    def __init__(self):

        #Initializes a new instance of the HabitTracker class without habits
        self.habits = []

    def add_habit(self, habit):

        #Addd a habit to the list of habits
        self.habits.append(habit)

    def mark_complete(self, habit_index, day_index):
    
        #Mark the specified day of the week as completed for the specified habit
        self.habits[habit_index].progress[day_index] = True

    def get_weekly_report(self):

        #Returns a weekly report of habits and their progress
        report = {}
        for habit in self.habits:
            report[habit.name] = {
                'completed': 0,
                'incomplete': 0
            }
            for i, day in enumerate(habit.progress):
                if day:
                    report[habit.name]['completed'] += 1
                else:
                    report[habit.name]['incomplete'] += 1
        return report

class ExitButton(tk.Button):
    def __init__(self, master):

        #Initializes a new instance of the ExitButton class with a reference to the master widget
        super().__init__(master, text="Exit", command=master.quit)

class WelcomeWindow(tk.Tk):
    def __init__(self, habit_tracker, image_path):

        #Initializes a new instance of the WelcomeWindow class with an instance of HabitTracker and an image paht
        super().__init__()

        self.title("Habit Tracker")
        self.geometry("400x400")

        self.habit_tracker = habit_tracker

        self.label = tk.Label(self, text="Welcome to Habit Tracker!")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Add Habit", command=self.add_habit)
        self.button.pack()

        self.habits_button = tk.Button(self, text="View Habits", command=self.view_habits)
        self.habits_button.pack()

        self.exit_button = ExitButton(self)
        self.exit_button.pack()

        #   1111         IIIIII  MM        MM       AA          GGGGGG   EEEEEEE
        #     11           II    MM MM  MM MM      A  A       GG         EE
        #     11           II    MM   MM   MM     AAAAAA     GG   GGG    EEEE
        #     11           II    MM        MM    AA    AA     GG     GG  EE 
        #   111111       iiiiII  MM        MM   AA      AA      GGGGG    EEEEEEE
      
        image_path = "C:\\Users\\adria\\Documents\\Homework\\Python\\FInal Project\\Home 4-2\\habit_track.png"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self, image=photo)
        self.image_label.image = photo  
        self.image_label.pack()

    def add_habit(self):

        #Add a habit to the HabitTracker instance using the name entered in the text box
        habit_name = self.entry.get()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        habit = Habit(habit_name, days_of_week)
        self.habit_tracker.add_habit(habit)
        self.entry.delete(0, tk.END)

    def view_habits(self):

        #Displays a popup window with the habits and their progress

        
        #     2222        IIIIII  MM        MM       AA          GGGGGG   EEEEEEE
        #   22    22        II    MM MM  MM MM      A  A       GG         EE
        #        22         II    MM   MM   MM     AAAAAA     GG   GGG    EEEE
        #      22           II    MM        MM    AA    AA     GG     GG  EE 
        #   22222222      iiiiII  MM        MM   AA      AA      GGGGG    EEEEEEE
        
        image_path2 = "C:\\Users\\adria\\Documents\\Homework\\Python\\FInal Project\\Home 4-2\\2habit.png"
        habits_window = tk.Toplevel(self)
        habits_window.title("Habits")
        habits_window.geometry("700x600")

        for i, habit in enumerate(self.habit_tracker.habits):
            row = tk.Frame(habits_window)
            row.pack()

            name_label = tk.Label(row, text=habit.name)
            name_label.grid(row=0, column=0)

            for j, day in enumerate(habit.days_of_week):
                check_var = tk.BooleanVar()
                check_box = tk.Checkbutton(row, variable=check_var, onvalue=True, offvalue=False, text=day)
                check_box.grid(row=0, column=j+1)
                check_box.bind("<Button-1>", lambda event, h=i, d=j: self.habit_tracker.mark_complete(h, d))

        back_button = tk.Button(habits_window, text="Back", command=habits_window.destroy)
        back_button.pack()

        image = Image.open(image_path2)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(habits_window, image=photo)
        image_label.image = photo  
        image_label.pack()

        self.exit_button = ExitButton(habits_window)
        self.exit_button.pack()

class HabitsWindow(tk.Toplevel):
    def __init__(self, habit_tracker, image_path):

        #Initializes a new instance of the HabitsWindow class with an instance of HabitTracker and an image path
        super().__init__()

        self.title("Habits")
        self.geometry("700x400")

        self.habit_tracker = habit_tracker

        for i, habit in enumerate(self.habit_tracker.habits):
            row = tk.Frame(self)
            row.pack()

            name_label = tk.Label(row, text=habit.name)
            name_label.grid(row=0, column=0)

            for j, day in enumerate(habit.days_of_week):
                check_var = tk.BooleanVar()
                check_box = tk.Checkbutton(row, variable=check_var, onvalue=True, offvalue=False, text=day)
                check_box.grid(row=0, column=j+1)
                check_box.bind("<Button-1>", lambda event, h=i, d=j: self.habit_tracker.mark_complete(h, d))

        back_button = tk.Button(self, text="Back", command=self.destroy)
        back_button.pack()

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self, image=photo)
        image_label.image = photo  
        image_label.pack()

        self.exit_button = ExitButton(self)
        self.exit_button.pack()

if __name__ == "__main__":
    habit_tracker = HabitTracker()
    welcome_window = WelcomeWindow(habit_tracker, "C:\\Users\\adria\\Documents\\Homework\\Python\\FInal Project\\Home 4-2\\habit_track.png")
    welcome_window.mainloop()
