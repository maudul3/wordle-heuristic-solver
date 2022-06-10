# Serena Glick for CS 541 AI, June 1, 2022

# functions to process list of outcomes
# and generate a bar plot for the Wordle program data

import random
import matplotlib.pyplot as plt


# generates a list of values 1-7 for sample data
def generate_list(list_length):
    outcome_list = []
    for i in range(0, list_length):
        entry = random.randint(1, 7)
        outcome_list.append(entry)
    return outcome_list


def remove_items(the_list, item):
    removal_count = the_list.count(item)
    for i in range(removal_count):
        the_list.remove(item)
    return the_list


def remove_failures(guesses_list):
    edited_list = list(guesses_list)
    edited_list = remove_items(edited_list, 7)
    return edited_list


def count_failures(guesses_list):
    failures = guesses_list.count(7)
    return failures


def percent_failures(guesses_list):
    failures = count_failures(guesses_list)
    fail_percent = failures / len(guesses_list)
    fail_percent *= 100
    return fail_percent


def percent_success(guesses_list):
    return 100 - percent_failures(guesses_list)


# counts successful guesses only (removes failures)
def avg_guesses(guesses_list):
    updated_list = remove_failures(guesses_list)
    avg = sum(updated_list) / len(updated_list)
    return avg

# list 1: no heuristic
# list 2: word frequency heuristic
# list 3: letter frequency heuristic
def generate_bar_plot(list1, list2, list3):

    # successful games bar plot
    l1_success = percent_success(list1)
    l2_success = percent_success(list2)
    l3_success = percent_success(list3)

    success_data = {'No\nHeuristic': l1_success, 
                    'Letter\nFrequency\nHeuristic': l2_success, 'Word\nFrequency\nHeuristic': l3_success}
    h_type_label = list(success_data.keys())
    percent_label = list(success_data.values())

    # Set size of chart window:
    plt.figure(figsize = (12,6))

    plt.subplot(1, 2, 1)
    plt.bar(h_type_label, percent_label, color='green', width=0.3)
    plt.ylabel("% Successful Games")
    plt.title("Agent Performance:\nSuccessful Games")

    # average guesses bar plot
    l1_avg = avg_guesses(list1)
    l2_avg = avg_guesses(list2)
    l3_avg = avg_guesses(list3)



    guess_data = {'No\nHeuristic': l1_avg,
                  'Letter\n Frequency\nHeuristic': l2_avg,
                   'Word\nFrequency\nHeuristic': l3_avg}

    h_type_label = list(guess_data.keys())
    percent_label = list(guess_data.values())

    plt.subplot(1, 2, 2)
    plt.bar(h_type_label, percent_label, color='blue', width=0.3)
    plt.ylabel("Average Number of Guesses")
    plt.title("Agent Performance:\nAverage Guesses")
    plt.show()
