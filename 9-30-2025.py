import pydytuesday
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('cranes.csv')
# print(df.info())

df['year'] = df['date'].str.split('-').str.get(0)
df['month'] = df['date'].str.split('-').str.get(1)
df['day'] = df['date'].str.split('-').str.get(2)

'''
Question 1: Has the crane population at Lake Hornborgasjon grown over the past 30 years?
'''
grouped_df = df.drop(['date', 'comment', 'weather_disruption', 'day'], axis=1)  # axis = 1 shows we are dropping from cols
grouped_df = grouped_df.groupby('year')['observations'].sum()

# making a visualization
x = grouped_df.index
y = grouped_df.values

fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor='white', linewidth=0.7)
ax.tick_params(axis='x', rotation=55)
plt.title('Crane Counts by Year')
plt.show()
'''
Yes! The data show that there has been a general increase in crane population, assuming there is
a constant proportion of cranes visiting this center. So far 2019 has had the largest count of
cranes visit. 
'''


'''
Question 2: If you wanted to see thousands of cranes, when is the best time of year to visit?
'''
month_df = df.drop(['date', 'comment', 'weather_disruption', 'day'], axis=1)
month_df = month_df.groupby('month')['observations'].mean()

# making my visualization
x = month_df.index
y = month_df.values

fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor='white', linewidth=0.7)
ax.tick_params(axis='x', rotation=55)
plt.title('Average Crane Count by Month')
plt.show()
'''
An important note to this question is that cranes are only counted (and likely only at the lake)
during month 3, 4, 8, 9 and 10. The best time to see any cranes would be during these months. The
very best time to see the most cranes would be late summer early, fall, speficially September.
'''
# make a heatmap? monthXday
# pivot data to accuratley reflect data
pivoted_data = df.pivot_table(
    index='month',
    columns='day',
    values='observations',
    aggfunc='mean' # taking the average for that day/month combo
)

# plot
plt.figure(figsize=(12,8))
sns.heatmap(pivoted_data, annot=False, cmap='YlGnBu')
plt.title('Heatmap of Crane Counts for Month and Day')
plt.show()
'''
I also created a heatmap to answer question 2. We can see that the spring months, specifically
April, have the most consistent high numbers for crane counts. The first week in April would be best.
Additionally, September is still a good time to visit, but the daily counts are, on average, a lot
more sporradic. That being said, the last half of September is still a great time to go.
'''