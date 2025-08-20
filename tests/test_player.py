import unittest
import sys
import os

# --- Make sure Python can find the player module ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from player import Player  # now it will import correctly

class TestPlayer(unittest.TestCase):
    def test_get_and_set_name(self):
        player = Player("Alice")
        self.assertEqual(player.get_name(), "Alice")

        player.set_name("Bob")
        self.assertEqual(player.get_name(), "Bob")

if __name__ == "__main__":
    unittest.main()
