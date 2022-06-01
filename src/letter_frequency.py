import pandas as pd
from pathlib import Path

data_path = (
    Path(__file__).parent.parent.absolute() / 'data/letter_frequency.csv'
) # Get full path of file on all machines

# Read in letter frequency data
letter_frequency_data = pd.read_csv(data_path, usecols=['Letter','Count','Frequency'])
print(letter_frequency_data)
def calculate_letter_frequency(rep):
    word = rep.upper()
    count = 0
    d = set(word)
    for s in d:
        for c in letter_frequency_data['Letter']:
            if c == s:
                count += float(letter_frequency_data.loc[letter_frequency_data['Letter'] == c, 'Frequency'])
    return count

if __name__ == '__main__':
    rep = 'Hello'
    print(calculate_letter_frequency(rep))