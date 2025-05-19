import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")
tips = sns.load_dataset("tips")
titanic = sns.load_dataset("titanic")

# sns.pairplot(data,hue="species",markers=['o','s','D'])
# plt.title("Iris Pair Plot, Hue로 꽃의 종을 시각화")
# print(titanic.head)
titanic.age = titanic.age.dropna()
temp = titanic.age.copy()
for a in temp:
    # print(a)
    b = int(a)
    print(b)
titanic_size = titanic.pivot_table(index="sex",columns="survived",aggfunc="size")
# print(titanic_size)

sns.heatmap(titanic_size,cmap=sns.light_palette("red",as_cmap=True),annot=True,fmt="d")


plt.title("Heatmap")
plt.show()

#sepal leng