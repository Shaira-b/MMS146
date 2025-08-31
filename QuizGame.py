import random
import Questions
from Questions import Music, Gaming, FilmTV

class QuizGame:
    '''
    Quiz Game class
    '''
    def __init__(self, question_bank):
        '''
        Initializes a new instance of the quiz game class.
        question_bank: Retrieves the question_bank dict from Questions and uses it for the quiz instance.
        current_category: By default, no category selected yet. Sets the category of the QuizGame and determines the question pool for the session.
        difficulties: The quiz game's difficulties; used for retrieving questions of a specific difficulty from the question_bank dict.
        current_difficulty_index: Records which difficulty the player is currently playing at. Changes as the game continues.
        current_index: Tracking which question you're up to inside each difficulty of the selected category.
        quiz_active: Checks for whether or not the quiz is ongoing or not.
        '''
        self.question_bank = question_bank
        self.score = 0
        self.current_category = None
        self.difficulties = ["Easy", "Moderate", "Hard"]
        self.current_difficulty_index = 0
        self.current_index = {}
        self.quiz_active = True

    # Lmk if need ko to palitan or tanggalin, tysm.
    def select_category(self, category):  # A method for when the player chooses a category.
        """Set the current category and shuffle its questions by difficulty."""
        while True:
            category = input("Please type out the category you'd like to select for this session: ")
            if category in ["Music", "Film and TV", "Gaming"]: # Checks if input is included in the category list.
                self.current_category = category  # Saves the chosen category.
                print("------------------------------------------------------------------------")
                self.shuffle_question_bank(category) # Shuffles all the questions inside that category.
                self.current_index = {difficulty: 0 for difficulty in self.question_bank[category]}  # Reset index tracking for each difficulty
                break
            else: # Result if input is not part of the list.
                print("Invalid input. Please re-enter your choice.")

    def shuffle_question_bank(self, category):
        """Shuffle only the chosen category, across all difficulties."""
        # A method that shuffles question only inside the category picked by the player.
        for difficulty, questions in self.question_bank[category].items():
            random.shuffle(questions)
        self.display_question()
        
    def display_question(self):
        '''
        Displays a question (class) from the shuffled question bank.
        This method will loop a certain number of times until a specific threshold is reached (4 questions completed in Easy, 3 in Moderate and Hard).
        From there, the difficulty will increase, and a new set of questions will be provided.
        Once a total of ten questions have been answered, the game comes to an end, and the final score is provided, along with an option to restart.
        '''
        difficulty = self.difficulties[self.current_difficulty_index]
        quizcontent = self.question_bank[self.current_category]
        questions_list = quizcontent[difficulty]

        if difficulty not in self.current_index:
            self.current_index[difficulty] = 0 

        while self.current_index[difficulty] < 4: # This ensures that a maximum of four questions within a difficulty are asked in a loop.
            if not self.quiz_active:  # Checks if the quiz instance was deactivated by later input; if player asked to end session, ends the game.
                return
            index = self.current_index[difficulty]
            giventext = questions_list[index]
            print("Question:", giventext.question_text) # This prints out the question.
            print("Choices:", giventext.answers) # This prints out the answers.

            player_input = input("Please type in the answer here: ") # This is where the player inputs their response, to which the display_question method will execute
            self.check_answer(player_input, giventext)               # the check_answer method.

            self.current_index[difficulty] += 1 # After a question is asked, the current_index increases.

            if self.current_index[difficulty] == 3 and self.current_difficulty_index == 2: # This activates after all of the Hard difficulty questions are asked.
                print("Awesome! You finished the quiz! Your score is: ", self.get_score(),"!")
                while True:
                    restart = input("Play again? Please type 'Yes', if you would like to play one more time, and 'No' if you would like to finish. ")
                    if restart == "Yes":
                        self.reset_game()
                        return
                    elif restart == "No":
                        print("Alright, then! Thanks for playing!")
                        self.quiz_active = False
                        return
                    else:
                        print("Invalid input. Please re-enter your response.")
            elif self.current_index[difficulty] == 4 and self.current_difficulty_index == 0: # This activates after all of the Easy difficulty questions are asked.
                self.current_difficulty_index += 1
                print("Alright! Moving onto a harder difficulty! Keep it up!")
                self.display_question()
            elif self.current_index[difficulty] == 3 and self.current_difficulty_index == 1: # This activates after all of the Moderate questions are asked.
                self.current_difficulty_index += 1
                print("Alright! Moving onto a harder difficulty! Keep it up!")
                self.display_question()
    
    def get_score(self):
        return self.score

    def check_answer(self, player_input, giventext):
        '''This method is activated within the display_question method. It checks for the correctness of the player's input and increases or retains their current score.'''
        if player_input == giventext.correct_answer: # If player answer is correct, add one point.
            self.score += 1
            print("Correct! Great job!")
        else:
            print("Oops, that was the wrong answer. The correct answer is: ", giventext.correct_answer) # If player answer is incorrect, retain current point standing.
        print()
        print("------------------------------------------------------------------------")
        print()


    def reset_game(self):
        self.score = 0 # Returns the score to 0.
        self.current_category = None  # Removes the current category selection.
        self.current_index = {}  # Clears the tracked questions in each difficulty.
        self.current_difficulty_index = 0 # Resets the difficulty.

    def reset_game(self):
        self.score = 0
        self.current_category = None  # Removes the current category selection.
        self.current_index = {}  # Clears the tracked questions in each difficulty.
        self.current_difficulty_index = 0
        print()
        print("------------------------------------------------------------------------")
        print()
        print(
    """
Hello and welcome to Group B's Quiz Game!
We've got some fun questions for you to answer today!
Here's some things to keep in mind before we start.

Things to keep in mind:
1. All inputs are case sensitive! Please type out your answer exactly how it is presented to you in the choices, or you'll be marked incorrect. That means looking out for punctuation!
2. There are a total of three difficulties to get through: Easy, Moderate, and Hard. You'll have to answer 3 questions in every category before moving up.
3. Questions are shuffled every time you start the quiz! So if you feel like playing again at the end, go ahead! You'll have random questions selected each time.

So, without further ado, let's begin!")
print("The categories are: Music, Film and TV, and Gaming.
    """
        )
        self.select_category()


