import pandas as pd

df = pd.read_csv('euroleague_basketball.csv')
print(df.info())

'''
1. Which teams are most represented in the Euro Leauge?
'''
country_count = df['Country'].value_counts()
print(f'Count of teams by country: {country_count}')  # count of teams by country

# find count of final four appearances and titles won by country
appearances = df.groupby('Country')['FinalFour_Appearances'].sum().sort_values(ascending=False)
titles = df.groupby('Country')['Titles_Won'].sum().sort_values(ascending=False)

print(f'Count of appearances: {appearances} \n Count of titles: {titles}')

'''
Spain has the most representation, with 4 teams. Turkey, Serbia, Greece, France, Italy and Israel
have 2 teams each. All other countries have 1 team each.

However, despite Spain having the most teams, Greece has the most representation in terms of
success. They have the most final four appearances and titles won, with 27 and 10 respectively.
Spain has the second most, with 12 and 9 respectively.
'''


'''
2. How do arena capacities compare across teams and countries?
'''
# some values for capacity list two capacities- use first arena and change to int
df['Capacity'] = df['Capacity'].str.split(' ').str[0]  # splitting by space, not comma!
df['Capacity'] = df['Capacity'].str.replace(',', '')  # remove commas
df['Capacity'] = pd.to_numeric(df['Capacity'], errors='coerce')  # convert to numeric, coerce errors to NaN

country_avg_capacity = df.groupby('Country')['Capacity'].mean().sort_values(ascending=False)
print(f'Average arena capacity by country: {country_avg_capacity}')
print(country_avg_capacity.describe())
min_capacity = df['Capacity'].min()
max_capacity = df['Capacity'].max()
min_capacity_team = df[df['Capacity'] == min_capacity]['Team'].values[0]
max_capacity_team = df[df['Capacity'] == max_capacity]['Team'].values[0]
print(f'Minimum capacity is {min_capacity} for team {min_capacity_team}')
print(f'Maximum capacity is {max_capacity} for team {max_capacity_team}')   

'''
Serbia, suprisingly, has the largest average arena capacity, with 18,386. Most teams have a
capacity between 11000 and 15500 (these are close to the IQR values).
The minimum capacity is 5000 for team Monaco.
The maximum capacity is 18386 for team Crvena zvezda Meridianbet.
'''

'''
3.Which clubs have been the most successful historically?
'''
team_titles = df[['Team','Titles_Won']].sort_values(by='Titles_Won', ascending=False)
print(team_titles)
team_finalfour = df[['Team','FinalFour_Appearances']].sort_values(by='FinalFour_Appearances', ascending=False)
print(team_finalfour)
'''
This sort shows that Panathinaikos has won the most titles (7) and Real Madrid has won the second
most (6). 
Olympiacos has the most final four appearances (14), followed by Panathinaikos and Real Madrid (13
and 12, respectively).
'''
# create a chart that shows when countries have final four appearances or titles won
