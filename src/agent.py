class Agent:
    def __init__(self, word_list):
        # Deep copy of the word list
        self.word_list = list(word_list)
    
    def guess(self, constraints, heuristic):
        """
        Args:
            constraints (): constraints on word list
            heuristic (str): which heuristic we would like to use
        """
        # Reduce word list based on existing constraints

        # Decide if it uses exploration route?
        # Consider words not in word list? Needs attribute in that case

        # Sort word list by heuristic
        if heuristic == 'letter':
            print (1)
        elif heuristic == 'word':
            print (1)
        else:
            raise ValueError('Undefined heuristic')

        # Choose word at front of word list

        return "guess"