# QUESTION BANK
question_bank = {
    "Music": {
        "Easy": [
            Music("Who sang 'Shake It Off'?",
                  ["Taylor Swift", "Katy Perry", "Ariana Grande"],
                  "Taylor Swift", "Easy"),

            Music("Which boy band included members Harry Styles and Niall Horan?",
                  ["One Direction", "BTS", "5 Seconds of Summer"],
                  "One Direction", "Easy"),

            Music("'Blinding Lights' is a hit song by which artist?",
                  ["The Weeknd", "Post Malone", "Ed Sheeran"],
                  "The Weeknd", "Easy"),

            Music("Who is known as the 'King of Pop'?",
                  ["Elvis Presley", "Michael Jackson", "Justin Timberlake"],
                  "Michael Jackson", "Easy"),

            Music("Billie Eilish’s breakout song in 2019 was?",
                  ["bad guy", "lovely", "ocean eyes"],
                  "bad guy", "Easy"),
        ],
        "Moderate": [
            Music("Which 2023 song became a viral Barbie movie hit?",
                  ["Dance the Night - Dua Lipa", "Karma - Taylor Swift", "Flowers - Miley Cyrus"],
                  "Dance the Night - Dua Lipa", "Moderate"),

            Music("BTS’s fanbase is called?",
                  ["BLINK", "ARMY", "MOA"],
                  "ARMY", "Moderate"),

            Music("Who featured on Lady Gaga’s 'Rain on Me'?",
                  ["Ariana Grande", "Katy Perry", "Sia"],
                  "Ariana Grande", "Moderate"),

            Music("Which artist released the album Eternal Sunshine in 2024?",
                  ["Ariana Grande", "Taylor Swift", "Olivia Rodrigo"],
                  "Ariana Grande", "Moderate"),

            Music("'Levitating' became a major TikTok trend in which year?",
                  ["2019", "2020", "2021"],
                  "2020", "Moderate"),
        ],
        "Hard": [
            Music("What is the title of Taylor Swift’s 12th studio album?",
                  ["The Life of a Showgirl", "The Tortured Poets Department", "Folklore"],
                  "The Life of a Showgirl", "Hard"),

            Music("Which artist won Album of the Year at the 2024 Grammys?",
                  ["Taylor Swift", "Jon Batiste", "Billie Eilish"],
                  "Taylor Swift", "Hard"),

            Music("Who composed the score for The Lion King (1994)?",
                  ["Hans Zimmer", "Alan Menken", "John Williams"],
                  "Hans Zimmer", "Hard"),

            Music("The hit 'Take On Me' is by which band?",
                  ["A-ha", "Duran Duran", "Tears for Fears"],
                  "A-ha", "Hard"),

            Music("What year did Spotify officially launch?",
                  ["2006", "2008", "2010"],
                  "2008", "Hard"),
        ],
    },

    "Film & TV": {
        "Easy": [
            FilmTV("Who plays Iron Man in the Marvel Cinematic Universe?",
                   ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth"],
                   "Robert Downey Jr.", "Easy"),

            FilmTV("Which TV show features the Upside Down?",
                   ["Stranger Things", "Wednesday", "The X-Files"],
                   "Stranger Things", "Easy"),

            FilmTV("In Frozen, which character sings 'Let It Go'?",
                   ["Anna", "Elsa", "Olaf"],
                   "Elsa", "Easy"),

            FilmTV("Who plays Hermione Granger in Harry Potter?",
                   ["Emma Watson", "Emma Roberts", "Keira Knightley"],
                   "Emma Watson", "Easy"),

            FilmTV("The animated movie Finding Nemo is produced by?",
                   ["Pixar", "DreamWorks", "Illumination"],
                   "Pixar", "Easy"),
        ],
        "Moderate": [
            FilmTV("Which year did the first Avengers movie release?",
                   ["2010", "2012", "2014"],
                   "2012", "Moderate"),

            FilmTV("Who voices Woody in Toy Story?",
                   ["Tom Hanks", "Tim Allen", "Chris Pratt"],
                   "Tom Hanks", "Moderate"),

            FilmTV("The series The Mandalorian is set in which universe?",
                   ["Star Wars", "Star Trek", "Marvel"],
                   "Star Wars", "Moderate"),

            FilmTV("Which Marvel film features the fictional African nation of Wakanda?",
                   ["Black Panther", "Eternals", "Doctor Strange"],
                   "Black Panther", "Moderate"),

            FilmTV("Who is the main protagonist of The Hunger Games trilogy?",
                   ["Katniss Everdeen", "Tris Prior", "Bella Swan"],
                   "Katniss Everdeen", "Moderate"),
        ],
        "Hard": [
            FilmTV("In Breaking Bad, what is Walter White’s alias?",
                   ["Heisenberg", "Eisenstein", "Goldberg"],
                   "Heisenberg", "Hard"),

            FilmTV("Who directed the 2019 Academy Award-winning film Parasite?",
                   ["Bong Joon-ho", "Park Chan-wook", "Kim Jee-woon"],
                   "Bong Joon-ho", "Hard"),

            FilmTV("Who directed Everything Everywhere All at Once?",
                   ["Daniels (Daniel Kwan & Daniel Scheinert)", "Bong Joon-ho", "Greta Gerwig"],
                   "Daniels (Daniel Kwan & Daniel Scheinert)", "Hard"),

            FilmTV("In Inception, which object is Cobb’s totem?",
                   ["Spinning top", "Dice", "Coin"],
                   "Spinning top", "Hard"),

            FilmTV("Which Studio Ghibli film features the Catbus?",
                   ["My Neighbor Totoro", "Spirited Away", "Kiki's Delivery Service"],
                   "My Neighbor Totoro", "Hard"),
        ],
    },

    "Gaming": {
        "Easy": [
            Gaming("Which game features the characters Mario and Luigi?",
                   ["Super Mario Bros.", "Sonic the Hedgehog", "Donkey Kong"],
                   "Super Mario Bros.", "Easy"),

            Gaming("Pikachu is from which franchise?",
                   ["Digimon", "Pokemon", "Yu-Gi-Oh!"],
                   "Pokemon", "Easy"),

            Gaming("The game Among Us became popular in which year?",
                   ["2018", "2020", "2022"],
                   "2020", "Easy"),

            Gaming("What is the main goal in Minecraft?",
                   ["Survive and build", "Rescue a princess", "Solve puzzles"],
                   "Survive and build", "Easy"),

            Gaming("Which game is known for the phrase 'Victory Royale'?",
                   ["Fortnite", "PUBG", "Apex Legends"],
                   "Fortnite", "Easy"),
        ],
        "Moderate": [
            Gaming("Who is the main character of The Legend of Zelda?",
                   ["Link", "Zelda", "Ganondorf"],
                   "Link", "Moderate"),

            Gaming("Which 2023 game is a remake of a 2005 PlayStation 2 classic?",
                   ["Resident Evil 4", "Dead Space", "Final Fantasy VII"],
                   "Resident Evil 4", "Moderate"),

            Gaming("What is the name of the haunted animatronic game series?",
                   ["Five Nights at Freddy's", "Bendy and the Ink Machine", "Poppy Playtime"],
                   "Five Nights at Freddy's", "Moderate"),

            Gaming("In Overwatch, which hero says 'Cheers, love! The cavalry’s here!'?",
                   ["Tracer", "Mercy", "D.Va"],
                   "Tracer", "Moderate"),

            Gaming("Which video game company created the Xbox?",
                   ["Microsoft", "Sony", "Nintendo"],
                   "Microsoft", "Moderate"),
        ],
        "Hard": [
            Gaming("In Final Fantasy X, what sport does Tidus play?",
                   ["Blitzball", "Sphereball", "Aquaball"],
                   "Blitzball", "Hard"),

            Gaming("Which annual event crowns the world champion team in League of Legends?",
                   ["Worlds", "The International", "MSI"],
                   "Worlds", "Hard"),

            Gaming("What is the name of the island in Animal Crossing: New Horizons?",
                   ["It's player-named", "Nook Island", "Horizon Island"],
                   "It's player-named", "Hard"),

            Gaming("In The Last of Us Part II, what is the name of Ellie’s guitar teacher?",
                   ["Joel", "Tommy", "Jesse"],
                   "Joel", "Hard"),

            Gaming("Which early 2000s MMORPG popularized the phrase 'Leeroy Jenkins'?",
                   ["World of Warcraft", "RuneScape", "EverQuest"],
                   "World of Warcraft", "Hard"),
        ],
    },
}

# Literally all you need to run the game.
quiz1 = QuizGame(question_bank)
quiz1.start_game()
