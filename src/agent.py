class Agent:
    def __init__(self, word_list):
        # Deep copy of the word list
        self.word_list = list(word_list)
        self.most_recent_guess = None
    
    def guess(self, constraints, heuristic=None):
        """
        Args:
            constraints (list<str>): constraints on word list, represented by
                2 - correct position
                1 - in word wrong position
                0 - not in word
            heuristic (str): which heuristic we would like to use
        """
        # letter in word but not in position
        # letter in word and in correct position
        # letter not in word
        # 'bread' = 10210'
        # 2 - correct position 1 - in word wrong position 0 - not in word
        # edge case - 2 of the same letters

        # Reduce word list based on existing constraints
        for idx, constraint in enumerate(constraints):
            reference_character = self.most_recent_guess.rep[idx]

            if constraint == '2':
                self.word_list = [
                    word for word in self.word_list 
                    if word.rep[idx] == reference_character
                ]
            elif constraint == '1':
                self.word_list = [
                   word for word in self.word_list 
                   if word.rep[idx] != reference_character and reference_character in word.rep
                ]
            elif constraint == '0':
                self.word_list = [
                   word for word in self.word_list 
                   if reference_character not in word.rep
                ]

        # Decide if it uses exploration route?
        # Consider words not in word list? Needs attribute in that case

        # Sort word list by heuristic
        if heuristic == 'letter':
            self.word_list = sorted(self.word_list, key=lambda x: x.wordfreq, reverse=True)
        elif heuristic == 'word':
            self.word_list = sorted(self.word_list, key=lambda x: x.characterfreq, reverse=True)

        # Choose word at front of word list
        self.most_recent_guess = self.word_list[0]

        return self.most_recent_guess
        
if __name__ == '__main__':
    from word import Word
    from wordlegame import WordleGame
    from word_lists import agent_list
    test = Word("sword")
    agent = Agent(agent_list)
    game = WordleGame(test)
    constraints = []
    while game.guesses_remaining and not game.correct_guess:
        guess = agent.guess(constraints, "letter")
        print ("Guess :", guess.rep)
        constraints = game.check_guess(guess)
        print ("Constraints: ", constraints)
    