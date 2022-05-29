import pandas as pd


letter_data = pd.read_csv('./letter_frequency.csv', usecols=['Letter','Count','Frequency'])

word_data = pd.read_csv('./word_frequency.csv')

#Filtering word df to include only five letter words
word_data['word']=word_data['word'].astype(str)
word_data.drop(word_data[word_data['word'].map(len) < 5 ].index, inplace=True) 
word_data.drop(word_data[word_data['word'].map(len) > 5 ].index, inplace=True) 
#print(word_data)
