# CS-441-541-Project

# Repository Structure

src - contains all original .py files<br>
data - contains all externally sourced data files

<br>

# SRC structure and dependencies on other files

letter_frequency.py - contains data processing of letter frequency data, function for determining heuristic value for word based on letter frequency<br>

word_frequency.py - contains data processing of word frequency data, function for determing heuristic value for word based on word frequency<br>

word.py - contains Word class definition, DEPENDENT on word_frequency.py, letter_frequency.py<br>

word_lists.py - creates the agent list and test list of words for simulating the game, DEPENDENT on word.py<br>

agent.py - contains Agent class definiton<br>

wordlegame.py - contains WordleGame class definition<br>

main.py - main script for running experiments DEPENDENT on agent.py,
wordlegame.py, word_lists.py <br>

<br>

# Install

## macOS

First make sure you have Python 3.x installed as well as Pip, the Python package manager.

Pip comes with Python, but if you want to make sure it is installed type:
'python3 -m ensurepip --upgrade'

Depending on your setup, you may need to specify `python` instead of `python3`.

You may need to update your $PATH in order to run python.
For example, to update zshell (MacOS default) do the following:
From the command prompt type: 'vi ~/.zshrc'
This will open the config file for your zshell where you can make alterations.
Depending on your configuration, you will probably want to add:
'export PATH=~/usr/local/bin/python3/bin:$PATH'

Also, please install pandas with the following line:
'pip3 install pandas'

Depending on your setup, you may need to specify `pip` instead of `pip3`.

Now, just navigate to the src folder. If you are using the terminal type:
'python3 main.py'

It takes a few moments to run, so just be patient. Pretty soon you'll see output to your screen.

Alternately, you can use an IDE to run the main.py file.



