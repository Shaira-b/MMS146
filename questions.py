# Main Class
class Question:  
    def __init__(self, question_text, answers, correct_answer, difficulty):
        self.question_text = question_text      # Store the question text
        self.answers = answers      # Store the multiple-choice options
        self.correct_answer = correct_answer      # Store the correct answer
        self.difficulty = difficulty      # Store the difficulty level (Easy, Medium, Hard)
        self.category = None      # Default category

    def get_question_text(self):     # Return the question text
        return self.question_text

    def get_answers(self):     # Return the answers list
        return self.answers

    def get_correct_answer(self):
        index = self.answers.index(self.correct_answer)     # Find the index of the correct answer in the answers list
        letter = chr(ord('A') + index)     # Convert the index to a letter (A, B, C, D)
        return f"{letter}. {self.correct_answer}"     # Return the correct answer with its letter label

    def get_category(self):     # Return question category
        return self.category     # This will be set by the subclass
    
    def get_difficulty(self):
        return self.difficulty     # Return the question's difficulty level


# Sub Classes
class Music(Question):  
    def __init__(self, question_text, answers, correct_answer, difficulty):     
        super().__init__(question_text, answers, correct_answer, difficulty)
        self.category = "Music"     # Set category to "Music"

class FilmTV(Question):  
    def __init__(self, question_text, answers, correct_answer, difficulty):     
        super().__init__(question_text, answers, correct_answer, difficulty)
        self.category = "Film & TV"     # Set category to "Film & TV"


class Gaming(Question):  
    def __init__(self, question_text, answers, correct_answer, difficulty):
        super().__init__(question_text, answers, correct_answer, difficulty)
        self.category = "Gaming"     # Set category to "Gaming"
