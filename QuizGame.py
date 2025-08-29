import random

class Question:
    '''Testing Placeholder'''
    def __init__(self, qu, a):
        self.qu = qu
        self.a = a
        self.score = 1

class QuizGame:
    '''
    Quiz Game class
    '''
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.score = 0
        self.current_category = None  # No category selected yet.
        self.current_index = {}  # Tracking which question you’re up to inside each difficulty of the selected category.

    # Lmk if need ko to palitan or tanggalin, tysm.
    def select_category(self, category):  # A method for when the player chooses a category.
        """Set the current category and shuffle its questions by difficulty."""
        self.current_category = category  # Saves the chosen category.
        self.shuffle_question_bank(category) # Shuffles all the questions inside that category.
        self.current_index = {difficulty: 0 for difficulty in self.question_bank[category]}  # Reset index tracking for each difficulty

    def shuffle_question_bank(self, category):
        """Shuffle only the chosen category, across all difficulties."""
        # A method that shuffles question only inside the category picked by the player.
        for difficulty, questions in self.question_bank[category].items():
            random.shuffle(questions)
        
    def display_question(self):
        '''
        Displays a question (class) from the shuffled question bank
        '''
        return random.choice(self.question_bank)
    
    def get_score(self):
        return self.score

    def check_answer(self):
        pass

    def reset_game(self):
        self.score = 0
        self.current_category = None  # Removes the current category selection.
        self.current_index = {}  # Clears the tracked questions in each difficulty.


question1 = Question(qu = "Meow?", a = "Meow.")
question2 = Question(qu ="Bark?", a = "Bark.")
question3 = Question(qu = "The", a ="Thinkerrr")
quiz1 = QuizGame(question_bank = [question1, question2, question3])

print(quiz1.display_question())



