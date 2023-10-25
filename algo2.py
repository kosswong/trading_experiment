import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('TQQQ.csv')

# Convert the 'Date' column to pandas datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Sort the data by date in ascending order
data = data.sort_values('Date')

# Define the parameters for the strategy
buy_threshold = 0.01  # 5% threshold for buying
sell_threshold = -0.05  # 5% threshold for selling
position = 0  # 0: out of position, 1: long position

money = 100000
newMoney = 100000

# Iterate over the data and generate trading signals
for i in range(1, len(data)):
    prev_close = data['Close'].iloc[i - 1]
    curr_close = data['Close'].iloc[i]

    if position == 0:
        if (curr_close - prev_close) / prev_close >= buy_threshold:
            position = 1
            newMoney -= float(curr_close)*200
            print(f"Buy at {data['Date'].iloc[i]} - Price: {curr_close:.2f}")
    elif position == 1:
        if (curr_close - prev_close) / prev_close <= sell_threshold:
            position = 0
            newMoney += float(curr_close)*200
            print(f"Sell at {data['Date'].iloc[i]} - Price: {curr_close:.2f}")

# If still in a position at the end, sell
if position == 1:
    last_close = data['Close'].iloc[-1]
    print(f"Sell at {data['Date'].iloc[-1]} - Price: {last_close:.2f}")

print(newMoney)