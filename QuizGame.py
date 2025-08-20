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

    def shuffle_question_bank(self):
        '''Randomly shuffles the list of questions available for the game. Should happen automatically when the game starts.'''
        pass

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
        pass


question1 = Question(qu = "Meow?", a = "Meow.")
question2 = Question(qu ="Bark?", a = "Bark.")
question3 = Question(qu = "The", a ="Thinkerrr")
quiz1 = QuizGame(question_bank = [question1, question2, question3])

print(quiz1.display_question())
