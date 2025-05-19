import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")
tips = sns.load_dataset("tips")
sns.jointplot(x='sepal_length',y='sepal_width',data=data, kind="kde")
plt.suptitle("JoinPlot by Iris Sepal""width/length",y=1.02)

plt.show()