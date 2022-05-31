# CS-441-541-Project

# Repository Structure
src - contains all original .py files<br>
data - contains all externally sourced data files

# SRC structure and dependencies on other files
 letter_frequency.py - contains data processing of letter frequency data, function for determining heuristic value for word based on letter frequency<br>

 word_frequency.py - contains data processing of word frequency data, function for determing heuristic value for word based on word frequency<br>

 word.py - contains Word class definition, DEPENDENT on word_frequency.py, letter_frequency.py<br>

 word_lists.py - creates the agent list and test list of words for simulating the game, DEPENDENT on word.py<br>

 agent.py - contains Agent class definiton<br>

wordlegame.py - contains WordleGame class definition<br>

main.py - main script for running experiments DEPENDENT on agent.py,
wordlegame.py, word_lists.py <br>