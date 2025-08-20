from abc import ABC, abstractmethod

# Abstract class (bonus feature)
class GameRole(ABC):
    def __init__(self, name="Unknown"):
        self._name = name  #encapsulated with underscore

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    @abstractmethod
    def get_role(self):
        pass


# Player inherits from GameRole
class Player(GameRole):
    def __init__(self, name="Player", score=0):
        super().__init__(name)
        self._score = score

    def add_score(self, points):
        self._score += points

    def get_score(self):
        return self._score

    def reset_score(self):
        self._score = 0

    # Polymorphism: override abstract method
    def get_role(self):
        return "Player"

# --- Helper method for saving ---
    def to_dict(self) -> dict:
        """Return player data in dictionary format (useful for saving to file)."""
        return {"name": self.get_name, "score": self._score}
