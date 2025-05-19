import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

np.random.seed(0)

sns.violinplot(x="day",y='total_bill',data=tips)
sns.stripplot(x="day",y='total_bill',data=tips, jitter=True)
sns.swarmplot(x="day",y='total_bill',data=tips)



plt.title("Heatmap")
plt.show()

#sepal leng