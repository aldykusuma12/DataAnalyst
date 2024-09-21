import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\user\Downloads\Ice Cream Ratings.csv")
df = df.set_index('Date')
df

print(plt.style.available)
plt.style.use('tableau-colorblind10')

df.plot(kind = 'line', title = 'Ice Cream Rating', xlabel = 'Daily Rating', ylabel = 'Rating Score')
plt.style.use('seaborn-v0_8-bright')

df.plot(kind = 'line', title = 'Ice Cream Rating', xlabel = 'Daily Rating', ylabel = 'Rating Score', subplots = True)
plt.style.use('fast')

df.plot(kind = 'barh', title = 'Ice Cream Rating', xlabel = 'Daily Rating', ylabel = 'Rating Score', stacked = True)
plt.style.use('tableau-colorblind10')

df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 50, c = 'Green')

df.plot.hist(bins = 20)

df.plot.box()

df['Overall Rating'].plot.area()

df.plot.pie(y = 'Flavor Rating', figsize = (6,6), title = 'Pie Chart', legend = False)
