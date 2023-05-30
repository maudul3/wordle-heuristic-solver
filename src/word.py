from letter_frequency import calculate_letter_frequency
from word_frequency import calculate_word_frequency


class Word:
    def __init__(self, rep):
        """
        Creates new Word object.

        Inputs:
            self: Word object
            rep (str): 5-letter string representation of word

        Outputs:
            Word object
        """
        if len(rep) != 5:
            raise ValueError("Word is not 5 letters")

        self.rep = rep.lower()  # use of lower function normalize words to lowercase
        self.unique = set(rep)  # unique characters in word
        self.characterfreq = calculate_letter_frequency(rep)
        self.wordfreq = calculate_word_frequency(rep)


if __name__ == "__main__":
    print(1)
