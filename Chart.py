import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('output_2.txt', names=['timestamp', 'price'])
data["timestamp"] = pd.to_datetime(data['timestamp'])

# for lines in data['price']:
#     print(lines)

data = data.plot(x='timestamp', y='price', figsize=(8,6))
data.set_title('BTC Chart')
data.set_xlabel('Time')
data.set_ylabel('Price in $')
plt.show()