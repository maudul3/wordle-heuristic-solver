import pandas as pd
from pathlib import Path

data_path = (
    Path(__file__).parent.parent.absolute() / 'data/letter_frequency.csv'
) # Get full path of file on all machines

# Read in letter frequency data
letter_frequency_data = pd.read_csv(data_path, usecols=['Letter','Count','Frequency'])

def calculate_letter_frequency(rep):
    """Calculate the total letter frequency for the five-letter word
    
    Args:
        rep (str): five-letter word

    Returns:
        int: heuristic value
    """
    return 1

if __name__ == '__main__':
    print (1)