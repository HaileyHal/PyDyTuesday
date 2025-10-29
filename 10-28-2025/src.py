import pandas as pd
prizes = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-10-28/prizes.csv')
prizes.to_csv('prizes.csv', index=False)

prizes = pd.read_csv('prizes.csv') 
print(prizes.info())


'''
In which genres are women, Black, Asian and ethnically diverse writers most likely to be
shortlisted and/or awarded?
'''
# find percent of black, asian, or other writers out of all, and group that by genre?
# calculating percentage of each ethnicity in awards
ethnicity_total = prizes['ethnicity_macro'].count()
ethnicities_counts = prizes['ethnicity_macro'].value_counts()
ethnicity_percentages = (ethnicities_counts / ethnicity_total * 100).round(2)  # % ethnicity in df
# mapping to df
prizes['ethnicity_percentage'] = prizes['ethnicity_macro'].map(ethnicity_percentages)
prizes.to_csv('prizes.csv', index=False)

genre_grouped = prizes.groupby('prize_genre')
print(genre_grouped)

'''
Have prizes improved their record on gender and/or ethnic representation in shortlists and
awardees?
'''
# take same percentages from above and list by year

'''
Is there a connection between specific educational credentials and/or educational institutions
and writers chances of being shortlisted or winning?
'''
# this sounds like modeling stuff idk