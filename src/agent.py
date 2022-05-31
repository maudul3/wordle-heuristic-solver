class Agent:
    def __init__(self, word_list):
        # Deep copy of the word list
        self.word_list = list(word_list)
        # self.letter_list = [] - possible use?
    
    def guess(self, constraints, heuristic):
        """
        Args:
            constraints (list<str>): constraints on word list, represented by
                0 - correct position
                1 - in word wrong position
                2 - not in word
            heuristic (str): which heuristic we would like to use
        """
        # letter in word but not in position
        # letter in word and in correct position
        # letter not in word
        # 'bread' = '10210'
        # 0 - correct position 1 - in word wrong position 2 - not in word
        # edge case - 2 of the same letters

        # Reduce word list based on existing constraints

        # Decide if it uses exploration route?
        # Consider words not in word list? Needs attribute in that case

        # Sort word list by heuristic
        if heuristic == 'letter':
            x = 1
        elif heuristic == 'word':
            x = 1
        else:
            raise ValueError('Undefined heuristic')

        # Choose word at front of word list

        return self.word_list[0]

