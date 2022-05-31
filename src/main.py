from word_lists import agent_list, test_list
from agent import Agent
from wordlegame import WordleGame, STARTING_GUESSES


if __name__ == '__main__':

    # Can likely make the below two blocks their own functions
    heuristic = 'letter'
    letter_time_to_guess = []
    # Possibly: subset the test list for compute time
        # if we subset the list, make sure words aren't repeated
    for word in test_list:
        agent = Agent(agent_list)
        game = WordleGame(word)
        constraints = None
        while game.guesses_remaining and not game.correct_guess:
            guess = agent.guess(constraints, heuristic)
            constraints = game.check_guess(guess)

        # Add to number of guesses list for data analysis
        # Use of correct_guess is to distinguish between
        # accurate and inaccurate final guesses
        # Values in list 1-6 == correctly guessed &
        # 7 == did not correctly guess
        letter_time_to_guess.append(
            (STARTING_GUESSES + (not game.correct_guess)) 
            - game.guesses_remaining
        )

        # Add file output for our time-to-guess lists
        # Possibly: list of words that were guessed correctly
        # Possibly: list of words that were not guessed

        # 2 list that is number of guesses [1-7, 1-7, 1-7]
        # one for each heuristics
    
    heuristic = 'word'
    word_time_to_guess = []
    for word in test_list:
        agent = Agent(agent_list)
        game = WordleGame(word)
        constraints = None
        while game.guesses_remaining and not game.correct_guess:
            guess = agent.guess(constraints, heuristic)
            constraints = game.check_guess(guess)

        # Add to number of guesses list for data analysis
        # Use of correct_guess is to distinguish between
        # accurate and inaccurate final guesses
        # Values in list 1-6 == correctly guessed &
        # 7 == did not correctly guess
        word_time_to_guess.append(
            (STARTING_GUESSES + (not game.correct_guess)) 
            - game.guesses_remaining
        )



