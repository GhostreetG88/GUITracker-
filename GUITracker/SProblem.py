"""
Program: SProblem.py
Author: Adrian Valdez
Date: 5/12/24

The purpose of this program is to check the "GUITraker" program for errors.

"""

import unittest
from GUITraker import Habit, HabitTracker

# Create a test class for the HabitTracker class
class TestHabitTracker(unittest.TestCase):

    # Set up a new instance of HabitTracker for each test
    def setUp(self):
        self.habit_tracker = HabitTracker()

    # Test adding a habit to the habit tracker
    def test_add_habit(self):
        
        habit = Habit("Test Habit", ["Monday", "Tuesday", "Wednesday"])
        self.habit_tracker.add_habit(habit)
        self.assertIn(habit, self.habit_tracker.habits)

    # Test marking a day of a habit as complete
    def test_mark_complete(self):

        habit = Habit("Test Habit", ["Monday", "Tuesday", "Wednesday"])
        self.habit_tracker.add_habit(habit)
        self.habit_tracker.mark_complete(0, 0)
        self.assertTrue(self.habit_tracker.habits[0].progress[0])

    # Test getting the weekly report of habits and their progress
    def test_get_weekly_report(self):
        
        habit1 = Habit("Habit 1", ["Monday", "Tuesday", "Wednesday"])
        habit2 = Habit("Habit 2", ["Tuesday", "Wednesday", "Thursday"])
        self.habit_tracker.add_habit(habit1)
        self.habit_tracker.add_habit(habit2)
        self.habit_tracker.mark_complete(0, 0)
        self.habit_tracker.mark_complete(0, 1)
        self.habit_tracker.mark_complete(1, 1)
        self.habit_tracker.mark_complete(1, 2)
        report = self.habit_tracker.get_weekly_report()
        self.assertEqual(report["Habit 1"]["completed"], 2)
        self.assertEqual(report["Habit 1"]["incomplete"], 1)
        self.assertEqual(report["Habit 2"]["completed"], 2)
        self.assertEqual(report["Habit 2"]["incomplete"], 1)

# Run the tests
if __name__ == '__main__':
    unittest.main()