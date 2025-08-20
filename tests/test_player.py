import unittest
from player import Player  # adjust if your file path is different

class TestPlayer(unittest.TestCase):
    def test_get_and_set_name(self):
        player = Player("Alice")
        self.assertEqual(player.get_name(), "Alice")

        player.set_name("Bob")
        self.assertEqual(player.get_name(), "Bob")

if __name__ == "__main__":
    unittest.main()
