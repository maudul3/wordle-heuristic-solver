from word import Word
from pathlib import Path

base_path = Path(
    __file__
).parent.parent.absolute()  # Get full path of file on all machines

# Word list source for the agent playing the game
agent_list = []
data_path = base_path / "data/websters_plus.txt"
with open(data_path, "r") as f:
    for line in f.readlines():
        agent_list.append(Word(line.strip()))

# Word list that is produced by the game and agent
# tries to guess
test_list = []
data_path = base_path / "data/wordle.txt"
with open(data_path, "r") as f:
    for line in f.readlines():
        test_list.append(Word(line.strip()))
