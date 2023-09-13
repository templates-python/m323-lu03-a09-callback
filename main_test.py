import unittest
from main import GreetingApp
import tkinter as tk


class TestGreetingApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = GreetingApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_greet_user(self):
        # Setze den Namen im Eingabefeld
        self.app.entry.insert(0, "John")

        # Rufe die Callback-Funktion auf
        self.app.greet_user()

        # Überprüfe, ob die Begrüßungsnachricht korrekt angezeigt wird
        self.assertEqual(self.app.greeting_label.cget("text"), "Hallo, John!")


if __name__ == '__main__':
    unittest.main()
