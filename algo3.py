import pandas as pd
import csv

def bollinger_band_strategy(prices, window, num_std):
    rolling_mean = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    upper_band = rolling_mean + num_std * rolling_std
    lower_band = rolling_mean - num_std * rolling_std
    
    positions = pd.Series(0, index=prices.index)
    positions[prices > upper_band] = -1  # 賣出信號
    positions[prices < lower_band] = 1  # 買入信號
    
    return positions

closing_prices = []
with open("TQQQ.csv", "r" ) as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        closing_prices.append(float(line["Close"]))

prices = pd.Series(closing_prices)
positions = bollinger_band_strategy(prices, 20, 2)
print(positions)