import pandas as pd

# Read in letter frequency data
letter_frequency_data = pd.read_csv('./data/letter_frequency.csv', usecols=['Letter','Count','Frequency'])

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