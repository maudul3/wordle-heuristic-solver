
STARTING_GUESSES = 6

class WordleGame:
    def __init__(self, word):
        """Initialize wordle game

        Args:
            word (Word): word player tries to guess
        
        Returns:
            self: WordleGame object
        """
        self.word = word
        self.correct_guess = False
        self.guesses_remaining = STARTING_GUESSES

    def check_guess(self, guess):
        """
        Args:
            guess (Word): agent's guess word

        Returns:
            constraints (?): constraints the agent 
            can use to make next guess
        """
        self.guesses_remaining -= 1

        if guess.rep == self.word.rep:
            self.correct_guess = True
        
        return 1