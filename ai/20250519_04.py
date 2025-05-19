import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

flights= sns.load_dataset("flights")

print(flights)
flights_passengers = flights.pivot(index="month",columns="year",values="passengers")

sns.heatmap(flights_passengers,annot=True,fmt="d",linewidths=1)

plt.title("Total Year/Month")
plt.show()

#sepal leng