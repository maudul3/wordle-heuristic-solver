import os
import platform
from word_lists import agent_list, test_list
from agent import Agent
from wordlegame import WordleGame, STARTING_GUESSES
from random import random
from bar_plot import *


def constraints_to_emoji(constraints):
    """Maps constrain to associated emoji

    Inputs:
        constraints (list<str>): constraints associated with
            the most recent guess

    Outputs:
        list<str>: emoji representation of the constraints
    """
    constraint_to_emoji = {
        "0": "\U0001F7E5",
        "1": "\U0001F7E8",
        "2": "\U0001F7E9",
    }
    constraints_rep = ""
    for constraint in constraints:
        constraints_rep += constraint_to_emoji[constraint]

    return constraints_rep


def run_experiment(heuristic=None, print_percentage=0.05):
    """Run an experiment that simulates the agent playing
    Wordle fot every word in the test list

    Inputs:
        heuristic (str): letter frequency 'letter' or
            word frequency 'word'
        print_percentage (float): 0 - 1, percentage of
            games to print out in emoji form

    Outputs:
        list<str>: list of number of turns it took to guess
            correctly for each game
    """
    # Can likely make the below two blocks their own functions
    time_to_guess = []
    # Possibly: subset the test list for compute time
    # if we subset the list, make sure words aren't repeated
    for word in test_list:
        agent = Agent(agent_list)
        game = WordleGame(word)
        constraints = []
        print_game = random.random()
        if print_game < print_percentage:
            print("\n\n--------GAME WORD--> ", word.rep, "\n")
        while game.guesses_remaining and not game.correct_guess:
            guess = agent.guess(constraints, heuristic)
            constraints = game.check_guess(guess)
            if print_game < print_percentage:
                print("\nGuess: ", guess.rep)
                visual_constraints = game.get_visual_constraints(guess)
                print("\tConstraints: ", constraints_to_emoji(visual_constraints))

        # Add to number of guesses list for data analysis
        # Use of correct_guess is to distinguish between
        # accurate and inaccurate final guesses
        # Values in list 1-6 == correctly guessed &
        # 7 == did not correctly guess
        time_to_guess.append(
            (STARTING_GUESSES + (not game.correct_guess)) - game.guesses_remaining
        )
        # Add file output for our time-to-guess lists
        # Possibly: list of words that were guessed correctly
        # Possibly: list of words that were not guessed

        # 2 list that is number of guesses [1-7, 1-7, 1-7]
        # one for each heuristics
    correct_guesses = sum(
        [1 if guess_number <= 6 else 0 for guess_number in time_to_guess]
    )
    no_correct_guesses = sum(
        [1 if guess_number == 7 else 0 for guess_number in time_to_guess]
    )

    print("\nHeuristic used: ", heuristic)
    print("\nTotal games: ", len(time_to_guess))
    print("\nNumber of games with correct guess: ", correct_guesses)
    print("\nNumber of games with no correct guesses", no_correct_guesses)
    print(
        "\n% Successful Games: ",
        round(correct_guesses / (correct_guesses + no_correct_guesses) * 100, 2),
    )

    return time_to_guess


if __name__ == "__main__":
    print(
        """This simulation will play thousands of games of Wordle, and
        using its super-bot smarts will solve as many games as possible.
        As it is finishing it will display some games and the percentage
        of games that it has won. It plays using either brute force,
        using a letter frequency heuristic, or a word frequency heuristic.
        AI bot is now playing the games. Please wait for results."""
    )

    cmd = platform.system()

    if cmd == "Darwin":
        os.system(
            "open -a 'Google Chrome' wordle.gif --args --new-window --window-size=454,480"
        )

    no_heuristic_results = run_experiment(heuristic=None, print_percentage=0.005)
    letter_results = run_experiment(heuristic="letter", print_percentage=0.005)
    word_results = run_experiment(heuristic="word", print_percentage=0.005)

    generate_bar_plot(no_heuristic_results, word_results, letter_results)
