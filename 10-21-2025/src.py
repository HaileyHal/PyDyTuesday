import pandas as pd
import matplotlib.pyplot as plt
historic_station_met = pd.read_csv('historic_station_met.csv')
station_meta = pd.read_csv('station_meta.csv')

# print(historic_station_met.info())
# print(historic_station_met.head())
# print('-------------------------------')
# print(station_meta.info())
# print(station_meta.head())

# Combine two csvs on station
combined_df = pd.merge(historic_station_met, station_meta, on='station', how='outer')
# print(combined_df.info())
combined_df.to_csv('combined_station_data.csv', index=False)


'''
Q1: Which are the rainiest/sunniest/hottest regions of the UK? Has that changed over time?
'''
rain_region = combined_df.groupby('station')[['rain', 'sun']].mean().sort_values(by='rain',
              ascending=False)
print(rain_region)

sun_region = combined_df.groupby('station')[['rain', 'sun']].mean().sort_values(by='sun',
             ascending=False)
print(sun_region)

'''
The rainiest station on average is Cwmystwyth, with an average of 149.43mm per year.
The sunniest station on average is Eastbourne, with an average of 154.53 hours of sun a year.

Check out my PowerBI dashboard showing the difference between rain and sun per station.
'''

'''
Q2: Were there any historic years that were particularly rainy/sunny/hot? Did that apply to all
regions of the UK?

Check out my PowerBI dashboard for visual analysis of historic years.
'''


'''
Q3: Have monthly patterns in the meteorological variables changed year-on-year?
'''
monthly_patterns = combined_df.groupby('month')[['rain', 'sun']].mean().reset_index()

# graph monthly patterns
width=0.35
plt.bar(monthly_patterns['month'] - width/2, monthly_patterns['rain'], width=width, color='blue', label='Rain')
plt.bar(monthly_patterns['month'] + width/2, monthly_patterns['sun'], width=width, color='yellow', label='Sun')

plt.xlabel('Month')
plt.ylabel('Average Rain(mm)/Sun(hours)')
plt.title('Average Rain/Sun by Month')
plt.legend()
plt.grid()

plt.show()

'''
In the shown chart, we can see that the summer months (obviously) have more hours of sunlight,
Oct-Dec have the months with the most rainfall.

I honestly am not sure how to answer the original question in python.
'''