import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

data = pd.read_csv("IMDB Dataset.csv")
data.head(5)
data.info()

"""####**Check Null Values**"""

data.isnull().sum()

"""**No feature has any null values**
#### ++Plot Histogram for feature Runtime++
"""

plt.hist(data['Runtime'])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

"""#### **Define parameter bins_runtime for feature Runtime and plot histogram for it++"""

data['Runtime'].unique()

bins_time = np.arange(80, 230, 10)

plt.hist(data['Runtime'], edgecolor="black", bins=bins_time, color='g')
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

"""#### **Define parameter bins_runtime for feature IMDB_Rating and plot histogram for it++"""

data['IMDB_Rating'].unique()

bins_rating = np.arange(8, 10, .20)

plt.hist(data['IMDB_Rating'], edgecolor="black", bins=bins_time, color='g')
plt.ylabel("Count of movies")
plt.xlabel("IMDB_Rating")
plt.xticks(bins_rating)
plt.show()