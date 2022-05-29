from word import Word

# Word list source for the agent playing the game 
agent_list = []
with open('./data/websters_plus.txt', 'r') as f:
    for line in f.readlines():
        agent_list.append(Word(line.strip()))

# Word list that is produced by the game and agent
# tries to get
test_list = []
with open('./data/wordle.txt', 'r') as f:
    for line in f.readlines():
        test_list.append(Word(line.strip()))