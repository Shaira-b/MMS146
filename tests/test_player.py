import unittest
from Player import Player   # adjust if filename is lowercase player.py

class TestPlayer(unittest.TestCase):
    def test_get_and_set_name(self):
        p = Player("Shaira")
        self.assertEqual(p.get_name(), "Shaira")

        p.set_name("Mae")
        self.assertEqual(p.get_name(), "Mae")

    def test_score_handling(self):
        p = Player("Shaira", score=5)
        p.add_score(10)
        self.assertEqual(p.get_score(), 15)

        p.reset_score()
        self.assertEqual(p.get_score(), 0)

    def test_to_dict(self):
        p = Player("Shaira", score=20)
        self.assertEqual(p.to_dict(), {"name": "Shaira", "score": 20})

if __name__ == "__main__":
    unittest.main()

