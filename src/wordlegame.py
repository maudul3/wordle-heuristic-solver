STARTING_GUESSES = 6


class WordleGame:
    def __init__(self, word):
        """Initialize wordle game

        Inputs:
            word (Word): word player tries to guess

        Outputs:
            self: WordleGame object
        """
        self.word = word
        self.correct_guess = False
        self.guesses_remaining = STARTING_GUESSES

    def check_guess(self, guess):
        """Check a player's guess

        Inputs:
            guess (Word): agent's guess word

        Outputs:
            constraints (list<str>): constraints on word list, represented by
                2 - correct position
                1 - in word wrong position
                0 - not in word
        """
        self.guesses_remaining -= 1

        if guess.rep == self.word.rep:
            self.correct_guess = True

        # Init with -1 for debugging:
        constraints = ["-1", "-1", "-1", "-1", "-1"]

        # Loop through and assign each position appropriate constraint code.
        for i, letter in enumerate(guess.rep):
            if letter == self.word.rep[i]:
                constraints[i] = "2"
            elif letter in self.word.rep:
                constraints[i] = "1"
            else:
                constraints[i] = "0"
        return constraints

    # Visualization requires slightly different constraint coding.
    # Repeated letters in guess should not show "right letter, wrong place",
    # for example, unless the target word has the letter repeated as well.
    def get_visual_constraints(self, guess):
        """Get constraints on word list that can be used for visualization

        Inputs:
            guess (Word): agent's guess word

        Outputs:
            constraints (list<str>): constraints on word list, represented by
                2 - correct position
                1 - in word wrong position
                0 - not in word
        """

        # Map each letter in target to number of instances of letter:
        word_dict = map_letters(self.word.rep)

        constraints = ["-1", "-1", "-1", "-1", "-1"]
        for i, letter in enumerate(guess.rep):
            if letter == self.word.rep[i]:
                constraints[i] = "2"
                word_dict[letter] -= 1
            # If the letter is "right letter, wrong place" AND we
            #  haven't already exhausted our allotment for that coding:
            elif letter in set(self.word.rep) and word_dict[letter] > 0:
                constraints[i] = "1"
                word_dict[letter] -= 1
            else:
                constraints[i] = "0"

        return constraints


def map_letters(rep):
    """Map letters in word to count

    Inputs:
        rep (str): string representation of word

    Outputs:
        dict[str -> int]: map of letter to count of
            letter in word
    """
    d = {}
    for idx, ltr in enumerate(rep):
        d[ltr] = sum(True for ltr in rep if ltr == rep[idx])
    return d


# For testing:
if __name__ == "__main__":
    from word import Word

    test = Word("lithe")
    guess = Word("lilts")
    game = WordleGame(test)
    constraints = game.check_guess(guess)
    print("Constraints: ", constraints)
    visual_constraints = game.get_visual_constraints(guess)
    print("Visual constraints: ", visual_constraints)
