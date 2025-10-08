import pandas as pd

df = pd.read_csv('euroleague_basketball.csv')
print(df.info())

'''
appearances and titles needs cleaning, change to title and year for columns with a y/n value.
change numbers that are strings into int
'''