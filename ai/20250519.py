import seaborn as sns
import matplotlib.pyplot as plt
print(sns.__version__)
print(sns.get_dataset_names())
data = sns.load_dataset("iris")
print(data.head())
x = data.petal_length.values

# sns.rugplot(x)

# sns.kdeplot(x)

# sns.displot(x, kde = True, rug = True)
# sns.countplot(x, data=x)
# plt.title("Iris Petal length")

# titanic = sns.load_dataset("titanic")
# sns.countplot(x="class", data=titanic)
# plt.title("Titanic count/class")

tips = sns.load_dataset("tips")
sns.countplot(x="day", data=tips)
plt.title("count of tips/day of week")

plt.show()