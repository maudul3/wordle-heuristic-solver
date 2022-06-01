
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
            constraints (list<str>): constraints on word list, represented by
                2 - correct position
                1 - in word wrong position
                0 - not in word 
        """
        self.guesses_remaining -= 1

        if guess.rep == self.word.rep:
            self.correct_guess = True

        constraints = ['-1','-1','-1','-1','-1']
        for i, letter in enumerate(guess.rep):
            if letter == self.word.rep[i]:
                constraints[i] = '2'
            elif letter in self.word.rep:
                constraints[i] = '1'
            else:
                constraints[i] = '0'

        return constraints 

if __name__ == '__main__':
    from word import Word
    test = Word("words")
    guess = Word("board")
    game = WordleGame(test)
    constraints = game.check_guess(guess)
    print ("Constraints: ", constraints)