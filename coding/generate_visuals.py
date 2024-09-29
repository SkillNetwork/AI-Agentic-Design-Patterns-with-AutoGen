# filename: generate_visuals.py
import pandas as pd
import matplotlib.pyplot as plt

# Simulated previously obtained DataFrame content with Daily Change included
data = {
    'Close': [
        96.749773, 96.358842, 93.224360, 91.284693, 92.209534, 90.078895,
        90.358849, 90.618805, 88.466168, 88.815107, 87.620307, 87.385346,
        90.723780, 90.159884, 90.597806, 88.103222, 88.760115, 86.175549,
        84.309864, 80.059576
    ],
    'Daily Change': [
        None, -0.404064, -3.252926, -2.080644, 1.013139, -2.310649,
        0.310788, 0.287693, -2.375486, 0.394432, -1.345267, -0.268158,
        3.820359, -0.621553, 0.485717, -2.753471, 0.745595, -2.911855,
        -2.164982, -5.041270
    ]
}

tickerDf = pd.DataFrame(data, index=[
    '2024-03-25', '2024-03-26', '2024-03-27', '2024-03-28', '2024-04-01',
    '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-08',
    '2024-04-09', '2024-04-10', '2024-04-11', '2024-04-12', '2024-04-15',
    '2024-04-16', '2024-04-17', '2024-04-18', '2024-04-19', '2024-04-22'
])
tickerDf.index = pd.to_datetime(tickerDf.index)

# Create a figure and a set of subplots
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Plot Closing Prices
ax[0].plot(tickerDf.index, tickerDf['Close'], marker='o', linestyle='-')
ax[0].set_title('Nvidia Closing Stock Prices')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Close Price (USD)')

# Plot Daily Changes
ax[1].bar(tickerDf.index, tickerDf['Daily Change'], color='skyblue')
ax[1].set_title('Daily Percentage Change in Nvidia Stock Price')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Daily Change (%)')

# Automatic date formatting
fig.autofmt_xdate()

plt.tight_layout()
plt.show()