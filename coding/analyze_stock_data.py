# filename: analyze_stock_data.py
import pandas as pd

# Simulated previously obtained DataFrame content
data = {
    'Close': [
        96.749773, 96.358842, 93.224360, 91.284693, 92.209534, 90.078895,
        90.358849, 90.618805, 88.466168, 88.815107, 87.620307, 87.385346,
        90.723780, 90.159884, 90.597806, 88.103222, 88.760115, 86.175549,
        84.309864, 80.059576
    ]
}

tickerDf = pd.DataFrame(data, index=[
    '2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-04-01',
    '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-08',
    '2024-04-09', '2024-04-10', '2024-04-11', '2024-04-12', '2024-04-15',
    '2024-04-16', '2024-04-17', '2024-04-18', '2024-04-19', '2024-04-22'
])

# Convert index to datetime
tickerDf.index = pd.to_datetime(tickerDf.index)

# Calculate daily percentage change in `Close` price
tickerDf['Daily Change'] = tickerDf['Close'].pct_change() * 100

# Calculate overall percentage change 
first_close = tickerDf['Close'].iloc[0]
last_close = tickerDf['Close'].iloc[-1]
overall_change = ((last_close - first_close) / first_close) * 100

# Calculate high, low, and average close
high_close = tickerDf['Close'].max()
low_close = tickerDf['Close'].min()
average_close = tickerDf['Close'].mean()

# Summary statistics
print("Daily Percentage Change:\n", tickerDf['Daily Change'])
print("Overall Percentage Change: {:.2f}%".format(overall_change))
print("High Close: {:.2f}".format(high_close))
print("Low Close: {:.2f}".format(low_close))
print("Average Close: {:.2f}".format(average_close))