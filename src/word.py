from character_frequency import characterfreq
from wordfrequency import wordfreq

class Word:
    def __init__(self, rep):
        """
        Creates new Word object. 

        Inputs:
            self: Word object
            rep (str): 5-letter string representation of word

        Returns:
            Word object
        """
        if len(rep) != 5:
             raise ValueError("Word is not 5 letters")

        self.rep = rep
        self.unique = set(rep)
        self.characterfreq = characterfreq(rep)
        self.wordfreq = wordfreq(rep)
    
if __name__ == '__main__':
    print (1)
