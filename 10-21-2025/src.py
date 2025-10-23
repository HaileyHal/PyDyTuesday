import pandas as pd
historic_station_met = pd.read_csv('historic_station_met.csv')
station_meta = pd.read_csv('station_meta.csv')

print(historic_station_met.info())
print(historic_station_met.head())
print('-------------------------------')
print(station_meta.info())
print(station_meta.head())

# Combine two csvs on station
combined_df = pd.merge(historic_station_met, station_meta, on='station', how='outer')
print(combined_df.info())
combined_df.to_csv('combined_station_data.csv', index=False)