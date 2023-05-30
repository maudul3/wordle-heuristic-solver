# Serena Glick for CS 541 AI, June 1, 2022

# functions to process list of outcomes
# and generate a bar plot for the Wordle program data

import random
import matplotlib.pyplot as plt


def generate_list(list_length):
    """Testing function. Generates a list of values
    in range 1-7 of specified legnth.

    Inputs:
        list_length (int): output list length

    Outputs:
        list<int>: list of values in range 1-7
    """
    outcome_list = []
    for _ in range(0, list_length):
        entry = random.randint(1, 7)
        outcome_list.append(entry)
    return outcome_list


def remove_items(the_list, item):
    """Remove items from a list

    Inputs:
        the_list (list): any list
        item (any): any value in list

    Outputs:
        list: the input list edited
    """
    removal_count = the_list.count(item)
    for _ in range(removal_count):
        the_list.remove(item)
    return the_list


def remove_failures(guesses_list):
    """Remove failures from guesses list

    Input:
        guesses_list (list<int>): list of number of guesses to solution

    Outputs:
        list<int>: edited copy of list with failures removed
    """
    edited_list = list(guesses_list)
    edited_list = remove_items(edited_list, 7)
    return edited_list


def count_failures(guesses_list):
    """Count failures in list of of guesses

    Inputs:
        guesses_list (list<int>): list of number of guesses to solution

    Outputs:
        int: number of times player did not solve wordle
    """
    failures = guesses_list.count(7)
    return failures


def percent_failures(guesses_list):
    """Determine percent failures in list of of guesses

    Inputs:
        guesses_list (list<int>): list of number of guesses to solution

    Outputs:
        float: percentage of times player did not solve wordle
    """
    failures = count_failures(guesses_list)
    fail_percent = failures / len(guesses_list)
    fail_percent *= 100
    return fail_percent


def percent_success(guesses_list):
    """Determine percent successes in list of of guesses

    Inputs:
        guesses_list (list<int>): list of number of guesses to solution

    Outputs:
        float: percentage of times player did not solve wordle
    """
    return 100 - percent_failures(guesses_list)


# counts successful guesses only (removes failures)
def avg_guesses(guesses_list):
    """Determine average number of guesses in list

    Inputs:
        guesses_list (list<int>): list of number of guesses to solution
    """
    updated_list = remove_failures(guesses_list)
    avg = sum(updated_list) / len(updated_list)
    return avg


# list 1: no heuristic
# list 2: word frequency heuristic
# list 3: letter frequency heuristic
def generate_bar_plot(no_heuristic, word_freq, letter_freq):
    """Generate bar plot for success and failure metrics

    Inputs:
        no_heuristic (list<int>): list of number of guesses to solution
            for no heuristic
        word_freq (list<int>): list of number of guesses to solution
            for word frequency heuristic
        letter_freq (list<int>): list of number of guesses to solution
            for letter frequency heuristic
    """

    # successful games bar plot
    no_heuristic_success = percent_success(no_heuristic)
    word_freq_success = percent_success(word_freq)
    letter_freq_success = percent_success(letter_freq)

    success_data = {
        "No\nHeuristic": no_heuristic_success,
        "Letter\nFrequency\nHeuristic": letter_freq_success,
        "Word\nFrequency\nHeuristic": word_freq_success,
    }
    h_type_label = list(success_data.keys())
    percent_label = list(success_data.values())

    # Set size of chart window:
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(h_type_label, percent_label, color="green", width=0.3)
    plt.ylabel("% Successful Games")
    plt.title("Agent Performance:\nSuccessful Games")

    # average guesses bar plot
    no_heuristic_avg = avg_guesses(no_heuristic)
    word_freq_avg = avg_guesses(word_freq)
    letter_freq_avg = avg_guesses(letter_freq)

    guess_data = {
        "No\nHeuristic": no_heuristic_avg,
        "Letter\n Frequency\nHeuristic": letter_freq_avg,
        "Word\nFrequency\nHeuristic": word_freq_avg,
    }

    h_type_label = list(guess_data.keys())
    percent_label = list(guess_data.values())

    plt.subplot(1, 2, 2)
    plt.bar(h_type_label, percent_label, color="blue", width=0.3)
    plt.ylabel("Average Number of Guesses")
    plt.title("Agent Performance:\nAverage Guesses")
    plt.show()
