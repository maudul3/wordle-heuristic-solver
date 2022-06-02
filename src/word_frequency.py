import pandas as pd
from pathlib import Path

data_path = (
    Path(__file__).parent.parent.absolute() / 'data/word_frequency.csv'
) # Get full path of file on all machines

# Read in word frequency data
word_frequency_data = pd.read_csv(data_path)

# Filtering word df to include only five letter words
word_frequency_data['word']=word_frequency_data['word'].astype(str)
word_frequency_data.drop(word_frequency_data[word_frequency_data['word'].map(len) < 5 ].index, inplace=True) 
word_frequency_data.drop(word_frequency_data[word_frequency_data['word'].map(len) > 5 ].index, inplace=True) 
#print(word_frequency_data)

def calculate_word_frequency(rep):
    try:
        count = int(word_frequency_data.loc[word_frequency_data['word'] == rep, 'count'])
    except:
        # If a word is not in the dataframe we assign a count of 1
        count = 1
    return count

if __name__ == '__main__':
    rep = "brain"
    print (calculate_word_frequency(rep))